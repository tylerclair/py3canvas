"""EnrollmentTerms API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class EnrollmentTermsAPI(BaseCanvasAPI):
    """EnrollmentTerms API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for EnrollmentTermsAPI."""
        super(EnrollmentTermsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.EnrollmentTermsAPI")

    def create_enrollment_term(
        self,
        account_id,
        enrollment_term_end_at=None,
        enrollment_term_name=None,
        enrollment_term_overrides_enrollment_type_end_at=None,
        enrollment_term_overrides_enrollment_type_start_at=None,
        enrollment_term_sis_term_id=None,
        enrollment_term_start_at=None,
    ):
        """
        Create enrollment term.

        Create a new enrollment term for the specified account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - enrollment_term[name]
        """
            The name of the term.
        """
        if enrollment_term_name is not None:
            data["enrollment_term[name]"] = enrollment_term_name

        # OPTIONAL - enrollment_term[start_at]
        """
            The day/time the term starts.
        Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        """
        if enrollment_term_start_at is not None:
            if issubclass(enrollment_term_start_at.__class__, str):
                enrollment_term_start_at = self._validate_iso8601_string(
                    enrollment_term_start_at
                )
            elif issubclass(enrollment_term_start_at.__class__, date) or issubclass(
                enrollment_term_start_at.__class__, datetime
            ):
                enrollment_term_start_at = enrollment_term_start_at.strftime(
                    "%Y-%m-%dT%H:%M:%S+00:00"
                )
            data["enrollment_term[start_at]"] = enrollment_term_start_at

        # OPTIONAL - enrollment_term[end_at]
        """
            The day/time the term ends.
        Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        """
        if enrollment_term_end_at is not None:
            if issubclass(enrollment_term_end_at.__class__, str):
                enrollment_term_end_at = self._validate_iso8601_string(
                    enrollment_term_end_at
                )
            elif issubclass(enrollment_term_end_at.__class__, date) or issubclass(
                enrollment_term_end_at.__class__, datetime
            ):
                enrollment_term_end_at = enrollment_term_end_at.strftime(
                    "%Y-%m-%dT%H:%M:%S+00:00"
                )
            data["enrollment_term[end_at]"] = enrollment_term_end_at

        # OPTIONAL - enrollment_term[sis_term_id]
        """
            The unique SIS identifier for the term.
        """
        if enrollment_term_sis_term_id is not None:
            data["enrollment_term[sis_term_id]"] = enrollment_term_sis_term_id

        # OPTIONAL - enrollment_term[overrides][enrollment_type][start_at]
        """
            The day/time the term starts, overridden for the given enrollment type.
        *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment
        """
        if enrollment_term_overrides_enrollment_type_start_at is not None:
            if issubclass(
                enrollment_term_overrides_enrollment_type_start_at.__class__, str
            ):
                enrollment_term_overrides_enrollment_type_start_at = (
                    self._validate_iso8601_string(
                        enrollment_term_overrides_enrollment_type_start_at
                    )
                )
            elif issubclass(
                enrollment_term_overrides_enrollment_type_start_at.__class__, date
            ) or issubclass(
                enrollment_term_overrides_enrollment_type_start_at.__class__, datetime
            ):
                enrollment_term_overrides_enrollment_type_start_at = (
                    enrollment_term_overrides_enrollment_type_start_at.strftime(
                        "%Y-%m-%dT%H:%M:%S+00:00"
                    )
                )
            data[
                "enrollment_term[overrides][enrollment_type][start_at]"
            ] = enrollment_term_overrides_enrollment_type_start_at

        # OPTIONAL - enrollment_term[overrides][enrollment_type][end_at]
        """
            The day/time the term ends, overridden for the given enrollment type.
        *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment
        """
        if enrollment_term_overrides_enrollment_type_end_at is not None:
            if issubclass(
                enrollment_term_overrides_enrollment_type_end_at.__class__, str
            ):
                enrollment_term_overrides_enrollment_type_end_at = (
                    self._validate_iso8601_string(
                        enrollment_term_overrides_enrollment_type_end_at
                    )
                )
            elif issubclass(
                enrollment_term_overrides_enrollment_type_end_at.__class__, date
            ) or issubclass(
                enrollment_term_overrides_enrollment_type_end_at.__class__, datetime
            ):
                enrollment_term_overrides_enrollment_type_end_at = (
                    enrollment_term_overrides_enrollment_type_end_at.strftime(
                        "%Y-%m-%dT%H:%M:%S+00:00"
                    )
                )
            data[
                "enrollment_term[overrides][enrollment_type][end_at]"
            ] = enrollment_term_overrides_enrollment_type_end_at

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/terms with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/terms".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_enrollment_term(
        self,
        account_id,
        id,
        enrollment_term_end_at=None,
        enrollment_term_name=None,
        enrollment_term_overrides_enrollment_type_end_at=None,
        enrollment_term_overrides_enrollment_type_start_at=None,
        enrollment_term_sis_term_id=None,
        enrollment_term_start_at=None,
    ):
        """
        Update enrollment term.

        Update an existing enrollment term for the specified account.
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

        # OPTIONAL - enrollment_term[name]
        """
            The name of the term.
        """
        if enrollment_term_name is not None:
            data["enrollment_term[name]"] = enrollment_term_name

        # OPTIONAL - enrollment_term[start_at]
        """
            The day/time the term starts.
        Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        """
        if enrollment_term_start_at is not None:
            if issubclass(enrollment_term_start_at.__class__, str):
                enrollment_term_start_at = self._validate_iso8601_string(
                    enrollment_term_start_at
                )
            elif issubclass(enrollment_term_start_at.__class__, date) or issubclass(
                enrollment_term_start_at.__class__, datetime
            ):
                enrollment_term_start_at = enrollment_term_start_at.strftime(
                    "%Y-%m-%dT%H:%M:%S+00:00"
                )
            data["enrollment_term[start_at]"] = enrollment_term_start_at

        # OPTIONAL - enrollment_term[end_at]
        """
            The day/time the term ends.
        Accepts times in ISO 8601 format, e.g. 2015-01-10T18:48:00Z.
        """
        if enrollment_term_end_at is not None:
            if issubclass(enrollment_term_end_at.__class__, str):
                enrollment_term_end_at = self._validate_iso8601_string(
                    enrollment_term_end_at
                )
            elif issubclass(enrollment_term_end_at.__class__, date) or issubclass(
                enrollment_term_end_at.__class__, datetime
            ):
                enrollment_term_end_at = enrollment_term_end_at.strftime(
                    "%Y-%m-%dT%H:%M:%S+00:00"
                )
            data["enrollment_term[end_at]"] = enrollment_term_end_at

        # OPTIONAL - enrollment_term[sis_term_id]
        """
            The unique SIS identifier for the term.
        """
        if enrollment_term_sis_term_id is not None:
            data["enrollment_term[sis_term_id]"] = enrollment_term_sis_term_id

        # OPTIONAL - enrollment_term[overrides][enrollment_type][start_at]
        """
            The day/time the term starts, overridden for the given enrollment type.
        *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment
        """
        if enrollment_term_overrides_enrollment_type_start_at is not None:
            if issubclass(
                enrollment_term_overrides_enrollment_type_start_at.__class__, str
            ):
                enrollment_term_overrides_enrollment_type_start_at = (
                    self._validate_iso8601_string(
                        enrollment_term_overrides_enrollment_type_start_at
                    )
                )
            elif issubclass(
                enrollment_term_overrides_enrollment_type_start_at.__class__, date
            ) or issubclass(
                enrollment_term_overrides_enrollment_type_start_at.__class__, datetime
            ):
                enrollment_term_overrides_enrollment_type_start_at = (
                    enrollment_term_overrides_enrollment_type_start_at.strftime(
                        "%Y-%m-%dT%H:%M:%S+00:00"
                    )
                )
            data[
                "enrollment_term[overrides][enrollment_type][start_at]"
            ] = enrollment_term_overrides_enrollment_type_start_at

        # OPTIONAL - enrollment_term[overrides][enrollment_type][end_at]
        """
            The day/time the term ends, overridden for the given enrollment type.
        *enrollment_type* can be one of StudentEnrollment, TeacherEnrollment, TaEnrollment, or DesignerEnrollment
        """
        if enrollment_term_overrides_enrollment_type_end_at is not None:
            if issubclass(
                enrollment_term_overrides_enrollment_type_end_at.__class__, str
            ):
                enrollment_term_overrides_enrollment_type_end_at = (
                    self._validate_iso8601_string(
                        enrollment_term_overrides_enrollment_type_end_at
                    )
                )
            elif issubclass(
                enrollment_term_overrides_enrollment_type_end_at.__class__, date
            ) or issubclass(
                enrollment_term_overrides_enrollment_type_end_at.__class__, datetime
            ):
                enrollment_term_overrides_enrollment_type_end_at = (
                    enrollment_term_overrides_enrollment_type_end_at.strftime(
                        "%Y-%m-%dT%H:%M:%S+00:00"
                    )
                )
            data[
                "enrollment_term[overrides][enrollment_type][end_at]"
            ] = enrollment_term_overrides_enrollment_type_end_at

        self.logger.debug(
            "PUT /api/v1/accounts/{account_id}/terms/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/terms/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_enrollment_term(self, account_id, id):
        """
        Delete enrollment term.

        Delete the specified enrollment term.
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
            "DELETE /api/v1/accounts/{account_id}/terms/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/accounts/{account_id}/terms/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def list_enrollment_terms(self, account_id, include=None, workflow_state=None):
        """
        List enrollment terms.

        An object with a paginated list of all of the terms in the account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - workflow_state
        """
            If set, only returns terms that are in the given state.
        Defaults to 'active'.
        """
        if workflow_state is not None:
            self._validate_enum(workflow_state, ["active", "deleted", "all"])
            params["workflow_state"] = workflow_state

        # OPTIONAL - include
        """
            Array of additional information to include.

        "overrides":: term start/end dates overridden for different enrollment types
        """
        if include is not None:
            self._validate_enum(include, ["overrides"])
            params["include"] = include

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/terms with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/terms".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def retrieve_enrollment_term(self, account_id, id):
        """
        Retrieve enrollment term.

        Retrieves the details for an enrollment term in the account. Includes overrides by default.
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
            "GET /api/v1/accounts/{account_id}/terms/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/terms/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Enrollmentterm(BaseModel):
    """Enrollmentterm Model."""

    def __init__(
        self,
        id=None,
        sis_term_id=None,
        sis_import_id=None,
        name=None,
        start_at=None,
        end_at=None,
        workflow_state=None,
        overrides=None,
    ):
        """Init method for Enrollmentterm class."""
        self._id = id
        self._sis_term_id = sis_term_id
        self._sis_import_id = sis_import_id
        self._name = name
        self._start_at = start_at
        self._end_at = end_at
        self._workflow_state = workflow_state
        self._overrides = overrides

        self.logger = logging.getLogger("py3canvas.Enrollmentterm")

    @property
    def id(self):
        """The unique identifier for the enrollment term."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def sis_term_id(self):
        """The SIS id of the term. Only included if the user has permission to view SIS information."""
        return self._sis_term_id

    @sis_term_id.setter
    def sis_term_id(self, value):
        """Setter for sis_term_id property."""
        self.logger.warn(
            "Setting values on sis_term_id will NOT update the remote Canvas instance."
        )
        self._sis_term_id = value

    @property
    def sis_import_id(self):
        """the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn(
            "Setting values on sis_import_id will NOT update the remote Canvas instance."
        )
        self._sis_import_id = value

    @property
    def name(self):
        """The name of the term."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def start_at(self):
        """The datetime of the start of the term."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn(
            "Setting values on start_at will NOT update the remote Canvas instance."
        )
        self._start_at = value

    @property
    def end_at(self):
        """The datetime of the end of the term."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn(
            "Setting values on end_at will NOT update the remote Canvas instance."
        )
        self._end_at = value

    @property
    def workflow_state(self):
        """The state of the term. Can be 'active' or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def overrides(self):
        """Term date overrides for specific enrollment types."""
        return self._overrides

    @overrides.setter
    def overrides(self, value):
        """Setter for overrides property."""
        self.logger.warn(
            "Setting values on overrides will NOT update the remote Canvas instance."
        )
        self._overrides = value


class Enrollmenttermslist(BaseModel):
    """Enrollmenttermslist Model."""

    def __init__(self, enrollment_terms=None):
        """Init method for Enrollmenttermslist class."""
        self._enrollment_terms = enrollment_terms

        self.logger = logging.getLogger("py3canvas.Enrollmenttermslist")

    @property
    def enrollment_terms(self):
        """a paginated list of all terms in the account."""
        return self._enrollment_terms

    @enrollment_terms.setter
    def enrollment_terms(self, value):
        """Setter for enrollment_terms property."""
        self.logger.warn(
            "Setting values on enrollment_terms will NOT update the remote Canvas instance."
        )
        self._enrollment_terms = value
