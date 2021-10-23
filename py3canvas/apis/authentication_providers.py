"""AuthenticationProviders API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class AuthenticationProvidersAPI(BaseCanvasAPI):
    """AuthenticationProviders API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AuthenticationProvidersAPI."""
        super(AuthenticationProvidersAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AuthenticationProvidersAPI")

    def list_authentication_providers(self, account_id):
        """
        List authentication providers.

        Returns a paginated list of authentication providers
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/authentication_providers with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/authentication_providers".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def add_authentication_provider(self, account_id):
        """
        Add authentication provider.

        Add external authentication provider(s) for the account.
        Services may be Apple, CAS, Facebook, GitHub, Google, LDAP, LinkedIn,
        Microsoft, OpenID Connect, SAML, or Twitter.

        Each authentication provider is specified as a set of parameters as
        described below. A provider specification must include an 'auth_type'
        parameter with a value of 'apple', 'canvas', 'cas', 'clever', 'facebook',
        'github', 'google', 'ldap', 'linkedin', 'microsoft', 'openid_connect',
        'saml', or 'twitter'. The other recognized parameters depend on this
        auth_type; unrecognized parameters are discarded. Provider specifications
        not specifying a valid auth_type are ignored.

        You can set the 'position' for any provider. The config in the 1st position
        is considered the default. You can set 'jit_provisioning' for any provider
        besides Canvas. You can set 'mfa_required' for any provider.

        For Apple, the additional recognized parameters are:

        - client_id [Required]

          The developer’s client identifier, as provided by WWDR. Not available if
          configured globally for Canvas.

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'sub' (the default), or 'email'

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'email',
          'firstName', 'lastName', and 'sub'.

        For Canvas, the additional recognized parameter is:

        - self_registration

          'all', 'none', or 'observer' - who is allowed to register as a new user

        For CAS, the additional recognized parameters are:

        - auth_base

          The CAS server's URL.

        - log_in_url [Optional]

          An alternate SSO URL for logging into CAS. You probably should not set
          this.

        For Clever, the additional recognized parameters are:

        - client_id [Required]

          The Clever application's Client ID. Not available if configured globally
          for Canvas.

        - client_secret [Required]

          The Clever application's Client Secret. Not available if configured
          globally for Canvas.

        - district_id [Optional]

          A district's Clever ID. Leave this blank to let Clever handle the details
          with its District Picker. This is required for Clever Instant Login to
          work in a multi-tenant environment.

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'id' (the default), 'sis_id', 'email', 'student_number', or
          'teacher_number'. Note that some fields may not be populated for
          all users at Clever.

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'id',
          'sis_id', 'email', 'student_number', and 'teacher_number'.

        For Facebook, the additional recognized parameters are:

        - app_id [Required]

          The Facebook App ID. Not available if configured globally for Canvas.

        - app_secret [Required]

          The Facebook App Secret. Not available if configured globally for Canvas.

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'id' (the default), or 'email'

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'email',
          'first_name', 'id', 'last_name', 'locale', and 'name'.

        For GitHub, the additional recognized parameters are:

        - domain [Optional]

          The domain of a GitHub Enterprise installation. I.e.
          github.mycompany.com. If not set, it will default to the public
          github.com.

        - client_id [Required]

          The GitHub application's Client ID. Not available if configured globally
          for Canvas.

        - client_secret [Required]

          The GitHub application's Client Secret. Not available if configured
          globally for Canvas.

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'id' (the default), or 'login'

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'email',
          'id', 'login', and 'name'.

        For Google, the additional recognized parameters are:

        - client_id [Required]

          The Google application's Client ID. Not available if configured globally
          for Canvas.

        - client_secret [Required]

          The Google application's Client Secret. Not available if configured
          globally for Canvas.

        - hosted_domain [Optional]

          A Google Apps domain to restrict logins to. See
          https://developers.google.com/identity/protocols/OpenIDConnect?hl=en#hd-param

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'sub' (the default), or 'email'

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'email',
          'family_name', 'given_name', 'locale', 'name', and 'sub'.

        For LDAP, the additional recognized parameters are:

        - auth_host

          The LDAP server's URL.

        - auth_port [Optional, Integer]

          The LDAP server's TCP port. (default: 389)

        - auth_over_tls [Optional]

          Whether to use TLS. Can be 'simple_tls', or 'start_tls'. For backwards
          compatibility, booleans are also accepted, with true meaning simple_tls.
          If not provided, it will default to start_tls.

        - auth_base [Optional]

          A default treebase parameter for searches performed against the LDAP
          server.

        - auth_filter

          LDAP search filter. Use !{{login}} as a placeholder for the username
          supplied by the user. For example: "(sAMAccountName=!{{login}})".

        - identifier_format [Optional]

          The LDAP attribute to use to look up the Canvas login. Omit to use
          the username supplied by the user.

        - auth_username

          Username

        - auth_password

          Password

        For LinkedIn, the additional recognized parameters are:

        - client_id [Required]

          The LinkedIn application's Client ID. Not available if configured globally
          for Canvas.

        - client_secret [Required]

          The LinkedIn application's Client Secret. Not available if configured
          globally for Canvas.

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'id' (the default), or 'emailAddress'

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'emailAddress',
          'firstName', 'id', 'formattedName', and 'lastName'.

        For Microsoft, the additional recognized parameters are:

        - application_id [Required]

          The application's ID.

        - application_secret [Required]

          The application's Client Secret (Password)

        - tenant [Optional]

          See https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-protocols/
          Valid values are 'common', 'organizations', 'consumers', or an Azure Active Directory Tenant
          (as either a UUID or domain, such as contoso.onmicrosoft.com). Defaults to 'common'

        - login_attribute [Optional]

          See https://azure.microsoft.com/en-us/documentation/articles/active-directory-v2-tokens/#idtokens
          Valid values are 'sub', 'email', 'oid', or 'preferred_username'. Note
          that email may not always be populated in the user's profile at
          Microsoft. Oid will not be populated for personal Microsoft accounts.
          Defaults to 'sub'

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'email',
          'name', 'preferred_username', 'oid', and 'sub'.

        For OpenID Connect, the additional recognized parameters are:

        - client_id [Required]

          The application's Client ID.

        - client_secret [Required]

          The application's Client Secret.

        - authorize_url [Required]

          The URL for getting starting the OAuth 2.0 web flow

        - token_url [Required]

          The URL for exchanging the OAuth 2.0 authorization code for an Access
          Token and ID Token

        - scope [Optional]

          Space separated additional scopes to request for the token. Note that
          you need not specify the 'openid' scope, or any scopes that can be
          automatically inferred by the rules defined at
          http://openid.net/specs/openid-connect-core-1_0.html#ScopeClaims

        - end_session_endpoint [Optional]

          URL to send the end user to after logging out of Canvas. See
          https://openid.net/specs/openid-connect-session-1_0.html#RPLogout

        - userinfo_endpoint [Optional]

          URL to request additional claims from. If the initial ID Token received
          from the provider cannot be used to satisfy the login_attribute and
          all federated_attributes, this endpoint will be queried for additional
          information.

        - login_attribute [Optional]

          The attribute of the ID Token to look up the user's login in Canvas.
          Defaults to 'sub'.

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Any value is allowed for the provider
          attribute names, but standard claims are listed at
          http://openid.net/specs/openid-connect-core-1_0.html#StandardClaims

        For SAML, the additional recognized parameters are:

        - metadata [Optional]

          An XML document to parse as SAML metadata, and automatically populate idp_entity_id,
          log_in_url, log_out_url, certificate_fingerprint, and identifier_format

        - metadata_uri [Optional]

          A URI to download the SAML metadata from, and automatically populate idp_entity_id,
          log_in_url, log_out_url, certificate_fingerprint, and identifier_format. This URI
          will also be saved, and the metadata periodically refreshed, automatically. If
          the metadata contains multiple entities, also supply idp_entity_id to distinguish
          which one you want (otherwise the only entity in the metadata will be inferred).
          If you provide the URI 'urn:mace:incommon' or 'http://ukfederation.org.uk',
          the InCommon or UK Access Management Federation metadata aggregate, respectively,
          will be used instead, and additional validation checks will happen (including
          validating that the metadata has been properly signed with the
          appropriate key).

        - idp_entity_id

          The SAML IdP's entity ID

        - log_in_url

          The SAML service's SSO target URL

        - log_out_url [Optional]

          The SAML service's SLO target URL

        - certificate_fingerprint

          The SAML service's certificate fingerprint.

        - identifier_format

          The SAML service's identifier format. Must be one of:

          - urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress
          - urn:oasis:names:tc:SAML:2.0:nameid-format:entity
          - urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos
          - urn:oasis:names:tc:SAML:2.0:nameid-format:persistent
          - urn:oasis:names:tc:SAML:2.0:nameid-format:transient
          - urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified
          - urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName
          - urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName

        - requested_authn_context [Optional]

          The SAML AuthnContext

        - sig_alg [Optional]

          If set, +AuthnRequest+, +LogoutRequest+, and +LogoutResponse+ messages
          are signed with the corresponding algorithm. Supported algorithms are:

          - {http://www.w3.org/2000/09/xmldsig#rsa-sha1}
          - {http://www.w3.org/2001/04/xmldsig-more#rsa-sha256}

          RSA-SHA1 and RSA-SHA256 are acceptable aliases.

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Any value is allowed for the provider attribute names.

        For Twitter, the additional recognized parameters are:

        - consumer_key [Required]

          The Twitter Consumer Key. Not available if configured globally for Canvas.

        - consumer_secret [Required]

          The Twitter Consumer Secret. Not available if configured globally for Canvas.

        - login_attribute [Optional]

          The attribute to use to look up the user's login in Canvas. Either
          'user_id' (the default), or 'screen_name'

        - parent_registration [Optional] - DEPRECATED 2017-11-03

          Accepts a boolean value, true designates the authentication service
          for use on parent registrations.  Only one service can be selected
          at a time so if set to true all others will be set to false

        - federated_attributes [Optional]

          See FederatedAttributesConfig. Valid provider attributes are 'name',
          'screen_name', 'time_zone', and 'user_id'.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/authentication_providers with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/authentication_providers".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_authentication_provider(self, account_id, id):
        """
        Update authentication provider.

        Update an authentication provider using the same options as the create endpoint.
        You can not update an existing provider to a new authentication type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "PUT /api/v1/accounts/{account_id}/authentication_providers/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/authentication_providers/{id}".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def get_authentication_provider(self, account_id, id):
        """
        Get authentication provider.

        Get the specified authentication provider
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/authentication_providers/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/authentication_providers/{id}".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_authentication_provider(self, account_id, id):
        """
        Delete authentication provider.

        Delete the config
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "DELETE /api/v1/accounts/{account_id}/authentication_providers/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/accounts/{account_id}/authentication_providers/{id}".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def show_account_auth_settings(self, account_id):
        """
        show account auth settings.

        The way to get the current state of each account level setting
        that's relevant to Single Sign On configuration

        You can list the current state of each setting with "update_sso_settings"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/sso_settings with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/sso_settings".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_account_auth_settings(self, account_id):
        """
        update account auth settings.

        For various cases of mixed SSO configurations, you may need to set some
        configuration at the account level to handle the particulars of your
        setup.

        This endpoint accepts a PUT request to set several possible account
        settings. All setting are optional on each request, any that are not
        provided at all are simply retained as is.  Any that provide the key but
        a null-ish value (blank string, null, undefined) will be UN-set.

        You can list the current state of each setting with "show_sso_settings"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "PUT /api/v1/accounts/{account_id}/sso_settings with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/sso_settings".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Authenticationprovider(BaseModel):
    """Authenticationprovider Model."""

    def __init__(
        self,
        identifier_format=None,
        auth_type=None,
        id=None,
        log_out_url=None,
        log_in_url=None,
        certificate_fingerprint=None,
        requested_authn_context=None,
        auth_host=None,
        auth_filter=None,
        auth_over_tls=None,
        auth_base=None,
        auth_username=None,
        auth_port=None,
        position=None,
        idp_entity_id=None,
        login_attribute=None,
        sig_alg=None,
        jit_provisioning=None,
        federated_attributes=None,
        mfa_required=None,
    ):
        """Init method for Authenticationprovider class."""
        self._identifier_format = identifier_format
        self._auth_type = auth_type
        self._id = id
        self._log_out_url = log_out_url
        self._log_in_url = log_in_url
        self._certificate_fingerprint = certificate_fingerprint
        self._requested_authn_context = requested_authn_context
        self._auth_host = auth_host
        self._auth_filter = auth_filter
        self._auth_over_tls = auth_over_tls
        self._auth_base = auth_base
        self._auth_username = auth_username
        self._auth_port = auth_port
        self._position = position
        self._idp_entity_id = idp_entity_id
        self._login_attribute = login_attribute
        self._sig_alg = sig_alg
        self._jit_provisioning = jit_provisioning
        self._federated_attributes = federated_attributes
        self._mfa_required = mfa_required

        self.logger = logging.getLogger("py3canvas.Authenticationprovider")

    @property
    def identifier_format(self):
        """Valid for SAML providers."""
        return self._identifier_format

    @identifier_format.setter
    def identifier_format(self, value):
        """Setter for identifier_format property."""
        self.logger.warn(
            "Setting values on identifier_format will NOT update the remote Canvas instance."
        )
        self._identifier_format = value

    @property
    def auth_type(self):
        """Valid for all providers."""
        return self._auth_type

    @auth_type.setter
    def auth_type(self, value):
        """Setter for auth_type property."""
        self.logger.warn(
            "Setting values on auth_type will NOT update the remote Canvas instance."
        )
        self._auth_type = value

    @property
    def id(self):
        """Valid for all providers."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def log_out_url(self):
        """Valid for SAML providers."""
        return self._log_out_url

    @log_out_url.setter
    def log_out_url(self, value):
        """Setter for log_out_url property."""
        self.logger.warn(
            "Setting values on log_out_url will NOT update the remote Canvas instance."
        )
        self._log_out_url = value

    @property
    def log_in_url(self):
        """Valid for SAML and CAS providers."""
        return self._log_in_url

    @log_in_url.setter
    def log_in_url(self, value):
        """Setter for log_in_url property."""
        self.logger.warn(
            "Setting values on log_in_url will NOT update the remote Canvas instance."
        )
        self._log_in_url = value

    @property
    def certificate_fingerprint(self):
        """Valid for SAML providers."""
        return self._certificate_fingerprint

    @certificate_fingerprint.setter
    def certificate_fingerprint(self, value):
        """Setter for certificate_fingerprint property."""
        self.logger.warn(
            "Setting values on certificate_fingerprint will NOT update the remote Canvas instance."
        )
        self._certificate_fingerprint = value

    @property
    def requested_authn_context(self):
        """Valid for SAML providers."""
        return self._requested_authn_context

    @requested_authn_context.setter
    def requested_authn_context(self, value):
        """Setter for requested_authn_context property."""
        self.logger.warn(
            "Setting values on requested_authn_context will NOT update the remote Canvas instance."
        )
        self._requested_authn_context = value

    @property
    def auth_host(self):
        """Valid for LDAP providers."""
        return self._auth_host

    @auth_host.setter
    def auth_host(self, value):
        """Setter for auth_host property."""
        self.logger.warn(
            "Setting values on auth_host will NOT update the remote Canvas instance."
        )
        self._auth_host = value

    @property
    def auth_filter(self):
        """Valid for LDAP providers."""
        return self._auth_filter

    @auth_filter.setter
    def auth_filter(self, value):
        """Setter for auth_filter property."""
        self.logger.warn(
            "Setting values on auth_filter will NOT update the remote Canvas instance."
        )
        self._auth_filter = value

    @property
    def auth_over_tls(self):
        """Valid for LDAP providers."""
        return self._auth_over_tls

    @auth_over_tls.setter
    def auth_over_tls(self, value):
        """Setter for auth_over_tls property."""
        self.logger.warn(
            "Setting values on auth_over_tls will NOT update the remote Canvas instance."
        )
        self._auth_over_tls = value

    @property
    def auth_base(self):
        """Valid for LDAP and CAS providers."""
        return self._auth_base

    @auth_base.setter
    def auth_base(self, value):
        """Setter for auth_base property."""
        self.logger.warn(
            "Setting values on auth_base will NOT update the remote Canvas instance."
        )
        self._auth_base = value

    @property
    def auth_username(self):
        """Valid for LDAP providers."""
        return self._auth_username

    @auth_username.setter
    def auth_username(self, value):
        """Setter for auth_username property."""
        self.logger.warn(
            "Setting values on auth_username will NOT update the remote Canvas instance."
        )
        self._auth_username = value

    @property
    def auth_port(self):
        """Valid for LDAP providers."""
        return self._auth_port

    @auth_port.setter
    def auth_port(self, value):
        """Setter for auth_port property."""
        self.logger.warn(
            "Setting values on auth_port will NOT update the remote Canvas instance."
        )
        self._auth_port = value

    @property
    def position(self):
        """Valid for all providers."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn(
            "Setting values on position will NOT update the remote Canvas instance."
        )
        self._position = value

    @property
    def idp_entity_id(self):
        """Valid for SAML providers."""
        return self._idp_entity_id

    @idp_entity_id.setter
    def idp_entity_id(self, value):
        """Setter for idp_entity_id property."""
        self.logger.warn(
            "Setting values on idp_entity_id will NOT update the remote Canvas instance."
        )
        self._idp_entity_id = value

    @property
    def login_attribute(self):
        """Valid for SAML providers."""
        return self._login_attribute

    @login_attribute.setter
    def login_attribute(self, value):
        """Setter for login_attribute property."""
        self.logger.warn(
            "Setting values on login_attribute will NOT update the remote Canvas instance."
        )
        self._login_attribute = value

    @property
    def sig_alg(self):
        """Valid for SAML providers."""
        return self._sig_alg

    @sig_alg.setter
    def sig_alg(self, value):
        """Setter for sig_alg property."""
        self.logger.warn(
            "Setting values on sig_alg will NOT update the remote Canvas instance."
        )
        self._sig_alg = value

    @property
    def jit_provisioning(self):
        """Just In Time provisioning. Valid for all providers except Canvas (which has the similar in concept self_registration setting)."""
        return self._jit_provisioning

    @jit_provisioning.setter
    def jit_provisioning(self, value):
        """Setter for jit_provisioning property."""
        self.logger.warn(
            "Setting values on jit_provisioning will NOT update the remote Canvas instance."
        )
        self._jit_provisioning = value

    @property
    def federated_attributes(self):
        """federated_attributes."""
        return self._federated_attributes

    @federated_attributes.setter
    def federated_attributes(self, value):
        """Setter for federated_attributes property."""
        self.logger.warn(
            "Setting values on federated_attributes will NOT update the remote Canvas instance."
        )
        self._federated_attributes = value

    @property
    def mfa_required(self):
        """If multi-factor authentication is required when logging in with this authentication provider. The account must not have MFA disabled."""
        return self._mfa_required

    @mfa_required.setter
    def mfa_required(self, value):
        """Setter for mfa_required property."""
        self.logger.warn(
            "Setting values on mfa_required will NOT update the remote Canvas instance."
        )
        self._mfa_required = value


