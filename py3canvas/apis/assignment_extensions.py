"""AssignmentExtensions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class AssignmentExtensionsAPI(BaseCanvasAPI):
    """AssignmentExtensions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AssignmentExtensionsAPI."""
        super(AssignmentExtensionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AssignmentExtensionsAPI")

    def set_extensions_for_student_assignment_submissions(
        self,
        assignment_extensions_extra_attempts,
        assignment_extensions_user_id,
        assignment_id,
        course_id,
    ):
        """
        Set extensions for student assignment submissions.

        <b>Responses</b>

        * <b>200 OK</b> if the request was successful
        * <b>403 Forbidden</b> if you are not allowed to extend assignments for this course
        * <b>400 Bad Request</b> if any of the extensions are invalid
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id

        # REQUIRED - assignment_extensions[user_id]
        """
            The ID of the user we want to add assignment extensions for.
        """
        data["assignment_extensions[user_id]"] = assignment_extensions_user_id

        # REQUIRED - assignment_extensions[extra_attempts]
        """
            Number of times the student is allowed to re-take the assignment over the
        limit.
        """
        data[
            "assignment_extensions[extra_attempts]"
        ] = assignment_extensions_extra_attempts

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/assignments/{assignment_id}/extensions with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/extensions".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )


class Assignmentextension(BaseModel):
    """Assignmentextension Model."""

    def __init__(self, assignment_id, user_id, extra_attempts=None):
        """Init method for Assignmentextension class."""
        self._assignment_id = assignment_id
        self._user_id = user_id
        self._extra_attempts = extra_attempts

        self.logger = logging.getLogger("py3canvas.Assignmentextension")

    @property
    def assignment_id(self):
        """The ID of the Assignment the extension belongs to."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn(
            "Setting values on assignment_id will NOT update the remote Canvas instance."
        )
        self._assignment_id = value

    @property
    def user_id(self):
        """The ID of the Student that needs the assignment extension."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def extra_attempts(self):
        """Number of times the student is allowed to re-submit the assignment."""
        return self._extra_attempts

    @extra_attempts.setter
    def extra_attempts(self, value):
        """Setter for extra_attempts property."""
        self.logger.warn(
            "Setting values on extra_attempts will NOT update the remote Canvas instance."
        )
        self._extra_attempts = value
