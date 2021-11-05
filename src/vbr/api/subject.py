from vbr.tableclasses import Subject

from .biosample import BiosampleApi

__all__ = ["SubjectApi"]


class SubjectApi(object):
    def get_subject(self, pkid: str) -> Subject:
        """Retrieve a Subject by primary identifier."""
        return self._get_row_from_table_with_id("subject", pkid)

    def get_subject_by_local_id(self, local_id: str) -> Subject:
        """Retrieve a Subject by local_id."""
        return self._get_row_from_table_with_local_id("subject", local_id)

    def get_subject_by_tracking_id(self, tracking_id: str) -> Subject:
        """Retrieve a Subject by tracking_id."""
        return self._get_row_from_table_with_tracking_id("subject", tracking_id)

    def get_subject_by_guid(self, guid: str) -> Subject:
        """Retrieve a Subject by GUID."""
        return self._get_row_from_table_with_tracking_id("subject", guid)

    def get_subject_by_redcap_record(self, record_id: str) -> Subject:
        """Retrieve a Subject by REDcap record identifier."""
        record_id = str(record_id)
        query = {"source_subject_id": {"operator": "=", "value": record_id}}
        return self._get_row_from_table_with_query("subject", query)

    # vbr_subject = Subject(
    #     project=vbr_project_id,
    #     source_subject_id=record_id,
    #     tracking_id=vbr_subject_tracking_id)

    def create_subject(
        self, tracking_id: str, project_id: int, source_subject_id: str
    ) -> Subject:
        """Create a new Subject."""
        # TODO - Add a data_event marking the creation
        sbj = Subject(
            tracking_id=tracking_id,
            project=project_id,
            source_subject_id=source_subject_id,
        )
        try:
            return self.vbr_client.create_row(sbj)[0]
        except Exception:
            raise

    def create_or_get_subject_by_tracking_id(
        self, tracking_id: str, project_id: int, source_subject_id: str
    ) -> Subject:
        """Create a Subject or return existing with specified tracking_id."""
        try:
            return self.create_subject(tracking_id, project_id, source_subject_id)
        except Exception:
            return self.get_subject_by_tracking_id(tracking_id)

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

    def get_subject_biosamples(
        self, local_id: str = None, biosample_id: int = None
    ) -> list:
        """Retrieve Biosamples derived from a Subject."""
        raise NotImplemented()

    # ! Relocate (new location or inside another container)
    # ! Update status
