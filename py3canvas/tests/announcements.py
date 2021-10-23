"""Announcements API Tests for Version 1.0.

This is a testing template for the generated AnnouncementsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.announcements import AnnouncementsAPI


class TestAnnouncementsAPI(unittest.TestCase):
    """Tests for the AnnouncementsAPI."""

    def setUp(self):
        self.client = AnnouncementsAPI(secrets.instance_address, secrets.access_token)

    def test_list_announcements(self):
        """Integration test for the AnnouncementsAPI.list_announcements method."""
        context_codes = None  # Change me!!

        r = self.client.list_announcements(
            context_codes,
            active_only=None,
            end_date=None,
            include=None,
            latest_only=None,
            start_date=None,
        )
