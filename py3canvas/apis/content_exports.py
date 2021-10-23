"""ContentExports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ContentExportsAPI(BaseCanvasAPI):
    """ContentExports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ContentExportsAPI."""
        super(ContentExportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ContentExportsAPI")

    def list_content_exports_courses(self, course_id):
        """
        List content exports.

        A paginated list of the past and pending content export jobs for a course,
        group, or user. Exports are returned newest first.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/courses/{course_id}/content_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_exports".format(**path), data=data, params=params, all_pages=True)

    def list_content_exports_groups(self, group_id):
        """
        List content exports.

        A paginated list of the past and pending content export jobs for a course,
        group, or user. Exports are returned newest first.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_exports".format(**path), data=data, params=params, all_pages=True)

    def list_content_exports_users(self, user_id):
        """
        List content exports.

        A paginated list of the past and pending content export jobs for a course,
        group, or user. Exports are returned newest first.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_exports".format(**path), data=data, params=params, all_pages=True)

    def show_content_export_courses(self, course_id, id):
        """
        Show content export.

        Get information about a single content export.
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


        self.logger.debug("GET /api/v1/courses/{course_id}/content_exports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_exports/{id}".format(**path), data=data, params=params, single_item=True)

    def show_content_export_groups(self, group_id, id):
        """
        Show content export.

        Get information about a single content export.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_exports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_exports/{id}".format(**path), data=data, params=params, single_item=True)

    def show_content_export_users(self, id, user_id):
        """
        Show content export.

        Get information about a single content export.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/users/{user_id}/content_exports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_exports/{id}".format(**path), data=data, params=params, single_item=True)

    def export_content_courses(self, course_id, export_type, select=None, skip_notifications=None):
        """
        Export content.

        Begin a content export job for a course, group, or user.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the export. The migration's progress is linked to with the
        _progress_url_ value.
        
        When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
        to retrieve a download URL for the exported content.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - export_type
        """
            "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format
        "qti":: Export quizzes from a course in the QTI format
        "zip":: Export files from a course, group, or user in a zip file
        """
        self._validate_enum(export_type, ["common_cartridge", "qti", "zip"])
        data["export_type"] = export_type


        # OPTIONAL - skip_notifications
        """
            Don't send the notifications about the export to the user. Default: false
        """
        if skip_notifications is not None:
            data["skip_notifications"] = skip_notifications


        # OPTIONAL - select
        """
            The select parameter allows exporting specific data. The keys are object types like 'files',
        'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an
        integer or a string.

        Multiple object types can be selected in the same call. However, not all object types are
        valid for every export_type. Common Cartridge supports all object types. Zip and QTI only
        support the object types as described below.

        "folders":: Also supported for zip export_type.
        "files":: Also supported for zip export_type.
        "quizzes":: Also supported for qti export_type.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/courses/{course_id}/content_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/content_exports".format(**path), data=data, params=params, single_item=True)

    def export_content_groups(self, export_type, group_id, select=None, skip_notifications=None):
        """
        Export content.

        Begin a content export job for a course, group, or user.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the export. The migration's progress is linked to with the
        _progress_url_ value.
        
        When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
        to retrieve a download URL for the exported content.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - export_type
        """
            "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format
        "qti":: Export quizzes from a course in the QTI format
        "zip":: Export files from a course, group, or user in a zip file
        """
        self._validate_enum(export_type, ["common_cartridge", "qti", "zip"])
        data["export_type"] = export_type


        # OPTIONAL - skip_notifications
        """
            Don't send the notifications about the export to the user. Default: false
        """
        if skip_notifications is not None:
            data["skip_notifications"] = skip_notifications


        # OPTIONAL - select
        """
            The select parameter allows exporting specific data. The keys are object types like 'files',
        'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an
        integer or a string.

        Multiple object types can be selected in the same call. However, not all object types are
        valid for every export_type. Common Cartridge supports all object types. Zip and QTI only
        support the object types as described below.

        "folders":: Also supported for zip export_type.
        "files":: Also supported for zip export_type.
        "quizzes":: Also supported for qti export_type.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/groups/{group_id}/content_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/content_exports".format(**path), data=data, params=params, single_item=True)

    def export_content_users(self, export_type, user_id, select=None, skip_notifications=None):
        """
        Export content.

        Begin a content export job for a course, group, or user.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the export. The migration's progress is linked to with the
        _progress_url_ value.
        
        When the export completes, use the {api:ContentExportsApiController#show Show content export} endpoint
        to retrieve a download URL for the exported content.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - export_type
        """
            "common_cartridge":: Export the contents of the course in the Common Cartridge (.imscc) format
        "qti":: Export quizzes from a course in the QTI format
        "zip":: Export files from a course, group, or user in a zip file
        """
        self._validate_enum(export_type, ["common_cartridge", "qti", "zip"])
        data["export_type"] = export_type


        # OPTIONAL - skip_notifications
        """
            Don't send the notifications about the export to the user. Default: false
        """
        if skip_notifications is not None:
            data["skip_notifications"] = skip_notifications


        # OPTIONAL - select
        """
            The select parameter allows exporting specific data. The keys are object types like 'files',
        'folders', 'pages', etc. The value for each key is a list of object ids. An id can be an
        integer or a string.

        Multiple object types can be selected in the same call. However, not all object types are
        valid for every export_type. Common Cartridge supports all object types. Zip and QTI only
        support the object types as described below.

        "folders":: Also supported for zip export_type.
        "files":: Also supported for zip export_type.
        "quizzes":: Also supported for qti export_type.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/users/{user_id}/content_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/content_exports".format(**path), data=data, params=params, single_item=True)


class Contentexport(BaseModel):
    """Contentexport Model."""

    def __init__(self, id=None, created_at=None, export_type=None, attachment=None, progress_url=None, user_id=None, workflow_state=None):
        """Init method for Contentexport class."""
        self._id = id
        self._created_at = created_at
        self._export_type = export_type
        self._attachment = attachment
        self._progress_url = progress_url
        self._user_id = user_id
        self._workflow_state = workflow_state

        self.logger = logging.getLogger('py3canvas.Contentexport')

    @property
    def id(self):
        """the unique identifier for the export."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def created_at(self):
        """the date and time this export was requested."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def export_type(self):
        """the type of content migration: 'common_cartridge' or 'qti'."""
        return self._export_type

    @export_type.setter
    def export_type(self, value):
        """Setter for export_type property."""
        self.logger.warn("Setting values on export_type will NOT update the remote Canvas instance.")
        self._export_type = value

    @property
    def attachment(self):
        """attachment api object for the export package (not present before the export completes or after it becomes unavailable for download.)."""
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        """Setter for attachment property."""
        self.logger.warn("Setting values on attachment will NOT update the remote Canvas instance.")
        self._attachment = value

    @property
    def progress_url(self):
        """The api endpoint for polling the current progress."""
        return self._progress_url

    @progress_url.setter
    def progress_url(self, value):
        """Setter for progress_url property."""
        self.logger.warn("Setting values on progress_url will NOT update the remote Canvas instance.")
        self._progress_url = value

    @property
    def user_id(self):
        """The ID of the user who started the export."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """Current state of the content migration: created exporting exported failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

