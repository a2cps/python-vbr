import os

from .constants import *

__all__ = ["redcap_to_vbr_project_id", "recap_project_to_token"]

# This is the name of a Tapis SK API secret
SECRET_NAME = "redcap_project_tokens"
# Owner of the secret
SECRET_OWNER = "vaughn"
# Tenant for the secret
TENANT = "a2cps-dev"

__all__ = ["redcap_to_vbr_project_id", "redcap_project_to_token"]


def redcap_to_vbr_project_id(project_id: str) -> str:
    # TODO - write real mapping code for this.
    # Need a canonical list of REDCap project_ids that map to the A2CPS project
    return "1"


def get_secret_map(
    tapis_client: object,
    secret_owner: str = None,
    secret_name: str = None,
    tenant: str = None,
) -> dict:

    if secret_name is None:
        secret_name = os.environ.get(TAPIS_SECRETS_NAME, SECRET_NAME)
    if secret_owner is None:
        secret_owner = os.environ.get(TAPIS_SECRETS_OWNER, SECRET_OWNER)
    if tenant is None:
        tenant = os.environ.get(
            TAPIS_SECRETS_TENANT, getattr(tapis_client, "tenant_id", TENANT)
        )

    return (
        tapis_client.sk.readSecret(
            secretType="user", secretName=secret_name, tenant=tenant, user=secret_owner
        )
        .get("secretMap")
        .__dict__
    )


# Expectation is there is a Tapis SK secret with structure
# {"$project_id": "token", ...} where project_id is a REDCap project
# and token is a valid access token for that project's API
def redcap_project_to_token(
    project_id: str,
    tapis_client: object,
    secret_owner: str = None,
    secret_name: str = None,
    tenant: str = None,
) -> str:
    try:
        token = get_secret_map(
            tapis_client=tapis_client,
            secret_owner=secret_owner,
            secret_name=secret_name,
            tenant=tenant,
        ).get(str(project_id))
        return token
    except KeyError:
        raise ValueError(
            "No token for {0} found in {1}".format(project_id, secret_name)
        )
