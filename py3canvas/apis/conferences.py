"""Conferences API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ConferencesAPI(BaseCanvasAPI):
    """Conferences API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ConferencesAPI."""
        super(ConferencesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ConferencesAPI")

    def list_conferences_courses(self, course_id):
        """
        List conferences.

        Retrieve the paginated list of conferences for this context
        
        This API returns a JSON object containing the list of conferences,
        the key for the list of conferences is "conferences"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/courses/{course_id}/conferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/conferences".format(**path), data=data, params=params, all_pages=True)

    def list_conferences_groups(self, group_id):
        """
        List conferences.

        Retrieve the paginated list of conferences for this context
        
        This API returns a JSON object containing the list of conferences,
        the key for the list of conferences is "conferences"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        self.logger.debug("GET /api/v1/groups/{group_id}/conferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/conferences".format(**path), data=data, params=params, all_pages=True)

    def list_conferences_for_current_user(self, state=None):
        """
        List conferences for the current user.

        Retrieve the paginated list of conferences for all courses and groups
        the current user belongs to
        
        This API returns a JSON object containing the list of conferences.
        The key for the list of conferences is "conferences".
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - state
        """
            If set to "live", returns only conferences that are live (i.e., have
        started and not finished yet). If omitted, returns all conferences for
        this user's groups and courses.
        """
        if state is not None:
            params["state"] = state


        self.logger.debug("GET /api/v1/conferences with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/conferences".format(**path), data=data, params=params, all_pages=True)


class Conferencerecording(BaseModel):
    """Conferencerecording Model."""

    def __init__(self, duration_minutes=None, title=None, updated_at=None, created_at=None, playback_url=None):
        """Init method for Conferencerecording class."""
        self._duration_minutes = duration_minutes
        self._title = title
        self._updated_at = updated_at
        self._created_at = created_at
        self._playback_url = playback_url

        self.logger = logging.getLogger('py3canvas.Conferencerecording')

    @property
    def duration_minutes(self):
        """duration_minutes."""
        return self._duration_minutes

    @duration_minutes.setter
    def duration_minutes(self, value):
        """Setter for duration_minutes property."""
        self.logger.warn("Setting values on duration_minutes will NOT update the remote Canvas instance.")
        self._duration_minutes = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def updated_at(self):
        """updated_at."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def created_at(self):
        """created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def playback_url(self):
        """playback_url."""
        return self._playback_url

    @playback_url.setter
    def playback_url(self, value):
        """Setter for playback_url property."""
        self.logger.warn("Setting values on playback_url will NOT update the remote Canvas instance.")
        self._playback_url = value


class Conference(BaseModel):
    """Conference Model."""

    def __init__(self, id=None, conference_type=None, conference_key=None, description=None, duration=None, ended_at=None, started_at=None, title=None, users=None, has_advanced_settings=None, long_running=None, user_settings=None, recordings=None, url=None, join_url=None, context_type=None, context_id=None):
        """Init method for Conference class."""
        self._id = id
        self._conference_type = conference_type
        self._conference_key = conference_key
        self._description = description
        self._duration = duration
        self._ended_at = ended_at
        self._started_at = started_at
        self._title = title
        self._users = users
        self._has_advanced_settings = has_advanced_settings
        self._long_running = long_running
        self._user_settings = user_settings
        self._recordings = recordings
        self._url = url
        self._join_url = join_url
        self._context_type = context_type
        self._context_id = context_id

        self.logger = logging.getLogger('py3canvas.Conference')

    @property
    def id(self):
        """The id of the conference."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def conference_type(self):
        """The type of conference."""
        return self._conference_type

    @conference_type.setter
    def conference_type(self, value):
        """Setter for conference_type property."""
        self.logger.warn("Setting values on conference_type will NOT update the remote Canvas instance.")
        self._conference_type = value

    @property
    def conference_key(self):
        """The 3rd party's ID for the conference."""
        return self._conference_key

    @conference_key.setter
    def conference_key(self, value):
        """Setter for conference_key property."""
        self.logger.warn("Setting values on conference_key will NOT update the remote Canvas instance.")
        self._conference_key = value

    @property
    def description(self):
        """The description for the conference."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def duration(self):
        """The expected duration the conference is supposed to last."""
        return self._duration

    @duration.setter
    def duration(self, value):
        """Setter for duration property."""
        self.logger.warn("Setting values on duration will NOT update the remote Canvas instance.")
        self._duration = value

    @property
    def ended_at(self):
        """The date that the conference ended at, null if it hasn't ended."""
        return self._ended_at

    @ended_at.setter
    def ended_at(self, value):
        """Setter for ended_at property."""
        self.logger.warn("Setting values on ended_at will NOT update the remote Canvas instance.")
        self._ended_at = value

    @property
    def started_at(self):
        """The date the conference started at, null if it hasn't started."""
        return self._started_at

    @started_at.setter
    def started_at(self, value):
        """Setter for started_at property."""
        self.logger.warn("Setting values on started_at will NOT update the remote Canvas instance.")
        self._started_at = value

    @property
    def title(self):
        """The title of the conference."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def users(self):
        """Array of user ids that are participants in the conference."""
        return self._users

    @users.setter
    def users(self, value):
        """Setter for users property."""
        self.logger.warn("Setting values on users will NOT update the remote Canvas instance.")
        self._users = value

    @property
    def has_advanced_settings(self):
        """True if the conference type has advanced settings."""
        return self._has_advanced_settings

    @has_advanced_settings.setter
    def has_advanced_settings(self, value):
        """Setter for has_advanced_settings property."""
        self.logger.warn("Setting values on has_advanced_settings will NOT update the remote Canvas instance.")
        self._has_advanced_settings = value

    @property
    def long_running(self):
        """If true the conference is long running and has no expected end time."""
        return self._long_running

    @long_running.setter
    def long_running(self, value):
        """Setter for long_running property."""
        self.logger.warn("Setting values on long_running will NOT update the remote Canvas instance.")
        self._long_running = value

    @property
    def user_settings(self):
        """A collection of settings specific to the conference type."""
        return self._user_settings

    @user_settings.setter
    def user_settings(self, value):
        """Setter for user_settings property."""
        self.logger.warn("Setting values on user_settings will NOT update the remote Canvas instance.")
        self._user_settings = value

    @property
    def recordings(self):
        """A List of recordings for the conference."""
        return self._recordings

    @recordings.setter
    def recordings(self, value):
        """Setter for recordings property."""
        self.logger.warn("Setting values on recordings will NOT update the remote Canvas instance.")
        self._recordings = value

    @property
    def url(self):
        """URL for the conference, may be null if the conference type doesn't set it."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def join_url(self):
        """URL to join the conference, may be null if the conference type doesn't set it."""
        return self._join_url

    @join_url.setter
    def join_url(self, value):
        """Setter for join_url property."""
        self.logger.warn("Setting values on join_url will NOT update the remote Canvas instance.")
        self._join_url = value

    @property
    def context_type(self):
        """The type of this conference's context, typically 'Course' or 'Group'."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """The ID of this conference's context."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

