"""PlagiarismDetectionPlatformAssignments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PlagiarismDetectionPlatformAssignmentsAPI(BaseCanvasAPI):
    """PlagiarismDetectionPlatformAssignments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PlagiarismDetectionPlatformAssignmentsAPI."""
        super(PlagiarismDetectionPlatformAssignmentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger(
            "py3canvas.PlagiarismDetectionPlatformAssignmentsAPI"
        )

    def get_single_assignment_lti(self, assignment_id, user_id=None):
        """
        Get a single assignment (lti).

        Get a single Canvas assignment by Canvas id or LTI id. Tool providers may only access
        assignments that are associated with their tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id

        # OPTIONAL - user_id
        """
            The id of the user. Can be a Canvas or LTI id for the user.
        """
        if user_id is not None:
            params["user_id"] = user_id

        self.logger.debug(
            "GET /api/lti/assignments/{assignment_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/lti/assignments/{assignment_id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Ltiassignment(BaseModel):
    """Ltiassignment Model.
    A Canvas assignment"""

    def __init__(
        self,
        id=None,
        name=None,
        description=None,
        points_possible=None,
        due_at=None,
        lti_id=None,
        course_id=None,
        lti_course_id=None,
    ):
        """Init method for Ltiassignment class."""
        self._id = id
        self._name = name
        self._description = description
        self._points_possible = points_possible
        self._due_at = due_at
        self._lti_id = lti_id
        self._course_id = course_id
        self._lti_course_id = lti_course_id

        self.logger = logging.getLogger("py3canvas.Ltiassignment")

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def name(self):
        """name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn(
            "Setting values on description will NOT update the remote Canvas instance."
        )
        self._description = value

    @property
    def points_possible(self):
        """points_possible."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn(
            "Setting values on points_possible will NOT update the remote Canvas instance."
        )
        self._points_possible = value

    @property
    def due_at(self):
        """The due date for the assignment. If a user id is supplied and an assignment override is in place this field will reflect the due date as it applies to the user."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn(
            "Setting values on due_at will NOT update the remote Canvas instance."
        )
        self._due_at = value

    @property
    def lti_id(self):
        """lti_id."""
        return self._lti_id

    @lti_id.setter
    def lti_id(self, value):
        """Setter for lti_id property."""
        self.logger.warn(
            "Setting values on lti_id will NOT update the remote Canvas instance."
        )
        self._lti_id = value

    @property
    def course_id(self):
        """course_id."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn(
            "Setting values on course_id will NOT update the remote Canvas instance."
        )
        self._course_id = value

    @property
    def lti_course_id(self):
        """lti_course_id."""
        return self._lti_course_id

    @lti_course_id.setter
    def lti_course_id(self, value):
        """Setter for lti_course_id property."""
        self.logger.warn(
            "Setting values on lti_course_id will NOT update the remote Canvas instance."
        )
        self._lti_course_id = value
