"""VBR Database Driver
"""
import logging
import os
import requests
import uuid
from typing import NoReturn, Any

from tapipy.tapis import Tapis, TapisResult

logging.basicConfig(level=logging.CRITICAL)

__all__ = ['Connection', 'TapisUserEnv', 'TapisDirectClient']


class Connection(object):
    """Provides a PgREST client
    """
    def __init__(self, tapis_client: Tapis, session=None, auto_connect=True):

        if session is None:
            self.session = uuid.uuid4().hex
        else:
            self.session = str(session)
        logging.debug('VBR Session: ' + self.session)

        self.client = tapis_client
        if auto_connect:
            self.connect()

    def connect(self, tapis_client: Tapis = None) -> NoReturn:
        if tapis_client is not None:
            self.client = tapis_client

        # try:
        #     self.client.get_tokens()
        # except Exception:
        #     # Probably running inside an Actor where this won't work
        #     pass


class TapisUserEnv(Tapis):
    """Supports initialization of a Tapis user client from env vars
    """
    def __init__(self, **kwargs):
        super().__init__(base_url=os.environ['VBR_HOST'],
                         username=os.environ['VBR_USERNAME'],
                         password=os.environ['VBR_PASSWORD'],
                         **kwargs)


class TapisDirectClient(object):
    """Requests client bootstrapped from a Tapis API client
    The intended use is to implement methods not expressed by the
    current OpenAPI spec and which are thus not accessible in TapiPy.
    """

    VERBOSE_ERRORS = True

    def __init__(self, tapis_client):
        # TODO - Catch when client is missing properties
        # token = tapis_client.token.token_info['access_token']
        # Always refresh when using a requests call
        token = tapis_client.access_token.access_token
        self.user_agent = 'TapisDirectClient/1.0'
        self.api_server = tapis_client.base_url
        self.api_key = tapis_client.client_id
        self.api_secret = tapis_client.client_key
        self.verify = tapis_client.verify
        self.service_name = None
        self.service_version = None
        self.api_path = None
        self.headers = {'user-agent': self.user_agent}
        # Only send Bearer if token is provided
        if token:
            self.headers['X-Tapis-Token'] = '{}'.format(token)

    def setup(self, service_name, service_version='v3', api_path=None):
        setattr(self, 'service_name', service_name)
        setattr(self, 'service_version', service_version)
        setattr(self, 'api_path', api_path)

    def build_url(self, *args):
        arg_els = args
        path_els = [self.service_version, self.service_name, self.api_path]
        path_els.extend(arg_els)
        # TODO - Filter for leading slashes in path_els
        # TODO - Strip trailing slash from api_server
        url_path_els = [self.api_server]
        url_path_els.extend(path_els)
        url_path_els = [u for u in url_path_els if u is not None]
        return '/'.join(url_path_els)

    def get(self, path=None):
        url = self.build_url(path)
        resp = requests.get(url, headers=self.headers, verify=self.verify)
        # show_curl(resp, verify=self.verify)
        resp = self._raise_for_status(resp)
        #        resp.raise_for_status()
        return resp.json().get('result', {})

    def delete(self, path=None):
        url = self.build_url(path)
        resp = requests.delete(url, headers=self.headers, verify=self.verify)
        # show_curl(resp, verify=self.verify)
        resp = self._raise_for_status(resp)
        #        resp.raise_for_status()
        return resp.json().get('result', {})

    def get_bytes(self, path=None):
        url = self.build_url(path)
        resp = requests.get(url, headers=self.headers, verify=self.verify)
        # show_curl(resp, verify=self.verify)
        resp = self._raise_for_status(resp)
        #        resp.raise_for_status()
        return resp

    def get_data(self, path=None, params={}):
        url = self.build_url(path)
        resp = requests.get(url,
                            headers=self.headers,
                            params=params,
                            verify=self.verify)
        # show_curl(resp, verify=self.verify)
        resp = self._raise_for_status(resp)
        #        resp.raise_for_status()
        return resp.json().get('result', {})

    def post(self,
             path=None,
             data=None,
             content_type=None,
             json=None,
             params=None):
        url = self.build_url(path)
        post_headers = self.headers
        if content_type is not None:
            post_headers['Content-type'] = content_type
        resp = requests.post(url,
                             data=data,
                             headers=post_headers,
                             params=params,
                             json=json,
                             verify=self.verify)
        # show_curl(resp, verify=self.verify)
        resp = self._raise_for_status(resp)

        # Some direct POST actions are management actions that return only a
        # message. Thus we try to return "result" first, then fail over
        # to returning "message" before handling the most annoying case where
        # no response is returned, in which case an empty dict is the
        # appropriate response. If there is no JSON available at all,
        # return the response body as bytes.
        try:
            result = resp.json().get('result', resp.json().get('message', {}))
        except JSONDecodeError:
            result = resp.content
        return result

    def post_data_basic(self,
                        data=None,
                        auth=None,
                        path=None,
                        content_type=None):
        url = self.build_url(path)
        post_headers = {'user-agent': self.user_agent}
        if content_type is not None:
            post_headers['Content-type'] = content_type
        if auth is None:
            auth = (self.api_key, self.api_secret)

        resp = requests.post(url,
                             headers=post_headers,
                             auth=auth,
                             data=data,
                             verify=self.verify)
        # show_curl(resp, verify=self.verify)

        resp = self._raise_for_status(resp)

        # The use case for post_data_basic is communicating with
        # Tapis APIs that accept only Basic Auth. These include all
        # the API manager APIs, and the appropriate response is to
        # return the entire JSON payload since APIM responses do not
        # adhere to the (status, version, result) structure favored
        # by the core Tapis APIs
        return resp.json()

    def _raise_for_status(self, resp):
        """Handler for requests raise_for_status to capture message from API server responses
        """
        try:
            resp.raise_for_status()
        except requests.exceptions.HTTPError as h:
            if self.VERBOSE_ERRORS:
                # Extract the API JSON message and attach it
                # to the HTTPError object before raising it
                code = h.response.status_code
                reason = h.response.reason + ' for ' + h.response.url
                try:
                    message = h.response.json().get('message')
                except Exception:
                    message = h.response.text
                raise requests.exceptions.HTTPError(code,
                                                    reason,
                                                    message,
                                                    response=h.response,
                                                    request=h.request)
            else:
                raise h
        return resp


# NOTE - One idea is to implement left/right relations in the connection class.
#        For example, do a retrieve on an object, then inspect to see if it has
#        any relations. If so, retrieve the related object and attach it to
#        the current one as a named property.  This would be done recursively
#        through the related object tree. Rendering to a dict/JSON for
#        consumption/usage would be recursive as well. We would not directly
#        support updates. Deletes should be supported implicitly via built-in
#        foreign key on_delete behavior.
