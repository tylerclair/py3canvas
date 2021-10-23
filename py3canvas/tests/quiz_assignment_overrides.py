"""QuizAssignmentOverrides API Tests for Version 1.0.

This is a testing template for the generated QuizAssignmentOverridesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.quiz_assignment_overrides import QuizAssignmentOverridesAPI
from py3canvas.apis.quiz_assignment_overrides import Quizassignmentoverrideset
from py3canvas.apis.quiz_assignment_overrides import Quizassignmentoverridesetcontainer
from py3canvas.apis.quiz_assignment_overrides import Quizassignmentoverride


class TestQuizAssignmentOverridesAPI(unittest.TestCase):
    """Tests for the QuizAssignmentOverridesAPI."""

    def setUp(self):
        self.client = QuizAssignmentOverridesAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_retrieve_assignment_overridden_dates_for_classic_quizzes(self):
        """Integration test for the QuizAssignmentOverridesAPI.retrieve_assignment_overridden_dates_for_classic_quizzes method."""
        course_id = None  # Change me!!

        r = self.client.retrieve_assignment_overridden_dates_for_classic_quizzes(
            course_id, quiz_assignment_overrides_0_quiz_ids=None
        )

    def test_retrieve_assignment_overridden_dates_for_new_quizzes(self):
        """Integration test for the QuizAssignmentOverridesAPI.retrieve_assignment_overridden_dates_for_new_quizzes method."""
        course_id = None  # Change me!!

        r = self.client.retrieve_assignment_overridden_dates_for_new_quizzes(
            course_id, quiz_assignment_overrides_0_quiz_ids=None
        )
