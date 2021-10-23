"""OutcomeImports API Tests for Version 1.0.

This is a testing template for the generated OutcomeImportsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.outcome_imports import OutcomeImportsAPI
from py3canvas.apis.outcome_imports import Outcomeimportdata
from py3canvas.apis.outcome_imports import Outcomeimport


class TestOutcomeImportsAPI(unittest.TestCase):
    """Tests for the OutcomeImportsAPI."""

    def setUp(self):
        self.client = OutcomeImportsAPI(secrets.instance_address, secrets.access_token)

    def test_import_outcomes_accounts(self):
        """Integration test for the OutcomeImportsAPI.import_outcomes_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_import_outcomes_courses(self):
        """Integration test for the OutcomeImportsAPI.import_outcomes_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_outcome_import_status_accounts(self):
        """Integration test for the OutcomeImportsAPI.get_outcome_import_status_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_outcome_import_status_accounts(account_id, id)

    def test_get_outcome_import_status_courses(self):
        """Integration test for the OutcomeImportsAPI.get_outcome_import_status_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_outcome_import_status_courses(course_id, id)

