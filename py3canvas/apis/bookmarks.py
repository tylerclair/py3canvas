"""Bookmarks API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class BookmarksAPI(BaseCanvasAPI):
    """Bookmarks API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for BookmarksAPI."""
        super(BookmarksAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.BookmarksAPI")

    def list_bookmarks(self):
        """
        List bookmarks.

        Returns the paginated list of bookmarks.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/users/self/bookmarks with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/bookmarks".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def create_bookmark(self, data=None, name=None, position=None, url=None):
        """
        Create bookmark.

        Creates a bookmark.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - name
        """
            The name of the bookmark
        """
        if name is not None:
            data["name"] = name

        # OPTIONAL - url
        """
            The url of the bookmark
        """
        if url is not None:
            data["url"] = url

        # OPTIONAL - position
        """
            The position of the bookmark. Defaults to the bottom.
        """
        if position is not None:
            data["position"] = position

        # OPTIONAL - data
        """
            The data associated with the bookmark
        """
        if data is not None:
            data["data"] = data

        self.logger.debug(
            "POST /api/v1/users/self/bookmarks with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/users/self/bookmarks".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_bookmark(self, id):
        """
        Get bookmark.

        Returns the details for a bookmark.
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
            "GET /api/v1/users/self/bookmarks/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/bookmarks/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_bookmark(self, id, data=None, name=None, position=None, url=None):
        """
        Update bookmark.

        Updates a bookmark
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # OPTIONAL - name
        """
            The name of the bookmark
        """
        if name is not None:
            data["name"] = name

        # OPTIONAL - url
        """
            The url of the bookmark
        """
        if url is not None:
            data["url"] = url

        # OPTIONAL - position
        """
            The position of the bookmark. Defaults to the bottom.
        """
        if position is not None:
            data["position"] = position

        # OPTIONAL - data
        """
            The data associated with the bookmark
        """
        if data is not None:
            data["data"] = data

        self.logger.debug(
            "PUT /api/v1/users/self/bookmarks/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/self/bookmarks/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_bookmark(self, id):
        """
        Delete bookmark.

        Deletes a bookmark
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
            "DELETE /api/v1/users/self/bookmarks/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/users/self/bookmarks/{id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )


class Bookmark(BaseModel):
    """Bookmark Model."""

    def __init__(self, id=None, name=None, url=None, position=None, data=None):
        """Init method for Bookmark class."""
        self._id = id
        self._name = name
        self._url = url
        self._position = position
        self._data = data

        self.logger = logging.getLogger("py3canvas.Bookmark")

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
    def name(self):
        """name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

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
    def position(self):
        """position."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn(
            "Setting values on position will NOT update the remote Canvas instance."
        )
        self._position = value

    @property
    def data(self):
        """data."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn(
            "Setting values on data will NOT update the remote Canvas instance."
        )
        self._data = value
