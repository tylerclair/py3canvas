"""Result API Tests for Version 1.0.

This is a testing template for the generated ResultAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.result import ResultAPI
from py3canvas.apis.result import Result


class TestResultAPI(unittest.TestCase):
    """Tests for the ResultAPI."""

    def setUp(self):
        self.client = ResultAPI(secrets.instance_address, secrets.access_token)

    def test_show_collection_of_results(self):
        """Integration test for the ResultAPI.show_collection_of_results method."""
        course_id = None  # Change me!!
        line_item_id = None  # Change me!!

        r = self.client.show_collection_of_results(course_id, line_item_id)

    def test_show_result(self):
        """Integration test for the ResultAPI.show_result method."""
        course_id = None  # Change me!!
        line_item_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_result(course_id, id, line_item_id)

