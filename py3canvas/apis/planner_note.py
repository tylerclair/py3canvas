"""PlannerNote API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PlannerNoteAPI(BaseCanvasAPI):
    """PlannerNote API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PlannerNoteAPI."""
        super(PlannerNoteAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PlannerNoteAPI")

    def list_planner_notes(self):
        """
        List planner notes.

        Retrieve the list of planner notes

        Retrieve planner note for a user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/planner_notes with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/planner_notes".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def show_plannernote(self, id):
        """
        Show a PlannerNote.

        Retrieve a planner note for the current user
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
            "GET /api/v1/planner_notes/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/planner_notes/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_plannernote(self, id):
        """
        Update a PlannerNote.

        Update a planner note for the current user
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
            "PUT /api/v1/planner_notes/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/planner_notes/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def create_planner_note(self):
        """
        Create a planner note.

        Create a planner note for the current user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "POST /api/v1/planner_notes with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/planner_notes".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_planner_note(self, id):
        """
        Delete a planner note.

        Delete a planner note for the current user
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
            "DELETE /api/v1/planner_notes/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/planner_notes/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Plannernote(BaseModel):
    """Plannernote Model.
    A planner note"""

    def __init__(
        self,
        id=None,
        title=None,
        description=None,
        user_id=None,
        workflow_state=None,
        course_id=None,
        todo_date=None,
    ):
        """Init method for Plannernote class."""
        self._id = id
        self._title = title
        self._description = description
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._course_id = course_id
        self._todo_date = todo_date

        self.logger = logging.getLogger("py3canvas.Plannernote")

    @property
    def id(self):
        """The ID of the planner note."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def title(self):
        """The title for a planner note."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn(
            "Setting values on title will NOT update the remote Canvas instance."
        )
        self._title = value

    @property
    def description(self):
        """The description of the planner note."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn(
            "Setting values on description will NOT update the remote Canvas instance."
        )
        self._description = value

    @property
    def user_id(self):
        """The id of the associated user creating the planner note."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def workflow_state(self):
        """The current published state of the planner note."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def course_id(self):
        """The course that the note is in relation too, if applicable."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn(
            "Setting values on course_id will NOT update the remote Canvas instance."
        )
        self._course_id = value

    @property
    def todo_date(self):
        """The datetime of when the planner note should show up on their planner."""
        return self._todo_date

    @todo_date.setter
    def todo_date(self, value):
        """Setter for todo_date property."""
        self.logger.warn(
            "Setting values on todo_date will NOT update the remote Canvas instance."
        )
        self._todo_date = value
