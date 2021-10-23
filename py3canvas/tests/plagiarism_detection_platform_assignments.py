"""PlagiarismDetectionPlatformAssignments API Tests for Version 1.0.

This is a testing template for the generated PlagiarismDetectionPlatformAssignmentsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.plagiarism_detection_platform_assignments import (
    PlagiarismDetectionPlatformAssignmentsAPI,
)
from py3canvas.apis.plagiarism_detection_platform_assignments import Ltiassignment


class TestPlagiarismDetectionPlatformAssignmentsAPI(unittest.TestCase):
    """Tests for the PlagiarismDetectionPlatformAssignmentsAPI."""

    def setUp(self):
        self.client = PlagiarismDetectionPlatformAssignmentsAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_get_single_assignment_lti(self):
        """Integration test for the PlagiarismDetectionPlatformAssignmentsAPI.get_single_assignment_lti method."""
        assignment_id = None  # Change me!!

        r = self.client.get_single_assignment_lti(assignment_id, user_id=None)
