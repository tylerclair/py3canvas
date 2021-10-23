"""Planner API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PlannerAPI(BaseCanvasAPI):
    """Planner API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PlannerAPI."""
        super(PlannerAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PlannerAPI")

    def list_planner_items_planner(
        self, context_codes=None, end_date=None, filter=None, start_date=None
    ):
        """
        List planner items.

        Retrieve the paginated list of objects to be shown on the planner for the
        current user with the associated planner override to override an item's
        visibility if set.

        Planner items for a student may also be retrieved by a linked observer. Use
        the path that accepts a user_id and supply the student's id.
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

        # OPTIONAL - context_codes
        """
            List of context codes of courses and/or groups whose items you want to see.
        If not specified, defaults to all contexts associated to the current user.
        Note that concluded courses will be ignored unless specified in the includes[]
        parameter. The format of this field is the context type, followed by an underscore,
        followed by the context id. For example: course_42, group_123
        """
        if context_codes is not None:
            params["context_codes"] = context_codes

        # OPTIONAL - filter
        """
            Only return items that have new or unread activity
        """
        if filter is not None:
            self._validate_enum(filter, ["new_activity"])
            params["filter"] = filter

        self.logger.debug(
            "GET /api/v1/planner/items with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/planner/items".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_planner_items_users(
        self, user_id, context_codes=None, end_date=None, filter=None, start_date=None
    ):
        """
        List planner items.

        Retrieve the paginated list of objects to be shown on the planner for the
        current user with the associated planner override to override an item's
        visibility if set.

        Planner items for a student may also be retrieved by a linked observer. Use
        the path that accepts a user_id and supply the student's id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

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

        # OPTIONAL - context_codes
        """
            List of context codes of courses and/or groups whose items you want to see.
        If not specified, defaults to all contexts associated to the current user.
        Note that concluded courses will be ignored unless specified in the includes[]
        parameter. The format of this field is the context type, followed by an underscore,
        followed by the context id. For example: course_42, group_123
        """
        if context_codes is not None:
            params["context_codes"] = context_codes

        # OPTIONAL - filter
        """
            Only return items that have new or unread activity
        """
        if filter is not None:
            self._validate_enum(filter, ["new_activity"])
            params["filter"] = filter

        self.logger.debug(
            "GET /api/v1/users/{user_id}/planner/items with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/planner/items".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_planner_notes(self, context_codes=None, end_date=None, start_date=None):
        """
        List planner notes.

        Retrieve the paginated list of planner notes

        Retrieve planner note for a user
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - start_date
        """
            Only return notes with todo dates since the start_date (inclusive).
        No default. The value should be formatted as: yyyy-mm-dd or
        ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if start_date is not None:
            if issubclass(start_date.__class__, str):
                start_date = self._validate_iso8601_string(start_date)
            elif issubclass(start_date.__class__, date) or issubclass(
                start_date.__class__, datetime
            ):
                start_date = start_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_date"] = start_date

        # OPTIONAL - end_date
        """
            Only return notes with todo dates before the end_date (inclusive).
        No default. The value should be formatted as: yyyy-mm-dd or
        ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        If end_date and start_date are both specified and equivalent,
        then only notes with todo dates on that day are returned.
        """
        if end_date is not None:
            if issubclass(end_date.__class__, str):
                end_date = self._validate_iso8601_string(end_date)
            elif issubclass(end_date.__class__, date) or issubclass(
                end_date.__class__, datetime
            ):
                end_date = end_date.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_date"] = end_date

        # OPTIONAL - context_codes
        """
            List of context codes of courses whose notes you want to see.
        If not specified, defaults to all contexts that the user belongs to.
        The format of this field is the context type, followed by an
        underscore, followed by the context id. For example: course_42
        Including a code matching the user's own context code (e.g. user_1)
        will include notes that are not associated with any particular course.
        """
        if context_codes is not None:
            params["context_codes"] = context_codes

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

    def show_planner_note(self, id):
        """
        Show a planner note.

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

    def update_planner_note(
        self, id, course_id=None, details=None, title=None, todo_date=None
    ):
        """
        Update a planner note.

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

        # OPTIONAL - title
        """
            The title of the planner note.
        """
        if title is not None:
            data["title"] = title

        # OPTIONAL - details
        """
            Text of the planner note.
        """
        if details is not None:
            data["details"] = details

        # OPTIONAL - todo_date
        """
            The date where this planner note should appear in the planner.
        The value should be formatted as: yyyy-mm-dd.
        """
        if todo_date is not None:
            data["todo_date"] = todo_date

        # OPTIONAL - course_id
        """
            The ID of the course to associate with the planner note. The caller must be able to view the course in order to
        associate it with a planner note. Use a null or empty value to remove a planner note from a course. Note that if
        the planner note is linked to a learning object, its course_id cannot be changed.
        """
        if course_id is not None:
            data["course_id"] = course_id

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

    def create_planner_note(
        self,
        course_id=None,
        details=None,
        linked_object_id=None,
        linked_object_type=None,
        title=None,
        todo_date=None,
    ):
        """
        Create a planner note.

        Create a planner note for the current user
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - title
        """
            The title of the planner note.
        """
        if title is not None:
            data["title"] = title

        # OPTIONAL - details
        """
            Text of the planner note.
        """
        if details is not None:
            data["details"] = details

        # OPTIONAL - todo_date
        """
            The date where this planner note should appear in the planner.
        The value should be formatted as: yyyy-mm-dd.
        """
        if todo_date is not None:
            data["todo_date"] = todo_date

        # OPTIONAL - course_id
        """
            The ID of the course to associate with the planner note. The caller must be able to view the course in order to
        associate it with a planner note.
        """
        if course_id is not None:
            data["course_id"] = course_id

        # OPTIONAL - linked_object_type
        """
            The type of a learning object to link to this planner note. Must be used in conjunction wtih linked_object_id
        and course_id. Valid linked_object_type values are:
        'announcement', 'assignment', 'discussion_topic', 'wiki_page', 'quiz'
        """
        if linked_object_type is not None:
            data["linked_object_type"] = linked_object_type

        # OPTIONAL - linked_object_id
        """
            The id of a learning object to link to this planner note. Must be used in conjunction with linked_object_type
        and course_id. The object must be in the same course as specified by course_id. If the title argument is not
        provided, the planner note will use the learning object's title as its title. Only one planner note may be
        linked to a specific learning object.
        """
        if linked_object_id is not None:
            data["linked_object_id"] = linked_object_id

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

    def list_planner_overrides(self):
        """
        List planner overrides.

        Retrieve a planner override for the current user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/planner/overrides with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/planner/overrides".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

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

        self.logger.debug(
            "GET /api/v1/planner/overrides/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/planner/overrides/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

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

        self.logger.debug(
            "PUT /api/v1/planner/overrides/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/planner/overrides/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def create_planner_override(
        self, plannable_id, plannable_type, dismissed=None, marked_complete=None
    ):
        """
        Create a planner override.

        Create a planner override for the current user
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - plannable_type
        """
            Type of the item that you are overriding in the planner
        """
        self._validate_enum(
            plannable_type,
            [
                "announcement",
                "assignment",
                "discussion_topic",
                "quiz",
                "wiki_page",
                "planner_note",
            ],
        )
        data["plannable_type"] = plannable_type

        # REQUIRED - plannable_id
        """
            ID of the item that you are overriding in the planner
        """
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

        self.logger.debug(
            "POST /api/v1/planner/overrides with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/planner/overrides".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

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

        self.logger.debug(
            "DELETE /api/v1/planner/overrides/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/planner/overrides/{id}".format(**path),
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
        linked_object_type=None,
        linked_object_id=None,
        linked_object_html_url=None,
        linked_object_url=None,
    ):
        """Init method for Plannernote class."""
        self._id = id
        self._title = title
        self._description = description
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._course_id = course_id
        self._todo_date = todo_date
        self._linked_object_type = linked_object_type
        self._linked_object_id = linked_object_id
        self._linked_object_html_url = linked_object_html_url
        self._linked_object_url = linked_object_url

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

    @property
    def linked_object_type(self):
        """the type of the linked learning object."""
        return self._linked_object_type

    @linked_object_type.setter
    def linked_object_type(self, value):
        """Setter for linked_object_type property."""
        self.logger.warn(
            "Setting values on linked_object_type will NOT update the remote Canvas instance."
        )
        self._linked_object_type = value

    @property
    def linked_object_id(self):
        """the id of the linked learning object."""
        return self._linked_object_id

    @linked_object_id.setter
    def linked_object_id(self, value):
        """Setter for linked_object_id property."""
        self.logger.warn(
            "Setting values on linked_object_id will NOT update the remote Canvas instance."
        )
        self._linked_object_id = value

    @property
    def linked_object_html_url(self):
        """the Canvas web URL of the linked learning object."""
        return self._linked_object_html_url

    @linked_object_html_url.setter
    def linked_object_html_url(self, value):
        """Setter for linked_object_html_url property."""
        self.logger.warn(
            "Setting values on linked_object_html_url will NOT update the remote Canvas instance."
        )
        self._linked_object_html_url = value

    @property
    def linked_object_url(self):
        """the API URL of the linked learning object."""
        return self._linked_object_url

    @linked_object_url.setter
    def linked_object_url(self, value):
        """Setter for linked_object_url property."""
        self.logger.warn(
            "Setting values on linked_object_url will NOT update the remote Canvas instance."
        )
        self._linked_object_url = value


class Planneroverride(BaseModel):
    """Planneroverride Model.
    User-controlled setting for whether an item should be displayed on the planner or not"""

    def __init__(
        self,
        id=None,
        plannable_type=None,
        plannable_id=None,
        user_id=None,
        assignment_id=None,
        workflow_state=None,
        marked_complete=None,
        dismissed=None,
        created_at=None,
        updated_at=None,
        deleted_at=None,
    ):
        """Init method for Planneroverride class."""
        self._id = id
        self._plannable_type = plannable_type
        self._plannable_id = plannable_id
        self._user_id = user_id
        self._assignment_id = assignment_id
        self._workflow_state = workflow_state
        self._marked_complete = marked_complete
        self._dismissed = dismissed
        self._created_at = created_at
        self._updated_at = updated_at
        self._deleted_at = deleted_at

        self.logger = logging.getLogger("py3canvas.Planneroverride")

    @property
    def id(self):
        """The ID of the planner override."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def plannable_type(self):
        """The type of the associated object for the planner override."""
        return self._plannable_type

    @plannable_type.setter
    def plannable_type(self, value):
        """Setter for plannable_type property."""
        self.logger.warn(
            "Setting values on plannable_type will NOT update the remote Canvas instance."
        )
        self._plannable_type = value

    @property
    def plannable_id(self):
        """The id of the associated object for the planner override."""
        return self._plannable_id

    @plannable_id.setter
    def plannable_id(self, value):
        """Setter for plannable_id property."""
        self.logger.warn(
            "Setting values on plannable_id will NOT update the remote Canvas instance."
        )
        self._plannable_id = value

    @property
    def user_id(self):
        """The id of the associated user for the planner override."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def assignment_id(self):
        """The id of the plannable's associated assignment, if it has one."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn(
            "Setting values on assignment_id will NOT update the remote Canvas instance."
        )
        self._assignment_id = value

    @property
    def workflow_state(self):
        """The current published state of the item, synced with the associated object."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def marked_complete(self):
        """Controls whether or not the associated plannable item is marked complete on the planner."""
        return self._marked_complete

    @marked_complete.setter
    def marked_complete(self, value):
        """Setter for marked_complete property."""
        self.logger.warn(
            "Setting values on marked_complete will NOT update the remote Canvas instance."
        )
        self._marked_complete = value

    @property
    def dismissed(self):
        """Controls whether or not the associated plannable item shows up in the opportunities list."""
        return self._dismissed

    @dismissed.setter
    def dismissed(self, value):
        """Setter for dismissed property."""
        self.logger.warn(
            "Setting values on dismissed will NOT update the remote Canvas instance."
        )
        self._dismissed = value

    @property
    def created_at(self):
        """The datetime of when the planner override was created."""
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
        """The datetime of when the planner override was updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value

    @property
    def deleted_at(self):
        """The datetime of when the planner override was deleted, if applicable."""
        return self._deleted_at

    @deleted_at.setter
    def deleted_at(self, value):
        """Setter for deleted_at property."""
        self.logger.warn(
            "Setting values on deleted_at will NOT update the remote Canvas instance."
        )
        self._deleted_at = value
