"""SisImportErrors API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class SisImportErrorsAPI(BaseCanvasAPI):
    """SisImportErrors API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SisImportErrorsAPI."""
        super(SisImportErrorsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SisImportErrorsAPI")

    def get_sis_import_error_list_sis_imports(self, account_id, id, failure=None):
        """
        Get SIS import error list.

        Returns the list of SIS import errors for an account or a SIS import. Import
        errors are only stored for 30 days.
        
        Example:
          curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
            -H "Authorization: Bearer <token>"
        
        Example:
          curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
            -H "Authorization: Bearer <token>"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - failure
        """
            If set, only shows errors on a sis import that would cause a failure.
        """
        if failure is not None:
            params["failure"] = failure


        self.logger.debug("GET /api/v1/accounts/{account_id}/sis_imports/{id}/errors with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/sis_imports/{id}/errors".format(**path), data=data, params=params, all_pages=True)

    def get_sis_import_error_list_sis_import_errors(self, account_id, failure=None):
        """
        Get SIS import error list.

        Returns the list of SIS import errors for an account or a SIS import. Import
        errors are only stored for 30 days.
        
        Example:
          curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<id>/sis_import_errors' \
            -H "Authorization: Bearer <token>"
        
        Example:
          curl 'https://<canvas>/api/v1/accounts/<account_id>/sis_import_errors' \
            -H "Authorization: Bearer <token>"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # OPTIONAL - failure
        """
            If set, only shows errors on a sis import that would cause a failure.
        """
        if failure is not None:
            params["failure"] = failure


        self.logger.debug("GET /api/v1/accounts/{account_id}/sis_import_errors with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/sis_import_errors".format(**path), data=data, params=params, all_pages=True)


class Sisimporterror(BaseModel):
    """Sisimporterror Model."""

    def __init__(self, sis_import_id=None, file=None, message=None, row_info=None, row=None):
        """Init method for Sisimporterror class."""
        self._sis_import_id = sis_import_id
        self._file = file
        self._message = message
        self._row_info = row_info
        self._row = row

        self.logger = logging.getLogger('py3canvas.Sisimporterror')

    @property
    def sis_import_id(self):
        """The unique identifier for the SIS import."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn("Setting values on sis_import_id will NOT update the remote Canvas instance.")
        self._sis_import_id = value

    @property
    def file(self):
        """The file where the error message occurred."""
        return self._file

    @file.setter
    def file(self, value):
        """Setter for file property."""
        self.logger.warn("Setting values on file will NOT update the remote Canvas instance.")
        self._file = value

    @property
    def message(self):
        """The error message that from the record."""
        return self._message

    @message.setter
    def message(self, value):
        """Setter for message property."""
        self.logger.warn("Setting values on message will NOT update the remote Canvas instance.")
        self._message = value

    @property
    def row_info(self):
        """The contents of the line that had the error."""
        return self._row_info

    @row_info.setter
    def row_info(self, value):
        """Setter for row_info property."""
        self.logger.warn("Setting values on row_info will NOT update the remote Canvas instance.")
        self._row_info = value

    @property
    def row(self):
        """The line number where the error occurred. Some Importers do not yet support this. This is a 1 based index starting with the header row."""
        return self._row

    @row.setter
    def row(self, value):
        """Setter for row property."""
        self.logger.warn("Setting values on row will NOT update the remote Canvas instance.")
        self._row = value

