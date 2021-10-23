"""PlagiarismDetectionPlatformUsers API Tests for Version 1.0.

This is a testing template for the generated PlagiarismDetectionPlatformUsersAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.plagiarism_detection_platform_users import (
    PlagiarismDetectionPlatformUsersAPI,
)


class TestPlagiarismDetectionPlatformUsersAPI(unittest.TestCase):
    """Tests for the PlagiarismDetectionPlatformUsersAPI."""

    def setUp(self):
        self.client = PlagiarismDetectionPlatformUsersAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_get_single_user_lti(self):
        """Integration test for the PlagiarismDetectionPlatformUsersAPI.get_single_user_lti method."""
        id = None  # Change me!!

        r = self.client.get_single_user_lti(id)

    def test_get_all_users_in_group_lti(self):
        """Integration test for the PlagiarismDetectionPlatformUsersAPI.get_all_users_in_group_lti method."""
        group_id = None  # Change me!!

        r = self.client.get_all_users_in_group_lti(group_id)
