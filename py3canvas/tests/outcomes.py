"""Outcomes API Tests for Version 1.0.

This is a testing template for the generated OutcomesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.outcomes import OutcomesAPI
from py3canvas.apis.outcomes import Outcome
from py3canvas.apis.outcomes import Outcomealignment


class TestOutcomesAPI(unittest.TestCase):
    """Tests for the OutcomesAPI."""

    def setUp(self):
        self.client = OutcomesAPI(secrets.instance_address, secrets.access_token)

    def test_show_outcome(self):
        """Integration test for the OutcomesAPI.show_outcome method."""
        id = None  # Change me!!

        r = self.client.show_outcome(id)

    def test_update_outcome(self):
        """Integration test for the OutcomesAPI.update_outcome method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_aligned_assignments_for_outcome_in_course_for_particular_student(self):
        """Integration test for the OutcomesAPI.get_aligned_assignments_for_outcome_in_course_for_particular_student method."""
        course_id = None  # Change me!!

        r = self.client.get_aligned_assignments_for_outcome_in_course_for_particular_student(
            course_id, student_id=None
        )