class Ssosettings(BaseModel):
    """Ssosettings Model.
    Settings that are applicable across an account's authentication configuration, even if there are multiple individual providers"""

    def __init__(
        self,
        login_handle_name=None,
        change_password_url=None,
        auth_discovery_url=None,
        unknown_user_url=None,
    ):
        """Init method for Ssosettings class."""
        self._login_handle_name = login_handle_name
        self._change_password_url = change_password_url
        self._auth_discovery_url = auth_discovery_url
        self._unknown_user_url = unknown_user_url

        self.logger = logging.getLogger("py3canvas.Ssosettings")

    @property
    def login_handle_name(self):
        """The label used for unique login identifiers."""
        return self._login_handle_name

    @login_handle_name.setter
    def login_handle_name(self, value):
        """Setter for login_handle_name property."""
        self.logger.warn(
            "Setting values on login_handle_name will NOT update the remote Canvas instance."
        )
        self._login_handle_name = value

    @property
    def change_password_url(self):
        """The url to redirect users to for password resets. Leave blank for default Canvas behavior."""
        return self._change_password_url

    @change_password_url.setter
    def change_password_url(self, value):
        """Setter for change_password_url property."""
        self.logger.warn(
            "Setting values on change_password_url will NOT update the remote Canvas instance."
        )
        self._change_password_url = value

    @property
    def auth_discovery_url(self):
        """If a discovery url is set, canvas will forward all users to that URL when they need to be authenticated. That page will need to then help the user figure out where they need to go to log in. If no discovery url is configured, the first configuration will be used to attempt to authenticate the user."""
        return self._auth_discovery_url

    @auth_discovery_url.setter
    def auth_discovery_url(self, value):
        """Setter for auth_discovery_url property."""
        self.logger.warn(
            "Setting values on auth_discovery_url will NOT update the remote Canvas instance."
        )
        self._auth_discovery_url = value

    @property
    def unknown_user_url(self):
        """If an unknown user url is set, Canvas will forward to that url when a service authenticates a user, but that user does not exist in Canvas. The default behavior is to present an error."""
        return self._unknown_user_url

    @unknown_user_url.setter
    def unknown_user_url(self, value):
        """Setter for unknown_user_url property."""
        self.logger.warn(
            "Setting values on unknown_user_url will NOT update the remote Canvas instance."
        )
        self._unknown_user_url = value


