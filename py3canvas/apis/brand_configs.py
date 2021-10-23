"""BrandConfigs API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI


class BrandConfigsAPI(BaseCanvasAPI):
    """BrandConfigs API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for BrandConfigsAPI."""
        super(BrandConfigsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.BrandConfigsAPI")

    def get_brand_config_variables_that_should_be_used_for_this_domain(self):
        """
        Get the brand config variables that should be used for this domain.

        Will redirect to a static json file that has all of the brand
        variables used by this account. Even though this is a redirect,
        do not store the redirected url since if the account makes any changes
        it will redirect to a new url. Needs no authentication.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/brand_variables with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/brand_variables".format(**path),
            data=data,
            params=params,
            no_data=True,
        )
