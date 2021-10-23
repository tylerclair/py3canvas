"""EPubExports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class EPubExportsAPI(BaseCanvasAPI):
    """EPubExports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for EPubExportsAPI."""
        super(EPubExportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.EPubExportsAPI")

    def list_courses_with_their_latest_epub_export(self):
        """
        List courses with their latest ePub export.

        A paginated list of all courses a user is actively participating in, and
        the latest ePub export associated with the user & course.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/epub_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/epub_exports".format(**path), data=data, params=params, all_pages=True)

    def create_epub_export(self, course_id):
        """
        Create ePub Export.

        Begin an ePub export for a course.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the export. The export's progress is linked to with the
        _progress_url_ value.
        
        When the export completes, use the {api:EpubExportsController#show Show content export} endpoint
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


        self.logger.debug("POST /api/v1/courses/{course_id}/epub_exports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/epub_exports".format(**path), data=data, params=params, single_item=True)

    def show_epub_export(self, course_id, id):
        """
        Show ePub export.

        Get information about a single ePub export.
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


        self.logger.debug("GET /api/v1/courses/{course_id}/epub_exports/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/epub_exports/{id}".format(**path), data=data, params=params, single_item=True)


class Courseepubexport(BaseModel):
    """Courseepubexport Model.
    Combination of a Course & EpubExport."""

    def __init__(self, id=None, name=None, epub_export=None):
        """Init method for Courseepubexport class."""
        self._id = id
        self._name = name
        self._epub_export = epub_export

        self.logger = logging.getLogger('py3canvas.Courseepubexport')

    @property
    def id(self):
        """the unique identifier for the course."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """the name for the course."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def epub_export(self):
        """ePub export API object."""
        return self._epub_export

    @epub_export.setter
    def epub_export(self, value):
        """Setter for epub_export property."""
        self.logger.warn("Setting values on epub_export will NOT update the remote Canvas instance.")
        self._epub_export = value


class Epubexport(BaseModel):
    """Epubexport Model."""

    def __init__(self, id=None, created_at=None, attachment=None, progress_url=None, user_id=None, workflow_state=None):
        """Init method for Epubexport class."""
        self._id = id
        self._created_at = created_at
        self._attachment = attachment
        self._progress_url = progress_url
        self._user_id = user_id
        self._workflow_state = workflow_state

        self.logger = logging.getLogger('py3canvas.Epubexport')

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
    def attachment(self):
        """attachment api object for the export ePub (not present until the export completes)."""
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
        """Current state of the ePub export: created exporting exported generating generated failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

