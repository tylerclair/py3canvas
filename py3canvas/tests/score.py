"""Score API Tests for Version 1.0.

This is a testing template for the generated ScoreAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.score import ScoreAPI
from py3canvas.apis.score import Score


class TestScoreAPI(unittest.TestCase):
    """Tests for the ScoreAPI."""

    def setUp(self):
        self.client = ScoreAPI(secrets.instance_address, secrets.access_token)

    def test_create_score(self):
        """Integration test for the ScoreAPI.create_score method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
