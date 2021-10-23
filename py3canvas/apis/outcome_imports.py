"""OutcomeImports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class OutcomeImportsAPI(BaseCanvasAPI):
    """OutcomeImports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for OutcomeImportsAPI."""
        super(OutcomeImportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.OutcomeImportsAPI")

    def import_outcomes_accounts(
        self, account_id, attachment=None, extension=None, import_type=None
    ):
        """
        Import Outcomes.

        Import outcomes into Canvas.

        For more information on the format that's expected here, please see the
        "Outcomes CSV" section in the API docs.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - import_type
        """
            Choose the data format for reading outcome data. With a standard Canvas
        install, this option can only be 'instructure_csv', and if unprovided,
        will be assumed to be so. Can be part of the query string.
        """
        if import_type is not None:
            data["import_type"] = import_type

        # OPTIONAL - attachment
        """
            There are two ways to post outcome import data - either via a
        multipart/form-data form-field-style attachment, or via a non-multipart
        raw post request.

        'attachment' is required for multipart/form-data style posts. Assumed to
        be outcome data from a file upload form field named 'attachment'.

        Examples:
          curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'
          curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv'

        If you decide to do a raw post, you can skip the 'attachment' argument,
        but you will then be required to provide a suitable Content-Type header.
        You are encouraged to also provide the 'extension' argument.

        Examples:
          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'

          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv'
        """
        if attachment is not None:
            data["attachment"] = attachment

        # OPTIONAL - extension
        """
            Recommended for raw post request style imports. This field will be used to
        distinguish between csv and other file format extensions that
        would usually be provided with the filename in the multipart post request
        scenario. If not provided, this value will be inferred from the
        Content-Type, falling back to csv-file format if all else fails.
        """
        if extension is not None:
            data["extension"] = extension

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/outcome_imports with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/outcome_imports".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def import_outcomes_courses(
        self, course_id, attachment=None, extension=None, import_type=None
    ):
        """
        Import Outcomes.

        Import outcomes into Canvas.

        For more information on the format that's expected here, please see the
        "Outcomes CSV" section in the API docs.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - import_type
        """
            Choose the data format for reading outcome data. With a standard Canvas
        install, this option can only be 'instructure_csv', and if unprovided,
        will be assumed to be so. Can be part of the query string.
        """
        if import_type is not None:
            data["import_type"] = import_type

        # OPTIONAL - attachment
        """
            There are two ways to post outcome import data - either via a
        multipart/form-data form-field-style attachment, or via a non-multipart
        raw post request.

        'attachment' is required for multipart/form-data style posts. Assumed to
        be outcome data from a file upload form field named 'attachment'.

        Examples:
          curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'
          curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv'

        If you decide to do a raw post, you can skip the 'attachment' argument,
        but you will then be required to provide a suitable Content-Type header.
        You are encouraged to also provide the 'extension' argument.

        Examples:
          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports?import_type=instructure_csv'

          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              'https://<canvas>/api/v1/courses/<course_id>/outcome_imports?import_type=instructure_csv'
        """
        if attachment is not None:
            data["attachment"] = attachment

        # OPTIONAL - extension
        """
            Recommended for raw post request style imports. This field will be used to
        distinguish between csv and other file format extensions that
        would usually be provided with the filename in the multipart post request
        scenario. If not provided, this value will be inferred from the
        Content-Type, falling back to csv-file format if all else fails.
        """
        if extension is not None:
            data["extension"] = extension

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/outcome_imports with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/outcome_imports".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_outcome_import_status_accounts(self, account_id, id):
        """
        Get Outcome import status.

        Get the status of an already created Outcome import. Pass 'latest' for the outcome import id
        for the latest import.
        
          Examples:
            curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
                -H "Authorization: Bearer <token>"
            curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
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

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/outcome_imports/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/outcome_imports/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_outcome_import_status_courses(self, course_id, id):
        """
        Get Outcome import status.

        Get the status of an already created Outcome import. Pass 'latest' for the outcome import id
        for the latest import.
        
          Examples:
            curl 'https://<canvas>/api/v1/accounts/<account_id>/outcome_imports/<outcome_import_id>' \
                -H "Authorization: Bearer <token>"
            curl 'https://<canvas>/api/v1/courses/<course_id>/outcome_imports/<outcome_import_id>' \
                -H "Authorization: Bearer <token>"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/outcome_imports/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/outcome_imports/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Outcomeimportdata(BaseModel):
    """Outcomeimportdata Model."""

    def __init__(self, import_type=None):
        """Init method for Outcomeimportdata class."""
        self._import_type = import_type

        self.logger = logging.getLogger("py3canvas.Outcomeimportdata")

    @property
    def import_type(self):
        """The type of outcome import."""
        return self._import_type

    @import_type.setter
    def import_type(self, value):
        """Setter for import_type property."""
        self.logger.warn(
            "Setting values on import_type will NOT update the remote Canvas instance."
        )
        self._import_type = value


class Outcomeimport(BaseModel):
    """Outcomeimport Model."""

    def __init__(
        self,
        id=None,
        created_at=None,
        ended_at=None,
        updated_at=None,
        workflow_state=None,
        data=None,
        progress=None,
        user=None,
        processing_errors=None,
    ):
        """Init method for Outcomeimport class."""
        self._id = id
        self._created_at = created_at
        self._ended_at = ended_at
        self._updated_at = updated_at
        self._workflow_state = workflow_state
        self._data = data
        self._progress = progress
        self._user = user
        self._processing_errors = processing_errors

        self.logger = logging.getLogger("py3canvas.Outcomeimport")

    @property
    def id(self):
        """The unique identifier for the outcome import."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def created_at(self):
        """The date the outcome import was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def ended_at(self):
        """The date the outcome import finished. Returns null if not finished."""
        return self._ended_at

    @ended_at.setter
    def ended_at(self, value):
        """Setter for ended_at property."""
        self.logger.warn(
            "Setting values on ended_at will NOT update the remote Canvas instance."
        )
        self._ended_at = value

    @property
    def updated_at(self):
        """The date the outcome import was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value

    @property
    def workflow_state(self):
        """The current state of the outcome import.
        - 'created': The outcome import has been created.
        - 'importing': The outcome import is currently processing.
        - 'succeeded': The outcome import has completed successfully.
        - 'failed': The outcome import failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def data(self):
        """See the OutcomeImportData specification above."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn(
            "Setting values on data will NOT update the remote Canvas instance."
        )
        self._data = value

    @property
    def progress(self):
        """The progress of the outcome import."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn(
            "Setting values on progress will NOT update the remote Canvas instance."
        )
        self._progress = value

    @property
    def user(self):
        """The user that initiated the outcome_import. See the Users API for details."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn(
            "Setting values on user will NOT update the remote Canvas instance."
        )
        self._user = value

    @property
    def processing_errors(self):
        """An array of row number / error message pairs. Returns the first 25 errors."""
        return self._processing_errors

    @processing_errors.setter
    def processing_errors(self, value):
        """Setter for processing_errors property."""
        self.logger.warn(
            "Setting values on processing_errors will NOT update the remote Canvas instance."
        )
        self._processing_errors = value
