"""ApiTokenScopes API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ApiTokenScopesAPI(BaseCanvasAPI):
    """ApiTokenScopes API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ApiTokenScopesAPI."""
        super(ApiTokenScopesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ApiTokenScopesAPI")

    def list_scopes(self, account_id, group_by=None):
        """
        List scopes.

        A list of scopes that can be applied to developer keys and access tokens.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # OPTIONAL - group_by
        """
            The attribute to group the scopes by. By default no grouping is done.
        """
        if group_by is not None:
            self._validate_enum(group_by, ["resource_name"])
            params["group_by"] = group_by


        self.logger.debug("GET /api/v1/accounts/{account_id}/scopes with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/scopes".format(**path), data=data, params=params, all_pages=True)


class Scope(BaseModel):
    """Scope Model."""

    def __init__(self, resource=None, resource_name=None, controller=None, action=None, verb=None, scope=None):
        """Init method for Scope class."""
        self._resource = resource
        self._resource_name = resource_name
        self._controller = controller
        self._action = action
        self._verb = verb
        self._scope = scope

        self.logger = logging.getLogger('py3canvas.Scope')

    @property
    def resource(self):
        """The resource the scope is associated with."""
        return self._resource

    @resource.setter
    def resource(self, value):
        """Setter for resource property."""
        self.logger.warn("Setting values on resource will NOT update the remote Canvas instance.")
        self._resource = value

    @property
    def resource_name(self):
        """The localized resource name."""
        return self._resource_name

    @resource_name.setter
    def resource_name(self, value):
        """Setter for resource_name property."""
        self.logger.warn("Setting values on resource_name will NOT update the remote Canvas instance.")
        self._resource_name = value

    @property
    def controller(self):
        """The controller the scope is associated to."""
        return self._controller

    @controller.setter
    def controller(self, value):
        """Setter for controller property."""
        self.logger.warn("Setting values on controller will NOT update the remote Canvas instance.")
        self._controller = value

    @property
    def action(self):
        """The controller action the scope is associated to."""
        return self._action

    @action.setter
    def action(self, value):
        """Setter for action property."""
        self.logger.warn("Setting values on action will NOT update the remote Canvas instance.")
        self._action = value

    @property
    def verb(self):
        """The HTTP verb for the scope."""
        return self._verb

    @verb.setter
    def verb(self, value):
        """Setter for verb property."""
        self.logger.warn("Setting values on verb will NOT update the remote Canvas instance.")
        self._verb = value

    @property
    def scope(self):
        """The identifier for the scope."""
        return self._scope

    @scope.setter
    def scope(self, value):
        """Setter for scope property."""
        self.logger.warn("Setting values on scope will NOT update the remote Canvas instance.")
        self._scope = value

