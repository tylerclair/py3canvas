"""PlannerOverride API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PlannerOverrideAPI(BaseCanvasAPI):
    """PlannerOverride API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PlannerOverrideAPI."""
        super(PlannerOverrideAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PlannerOverrideAPI")

    def list_planner_items(self, end_date=None, filter=None, start_date=None):
        """
        List planner items.

        Retrieve the list of objects to be shown on the planner for the current user
        with the associated planner override to override an item's visibility if set.
        
        [
          {
            "context_type": "Course",
            "course_id": 1,
            "visible_in_planner": true, // Whether or not it is displayed on the student planner
            "planner_override": { ... planner override object ... }, // Associated PlannerOverride object if user has toggled visibility for the object on the planner
            "submissions": false, // The statuses of the user's submissions for this object
            "plannable_id": "123",
            "plannable_type": "discussion_topic",
            "plannable": { ... discussion topic object },
            "html_url": "/courses/1/discussion_topics/8"
          },
          {
            "context_type": "Course",
            "course_id": 1,
            "visible_in_planner": true,
            "planner_override": {
                "id": 3,
                "plannable_type": "Assignment",
                "plannable_id": 1,
                "user_id": 2,
                "workflow_state": "active",
                "marked_complete": true, // A user-defined setting for marking items complete in the planner
                "dismissed": false, // A user-defined setting for hiding items from the opportunities list
                "deleted_at": null,
                "created_at": "2017-05-18T18:35:55Z",
                "updated_at": "2017-05-18T18:35:55Z"
            },
            "submissions": { // The status as it pertains to the current user
              "excused": false,
              "graded": false,
              "late": false,
              "missing": true,
              "needs_grading": false,
              "with_feedback": false
            },
            "plannable_id": "456",
            "plannable_type": "assignment",
            "plannable": { ... assignment object ...  },
            "html_url": "http://canvas.instructure.com/courses/1/assignments/1#submit"
          },
          {
            "visible_in_planner": true,
            "planner_override": null,
            "submissions": false, // false if no associated assignment exists for the plannable item
            "plannable_id": "789",
            "plannable_type": "planner_note",
            "plannable": {
              "id": 1,
              "todo_date": "2017-05-30T06:00:00Z",
              "title": "hello",
              "details": "world",
              "user_id": 2,
              "course_id": null,
              "workflow_state": "active",
              "created_at": "2017-05-30T16:29:04Z",
              "updated_at": "2017-05-30T16:29:15Z"
            },
            "html_url": "http://canvas.instructure.com/api/v1/planner_notes.1"
          }
        ]
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - start_date
        """
            Only return items starting from the given date.
        The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if start_date is not None:
            params["start_date"] = start_date


        # OPTIONAL - end_date
        """
            Only return items up to the given date.
        The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if end_date is not None:
            params["end_date"] = end_date


        # OPTIONAL - filter
        """
            Only return items that have new or unread activity
        """
        if filter is not None:
            self._validate_enum(filter, ["new_activity"])
            params["filter"] = filter


        self.logger.debug("GET /api/v1/planner/items with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/planner/items".format(**path), data=data, params=params, no_data=True)

    def list_planner_overrides(self):
        """
        List planner overrides.

        Retrieve a planner override for the current user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/planner/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/planner/overrides".format(**path), data=data, params=params, all_pages=True)

    def show_planner_override(self, id):
        """
        Show a planner override.

        Retrieve a planner override for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/planner/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/planner/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def update_planner_override(self, id, dismissed=None, marked_complete=None):
        """
        Update a planner override.

        Update a planner override's visibilty for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - marked_complete
        """
            determines whether the planner item is marked as completed
        """
        if marked_complete is not None:
            data["marked_complete"] = marked_complete


        # OPTIONAL - dismissed
        """
            determines whether the planner item shows in the opportunities list
        """
        if dismissed is not None:
            data["dismissed"] = dismissed


        self.logger.debug("PUT /api/v1/planner/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/planner/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def create_planner_override(self, dismissed=None, marked_complete=None, plannable_id=None, plannable_type=None):
        """
        Create a planner override.

        Create a planner override for the current user
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - plannable_type
        """
            Type of the item that you are overriding in the planner
        """
        if plannable_type is not None:
            self._validate_enum(plannable_type, ["announcement", "assignment", "discussion_topic", "quiz", "wiki_page", "planner_note"])
            data["plannable_type"] = plannable_type


        # OPTIONAL - plannable_id
        """
            ID of the item that you are overriding in the planner
        """
        if plannable_id is not None:
            data["plannable_id"] = plannable_id


        # OPTIONAL - marked_complete
        """
            If this is true, the item will show in the planner as completed
        """
        if marked_complete is not None:
            data["marked_complete"] = marked_complete


        # OPTIONAL - dismissed
        """
            If this is true, the item will not show in the opportunities list
        """
        if dismissed is not None:
            data["dismissed"] = dismissed


        self.logger.debug("POST /api/v1/planner/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/planner/overrides".format(**path), data=data, params=params, single_item=True)

    def delete_planner_override(self, id):
        """
        Delete a planner override.

        Delete a planner override for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/v1/planner/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/planner/overrides/{id}".format(**path), data=data, params=params, single_item=True)


class Planneroverride(BaseModel):
    """Planneroverride Model.
    User-controlled setting for whether an item should be displayed on the planner or not"""

    def __init__(self, id=None, plannable_type=None, plannable_id=None, user_id=None, workflow_state=None, marked_complete=None, dismissed=None, created_at=None, updated_at=None, deleted_at=None):
        """Init method for Planneroverride class."""
        self._id = id
        self._plannable_type = plannable_type
        self._plannable_id = plannable_id
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._marked_complete = marked_complete
        self._dismissed = dismissed
        self._created_at = created_at
        self._updated_at = updated_at
        self._deleted_at = deleted_at

        self.logger = logging.getLogger('py3canvas.Planneroverride')

    @property
    def id(self):
        """The ID of the planner override."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def plannable_type(self):
        """The type of the associated object for the planner override."""
        return self._plannable_type

    @plannable_type.setter
    def plannable_type(self, value):
        """Setter for plannable_type property."""
        self.logger.warn("Setting values on plannable_type will NOT update the remote Canvas instance.")
        self._plannable_type = value

    @property
    def plannable_id(self):
        """The id of the associated object for the planner override."""
        return self._plannable_id

    @plannable_id.setter
    def plannable_id(self, value):
        """Setter for plannable_id property."""
        self.logger.warn("Setting values on plannable_id will NOT update the remote Canvas instance.")
        self._plannable_id = value

    @property
    def user_id(self):
        """The id of the associated user for the planner override."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """The current published state of the item, synced with the associated object."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def marked_complete(self):
        """Controls whether or not the associated plannable item is marked complete on the planner."""
        return self._marked_complete

    @marked_complete.setter
    def marked_complete(self, value):
        """Setter for marked_complete property."""
        self.logger.warn("Setting values on marked_complete will NOT update the remote Canvas instance.")
        self._marked_complete = value

    @property
    def dismissed(self):
        """Controls whether or not the associated plannable item shows up in the opportunities list."""
        return self._dismissed

    @dismissed.setter
    def dismissed(self, value):
        """Setter for dismissed property."""
        self.logger.warn("Setting values on dismissed will NOT update the remote Canvas instance.")
        self._dismissed = value

    @property
    def created_at(self):
        """The datetime of when the planner override was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """The datetime of when the planner override was updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def deleted_at(self):
        """The datetime of when the planner override was deleted, if applicable."""
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, value):
        """Setter for deleted_at property."""
        self.logger.warn("Setting values on deleted_at will NOT update the remote Canvas instance.")
        self._deleted_at = value

