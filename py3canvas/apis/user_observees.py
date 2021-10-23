"""UserObservees API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class UserObserveesAPI(BaseCanvasAPI):
    """UserObservees API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for UserObserveesAPI."""
        super(UserObserveesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.UserObserveesAPI")

    def list_observees(self, user_id, include=None):
        """
        List observees.

        A paginated list of the users that the given user is observing.
        
        *Note:* all users are allowed to list their own observees. Administrators can list
        other users' observees.
        
        The returned observees will include an attribute "observation_link_root_account_ids", a list
        of ids for the root accounts the observer and observee are linked on. The observer will only be able to
        observe in courses associated with these root accounts.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # OPTIONAL - include
        """
            - "avatar_url": Optionally include avatar_url.
        """
        if include is not None:
            self._validate_enum(include, ["avatar_url"])
            params["include"] = include


        self.logger.debug("GET /api/v1/users/{user_id}/observees with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/observees".format(**path), data=data, params=params, all_pages=True)

    def list_observers(self, user_id, include=None):
        """
        List observers.

        A paginated list of the observers of a given user.
        
        *Note:* all users are allowed to list their own observers. Administrators can list
        other users' observers.
        
        The returned observers will include an attribute "observation_link_root_account_ids", a list
        of ids for the root accounts the observer and observee are linked on. The observer will only be able to
        observe in courses associated with these root accounts.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # OPTIONAL - include
        """
            - "avatar_url": Optionally include avatar_url.
        """
        if include is not None:
            self._validate_enum(include, ["avatar_url"])
            params["include"] = include


        self.logger.debug("GET /api/v1/users/{user_id}/observers with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/observers".format(**path), data=data, params=params, all_pages=True)

    def add_observee_with_credentials(self, user_id, access_token=None, observee_password=None, observee_unique_id=None, pairing_code=None, root_account_id=None):
        """
        Add an observee with credentials.

        Register the given user to observe another user, given the observee's credentials.
        
        *Note:* all users are allowed to add their own observees, given the observee's
        credentials or access token are provided. Administrators can add observees given credentials, access token or
        the {api:UserObserveesController#update observee's id}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # OPTIONAL - observee[unique_id]
        """
            The login id for the user to observe.  Required if access_token is omitted.
        """
        if observee_unique_id is not None:
            data["observee[unique_id]"] = observee_unique_id


        # OPTIONAL - observee[password]
        """
            The password for the user to observe. Required if access_token is omitted.
        """
        if observee_password is not None:
            data["observee[password]"] = observee_password


        # OPTIONAL - access_token
        """
            The access token for the user to observe.  Required if <tt>observee[unique_id]</tt> or <tt>observee[password]</tt> are omitted.
        """
        if access_token is not None:
            data["access_token"] = access_token


        # OPTIONAL - pairing_code
        """
            A generated pairing code for the user to observe. Required if the Observer pairing code feature flag is enabled
        """
        if pairing_code is not None:
            data["pairing_code"] = pairing_code


        # OPTIONAL - root_account_id
        """
            The ID for the root account to associate with the observation link.
        Defaults to the current domain account.
        If 'all' is specified, a link will be created for each root account associated
        to both the observer and observee.
        """
        if root_account_id is not None:
            data["root_account_id"] = root_account_id


        self.logger.debug("POST /api/v1/users/{user_id}/observees with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/observees".format(**path), data=data, params=params, single_item=True)

    def show_observee(self, observee_id, user_id):
        """
        Show an observee.

        Gets information about an observed user.
        
        *Note:* all users are allowed to view their own observees.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - observee_id
        """
            ID
        """
        path["observee_id"] = observee_id


        self.logger.debug("GET /api/v1/users/{user_id}/observees/{observee_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/observees/{observee_id}".format(**path), data=data, params=params, single_item=True)

    def show_observer(self, observer_id, user_id):
        """
        Show an observer.

        Gets information about an observer.
        
        *Note:* all users are allowed to view their own observers.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - observer_id
        """
            ID
        """
        path["observer_id"] = observer_id


        self.logger.debug("GET /api/v1/users/{user_id}/observers/{observer_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/observers/{observer_id}".format(**path), data=data, params=params, single_item=True)

    def add_observee(self, observee_id, user_id, root_account_id=None):
        """
        Add an observee.

        Registers a user as being observed by the given user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - observee_id
        """
            ID
        """
        path["observee_id"] = observee_id


        # OPTIONAL - root_account_id
        """
            The ID for the root account to associate with the observation link.
        If not specified, a link will be created for each root account associated
        to both the observer and observee.
        """
        if root_account_id is not None:
            data["root_account_id"] = root_account_id


        self.logger.debug("PUT /api/v1/users/{user_id}/observees/{observee_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/observees/{observee_id}".format(**path), data=data, params=params, single_item=True)

    def remove_observee(self, observee_id, user_id, root_account_id=None):
        """
        Remove an observee.

        Unregisters a user as being observed by the given user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - observee_id
        """
            ID
        """
        path["observee_id"] = observee_id


        # OPTIONAL - root_account_id
        """
            If specified, only removes the link for the given root account
        """
        if root_account_id is not None:
            params["root_account_id"] = root_account_id


        self.logger.debug("DELETE /api/v1/users/{user_id}/observees/{observee_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/users/{user_id}/observees/{observee_id}".format(**path), data=data, params=params, single_item=True)

    def create_observer_pairing_code(self, user_id):
        """
        Create observer pairing code.

        If the user is a student, will generate a code to be used with self registration
        or observees APIs to link another user to this student.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("POST /api/v1/users/{user_id}/observer_pairing_codes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/observer_pairing_codes".format(**path), data=data, params=params, single_item=True)


class Pairingcode(BaseModel):
    """Pairingcode Model.
    A code used for linking a user to a student to observe them."""

    def __init__(self, user_id=None, code=None, expires_at=None, workflow_state=None):
        """Init method for Pairingcode class."""
        self._user_id = user_id
        self._code = code
        self._expires_at = expires_at
        self._workflow_state = workflow_state

        self.logger = logging.getLogger('py3canvas.Pairingcode')

    @property
    def user_id(self):
        """The ID of the user."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def code(self):
        """The actual code to be sent to other APIs."""
        return self._code

    @code.setter
    def code(self, value):
        """Setter for code property."""
        self.logger.warn("Setting values on code will NOT update the remote Canvas instance.")
        self._code = value

    @property
    def expires_at(self):
        """When the code expires."""
        return self._expires_at

    @expires_at.setter
    def expires_at(self, value):
        """Setter for expires_at property."""
        self.logger.warn("Setting values on expires_at will NOT update the remote Canvas instance.")
        self._expires_at = value

    @property
    def workflow_state(self):
        """The current status of the code."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

