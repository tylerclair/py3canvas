"""History API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class HistoryAPI(BaseCanvasAPI):
    """History API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for HistoryAPI."""
        super(HistoryAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.HistoryAPI")

    def list_recent_history_for_user(self, user_id):
        """
        List recent history for a user.

        Return a paginated list of the user's recent history. History entries are returned in descending order,
        newest to oldest. You may list history entries for yourself (use +self+ as the user_id), for a student you observe,
        or for a user you manage as an administrator. Note that the +per_page+ pagination argument is not supported
        and the number of history entries returned per page will vary.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        self.logger.debug(
            "GET /api/v1/users/{user_id}/history with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/history".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )


class Historyentry(BaseModel):
    """Historyentry Model.
    Information about a recently visited item or page in Canvas"""

    def __init__(
        self,
        asset_code,
        asset_name,
        visited_url,
        visited_at,
        asset_icon=None,
        asset_readable_category=None,
        context_type=None,
        context_id=None,
        context_name=None,
        interaction_seconds=None,
    ):
        """Init method for Historyentry class."""
        self._asset_code = asset_code
        self._asset_name = asset_name
        self._asset_icon = asset_icon
        self._asset_readable_category = asset_readable_category
        self._context_type = context_type
        self._context_id = context_id
        self._context_name = context_name
        self._visited_url = visited_url
        self._visited_at = visited_at
        self._interaction_seconds = interaction_seconds

        self.logger = logging.getLogger("py3canvas.Historyentry")

    @property
    def asset_code(self):
        """The asset string for the item viewed."""
        return self._asset_code

    @asset_code.setter
    def asset_code(self, value):
        """Setter for asset_code property."""
        self.logger.warn(
            "Setting values on asset_code will NOT update the remote Canvas instance."
        )
        self._asset_code = value

    @property
    def asset_name(self):
        """The name of the item."""
        return self._asset_name

    @asset_name.setter
    def asset_name(self, value):
        """Setter for asset_name property."""
        self.logger.warn(
            "Setting values on asset_name will NOT update the remote Canvas instance."
        )
        self._asset_name = value

    @property
    def asset_icon(self):
        """The icon type shown for the item. One of 'icon-announcement', 'icon-assignment', 'icon-calendar-month', 'icon-discussion', 'icon-document', 'icon-download', 'icon-gradebook', 'icon-home', 'icon-message', 'icon-module', 'icon-outcomes', 'icon-quiz', 'icon-user', 'icon-syllabus'."""
        return self._asset_icon

    @asset_icon.setter
    def asset_icon(self, value):
        """Setter for asset_icon property."""
        self.logger.warn(
            "Setting values on asset_icon will NOT update the remote Canvas instance."
        )
        self._asset_icon = value

    @property
    def asset_readable_category(self):
        """The associated category describing the asset_icon."""
        return self._asset_readable_category

    @asset_readable_category.setter
    def asset_readable_category(self, value):
        """Setter for asset_readable_category property."""
        self.logger.warn(
            "Setting values on asset_readable_category will NOT update the remote Canvas instance."
        )
        self._asset_readable_category = value

    @property
    def context_type(self):
        """The type of context of the item visited. One of 'Course', 'Group', 'User', or 'Account'."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn(
            "Setting values on context_type will NOT update the remote Canvas instance."
        )
        self._context_type = value

    @property
    def context_id(self):
        """The id of the context, if applicable."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn(
            "Setting values on context_id will NOT update the remote Canvas instance."
        )
        self._context_id = value

    @property
    def context_name(self):
        """The name of the context."""
        return self._context_name

    @context_name.setter
    def context_name(self, value):
        """Setter for context_name property."""
        self.logger.warn(
            "Setting values on context_name will NOT update the remote Canvas instance."
        )
        self._context_name = value

    @property
    def visited_url(self):
        """The URL of the item."""
        return self._visited_url

    @visited_url.setter
    def visited_url(self, value):
        """Setter for visited_url property."""
        self.logger.warn(
            "Setting values on visited_url will NOT update the remote Canvas instance."
        )
        self._visited_url = value

    @property
    def visited_at(self):
        """When the page was visited."""
        return self._visited_at

    @visited_at.setter
    def visited_at(self, value):
        """Setter for visited_at property."""
        self.logger.warn(
            "Setting values on visited_at will NOT update the remote Canvas instance."
        )
        self._visited_at = value

    @property
    def interaction_seconds(self):
        """The estimated time spent on the page in seconds."""
        return self._interaction_seconds

    @interaction_seconds.setter
    def interaction_seconds(self, value):
        """Setter for interaction_seconds property."""
        self.logger.warn(
            "Setting values on interaction_seconds will NOT update the remote Canvas instance."
        )
        self._interaction_seconds = value
