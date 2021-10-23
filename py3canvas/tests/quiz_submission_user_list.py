"""QuizSubmissionUserList API Tests for Version 1.0.

This is a testing template for the generated QuizSubmissionUserListAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.quiz_submission_user_list import QuizSubmissionUserListAPI
from py3canvas.apis.quiz_submission_user_list import Quizsubmissionuserlist
from py3canvas.apis.quiz_submission_user_list import Quizsubmissionuserlistmeta
from py3canvas.apis.quiz_submission_user_list import Jsonapipagination


class TestQuizSubmissionUserListAPI(unittest.TestCase):
    """Tests for the QuizSubmissionUserListAPI."""

    def setUp(self):
        self.client = QuizSubmissionUserListAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_send_message_to_unsubmitted_or_submitted_users_for_quiz(self):
        """Integration test for the QuizSubmissionUserListAPI.send_message_to_unsubmitted_or_submitted_users_for_quiz method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