class Federatedattributesconfig(BaseModel):
    """Federatedattributesconfig Model.
    A mapping of Canvas attribute names to attribute names that a provider may send, in order to update the value of these attributes when a user logs in. The values can be a FederatedAttributeConfig, or a raw string corresponding to the "attribute" property of a FederatedAttributeConfig. In responses, full FederatedAttributeConfig objects are returned if JIT provisioning is enabled, otherwise just the attribute names are returned."""

    def __init__(
        self,
        admin_roles=None,
        display_name=None,
        email=None,
        given_name=None,
        integration_id=None,
        locale=None,
        name=None,
        sis_user_id=None,
        sortable_name=None,
        surname=None,
        timezone=None,
    ):
        """Init method for Federatedattributesconfig class."""
        self._admin_roles = admin_roles
        self._display_name = display_name
        self._email = email
        self._given_name = given_name
        self._integration_id = integration_id
        self._locale = locale
        self._name = name
        self._sis_user_id = sis_user_id
        self._sortable_name = sortable_name
        self._surname = surname
        self._timezone = timezone

        self.logger = logging.getLogger("py3canvas.Federatedattributesconfig")

    @property
    def admin_roles(self):
        """A comma separated list of role names to grant to the user. Note that these only apply at the root account level, and not sub-accounts. If the attribute is not marked for provisioning only, the user will also be removed from any other roles they currently hold that are not still specified by the IdP."""
        return self._admin_roles

    @admin_roles.setter
    def admin_roles(self, value):
        """Setter for admin_roles property."""
        self.logger.warn(
            "Setting values on admin_roles will NOT update the remote Canvas instance."
        )
        self._admin_roles = value

    @property
    def display_name(self):
        """The full display name of the user."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn(
            "Setting values on display_name will NOT update the remote Canvas instance."
        )
        self._display_name = value

    @property
    def email(self):
        """The user's e-mail address."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email property."""
        self.logger.warn(
            "Setting values on email will NOT update the remote Canvas instance."
        )
        self._email = value

    @property
    def given_name(self):
        """The first, or given, name of the user."""
        return self._given_name

    @given_name.setter
    def given_name(self, value):
        """Setter for given_name property."""
        self.logger.warn(
            "Setting values on given_name will NOT update the remote Canvas instance."
        )
        self._given_name = value

    @property
    def integration_id(self):
        """The secondary unique identifier for SIS purposes."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn(
            "Setting values on integration_id will NOT update the remote Canvas instance."
        )
        self._integration_id = value

    @property
    def locale(self):
        """The user's preferred locale/language."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn(
            "Setting values on locale will NOT update the remote Canvas instance."
        )
        self._locale = value

    @property
    def name(self):
        """The full name of the user."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def sis_user_id(self):
        """The unique SIS identifier."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn(
            "Setting values on sis_user_id will NOT update the remote Canvas instance."
        )
        self._sis_user_id = value

    @property
    def sortable_name(self):
        """The full name of the user for sorting purposes."""
        return self._sortable_name

    @sortable_name.setter
    def sortable_name(self, value):
        """Setter for sortable_name property."""
        self.logger.warn(
            "Setting values on sortable_name will NOT update the remote Canvas instance."
        )
        self._sortable_name = value

    @property
    def surname(self):
        """The surname, or last name, of the user."""
        return self._surname

    @surname.setter
    def surname(self, value):
        """Setter for surname property."""
        self.logger.warn(
            "Setting values on surname will NOT update the remote Canvas instance."
        )
        self._surname = value

    @property
    def timezone(self):
        """The user's preferred time zone."""
        return self._timezone

    @timezone.setter
    def timezone(self, value):
        """Setter for timezone property."""
        self.logger.warn(
            "Setting values on timezone will NOT update the remote Canvas instance."
        )
        self._timezone = value


class Federatedattributeconfig(BaseModel):
    """Federatedattributeconfig Model.
    A single attribute name to be federated when a user logs in"""

    def __init__(self, attribute=None, provisioning_only=False):
        """Init method for Federatedattributeconfig class."""
        self._attribute = attribute
        self._provisioning_only = provisioning_only

        self.logger = logging.getLogger("py3canvas.Federatedattributeconfig")

    @property
    def attribute(self):
        """The name of the attribute as it will be sent from the authentication provider."""
        return self._attribute

    @attribute.setter
    def attribute(self, value):
        """Setter for attribute property."""
        self.logger.warn(
            "Setting values on attribute will NOT update the remote Canvas instance."
        )
        self._attribute = value

    @property
    def provisioning_only(self):
        """If the attribute should be applied only when provisioning a new user, rather than all logins."""
        return self._provisioning_only

    @provisioning_only.setter
    def provisioning_only(self, value):
        """Setter for provisioning_only property."""
        self.logger.warn(
            "Setting values on provisioning_only will NOT update the remote Canvas instance."
        )
        self._provisioning_only = value
