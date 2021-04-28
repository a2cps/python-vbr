import logging
from . import connection
from . import constants
from . import errors

logging.basicConfig(level=logging.DEBUG)

__all__ = ['VBR']

class VBR(connection.VBRConn):
    def get_key_for_table(self,
                          key_column: str,
                          table: str,
                          query_column: str,
                          query_value: str,
                          exact_match=True) -> str:
        if exact_match:
            SQL = "SELECT {0} FROM {1} WHERE {2} = %s;".format(
                key_column, table, query_column)
        else:
            SQL = "SELECT {0} FROM {1} WHERE {2} LIKE %s;".format(
                key_column, table, query_column)

        conn = self.db
        cur = conn.cursor()
        cur.execute(SQL, [
            query_value,
        ])
        resp = cur.fetchall()
        if len(resp) > 1:
            logging.warning('More than one {0} record matches the {1}'.format(
                table, query_column))
        try:
            return resp[0][0]
        except IndexError:
            raise errors.RecordNotFoundError(
                'No {0} record with {1} matching "{2}" was found'.format(
                    table, query_column, query_value))
        except Exception:
            raise

    def organization_name_from_id(self, organization_id: str) -> str:
        """Resolve an organization name from its primary identifier
        """
        # https://docs.google.com/document/d/1Rd1lxdcb7lLOnFO_tDCfqcG5tdqrp-A3i4DUiavr0WM/edit#bookmark=id.w6w9zincfs9m
        return self.get_key_for_table('name',
                                      'organization',
                                      'organization_id',
                                      organization_id,
                                      exact_match=True)

    def organization_id_from_name(self, name: str) -> str:
        """Resolve an organization identifier from its name
        """
        # https://docs.google.com/document/d/1Rd1lxdcb7lLOnFO_tDCfqcG5tdqrp-A3i4DUiavr0WM/edit#bookmark=id.w6w9zincfs9m
        return self.get_key_for_table('organization_id',
                                      'organization',
                                      'name',
                                      name,
                                      exact_match=True)

    def organization_id_from_synonym(self, synonym: str) -> str:
        """Resolve an organization identifier from one of its synonyms
        """
        # https://docs.google.com/document/d/1Rd1lxdcb7lLOnFO_tDCfqcG5tdqrp-A3i4DUiavr0WM/edit#bookmark=id.w6w9zincfs9m
        return self.get_key_for_table('organization_id',
                                      'organization',
                                      'synonyms',
                                      synonym,
                                      exact_match=False)

    def protocol_id_from_name(self, protocol_name: str) -> str:
        return self.get_key_for_table('protocol_id', 'protocol', 'name',
                                      protocol_name)

    def dataset_id_from_description(self, dataset_description: str) -> str:
        return self.get_key_for_table('dataset_id', 'dataset', 'description',
                                      dataset_description)

    def baseline_visit_dataset_id_from_subject_title(
            self, subject_title: str) -> str:
        baseline_query = 'baseline visit for {}'.format(' '.join(
            subject_title.split('_')))
        return self.dataset_id_from_description(baseline_query)
