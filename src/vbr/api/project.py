from vbr.tableclasses import Project

__all__ = ['ProjectApi']


class ProjectApi(object):
    def get_project(self, pkid: str) -> Project:
        """Retrieve a Project by primary identifier."""
        return self._get_row_from_table_with_id('project', pkid)

    def get_project_by_local_id(self, local_id: str) -> Project:
        raise NotImplemented('Projects do not have local_id')

    def get_project_by_tracking_id(self, tracking_id: str) -> Project:
        raise NotImplemented('Projects do not have tracking_id')

    def redcap_to_vbr_project(self, redcap_record_id: str) -> Project:
        """Retrieve a Project via its REDCap project identifier."""
        # TODO - write real mapping code for this.
        # Need a canonical list of REDCap project_ids that map to the A2CPS project
        # The annoying thing is that we have multiple REDcap projects
        # mapping to a single VBR Project, so just using a persistent id
        # in the Project record won't do it. I suppose it could be a list but
        # that is not great design.
        return self.get_project(pkid=1)

    def redcap_to_vbr_project_id(self, redcap_record_id: str) -> str:
        """Return the VBR project_id for a given REDCap project identifier."""
        return self.redcap_to_vbr_project(redcap_record_id).project_id

    def relabel_project(self, local_id: str, new_tracking_id: str) -> Project:
        raise NotImplemented('Projects do not have tracking_id')
