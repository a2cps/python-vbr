from vbr.tableclasses import Subject
from .biosample import BiosampleApi

__all__ = ['SubjectApi']


class SubjectApi(object):
    def get_subject(self, pkid: str) -> Subject:
        """Retrieve a Subject by primary identifier."""
        return self._get_row_from_table_with_id('subject', pkid)

    def get_subject_by_local_id(self, local_id: str) -> Subject:
        """Retrieve a Subject by local_id."""
        return self._get_row_from_table_with_local_id('subject', local_id)

    def get_subject_by_tracking_id(self, tracking_id: str) -> Subject:
        """Retrieve a Subject by tracking_id."""
        return self._get_row_from_table_with_tracking_id(
            'subject', tracking_id)

    def get_subject_by_guid(self, guid: str) -> Subject:
        """Retrieve a Subject by GUID."""
        return self._get_row_from_table_with_tracking_id('subject', guid)

    def get_subject_by_redcap_record(self, record_id: str) -> Subject:
        """Retrieve a Subject by REDcap record identifier."""
        record_id = str(record_id)
        query = {'source_subject_id': {'operator': '=', 'value': record_id}}
        return self._get_row_from_table_with_query('subject', query)

    def relabel_subject(self, local_id: str, new_tracking_id: str) -> Subject:
        """Update the tracking_id for a Subject by local_id."""
        # 1. Query for row matching local_id
        # 2. Set the new value
        # 3. Do database update via vbr_client.update_row()
        # 4. TODO Create and link a 'rename' data_event
        subj = self.get_subject_by_local_id(local_id)
        subj.tracking_id = new_tracking_id
        subj = self.vbr_client.update_row(subj)
        return subj

    def get_subject_biosamples(self,
                               local_id: str = None,
                               biosample_id: int = None) -> list:
        """Retrieve Biosamples derived from a Subject."""
        raise NotImplemented()

    # ! Relocate (new location or inside another container)
    # ! Update status
