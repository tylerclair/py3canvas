"""BlueprintCourses API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class BlueprintCoursesAPI(BaseCanvasAPI):
    """BlueprintCourses API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for BlueprintCoursesAPI."""
        super(BlueprintCoursesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.BlueprintCoursesAPI")

    def get_blueprint_information(self, course_id, template_id):
        """
        Get blueprint information.

        Using 'default' as the template_id should suffice for the current implmentation (as there should be only one template per course).
        However, using specific template ids may become necessary in the future
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_templates/{template_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}".format(**path), data=data, params=params, single_item=True)

    def get_associated_course_information(self, course_id, template_id):
        """
        Get associated course information.

        Returns a list of courses that are configured to receive updates from this blueprint
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/associated_courses".format(**path), data=data, params=params, all_pages=True)

    def update_associated_courses(self, course_id, template_id, course_ids_to_add=None, course_ids_to_remove=None):
        """
        Update associated courses.

        Send a list of course ids to add or remove new associations for the template.
        Cannot add courses that do not belong to the blueprint course's account. Also cannot add
        other blueprint courses or courses that already have an association with another blueprint course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        # OPTIONAL - course_ids_to_add
        """Courses to add as associated courses"""
        if course_ids_to_add is not None:
            data["course_ids_to_add"] = course_ids_to_add

        # OPTIONAL - course_ids_to_remove
        """Courses to remove as associated courses"""
        if course_ids_to_remove is not None:
            data["course_ids_to_remove"] = course_ids_to_remove

        self.logger.debug("PUT /api/v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/update_associations".format(**path), data=data, params=params, no_data=True)

    def begin_migration_to_push_to_associated_courses(self, course_id, template_id, comment=None, copy_settings=None, send_notification=None):
        """
        Begin a migration to push to associated courses.

        Begins a migration to push recently updated content to all associated courses.
        Only one migration can be running at a time.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        # OPTIONAL - comment
        """An optional comment to be included in the sync history."""
        if comment is not None:
            data["comment"] = comment

        # OPTIONAL - send_notification
        """Send a notification to the calling user when the sync completes."""
        if send_notification is not None:
            data["send_notification"] = send_notification

        # OPTIONAL - copy_settings
        """Whether course settings should be copied over to associated courses.
        Defaults to true for newly associated courses."""
        if copy_settings is not None:
            data["copy_settings"] = copy_settings

        self.logger.debug("POST /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations".format(**path), data=data, params=params, single_item=True)

    def set_or_remove_restrictions_on_blueprint_course_object(self, course_id, template_id, content_id=None, content_type=None, restricted=None, restrictions=None):
        """
        Set or remove restrictions on a blueprint course object.

        If a blueprint course object is restricted, editing will be limited for copies in associated courses.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        # OPTIONAL - content_type
        """The type of the object."""
        if content_type is not None:
            self._validate_enum(content_type, ["assignment", "attachment", "discussion_topic", "external_tool", "quiz", "wiki_page"])
            data["content_type"] = content_type

        # OPTIONAL - content_id
        """The ID of the object."""
        if content_id is not None:
            data["content_id"] = content_id

        # OPTIONAL - restricted
        """Whether to apply restrictions."""
        if restricted is not None:
            data["restricted"] = restricted

        # OPTIONAL - restrictions
        """(Optional) If the object is restricted, this specifies a set of restrictions. If not specified,
        the course-level restrictions will be used. See {api:CoursesController#update Course API update documentation}"""
        if restrictions is not None:
            data["restrictions"] = restrictions

        self.logger.debug("PUT /api/v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/restrict_item".format(**path), data=data, params=params, no_data=True)

    def get_unsynced_changes(self, course_id, template_id):
        """
        Get unsynced changes.

        Retrieve a list of learning objects that have changed since the last blueprint sync operation.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_templates/{template_id}/unsynced_changes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/unsynced_changes".format(**path), data=data, params=params, all_pages=True)

    def list_blueprint_migrations(self, course_id, template_id):
        """
        List blueprint migrations.

        Shows migrations for the template, starting with the most recent. This endpoint can be called on a
        blueprint course. See also {api:MasterCourses::MasterTemplatesController#imports_index the associated course side}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations".format(**path), data=data, params=params, all_pages=True)

    def show_blueprint_migration(self, id, course_id, template_id):
        """
        Show a blueprint migration.

        Shows the status of a migration. This endpoint can be called on a blueprint course. See also
        {api:MasterCourses::MasterTemplatesController#imports_show the associated course side}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_details(self, id, course_id, template_id):
        """
        Get migration details.

        Show the changes that were propagated in a blueprint migration. This endpoint can be called on a
        blueprint course. See also {api:MasterCourses::MasterTemplatesController#import_details the associated course side}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - template_id
        """ID"""
        path["template_id"] = template_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}/details with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_templates/{template_id}/migrations/{id}/details".format(**path), data=data, params=params, all_pages=True)

    def list_blueprint_imports(self, course_id, subscription_id):
        """
        List blueprint imports.

        Shows migrations imported into a course associated with a blueprint, starting with the most recent. See also
        {api:MasterCourses::MasterTemplatesController#migrations_index the blueprint course side}.
        
        Use 'default' as the subscription_id to use the currently active blueprint subscription.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - subscription_id
        """ID"""
        path["subscription_id"] = subscription_id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations".format(**path), data=data, params=params, all_pages=True)

    def show_blueprint_import(self, id, course_id, subscription_id):
        """
        Show a blueprint import.

        Shows the status of an import into a course associated with a blueprint. See also
        {api:MasterCourses::MasterTemplatesController#migrations_show the blueprint course side}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - subscription_id
        """ID"""
        path["subscription_id"] = subscription_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_import_details(self, id, course_id, subscription_id):
        """
        Get import details.

        Show the changes that were propagated to a course associated with a blueprint.  See also
        {api:MasterCourses::MasterTemplatesController#migration_details the blueprint course side}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - subscription_id
        """ID"""
        path["subscription_id"] = subscription_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/blueprint_subscriptions/{subscription_id}/migrations/{id}/details".format(**path), data=data, params=params, all_pages=True)


class Blueprintrestriction(BaseModel):
    """Blueprintrestriction Model.
    A set of restrictions on editing for copied objects in associated courses"""

    def __init__(self, content=None, due_dates=None, points=None, availability_dates=None):
        """Init method for Blueprintrestriction class."""
        self._content = content
        self._due_dates = due_dates
        self._points = points
        self._availability_dates = availability_dates

        self.logger = logging.getLogger('py3canvas.Blueprintrestriction')

    @property
    def content(self):
        """Restriction on main content (e.g. title, description)."""
        return self._content

    @content.setter
    def content(self, value):
        """Setter for content property."""
        self.logger.warn("Setting values on content will NOT update the remote Canvas instance.")
        self._content = value

    @property
    def due_dates(self):
        """Restriction on due dates for assignments and graded learning objects."""
        return self._due_dates

    @due_dates.setter
    def due_dates(self, value):
        """Setter for due_dates property."""
        self.logger.warn("Setting values on due_dates will NOT update the remote Canvas instance.")
        self._due_dates = value

    @property
    def points(self):
        """Restriction on points possible for assignments and graded learning objects."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn("Setting values on points will NOT update the remote Canvas instance.")
        self._points = value

    @property
    def availability_dates(self):
        """Restriction on availability dates for an object."""
        return self._availability_dates

    @availability_dates.setter
    def availability_dates(self, value):
        """Setter for availability_dates property."""
        self.logger.warn("Setting values on availability_dates will NOT update the remote Canvas instance.")
        self._availability_dates = value


class Blueprinttemplate(BaseModel):
    """Blueprinttemplate Model."""

    def __init__(self, course_id=None, last_export_completed_at=None, id=None):
        """Init method for Blueprinttemplate class."""
        self._course_id = course_id
        self._last_export_completed_at = last_export_completed_at
        self._id = id

        self.logger = logging.getLogger('py3canvas.Blueprinttemplate')

    @property
    def course_id(self):
        """The ID of the Course the template belongs to."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def last_export_completed_at(self):
        """Time when the last export was completed."""
        return self._last_export_completed_at

    @last_export_completed_at.setter
    def last_export_completed_at(self, value):
        """Setter for last_export_completed_at property."""
        self.logger.warn("Setting values on last_export_completed_at will NOT update the remote Canvas instance.")
        self._last_export_completed_at = value

    @property
    def id(self):
        """The ID of the template."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Changerecord(BaseModel):
    """Changerecord Model.
    Describes a learning object change propagated to associated courses from a blueprint course"""

    def __init__(self, asset_id=None, change_type=None, html_url=None, asset_name=None, exceptions=None, locked=None, asset_type=None):
        """Init method for Changerecord class."""
        self._asset_id = asset_id
        self._change_type = change_type
        self._html_url = html_url
        self._asset_name = asset_name
        self._exceptions = exceptions
        self._locked = locked
        self._asset_type = asset_type

        self.logger = logging.getLogger('py3canvas.Changerecord')

    @property
    def asset_id(self):
        """The ID of the learning object that was changed in the blueprint course."""
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        """Setter for asset_id property."""
        self.logger.warn("Setting values on asset_id will NOT update the remote Canvas instance.")
        self._asset_id = value

    @property
    def change_type(self):
        """The type of change; one of 'created', 'updated', 'deleted'."""
        return self._change_type

    @change_type.setter
    def change_type(self, value):
        """Setter for change_type property."""
        self.logger.warn("Setting values on change_type will NOT update the remote Canvas instance.")
        self._change_type = value

    @property
    def html_url(self):
        """The URL of the changed object."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def asset_name(self):
        """The name of the learning object that was changed in the blueprint course."""
        return self._asset_name

    @asset_name.setter
    def asset_name(self, value):
        """Setter for asset_name property."""
        self.logger.warn("Setting values on asset_name will NOT update the remote Canvas instance.")
        self._asset_name = value

    @property
    def exceptions(self):
        """A list of ExceptionRecords for linked courses that did not receive this update."""
        return self._exceptions

    @exceptions.setter
    def exceptions(self, value):
        """Setter for exceptions property."""
        self.logger.warn("Setting values on exceptions will NOT update the remote Canvas instance.")
        self._exceptions = value

    @property
    def locked(self):
        """Whether the object is locked in the blueprint."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def asset_type(self):
        """The type of the learning object that was changed in the blueprint course.  One of 'assignment', 'attachment', 'discussion_topic', 'external_tool', 'quiz', or 'wiki_page'."""
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        """Setter for asset_type property."""
        self.logger.warn("Setting values on asset_type will NOT update the remote Canvas instance.")
        self._asset_type = value


class Blueprintmigration(BaseModel):
    """Blueprintmigration Model."""

    def __init__(self, comment=None, user_id=None, workflow_state=None, created_at=None, imports_queued_at=None, imports_completed_at=None, template_id=None, exports_started_at=None, subscription_id=None, id=None):
        """Init method for Blueprintmigration class."""
        self._comment = comment
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._created_at = created_at
        self._imports_queued_at = imports_queued_at
        self._imports_completed_at = imports_completed_at
        self._template_id = template_id
        self._exports_started_at = exports_started_at
        self._subscription_id = subscription_id
        self._id = id

        self.logger = logging.getLogger('py3canvas.Blueprintmigration')

    @property
    def comment(self):
        """User-specified comment describing changes made in this operation."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Setter for comment property."""
        self.logger.warn("Setting values on comment will NOT update the remote Canvas instance.")
        self._comment = value

    @property
    def user_id(self):
        """The ID of the user who queued the migration."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """Current state of the content migration: queued, exporting, imports_queued, completed, exports_failed, imports_failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def created_at(self):
        """Time when the migration was queued."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def imports_queued_at(self):
        """Time when the exports were completed and imports were queued."""
        return self._imports_queued_at

    @imports_queued_at.setter
    def imports_queued_at(self, value):
        """Setter for imports_queued_at property."""
        self.logger.warn("Setting values on imports_queued_at will NOT update the remote Canvas instance.")
        self._imports_queued_at = value

    @property
    def imports_completed_at(self):
        """Time when the imports were completed."""
        return self._imports_completed_at

    @imports_completed_at.setter
    def imports_completed_at(self, value):
        """Setter for imports_completed_at property."""
        self.logger.warn("Setting values on imports_completed_at will NOT update the remote Canvas instance.")
        self._imports_completed_at = value

    @property
    def template_id(self):
        """The ID of the template the migration belongs to. Only present when querying a blueprint course."""
        return self._template_id

    @template_id.setter
    def template_id(self, value):
        """Setter for template_id property."""
        self.logger.warn("Setting values on template_id will NOT update the remote Canvas instance.")
        self._template_id = value

    @property
    def exports_started_at(self):
        """Time when the exports begun."""
        return self._exports_started_at

    @exports_started_at.setter
    def exports_started_at(self, value):
        """Setter for exports_started_at property."""
        self.logger.warn("Setting values on exports_started_at will NOT update the remote Canvas instance.")
        self._exports_started_at = value

    @property
    def subscription_id(self):
        """The ID of the associated course's blueprint subscription. Only present when querying a course associated with a blueprint."""
        return self._subscription_id

    @subscription_id.setter
    def subscription_id(self, value):
        """Setter for subscription_id property."""
        self.logger.warn("Setting values on subscription_id will NOT update the remote Canvas instance.")
        self._subscription_id = value

    @property
    def id(self):
        """The ID of the migration."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Exceptionrecord(BaseModel):
    """Exceptionrecord Model.
    Lists associated courses that did not receive a change propagated from a blueprint"""

    def __init__(self, course_id=None, conflicting_changes=None):
        """Init method for Exceptionrecord class."""
        self._course_id = course_id
        self._conflicting_changes = conflicting_changes

        self.logger = logging.getLogger('py3canvas.Exceptionrecord')

    @property
    def course_id(self):
        """The ID of the associated course."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def conflicting_changes(self):
        """A list of change classes in the associated course's copy of the item that prevented a blueprint change from being applied. One or more of ['content', 'points', 'due_dates', 'availability_dates']."""
        return self._conflicting_changes

    @conflicting_changes.setter
    def conflicting_changes(self, value):
        """Setter for conflicting_changes property."""
        self.logger.warn("Setting values on conflicting_changes will NOT update the remote Canvas instance.")
        self._conflicting_changes = value

