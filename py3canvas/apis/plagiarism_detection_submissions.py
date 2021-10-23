"""PlagiarismDetectionSubmissions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PlagiarismDetectionSubmissionsAPI(BaseCanvasAPI):
    """PlagiarismDetectionSubmissions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PlagiarismDetectionSubmissionsAPI."""
        super(PlagiarismDetectionSubmissionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PlagiarismDetectionSubmissionsAPI")

    def get_single_submission(self, assignment_id, submission_id):
        """
        Get a single submission.

        Get a single submission, based on submission id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id

        self.logger.debug(
            "GET /api/lti/assignments/{assignment_id}/submissions/{submission_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/lti/assignments/{assignment_id}/submissions/{submission_id}".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_history_of_single_submission(self, assignment_id, submission_id):
        """
        Get the history of a single submission.

        Get a list of all attempts made for a submission, based on submission id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id

        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id

        self.logger.debug(
            "GET /api/lti/assignments/{assignment_id}/submissions/{submission_id}/history with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/history".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )


class Submission(BaseModel):
    """Submission Model."""

    def __init__(
        self,
        lti_course_id=None,
        course_id=None,
        assignment_id=None,
        attempt=None,
        body=None,
        submission_type=None,
        submitted_at=None,
        url=None,
        user_id=None,
        eula_agreement_timestamp=None,
        workflow_state=None,
        attachments=None,
    ):
        """Init method for Submission class."""
        self._lti_course_id = lti_course_id
        self._course_id = course_id
        self._assignment_id = assignment_id
        self._attempt = attempt
        self._body = body
        self._submission_type = submission_type
        self._submitted_at = submitted_at
        self._url = url
        self._user_id = user_id
        self._eula_agreement_timestamp = eula_agreement_timestamp
        self._workflow_state = workflow_state
        self._attachments = attachments

        self.logger = logging.getLogger("py3canvas.Submission")

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
    def assignment_id(self):
        """The submission's assignment id."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn(
            "Setting values on assignment_id will NOT update the remote Canvas instance."
        )
        self._assignment_id = value

    @property
    def attempt(self):
        """This is the submission attempt number."""
        return self._attempt

    @attempt.setter
    def attempt(self, value):
        """Setter for attempt property."""
        self.logger.warn(
            "Setting values on attempt will NOT update the remote Canvas instance."
        )
        self._attempt = value

    @property
    def body(self):
        """The content of the submission, if it was submitted directly in a text field."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn(
            "Setting values on body will NOT update the remote Canvas instance."
        )
        self._body = value

    @property
    def submission_type(self):
        """The types of submission ex: ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_annotation')."""
        return self._submission_type

    @submission_type.setter
    def submission_type(self, value):
        """Setter for submission_type property."""
        self.logger.warn(
            "Setting values on submission_type will NOT update the remote Canvas instance."
        )
        self._submission_type = value

    @property
    def submitted_at(self):
        """The timestamp when the assignment was submitted."""
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, value):
        """Setter for submitted_at property."""
        self.logger.warn(
            "Setting values on submitted_at will NOT update the remote Canvas instance."
        )
        self._submitted_at = value

    @property
    def url(self):
        """The URL of the submission (for 'online_url' submissions)."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn(
            "Setting values on url will NOT update the remote Canvas instance."
        )
        self._url = value

    @property
    def user_id(self):
        """The id of the user who created the submission."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def eula_agreement_timestamp(self):
        """UTC timestamp showing when the user agreed to the EULA (if given by the tool provider)."""
        return self._eula_agreement_timestamp

    @eula_agreement_timestamp.setter
    def eula_agreement_timestamp(self, value):
        """Setter for eula_agreement_timestamp property."""
        self.logger.warn(
            "Setting values on eula_agreement_timestamp will NOT update the remote Canvas instance."
        )
        self._eula_agreement_timestamp = value

    @property
    def workflow_state(self):
        """The current state of the submission."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def attachments(self):
        """Files that are attached to the submission."""
        return self._attachments

    @attachments.setter
    def attachments(self, value):
        """Setter for attachments property."""
        self.logger.warn(
            "Setting values on attachments will NOT update the remote Canvas instance."
        )
        self._attachments = value


class File(BaseModel):
    """File Model."""

    def __init__(
        self,
        size=None,
        content_type=None,
        url=None,
        id=None,
        display_name=None,
        created_at=None,
        updated_at=None,
    ):
        """Init method for File class."""
        self._size = size
        self._content_type = content_type
        self._url = url
        self._id = id
        self._display_name = display_name
        self._created_at = created_at
        self._updated_at = updated_at

        self.logger = logging.getLogger("py3canvas.File")

    @property
    def size(self):
        """size."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size property."""
        self.logger.warn(
            "Setting values on size will NOT update the remote Canvas instance."
        )
        self._size = value

    @property
    def content_type(self):
        """content_type."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn(
            "Setting values on content_type will NOT update the remote Canvas instance."
        )
        self._content_type = value

    @property
    def url(self):
        """url."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn(
            "Setting values on url will NOT update the remote Canvas instance."
        )
        self._url = value

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
    def display_name(self):
        """display_name."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn(
            "Setting values on display_name will NOT update the remote Canvas instance."
        )
        self._display_name = value

    @property
    def created_at(self):
        """created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def updated_at(self):
        """updated_at."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value
