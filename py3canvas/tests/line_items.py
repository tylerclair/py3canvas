"""LineItems API Tests for Version 1.0.

This is a testing template for the generated LineItemsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.line_items import LineItemsAPI
from py3canvas.apis.line_items import Lineitem


class TestLineItemsAPI(unittest.TestCase):
    """Tests for the LineItemsAPI."""

    def setUp(self):
        self.client = LineItemsAPI(secrets.instance_address, secrets.access_token)

    def test_create_line_item(self):
        """Integration test for the LineItemsAPI.create_line_item method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_line_item(self):
        """Integration test for the LineItemsAPI.update_line_item method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_line_item(self):
        """Integration test for the LineItemsAPI.show_line_item method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_line_item(course_id, id)

    def test_list_line_items(self):
        """Integration test for the LineItemsAPI.list_line_items method."""
        course_id = None  # Change me!!

        r = self.client.list_line_items(course_id, limit=None, resource_id=None, resource_link_id=None, tag=None)

    def test_delete_line_item(self):
        """Integration test for the LineItemsAPI.delete_line_item method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_line_item(course_id, id)

