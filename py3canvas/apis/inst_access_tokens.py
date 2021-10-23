"""InstAccessTokens API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class InstAccessTokensAPI(BaseCanvasAPI):
    """InstAccessTokens API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for InstAccessTokensAPI."""
        super(InstAccessTokensAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.InstAccessTokensAPI")

    def create_instaccess_token(self):
        """
        Create InstAccess token.

        Create a unique, encrypted InstAccess token.

        Generates a different InstAccess token each time it's called, each one expires
        after a short window (1 hour).
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "POST /api/v1/inst_access_tokens with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/inst_access_tokens".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Instaccesstoken(BaseModel):
    """Instaccesstoken Model."""

    def __init__(self, token=None):
        """Init method for Instaccesstoken class."""
        self._token = token

        self.logger = logging.getLogger("py3canvas.Instaccesstoken")

    @property
    def token(self):
        """The InstAccess token itself -- a signed, encrypted JWT."""
        return self._token

    @token.setter
    def token(self, value):
        """Setter for token property."""
        self.logger.warn(
            "Setting values on token will NOT update the remote Canvas instance."
        )
        self._token = value
