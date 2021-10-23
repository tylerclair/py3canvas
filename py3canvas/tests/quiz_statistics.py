"""QuizStatistics API Tests for Version 1.0.

This is a testing template for the generated QuizStatisticsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.quiz_statistics import QuizStatisticsAPI
from py3canvas.apis.quiz_statistics import Quizstatistics
from py3canvas.apis.quiz_statistics import Quizstatisticslinks
from py3canvas.apis.quiz_statistics import Quizstatisticsquestionstatistics
from py3canvas.apis.quiz_statistics import Quizstatisticsanswerstatistics
from py3canvas.apis.quiz_statistics import Quizstatisticsanswerpointbiserial
from py3canvas.apis.quiz_statistics import Quizstatisticssubmissionstatistics


class TestQuizStatisticsAPI(unittest.TestCase):
    """Tests for the QuizStatisticsAPI."""

    def setUp(self):
        self.client = QuizStatisticsAPI(secrets.instance_address, secrets.access_token)

    def test_fetching_latest_quiz_statistics(self):
        """Integration test for the QuizStatisticsAPI.fetching_latest_quiz_statistics method."""
        course_id = None  # Change me!!
        quiz_id = None  # Change me!!

        r = self.client.fetching_latest_quiz_statistics(
            course_id, quiz_id, all_versions=None
        )
