from re import M
from typing import List

from vbr.pgrest.time import timestamp
from vbr.tableclasses import Biosample, File
from vbr.utils import utc_time_in_seconds

from .data_event import DataEventApi

DEFAULT_VOLUME_ML = 0.5

__all__ = ["FileApi"]


class FileApi(object):
    def get_file(self, pkid: str) -> File:
        """Retrieve a Measurement by primary identifier."""
        return self._get_row_from_table_with_id("file", pkid)

    def get_file_by_local_id(self, local_id: str) -> File:
        """Retrieve a File by local_id."""
        return self._get_row_from_table_with_local_id("file", local_id)

    def get_file_by_tracking_id(self, tracking_id: str) -> File:
        """Retrieve a File by tracking_id."""
        return self._get_row_from_table_with_tracking_id("file", tracking_id)

    def create_file(
        self,
        file: int,
        project_id: int,
        tracking_id: str,
        size_in_bytes: int,
        uncompressed_size_in_bytes: int,
        sha256: str,
        md5: str,
        filename: str,
        file_format: int,
        data_type: int,
        assay_type: int,
        mime_type: str = None,
        creation_timestr: str = None,
    ) -> File:
        """Create a new File."""
        # TODO - data_event
        fr = File(
            file_id=file,
            project=project_id,
            tracking_id=tracking_id,
            size_in_bytes=size_in_bytes,
            uncompressed_size_in_bytes=uncompressed_size_in_bytes,
            sha256=sha256,
            md5=md5,
            filename=filename,
            file_format=file_format,
            data_type=data_type,
            assay_type=assay_type,
            mime_type=mime_type,
            creation_time=creation_timestr,
        )
        try:
            return self.vbr_client.create_row(fr)[0]
        except Exception:
            raise

    def create_or_get_file_by_tracking_id(
        self,
        file: int,
        project_id: int,
        tracking_id: str,
        size_in_bytes: int,
        uncompressed_size_in_bytes: int,
        sha256: str,
        md5: str,
        filename: str,
        file_format: int,
        data_type: int,
        assay_type: int,
        mime_type: str = None,
        creation_timestr: str = None,
    ) -> File:
        """Create a File or return existing with specified tracking_id."""
        try:
            return self.create_file(
                file,
                project_id,
                tracking_id,
                size_in_bytes,
                uncompressed_size_in_bytes,
                sha256,
                md5,
                filename,
                file_format,
                data_type,
                assay_type,
                mime_type,
                creation_timestr,
            )
        except Exception:
            return self.get_file_by_tracking_id(tracking_id)

    
