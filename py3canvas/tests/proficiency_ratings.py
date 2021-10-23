"""ProficiencyRatings API Tests for Version 1.0.

This is a testing template for the generated ProficiencyRatingsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.proficiency_ratings import ProficiencyRatingsAPI
from py3canvas.apis.proficiency_ratings import Proficiencyrating
from py3canvas.apis.proficiency_ratings import Proficiency


class TestProficiencyRatingsAPI(unittest.TestCase):
    """Tests for the ProficiencyRatingsAPI."""

    def setUp(self):
        self.client = ProficiencyRatingsAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_create_update_proficiency_ratings_accounts(self):
        """Integration test for the ProficiencyRatingsAPI.create_update_proficiency_ratings_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_update_proficiency_ratings_courses(self):
        """Integration test for the ProficiencyRatingsAPI.create_update_proficiency_ratings_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_proficiency_ratings_accounts(self):
        """Integration test for the ProficiencyRatingsAPI.get_proficiency_ratings_accounts method."""
        account_id = None  # Change me!!

        r = self.client.get_proficiency_ratings_accounts(account_id)

    def test_get_proficiency_ratings_courses(self):
        """Integration test for the ProficiencyRatingsAPI.get_proficiency_ratings_courses method."""
        course_id = None  # Change me!!

        r = self.client.get_proficiency_ratings_courses(course_id)
