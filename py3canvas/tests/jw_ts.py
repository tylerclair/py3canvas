"""JwTs API Tests for Version 1.0.

This is a testing template for the generated JwTsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.jw_ts import JwTsAPI
from py3canvas.apis.jw_ts import Jwt


class TestJwTsAPI(unittest.TestCase):
    """Tests for the JwTsAPI."""

    def setUp(self):
        self.client = JwTsAPI(secrets.instance_address, secrets.access_token)

    def test_create_jwt(self):
        """Integration test for the JwTsAPI.create_jwt method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_refresh_jwt(self):
        """Integration test for the JwTsAPI.refresh_jwt method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
