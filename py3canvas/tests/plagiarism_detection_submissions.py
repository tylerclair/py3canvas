"""PlagiarismDetectionSubmissions API Tests for Version 1.0.

This is a testing template for the generated PlagiarismDetectionSubmissionsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.plagiarism_detection_submissions import (
    PlagiarismDetectionSubmissionsAPI,
)
from py3canvas.apis.plagiarism_detection_submissions import Submission
from py3canvas.apis.plagiarism_detection_submissions import File


class TestPlagiarismDetectionSubmissionsAPI(unittest.TestCase):
    """Tests for the PlagiarismDetectionSubmissionsAPI."""

    def setUp(self):
        self.client = PlagiarismDetectionSubmissionsAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_get_single_submission(self):
        """Integration test for the PlagiarismDetectionSubmissionsAPI.get_single_submission method."""
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!

        r = self.client.get_single_submission(assignment_id, submission_id)

    def test_get_history_of_single_submission(self):
        """Integration test for the PlagiarismDetectionSubmissionsAPI.get_history_of_single_submission method."""
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!

        r = self.client.get_history_of_single_submission(assignment_id, submission_id)
