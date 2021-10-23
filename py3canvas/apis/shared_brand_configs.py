"""SharedBrandConfigs API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class SharedBrandConfigsAPI(BaseCanvasAPI):
    """SharedBrandConfigs API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SharedBrandConfigsAPI."""
        super(SharedBrandConfigsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SharedBrandConfigsAPI")

    def share_brandconfig_theme(
        self, account_id, shared_brand_config_brand_config_md5, shared_brand_config_name
    ):
        """
        Share a BrandConfig (Theme).

        Create a SharedBrandConfig, which will give the given brand_config a name
        and make it available to other users of this account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - shared_brand_config[name]
        """
            Name to share this BrandConfig (theme) as.
        """
        data["shared_brand_config[name]"] = shared_brand_config_name

        # REQUIRED - shared_brand_config[brand_config_md5]
        """
            MD5 of brand_config to share
        """
        data[
            "shared_brand_config[brand_config_md5]"
        ] = shared_brand_config_brand_config_md5

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/shared_brand_configs with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/shared_brand_configs".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_shared_theme(self, account_id, id):
        """
        Update a shared theme.

        Update the specified shared_brand_config with a new name or to point to a new brand_config.
        Uses same parameters as create.
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
            "PUT /api/v1/accounts/{account_id}/shared_brand_configs/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/shared_brand_configs/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def un_share_brandconfig_theme(self, id):
        """
        Un-share a BrandConfig (Theme).

        Delete a SharedBrandConfig, which will unshare it so you nor anyone else in
        your account will see it as an option to pick from.
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
            "DELETE /api/v1/shared_brand_configs/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/shared_brand_configs/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Sharedbrandconfig(BaseModel):
    """Sharedbrandconfig Model."""

    def __init__(
        self,
        id=None,
        account_id=None,
        brand_config_md5=None,
        name=None,
        created_at=None,
        updated_at=None,
    ):
        """Init method for Sharedbrandconfig class."""
        self._id = id
        self._account_id = account_id
        self._brand_config_md5 = brand_config_md5
        self._name = name
        self._created_at = created_at
        self._updated_at = updated_at

        self.logger = logging.getLogger("py3canvas.Sharedbrandconfig")

    @property
    def id(self):
        """The shared_brand_config identifier."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def account_id(self):
        """The id of the account it should be shared within."""
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        """Setter for account_id property."""
        self.logger.warn(
            "Setting values on account_id will NOT update the remote Canvas instance."
        )
        self._account_id = value

    @property
    def brand_config_md5(self):
        """The md5 (since BrandConfigs are identified by MD5 and not numeric id) of the BrandConfig to share."""
        return self._brand_config_md5

    @brand_config_md5.setter
    def brand_config_md5(self, value):
        """Setter for brand_config_md5 property."""
        self.logger.warn(
            "Setting values on brand_config_md5 will NOT update the remote Canvas instance."
        )
        self._brand_config_md5 = value

    @property
    def name(self):
        """The name to share this theme as."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def created_at(self):
        """When this was created."""
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
        """When this was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value
