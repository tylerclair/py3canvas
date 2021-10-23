"""Rubrics API Tests for Version 1.0.

This is a testing template for the generated RubricsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.rubrics import RubricsAPI
from py3canvas.apis.rubrics import Rubric
from py3canvas.apis.rubrics import Rubriccriterion
from py3canvas.apis.rubrics import Rubricrating
from py3canvas.apis.rubrics import Rubricassessment
from py3canvas.apis.rubrics import Rubricassociation


class TestRubricsAPI(unittest.TestCase):
    """Tests for the RubricsAPI."""

    def setUp(self):
        self.client = RubricsAPI(secrets.instance_address, secrets.access_token)

    def test_create_single_rubric(self):
        """Integration test for the RubricsAPI.create_single_rubric method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_rubric(self):
        """Integration test for the RubricsAPI.update_single_rubric method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_single_rubric(self):
        """Integration test for the RubricsAPI.delete_single_rubric method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_single_rubric(course_id, id)

    def test_list_rubrics_accounts(self):
        """Integration test for the RubricsAPI.list_rubrics_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_rubrics_accounts(account_id)

    def test_list_rubrics_courses(self):
        """Integration test for the RubricsAPI.list_rubrics_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_rubrics_courses(course_id)

    def test_get_single_rubric_accounts(self):
        """Integration test for the RubricsAPI.get_single_rubric_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_rubric_accounts(account_id, id, include=None, style=None)

    def test_get_single_rubric_courses(self):
        """Integration test for the RubricsAPI.get_single_rubric_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_rubric_courses(course_id, id, include=None, style=None)

    def test_create_single_rubric_assessment(self):
        """Integration test for the RubricsAPI.create_single_rubric_assessment method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_single_rubric_assessment(self):
        """Integration test for the RubricsAPI.update_single_rubric_assessment method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_single_rubric_assessment(self):
        """Integration test for the RubricsAPI.delete_single_rubric_assessment method."""
        course_id = None  # Change me!!
        rubric_association_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_single_rubric_assessment(course_id, id, rubric_association_id)

    def test_create_rubricassociation(self):
        """Integration test for the RubricsAPI.create_rubricassociation method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_rubricassociation(self):
        """Integration test for the RubricsAPI.update_rubricassociation method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_rubricassociation(self):
        """Integration test for the RubricsAPI.delete_rubricassociation method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_rubricassociation(course_id, id)

