"""SisIntegration API Tests for Version 1.0.

This is a testing template for the generated SisIntegrationAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.sis_integration import SisIntegrationAPI
from py3canvas.apis.sis_integration import Sisassignment
from py3canvas.apis.sis_integration import Assignmentgroupattributes
from py3canvas.apis.sis_integration import Sectionattributes
from py3canvas.apis.sis_integration import Courseattributes
from py3canvas.apis.sis_integration import Sectionassignmentoverrideattributes
from py3canvas.apis.sis_integration import Userassignmentoverrideattributes
from py3canvas.apis.sis_integration import Studentattributes


class TestSisIntegrationAPI(unittest.TestCase):
    """Tests for the SisIntegrationAPI."""

    def setUp(self):
        self.client = SisIntegrationAPI(secrets.instance_address, secrets.access_token)

    def test_retrieve_assignments_enabled_for_grade_export_to_sis_accounts(self):
        """Integration test for the SisIntegrationAPI.retrieve_assignments_enabled_for_grade_export_to_sis_accounts method."""
        account_id = None  # Change me!!

        r = self.client.retrieve_assignments_enabled_for_grade_export_to_sis_accounts(account_id, course_id=None, ends_after=None, include=None, starts_before=None)

    def test_retrieve_assignments_enabled_for_grade_export_to_sis_courses(self):
        """Integration test for the SisIntegrationAPI.retrieve_assignments_enabled_for_grade_export_to_sis_courses method."""
        course_id = None  # Change me!!

        r = self.client.retrieve_assignments_enabled_for_grade_export_to_sis_courses(course_id, account_id=None, ends_after=None, include=None, starts_before=None)

    def test_disable_assignments_currently_enabled_for_grade_export_to_sis(self):
        """Integration test for the SisIntegrationAPI.disable_assignments_currently_enabled_for_grade_export_to_sis method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

