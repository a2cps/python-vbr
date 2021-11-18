from vbr.tableclasses import Biosample
from .data_event import DataEventApi

__all__ = ["BiosampleApi"]


class BiosampleApi(object):
    def get_biosample(self, pkid: str) -> Biosample:
        """Retrieve a Biosample by primary identifier."""
        return self._get_row_from_table_with_id("biosample", pkid)

    def get_biosample_by_local_id(self, local_id: str) -> Biosample:
        """Retrieve a Biosample by local_id."""
        return self._get_row_from_table_with_local_id("biosample", local_id)

    def get_biosample_by_tracking_id(self, tracking_id: str) -> Biosample:
        """Retrieve a Biosample by tracking_id."""
        return self._get_row_from_table_with_tracking_id("biosample", tracking_id)

    def get_biosample_by_subject_and_protocol(
        self, subject_id: str, protocol_id: str
    ) -> Biosample:
        """Retrieve a Biosample by subject and protocol IDs."""
        query = {
            "subject": {"operator": "=", "value": subject_id},
            "protocol": {"operator": "=", "value": protocol_id},
        }
        return self._get_row_from_table_with_query("biosample", query=query)

    def relabel_biosample(self, local_id: str, new_tracking_id: str) -> Biosample:
        """Update the tracking_id for a Biosample by local_id."""
        # 1. Query for row matching local_id
        # 2. Set the new value
        # 3. Do database update via vbr_client.update_row()
        # 4. TODO Create and link a 'rename' data_event
        bsam = self.get_biosample_by_local_id(local_id)
        original_tracking_id = bsam.tracking_id
        bsam.tracking_id = new_tracking_id
        bsam = self.vbr_client.update_row(bsam)
        DataEventApi.create_and_link(
            self,
            comment="Relabeled from original tracking ID {0}".format(
                original_tracking_id
            ),
            link_target=bsam,
        )
        return bsam

    def create_biosample(
        self,
        tracking_id: str,
        subject_id: int,
        project_id: int,
        protocol_id: int,
        anatomy_id: int,
        creation_timestr: str = None,
    ) -> Biosample:
        """Create a new Biosample."""
        # TODO - Add a data_event marking the creation
        bs = Biosample(
            tracking_id=tracking_id,
            subject=subject_id,
            project=project_id,
            protocol=protocol_id,
            anatomy=anatomy_id,
            creation_time=creation_timestr,
        )
        try:
            return self.vbr_client.create_row(bs)[0]
        except Exception:
            raise

    def create_or_get_biosample_by_tracking_id(
        self,
        tracking_id: str,
        subject_id: int,
        project_id: int,
        protocol_id: int,
        anatomy_id: int,
        creation_timestr: str = None,
    ) -> Biosample:
        """Create a Biosample or return existing with specified tracking_id."""
        try:
            return self.create_biosample(
                tracking_id,
                subject_id,
                project_id,
                protocol_id,
                anatomy_id,
                creation_timestr,
            )
        except Exception:
            return self.get_biosample_by_tracking_id(tracking_id)

    # ! Relocate (new location or inside another container)
    # Update status
