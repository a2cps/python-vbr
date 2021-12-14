from vbr.tableclasses import Project
from vbr.utils import redcaptasks

__all__ = ["ProjectApi"]


class ProjectApi(object):
    def get_project(self, pkid: str) -> Project:
        """Retrieve a Project by primary identifier."""
        return self._get_row_from_table_with_id("project", pkid)

    def get_project_by_local_id(self, local_id: str) -> Project:
        """Retrieve a Project by local_id."""
        return self._get_row_from_table_with_local_id("project", local_id)

    def redcap_to_vbr_project_id(self, redcap_project_id: str) -> str:
        """Return the VBR project_id for a given REDCap project identifier."""
        vbr_project_id = redcaptasks.redcap_to_vbr_project_id(redcap_project_id)
        return vbr_project_id

    def redcap_to_vbr_project(self, redcap_project_id: str) -> Project:
        """Retrieve a Project via its REDCap project identifier."""
        vbr_project_id = self.redcap_to_vbr_project_id(redcap_project_id)
        return self.get_project(vbr_project_id)
