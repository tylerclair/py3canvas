"""QuizQuestions API Tests for Version 1.0.

This is a testing template for the generated QuizQuestionsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.quiz_questions import QuizQuestionsAPI
from py3canvas.apis.quiz_questions import Quizquestion
from py3canvas.apis.quiz_questions import Answer


class TestQuizQuestionsAPI(unittest.TestCase):
    """Tests for the QuizQuestionsAPI."""

    def setUp(self):
        self.client = QuizQuestionsAPI(secrets.instance_address, secrets.access_token)

    def test_list_questions_in_quiz_or_submission(self):
        """Integration test for the QuizQuestionsAPI.list_questions_in_quiz_or_submission method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.list_questions_in_quiz_or_submission(
            course_id, quiz_id, quiz_submission_attempt=None, quiz_submission_id=None
        )

    def test_get_single_quiz_question(self):
        """Integration test for the QuizQuestionsAPI.get_single_quiz_question method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_quiz_question(course_id, id, quiz_id)

    def test_create_single_quiz_question(self):
        """Integration test for the QuizQuestionsAPI.create_single_quiz_question method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_existing_quiz_question(self):
        """Integration test for the QuizQuestionsAPI.update_existing_quiz_question method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_quiz_question(self):
        """Integration test for the QuizQuestionsAPI.delete_quiz_question method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_quiz_question(course_id, id, quiz_id)
