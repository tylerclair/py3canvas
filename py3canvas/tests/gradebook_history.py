"""GradebookHistory API Tests for Version 1.0.

This is a testing template for the generated GradebookHistoryAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.gradebook_history import GradebookHistoryAPI
from py3canvas.apis.gradebook_history import Grader
from py3canvas.apis.gradebook_history import Day
from py3canvas.apis.gradebook_history import Submissionversion
from py3canvas.apis.gradebook_history import Submissionhistory


class TestGradebookHistoryAPI(unittest.TestCase):
    """Tests for the GradebookHistoryAPI."""

    def setUp(self):
        self.client = GradebookHistoryAPI(secrets.instance_address, secrets.access_token)

    def test_days_in_gradebook_history_for_this_course(self):
        """Integration test for the GradebookHistoryAPI.days_in_gradebook_history_for_this_course method."""
        course_id = None  # Change me!!

        r = self.client.days_in_gradebook_history_for_this_course(course_id)

    def test_details_for_given_date_in_gradebook_history_for_this_course(self):
        """Integration test for the GradebookHistoryAPI.details_for_given_date_in_gradebook_history_for_this_course method."""
        course_id = None  # Change me!!
        date = None  # Change me!!

        r = self.client.details_for_given_date_in_gradebook_history_for_this_course(course_id, date)

    def test_lists_submissions(self):
        """Integration test for the GradebookHistoryAPI.lists_submissions method."""
        course_id = None  # Change me!!
        date = None  # Change me!!
        grader_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.lists_submissions(assignment_id, course_id, date, grader_id)

    def test_list_uncollated_submission_versions(self):
        """Integration test for the GradebookHistoryAPI.list_uncollated_submission_versions method."""
        course_id = None  # Change me!!

        r = self.client.list_uncollated_submission_versions(course_id, ascending=None, assignment_id=None, user_id=None)

