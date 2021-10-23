"""Bookmarks API Tests for Version 1.0.

This is a testing template for the generated BookmarksAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.bookmarks import BookmarksAPI
from py3canvas.apis.bookmarks import Bookmark


class TestBookmarksAPI(unittest.TestCase):
    """Tests for the BookmarksAPI."""

    def setUp(self):
        self.client = BookmarksAPI(secrets.instance_address, secrets.access_token)

    def test_list_bookmarks(self):
        """Integration test for the BookmarksAPI.list_bookmarks method."""

        r = self.client.list_bookmarks()

    def test_create_bookmark(self):
        """Integration test for the BookmarksAPI.create_bookmark method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_bookmark(self):
        """Integration test for the BookmarksAPI.get_bookmark method."""
        id = None  # Change me!!

        r = self.client.get_bookmark(id)

    def test_update_bookmark(self):
        """Integration test for the BookmarksAPI.update_bookmark method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_bookmark(self):
        """Integration test for the BookmarksAPI.delete_bookmark method."""
        id = None  # Change me!!

        r = self.client.delete_bookmark(id)

