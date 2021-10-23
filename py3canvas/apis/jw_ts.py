"""JwTs API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class JwTsAPI(BaseCanvasAPI):
    """JwTs API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for JwTsAPI."""
        super(JwTsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.JwTsAPI")

    def create_jwt(self, workflows=None):
        """
        Create JWT.

        Create a unique jwt for using with other canvas services

        Generates a different JWT each time it's called, each one expires
        after a short window (1 hour)
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - workflows
        """
            Adds additional data to the JWT to be used by the consuming service workflow
        """
        if workflows is not None:
            data["workflows"] = workflows

        self.logger.debug(
            "POST /api/v1/jwts with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/jwts".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def refresh_jwt(self, jwt):
        """
        Refresh JWT.

        Refresh a JWT for use with other canvas services

        Generates a different JWT each time it's called, each one expires
        after a short window (1 hour).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - jwt
        """
            An existing JWT token to be refreshed. The new token will have
        the same context and workflows as the existing token.
        """
        data["jwt"] = jwt

        self.logger.debug(
            "POST /api/v1/jwts/refresh with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/jwts/refresh".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Jwt(BaseModel):
    """Jwt Model."""

    def __init__(self, token=None):
        """Init method for Jwt class."""
        self._token = token

        self.logger = logging.getLogger("py3canvas.Jwt")

    @property
    def token(self):
        """The signed, encrypted, base64 encoded JWT."""
        return self._token

    @token.setter
    def token(self, value):
        """Setter for token property."""
        self.logger.warn(
            "Setting values on token will NOT update the remote Canvas instance."
        )
        self._token = value
