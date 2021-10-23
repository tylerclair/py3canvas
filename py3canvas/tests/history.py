"""History API Tests for Version 1.0.

This is a testing template for the generated HistoryAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.history import HistoryAPI
from py3canvas.apis.history import Historyentry


class TestHistoryAPI(unittest.TestCase):
    """Tests for the HistoryAPI."""

    def setUp(self):
        self.client = HistoryAPI(secrets.instance_address, secrets.access_token)

    def test_list_recent_history_for_user(self):
        """Integration test for the HistoryAPI.list_recent_history_for_user method."""
        user_id = None  # Change me!!

        r = self.client.list_recent_history_for_user(user_id)

