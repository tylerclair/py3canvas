"""InstAccessTokens API Tests for Version 1.0.

This is a testing template for the generated InstAccessTokensAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.inst_access_tokens import InstAccessTokensAPI
from py3canvas.apis.inst_access_tokens import Instaccesstoken


class TestInstAccessTokensAPI(unittest.TestCase):
    """Tests for the InstAccessTokensAPI."""

    def setUp(self):
        self.client = InstAccessTokensAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_create_instaccess_token(self):
        """Integration test for the InstAccessTokensAPI.create_instaccess_token method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
