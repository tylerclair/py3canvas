"""ErrorReports API Tests for Version 1.0.

This is a testing template for the generated ErrorReportsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.error_reports import ErrorReportsAPI
from py3canvas.apis.error_reports import Errorreport


class TestErrorReportsAPI(unittest.TestCase):
    """Tests for the ErrorReportsAPI."""

    def setUp(self):
        self.client = ErrorReportsAPI(secrets.instance_address, secrets.access_token)

    def test_create_error_report(self):
        """Integration test for the ErrorReportsAPI.create_error_report method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
