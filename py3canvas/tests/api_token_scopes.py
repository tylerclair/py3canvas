"""ApiTokenScopes API Tests for Version 1.0.

This is a testing template for the generated ApiTokenScopesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.api_token_scopes import ApiTokenScopesAPI
from py3canvas.apis.api_token_scopes import Scope


class TestApiTokenScopesAPI(unittest.TestCase):
    """Tests for the ApiTokenScopesAPI."""

    def setUp(self):
        self.client = ApiTokenScopesAPI(secrets.instance_address, secrets.access_token)

    def test_list_scopes(self):
        """Integration test for the ApiTokenScopesAPI.list_scopes method."""
        account_id = None  # Change me!!

        r = self.client.list_scopes(account_id, group_by=None)
