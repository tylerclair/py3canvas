"""ContentShares API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ContentSharesAPI(BaseCanvasAPI):
    """ContentShares API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ContentSharesAPI."""
        super(ContentSharesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ContentSharesAPI")

    def create_content_share(self, content_id, content_type, receiver_ids, user_id):
        """
        Create a content share.

        Share content directly between two or more users
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - receiver_ids
        """
            IDs of users to share the content with.
        """
        data["receiver_ids"] = receiver_ids


        # REQUIRED - content_type
        """
            Type of content you are sharing.
        """
        self._validate_enum(content_type, ["assignment", "discussion_topic", "page", "quiz", "module", "module_item"])
        data["content_type"] = content_type


        # REQUIRED - content_id
        """
            The id of the content that you are sharing
        """
        data["content_id"] = content_id


        self.logger.debug("POST /api/v1/users/{user_id}/content_shares with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/content_shares".format(**path), data=data, params=params, single_item=True)

    def list_content_shares_sent(self, user_id):
        """
        List content shares.

        Return a paginated list of content shares a user has sent or received. Use +self+ as the user_id
        to retrieve your own content shares. Only linked observers and administrators may view other users'
        content shares.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_shares/sent with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_shares/sent".format(**path), data=data, params=params, all_pages=True)

    def list_content_shares_received(self, user_id):
        """
        List content shares.

        Return a paginated list of content shares a user has sent or received. Use +self+ as the user_id
        to retrieve your own content shares. Only linked observers and administrators may view other users'
        content shares.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_shares/received with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_shares/received".format(**path), data=data, params=params, all_pages=True)

    def get_unread_shares_count(self, user_id):
        """
        Get unread shares count.

        Return the number of content shares a user has received that have not yet been read. Use +self+ as the user_id
        to retrieve your own content shares. Only linked observers and administrators may view other users'
        content shares.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_shares/unread_count with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_shares/unread_count".format(**path), data=data, params=params, single_item=True)

    def get_content_share(self, id, user_id):
        """
        Get content share.

        Return information about a single content share. You may use +self+ as the user_id to retrieve your own content share.
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


        self.logger.debug("GET /api/v1/users/{user_id}/content_shares/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_shares/{id}".format(**path), data=data, params=params, single_item=True)

    def remove_content_share(self, id, user_id):
        """
        Remove content share.

        Remove a content share from your list. Use +self+ as the user_id. Note that this endpoint does not delete other users'
        copies of the content share.
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


        self.logger.debug("DELETE /api/v1/users/{user_id}/content_shares/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/content_shares/{id}".format(**path), data=data, params=params, no_data=True)

    def add_users_to_content_share(self, id, user_id, receiver_ids=None):
        """
        Add users to content share.

        Send a previously created content share to additional users
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


        # OPTIONAL - receiver_ids
        """
            IDs of users to share the content with.
        """
        if receiver_ids is not None:
            data["receiver_ids"] = receiver_ids


        self.logger.debug("POST /api/v1/users/{user_id}/content_shares/{id}/add_users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/content_shares/{id}/add_users".format(**path), data=data, params=params, single_item=True)

    def update_content_share(self, id, user_id, read_state=None):
        """
        Update a content share.

        Mark a content share read or unread
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


        # OPTIONAL - read_state
        """
            Read state for the content share
        """
        if read_state is not None:
            self._validate_enum(read_state, ["read", "unread"])
            data["read_state"] = read_state


        self.logger.debug("PUT /api/v1/users/{user_id}/content_shares/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/content_shares/{id}".format(**path), data=data, params=params, single_item=True)


class Contentshare(BaseModel):
    """Contentshare Model.
    Content shared between users"""

    def __init__(self, id=None, name=None, content_type=None, created_at=None, updated_at=None, user_id=None, sender=None, receivers=None, source_course=None, read_state=None, content_export=None):
        """Init method for Contentshare class."""
        self._id = id
        self._name = name
        self._content_type = content_type
        self._created_at = created_at
        self._updated_at = updated_at
        self._user_id = user_id
        self._sender = sender
        self._receivers = receivers
        self._source_course = source_course
        self._read_state = read_state
        self._content_export = content_export

        self.logger = logging.getLogger('py3canvas.Contentshare')

    @property
    def id(self):
        """The id of the content share for the current user."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """The name of the shared content."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def content_type(self):
        """The type of content that was shared. Can be assignment, discussion_topic, page, quiz, module, or module_item."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn("Setting values on content_type will NOT update the remote Canvas instance.")
        self._content_type = value

    @property
    def created_at(self):
        """The datetime the content was shared with this user."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """The datetime the content was updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def user_id(self):
        """The id of the user who sent or received the content share."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def sender(self):
        """The user who shared the content. This field is provided only to receivers; it is not populated in the sender's list of sent content shares."""
        return self._sender

    @sender.setter
    def sender(self, value):
        """Setter for sender property."""
        self.logger.warn("Setting values on sender will NOT update the remote Canvas instance.")
        self._sender = value

    @property
    def receivers(self):
        """An Array of users the content is shared with.  This field is provided only to senders; an empty array will be returned for the receiving users."""
        return self._receivers

    @receivers.setter
    def receivers(self, value):
        """Setter for receivers property."""
        self.logger.warn("Setting values on receivers will NOT update the remote Canvas instance.")
        self._receivers = value

    @property
    def source_course(self):
        """The course the content was originally shared from."""
        return self._source_course

    @source_course.setter
    def source_course(self, value):
        """Setter for source_course property."""
        self.logger.warn("Setting values on source_course will NOT update the remote Canvas instance.")
        self._source_course = value

    @property
    def read_state(self):
        """Whether the recipient has viewed the content share."""
        return self._read_state

    @read_state.setter
    def read_state(self, value):
        """Setter for read_state property."""
        self.logger.warn("Setting values on read_state will NOT update the remote Canvas instance.")
        self._read_state = value

    @property
    def content_export(self):
        """The content export record associated with this content share."""
        return self._content_export

    @content_export.setter
    def content_export(self, value):
        """Setter for content_export property."""
        self.logger.warn("Setting values on content_export will NOT update the remote Canvas instance.")
        self._content_export = value

