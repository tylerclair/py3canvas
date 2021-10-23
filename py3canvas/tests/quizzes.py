"""Quizzes API Tests for Version 1.0.

This is a testing template for the generated QuizzesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.quizzes import QuizzesAPI
from py3canvas.apis.quizzes import Quiz
from py3canvas.apis.quizzes import Quizpermissions


class TestQuizzesAPI(unittest.TestCase):
    """Tests for the QuizzesAPI."""

    def setUp(self):
        self.client = QuizzesAPI(secrets.instance_address, secrets.access_token)

    def test_list_quizzes_in_course(self):
        """Integration test for the QuizzesAPI.list_quizzes_in_course method."""
        course_id = None  # Change me!!

        r = self.client.list_quizzes_in_course(course_id, search_term=None)

    def test_get_single_quiz(self):
        """Integration test for the QuizzesAPI.get_single_quiz method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_quiz(course_id, id)

    def test_create_quiz(self):
        """Integration test for the QuizzesAPI.create_quiz method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_quiz(self):
        """Integration test for the QuizzesAPI.edit_quiz method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_quiz(self):
        """Integration test for the QuizzesAPI.delete_quiz method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_quiz(course_id, id)

    def test_reorder_quiz_items(self):
        """Integration test for the QuizzesAPI.reorder_quiz_items method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_validate_quiz_access_code(self):
        """Integration test for the QuizzesAPI.validate_quiz_access_code method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
