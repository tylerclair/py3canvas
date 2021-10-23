"""Progress API Tests for Version 1.0.

This is a testing template for the generated ProgressAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.progress import ProgressAPI
from py3canvas.apis.progress import Progress


class TestProgressAPI(unittest.TestCase):
    """Tests for the ProgressAPI."""

    def setUp(self):
        self.client = ProgressAPI(secrets.instance_address, secrets.access_token)

    def test_query_progress(self):
        """Integration test for the ProgressAPI.query_progress method."""
        id = None  # Change me!!

        r = self.client.query_progress(id)

    def test_query_progress(self):
        """Integration test for the ProgressAPI.query_progress method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.query_progress(course_id, id)
