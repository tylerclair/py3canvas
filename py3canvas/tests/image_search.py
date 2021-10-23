"""ImageSearch API Tests for Version 1.0.

This is a testing template for the generated ImageSearchAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.image_search import ImageSearchAPI


class TestImageSearchAPI(unittest.TestCase):
    """Tests for the ImageSearchAPI."""

    def setUp(self):
        self.client = ImageSearchAPI(secrets.instance_address, secrets.access_token)

    def test_find_images(self):
        """Integration test for the ImageSearchAPI.find_images method."""
        query = None  # Change me!!

        r = self.client.find_images(query)

    def test_confirm_image_selection(self):
        """Integration test for the ImageSearchAPI.confirm_image_selection method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
