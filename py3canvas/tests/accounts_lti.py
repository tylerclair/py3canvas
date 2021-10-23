"""Accounts(lti) API Tests for Version 1.0.

This is a testing template for the generated Accounts(lti)API Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.accounts_lti import AccountsLtiAPI
from py3canvas.apis.accounts_lti import Account


class TestAccountsLtiAPI(unittest.TestCase):
    """Tests for the Accounts(lti)API."""

    def setUp(self):
        self.client = AccountsLtiAPI(secrets.instance_address, secrets.access_token)

    def test_get_account(self):
        """Integration test for the Accounts(lti)API.get_account method."""
        account_id = None  # Change me!!

        r = self.client.get_account(account_id)
