"""Accounts(lti) API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class Accounts(lti)API(BaseCanvasAPI):
    """Accounts(lti) API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for Accounts(lti)API."""
        super(Accounts(lti)API, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.Accounts(lti)API")

    def get_account(self, account_id):
        """
        Get account.

        Retrieve information on an individual account, given by local or global ID.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/lti/accounts/{account_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/accounts/{account_id}".format(**path), data=data, params=params, single_item=True)


class Account(BaseModel):
    """Account Model."""

    def __init__(self, id=None, name=None, uuid=None, parent_account_id=None, root_account_id=None, workflow_state=None):
        """Init method for Account class."""
        self._id = id
        self._name = name
        self._uuid = uuid
        self._parent_account_id = parent_account_id
        self._root_account_id = root_account_id
        self._workflow_state = workflow_state

        self.logger = logging.getLogger('py3canvas.Account')

    @property
    def id(self):
        """the ID of the Account object."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """The display name of the account."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def uuid(self):
        """The UUID of the account."""
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """Setter for uuid property."""
        self.logger.warn("Setting values on uuid will NOT update the remote Canvas instance.")
        self._uuid = value

    @property
    def parent_account_id(self):
        """The account's parent ID, or null if this is the root account."""
        return self._parent_account_id

    @parent_account_id.setter
    def parent_account_id(self, value):
        """Setter for parent_account_id property."""
        self.logger.warn("Setting values on parent_account_id will NOT update the remote Canvas instance.")
        self._parent_account_id = value

    @property
    def root_account_id(self):
        """The ID of the root account, or null if this is the root account."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn("Setting values on root_account_id will NOT update the remote Canvas instance.")
        self._root_account_id = value

    @property
    def workflow_state(self):
        """The state of the account. Can be 'active' or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

