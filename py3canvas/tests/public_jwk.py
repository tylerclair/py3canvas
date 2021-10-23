"""PublicJwk API Tests for Version 1.0.

This is a testing template for the generated PublicJwkAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.public_jwk import PublicJwkAPI
from py3canvas.apis.public_jwk import Developerkey


class TestPublicJwkAPI(unittest.TestCase):
    """Tests for the PublicJwkAPI."""

    def setUp(self):
        self.client = PublicJwkAPI(secrets.instance_address, secrets.access_token)

    def test_update_public_jwk(self):
        """Integration test for the PublicJwkAPI.update_public_jwk method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass
