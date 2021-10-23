"""LatePolicy API Tests for Version 1.0.

This is a testing template for the generated LatePolicyAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.late_policy import LatePolicyAPI
from py3canvas.apis.late_policy import Latepolicy


class TestLatePolicyAPI(unittest.TestCase):
    """Tests for the LatePolicyAPI."""

    def setUp(self):
        self.client = LatePolicyAPI(secrets.instance_address, secrets.access_token)

    def test_get_late_policy(self):
        """Integration test for the LatePolicyAPI.get_late_policy method."""
        id = None  # Change me!!

        r = self.client.get_late_policy(id)

    def test_create_late_policy(self):
        """Integration test for the LatePolicyAPI.create_late_policy method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_patch_late_policy(self):
        """Integration test for the LatePolicyAPI.patch_late_policy method."""
        id = None  # Change me!!

        r = self.client.patch_late_policy(id, late_policy_late_submission_deduction=None, late_policy_late_submission_deduction_enabled=None, late_policy_late_submission_interval=None, late_policy_late_submission_minimum_percent=None, late_policy_late_submission_minimum_percent_enabled=None, late_policy_missing_submission_deduction=None, late_policy_missing_submission_deduction_enabled=None)

