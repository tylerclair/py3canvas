"""ImageSearch API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class ImageSearchAPI(BaseCanvasAPI):
    """ImageSearch API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ImageSearchAPI."""
        super(ImageSearchAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ImageSearchAPI")

    def find_images(self, query):
        """
        Find images.

        Find public domain images for use in courses and user content.  If you select an image using this API, please use the {api:InternetImageController#image_selection Confirm image selection API} to indicate photo usage to the server.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - query
        """
            Search terms used for matching images (e.g. "cats").
        """
        params["query"] = query


        self.logger.debug("GET /api/v1/image_search with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/image_search".format(**path), data=data, params=params, no_data=True)

    def confirm_image_selection(self, id):
        """
        Confirm image selection.

        After you have used the search API, you should hit this API to indicate photo usage to the server.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            The ID from the image_search result.
        """
        path["id"] = id


        self.logger.debug("POST /api/v1/image_selection/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/image_selection/{id}".format(**path), data=data, params=params, no_data=True)

