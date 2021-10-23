"""SubmissionComments API Tests for Version 1.0.

This is a testing template for the generated SubmissionCommentsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.submission_comments import SubmissionCommentsAPI


class TestSubmissionCommentsAPI(unittest.TestCase):
    """Tests for the SubmissionCommentsAPI."""

    def setUp(self):
        self.client = SubmissionCommentsAPI(secrets.instance_address, secrets.access_token)

    def test_edit_submission_comment(self):
        """Integration test for the SubmissionCommentsAPI.edit_submission_comment method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_submission_comment(self):
        """Integration test for the SubmissionCommentsAPI.delete_submission_comment method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_submission_comment(assignment_id, course_id, id, user_id)

    def test_upload_file(self):
        """Integration test for the SubmissionCommentsAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

