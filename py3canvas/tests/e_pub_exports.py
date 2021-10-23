"""EPubExports API Tests for Version 1.0.

This is a testing template for the generated EPubExportsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.e_pub_exports import EPubExportsAPI
from py3canvas.apis.e_pub_exports import Courseepubexport
from py3canvas.apis.e_pub_exports import Epubexport


class TestEPubExportsAPI(unittest.TestCase):
    """Tests for the EPubExportsAPI."""

    def setUp(self):
        self.client = EPubExportsAPI(secrets.instance_address, secrets.access_token)

    def test_list_courses_with_their_latest_epub_export(self):
        """Integration test for the EPubExportsAPI.list_courses_with_their_latest_epub_export method."""

        r = self.client.list_courses_with_their_latest_epub_export()

    def test_create_epub_export(self):
        """Integration test for the EPubExportsAPI.create_epub_export method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_epub_export(self):
        """Integration test for the EPubExportsAPI.show_epub_export method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_epub_export(course_id, id)
