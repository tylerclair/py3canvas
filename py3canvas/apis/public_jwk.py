"""PublicJwk API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PublicJwkAPI(BaseCanvasAPI):
    """PublicJwk API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PublicJwkAPI."""
        super(PublicJwkAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PublicJwkAPI")

    def update_public_jwk(self, public_jwk):
        """
        Update Public JWK.

        Rotate the public key in jwk format when using lti services
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - public_jwk
        """
            The new public jwk that will be set to the tools current public jwk.
        """
        data["public_jwk"] = public_jwk

        self.logger.debug(
            "PUT /api/lti/developer_key/update_public_jwk with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/lti/developer_key/update_public_jwk".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Developerkey(BaseModel):
    """Developerkey Model."""

    def __init__(
        self,
        id=None,
        is_lti_key=None,
        visible=None,
        account_name=None,
        public_jwk=None,
        vendor_code=None,
        last_used_at=None,
        access_token_count=None,
        redirect_uris=None,
        redirect_uri=None,
        api_key=None,
        notes=None,
        name=None,
        user_id=None,
        created_at=None,
        user_name=None,
        email=None,
        require_scopes=None,
        icon_url=None,
        scopes=None,
        workflow_state=None,
    ):
        """Init method for Developerkey class."""
        self._id = id
        self._is_lti_key = is_lti_key
        self._visible = visible
        self._account_name = account_name
        self._public_jwk = public_jwk
        self._vendor_code = vendor_code
        self._last_used_at = last_used_at
        self._access_token_count = access_token_count
        self._redirect_uris = redirect_uris
        self._redirect_uri = redirect_uri
        self._api_key = api_key
        self._notes = notes
        self._name = name
        self._user_id = user_id
        self._created_at = created_at
        self._user_name = user_name
        self._email = email
        self._require_scopes = require_scopes
        self._icon_url = icon_url
        self._scopes = scopes
        self._workflow_state = workflow_state

        self.logger = logging.getLogger("py3canvas.Developerkey")

    @property
    def id(self):
        """The ID should match the Developer Key ID in canvas."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def is_lti_key(self):
        """true the tool is a lti key, null is not a lti key."""
        return self._is_lti_key

    @is_lti_key.setter
    def is_lti_key(self, value):
        """Setter for is_lti_key property."""
        self.logger.warn(
            "Setting values on is_lti_key will NOT update the remote Canvas instance."
        )
        self._is_lti_key = value

    @property
    def visible(self):
        """Controls if the tool is visable."""
        return self._visible

    @visible.setter
    def visible(self, value):
        """Setter for visible property."""
        self.logger.warn(
            "Setting values on visible will NOT update the remote Canvas instance."
        )
        self._visible = value

    @property
    def account_name(self):
        """The name of the account associated with the tool."""
        return self._account_name

    @account_name.setter
    def account_name(self, value):
        """Setter for account_name property."""
        self.logger.warn(
            "Setting values on account_name will NOT update the remote Canvas instance."
        )
        self._account_name = value

    @property
    def public_jwk(self):
        """The public key in jwk format."""
        return self._public_jwk

    @public_jwk.setter
    def public_jwk(self, value):
        """Setter for public_jwk property."""
        self.logger.warn(
            "Setting values on public_jwk will NOT update the remote Canvas instance."
        )
        self._public_jwk = value

    @property
    def vendor_code(self):
        """The code of the vendor managing the tool."""
        return self._vendor_code

    @vendor_code.setter
    def vendor_code(self, value):
        """Setter for vendor_code property."""
        self.logger.warn(
            "Setting values on vendor_code will NOT update the remote Canvas instance."
        )
        self._vendor_code = value

    @property
    def last_used_at(self):
        """The date and time the tool was last used."""
        return self._last_used_at

    @last_used_at.setter
    def last_used_at(self, value):
        """Setter for last_used_at property."""
        self.logger.warn(
            "Setting values on last_used_at will NOT update the remote Canvas instance."
        )
        self._last_used_at = value

    @property
    def access_token_count(self):
        """The number of active access tokens associated with the tool."""
        return self._access_token_count

    @access_token_count.setter
    def access_token_count(self, value):
        """Setter for access_token_count property."""
        self.logger.warn(
            "Setting values on access_token_count will NOT update the remote Canvas instance."
        )
        self._access_token_count = value

    @property
    def redirect_uris(self):
        """redirect uris description."""
        return self._redirect_uris

    @redirect_uris.setter
    def redirect_uris(self, value):
        """Setter for redirect_uris property."""
        self.logger.warn(
            "Setting values on redirect_uris will NOT update the remote Canvas instance."
        )
        self._redirect_uris = value

    @property
    def redirect_uri(self):
        """redirect uri description."""
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, value):
        """Setter for redirect_uri property."""
        self.logger.warn(
            "Setting values on redirect_uri will NOT update the remote Canvas instance."
        )
        self._redirect_uri = value

    @property
    def api_key(self):
        """Api key for api access for the tool."""
        return self._api_key

    @api_key.setter
    def api_key(self, value):
        """Setter for api_key property."""
        self.logger.warn(
            "Setting values on api_key will NOT update the remote Canvas instance."
        )
        self._api_key = value

    @property
    def notes(self):
        """Notes for use specifications for the tool."""
        return self._notes

    @notes.setter
    def notes(self, value):
        """Setter for notes property."""
        self.logger.warn(
            "Setting values on notes will NOT update the remote Canvas instance."
        )
        self._notes = value

    @property
    def name(self):
        """Display name of the tool."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def user_id(self):
        """ID of the user associated with the tool."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def created_at(self):
        """The time the jwk was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def user_name(self):
        """The user name of the tool creator."""
        return self._user_name

    @user_name.setter
    def user_name(self, value):
        """Setter for user_name property."""
        self.logger.warn(
            "Setting values on user_name will NOT update the remote Canvas instance."
        )
        self._user_name = value

    @property
    def email(self):
        """Email associated with the tool owner."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email property."""
        self.logger.warn(
            "Setting values on email will NOT update the remote Canvas instance."
        )
        self._email = value

    @property
    def require_scopes(self):
        """True if the tool has required permissions, null if there are no needed permissions."""
        return self._require_scopes

    @require_scopes.setter
    def require_scopes(self, value):
        """Setter for require_scopes property."""
        self.logger.warn(
            "Setting values on require_scopes will NOT update the remote Canvas instance."
        )
        self._require_scopes = value

    @property
    def icon_url(self):
        """Icon to be displayed with the name of the tool."""
        return self._icon_url

    @icon_url.setter
    def icon_url(self, value):
        """Setter for icon_url property."""
        self.logger.warn(
            "Setting values on icon_url will NOT update the remote Canvas instance."
        )
        self._icon_url = value

    @property
    def scopes(self):
        """Specified permissions for the tool."""
        return self._scopes

    @scopes.setter
    def scopes(self, value):
        """Setter for scopes property."""
        self.logger.warn(
            "Setting values on scopes will NOT update the remote Canvas instance."
        )
        self._scopes = value

    @property
    def workflow_state(self):
        """The current state of the tool."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value
