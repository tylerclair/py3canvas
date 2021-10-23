"""Progress API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ProgressAPI(BaseCanvasAPI):
    """Progress API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ProgressAPI."""
        super(ProgressAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ProgressAPI")

    def query_progress(self, id):
        """
        Query progress.

        Return completion and status information about an asynchronous job
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/v1/progress/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/progress/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def query_progress(self, course_id, id):
        """
        Query progress.

        Return completion and status information about an asynchronous job
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
            "GET /api/lti/courses/{course_id}/progress/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/lti/courses/{course_id}/progress/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Progress(BaseModel):
    """Progress Model."""

    def __init__(
        self,
        id=None,
        context_id=None,
        context_type=None,
        user_id=None,
        tag=None,
        completion=None,
        workflow_state=None,
        created_at=None,
        updated_at=None,
        message=None,
        results=None,
        url=None,
    ):
        """Init method for Progress class."""
        self._id = id
        self._context_id = context_id
        self._context_type = context_type
        self._user_id = user_id
        self._tag = tag
        self._completion = completion
        self._workflow_state = workflow_state
        self._created_at = created_at
        self._updated_at = updated_at
        self._message = message
        self._results = results
        self._url = url

        self.logger = logging.getLogger("py3canvas.Progress")

    @property
    def id(self):
        """the ID of the Progress object."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def context_id(self):
        """the context owning the job."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn(
            "Setting values on context_id will NOT update the remote Canvas instance."
        )
        self._context_id = value

    @property
    def context_type(self):
        """context_type."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn(
            "Setting values on context_type will NOT update the remote Canvas instance."
        )
        self._context_type = value

    @property
    def user_id(self):
        """the id of the user who started the job."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def tag(self):
        """the type of operation."""
        return self._tag

    @tag.setter
    def tag(self, value):
        """Setter for tag property."""
        self.logger.warn(
            "Setting values on tag will NOT update the remote Canvas instance."
        )
        self._tag = value

    @property
    def completion(self):
        """percent completed."""
        return self._completion

    @completion.setter
    def completion(self, value):
        """Setter for completion property."""
        self.logger.warn(
            "Setting values on completion will NOT update the remote Canvas instance."
        )
        self._completion = value

    @property
    def workflow_state(self):
        """the state of the job one of 'queued', 'running', 'completed', 'failed'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def created_at(self):
        """the time the job was created."""
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
        """the time the job was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value

    @property
    def message(self):
        """optional details about the job."""
        return self._message

    @message.setter
    def message(self, value):
        """Setter for message property."""
        self.logger.warn(
            "Setting values on message will NOT update the remote Canvas instance."
        )
        self._message = value

    @property
    def results(self):
        """optional results of the job. omitted when job is still pending."""
        return self._results

    @results.setter
    def results(self, value):
        """Setter for results property."""
        self.logger.warn(
            "Setting values on results will NOT update the remote Canvas instance."
        )
        self._results = value

    @property
    def url(self):
        """url where a progress update can be retrieved with an LTI access token."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn(
            "Setting values on url will NOT update the remote Canvas instance."
        )
        self._url = value
