"""MediaObjects API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class MediaObjectsAPI(BaseCanvasAPI):
    """MediaObjects API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for MediaObjectsAPI."""
        super(MediaObjectsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.MediaObjectsAPI")

    def list_media_tracks_for_media_object(self, media_object_id, include=None):
        """
        List media tracks for a Media Object.

        List the media tracks associated with a media object
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - media_object_id
        """
            ID
        """
        path["media_object_id"] = media_object_id

        # OPTIONAL - include
        """
            By default, index returns id, locale, kind, media_object_id, and user_id for each of the
        result MediaTracks. Use include[] to
        add additional fields. For example include[]=content
        """
        if include is not None:
            self._validate_enum(
                include, ["content", "webvtt_content", "updated_at", "created_at"]
            )
            params["include"] = include

        self.logger.debug(
            "GET /api/v1/media_objects/{media_object_id}/media_tracks with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/media_objects/{media_object_id}/media_tracks".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def update_media_tracks(self, media_object_id, include=None):
        """
        Update Media Tracks.

        Replace the media tracks associated with a media object with
        the array of tracks provided in the body.
        Update will
        delete any existing tracks not listed,
        leave untouched any tracks with no content field,
        and update or create tracks with a content field.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - media_object_id
        """
            ID
        """
        path["media_object_id"] = media_object_id

        # OPTIONAL - include
        """
            Retuns a listing of the resulting set of MediaTracks.
        Like List Media Objects, use the include[] parameter to
        add additional fields.
        """
        if include is not None:
            data["include"] = include

        self.logger.debug(
            "PUT /api/v1/media_objects/{media_object_id}/media_tracks with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/media_objects/{media_object_id}/media_tracks".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_media_objects_media_objects(self, exclude=None, order=None, sort=None):
        """
        List Media Objects.

        Returns media objects created by the user making the request. When
        using the second version, returns media objects associated with
        the given course.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - sort
        """
            Field to sort on. Default is "title"

        title:: sorts on user_entered_title if available, title if not.

        created_at:: sorts on the object's creation time.
        """
        if sort is not None:
            self._validate_enum(sort, ["title", "created_at"])
            params["sort"] = sort

        # OPTIONAL - order
        """
            Sort direction. Default is "asc"
        """
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        # OPTIONAL - exclude
        """
            Array of data to exclude. By excluding "sources" and "tracks",
        the api will not need to query kaltura, which greatly
        speeds up its response.

        sources:: Do not query kaltura for media_sources
        tracks:: Do not query kaltura for media_tracks
        """
        if exclude is not None:
            self._validate_enum(exclude, ["sources", "tracks"])
            params["exclude"] = exclude

        self.logger.debug(
            "GET /api/v1/media_objects with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/media_objects".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_media_objects_courses(
        self, course_id, exclude=None, order=None, sort=None
    ):
        """
        List Media Objects.

        Returns media objects created by the user making the request. When
        using the second version, returns media objects associated with
        the given course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - sort
        """
            Field to sort on. Default is "title"

        title:: sorts on user_entered_title if available, title if not.

        created_at:: sorts on the object's creation time.
        """
        if sort is not None:
            self._validate_enum(sort, ["title", "created_at"])
            params["sort"] = sort

        # OPTIONAL - order
        """
            Sort direction. Default is "asc"
        """
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        # OPTIONAL - exclude
        """
            Array of data to exclude. By excluding "sources" and "tracks",
        the api will not need to query kaltura, which greatly
        speeds up its response.

        sources:: Do not query kaltura for media_sources
        tracks:: Do not query kaltura for media_tracks
        """
        if exclude is not None:
            self._validate_enum(exclude, ["sources", "tracks"])
            params["exclude"] = exclude

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/media_objects with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/media_objects".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_media_objects_groups(self, group_id, exclude=None, order=None, sort=None):
        """
        List Media Objects.

        Returns media objects created by the user making the request. When
        using the second version, returns media objects associated with
        the given course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id

        # OPTIONAL - sort
        """
            Field to sort on. Default is "title"

        title:: sorts on user_entered_title if available, title if not.

        created_at:: sorts on the object's creation time.
        """
        if sort is not None:
            self._validate_enum(sort, ["title", "created_at"])
            params["sort"] = sort

        # OPTIONAL - order
        """
            Sort direction. Default is "asc"
        """
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        # OPTIONAL - exclude
        """
            Array of data to exclude. By excluding "sources" and "tracks",
        the api will not need to query kaltura, which greatly
        speeds up its response.

        sources:: Do not query kaltura for media_sources
        tracks:: Do not query kaltura for media_tracks
        """
        if exclude is not None:
            self._validate_enum(exclude, ["sources", "tracks"])
            params["exclude"] = exclude

        self.logger.debug(
            "GET /api/v1/groups/{group_id}/media_objects with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/groups/{group_id}/media_objects".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def update_media_object(self, media_object_id, user_entered_title=None):
        """
        Update Media Object.


        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - media_object_id
        """
            ID
        """
        path["media_object_id"] = media_object_id

        # OPTIONAL - user_entered_title
        """
            The new title.
        """
        if user_entered_title is not None:
            data["user_entered_title"] = user_entered_title

        self.logger.debug(
            "PUT /api/v1/media_objects/{media_object_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/media_objects/{media_object_id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )


class Mediatrack(BaseModel):
    """Mediatrack Model."""

    def __init__(
        self,
        id=None,
        user_id=None,
        media_object_id=None,
        kind=None,
        locale=None,
        content=None,
        created_at=None,
        updated_at=None,
        webvtt_content=None,
    ):
        """Init method for Mediatrack class."""
        self._id = id
        self._user_id = user_id
        self._media_object_id = media_object_id
        self._kind = kind
        self._locale = locale
        self._content = content
        self._created_at = created_at
        self._updated_at = updated_at
        self._webvtt_content = webvtt_content

        self.logger = logging.getLogger("py3canvas.Mediatrack")

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
    def user_id(self):
        """user_id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def media_object_id(self):
        """media_object_id."""
        return self._media_object_id

    @media_object_id.setter
    def media_object_id(self, value):
        """Setter for media_object_id property."""
        self.logger.warn(
            "Setting values on media_object_id will NOT update the remote Canvas instance."
        )
        self._media_object_id = value

    @property
    def kind(self):
        """kind."""
        return self._kind

    @kind.setter
    def kind(self, value):
        """Setter for kind property."""
        self.logger.warn(
            "Setting values on kind will NOT update the remote Canvas instance."
        )
        self._kind = value

    @property
    def locale(self):
        """locale."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn(
            "Setting values on locale will NOT update the remote Canvas instance."
        )
        self._locale = value

    @property
    def content(self):
        """content."""
        return self._content

    @content.setter
    def content(self, value):
        """Setter for content property."""
        self.logger.warn(
            "Setting values on content will NOT update the remote Canvas instance."
        )
        self._content = value

    @property
    def created_at(self):
        """created_at."""
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
        """updated_at."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value

    @property
    def webvtt_content(self):
        """webvtt_content."""
        return self._webvtt_content

    @webvtt_content.setter
    def webvtt_content(self, value):
        """Setter for webvtt_content property."""
        self.logger.warn(
            "Setting values on webvtt_content will NOT update the remote Canvas instance."
        )
        self._webvtt_content = value


class Mediaobject(BaseModel):
    """Mediaobject Model."""

    def __init__(
        self,
        can_add_captions=None,
        user_entered_title=None,
        title=None,
        media_id=None,
        media_type=None,
        media_tracks=None,
        media_sources=None,
    ):
        """Init method for Mediaobject class."""
        self._can_add_captions = can_add_captions
        self._user_entered_title = user_entered_title
        self._title = title
        self._media_id = media_id
        self._media_type = media_type
        self._media_tracks = media_tracks
        self._media_sources = media_sources

        self.logger = logging.getLogger("py3canvas.Mediaobject")

    @property
    def can_add_captions(self):
        """can_add_captions."""
        return self._can_add_captions

    @can_add_captions.setter
    def can_add_captions(self, value):
        """Setter for can_add_captions property."""
        self.logger.warn(
            "Setting values on can_add_captions will NOT update the remote Canvas instance."
        )
        self._can_add_captions = value

    @property
    def user_entered_title(self):
        """user_entered_title."""
        return self._user_entered_title

    @user_entered_title.setter
    def user_entered_title(self, value):
        """Setter for user_entered_title property."""
        self.logger.warn(
            "Setting values on user_entered_title will NOT update the remote Canvas instance."
        )
        self._user_entered_title = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn(
            "Setting values on title will NOT update the remote Canvas instance."
        )
        self._title = value

    @property
    def media_id(self):
        """media_id."""
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        """Setter for media_id property."""
        self.logger.warn(
            "Setting values on media_id will NOT update the remote Canvas instance."
        )
        self._media_id = value

    @property
    def media_type(self):
        """media_type."""
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        """Setter for media_type property."""
        self.logger.warn(
            "Setting values on media_type will NOT update the remote Canvas instance."
        )
        self._media_type = value

    @property
    def media_tracks(self):
        """media_tracks."""
        return self._media_tracks

    @media_tracks.setter
    def media_tracks(self, value):
        """Setter for media_tracks property."""
        self.logger.warn(
            "Setting values on media_tracks will NOT update the remote Canvas instance."
        )
        self._media_tracks = value

    @property
    def media_sources(self):
        """media_sources."""
        return self._media_sources

    @media_sources.setter
    def media_sources(self, value):
        """Setter for media_sources property."""
        self.logger.warn(
            "Setting values on media_sources will NOT update the remote Canvas instance."
        )
        self._media_sources = value
