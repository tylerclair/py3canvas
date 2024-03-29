"""EnrollmentTerms API Tests for Version 1.0.

This is a testing template for the generated EnrollmentTermsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.enrollment_terms import EnrollmentTermsAPI
from py3canvas.apis.enrollment_terms import Enrollmentterm
from py3canvas.apis.enrollment_terms import Enrollmenttermslist


class TestEnrollmentTermsAPI(unittest.TestCase):
    """Tests for the EnrollmentTermsAPI."""

    def setUp(self):
        self.client = EnrollmentTermsAPI(secrets.instance_address, secrets.access_token)

    def test_create_enrollment_term(self):
        """Integration test for the EnrollmentTermsAPI.create_enrollment_term method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_enrollment_term(self):
        """Integration test for the EnrollmentTermsAPI.update_enrollment_term method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_enrollment_term(self):
        """Integration test for the EnrollmentTermsAPI.delete_enrollment_term method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_enrollment_term(account_id, id)

    def test_list_enrollment_terms(self):
        """Integration test for the EnrollmentTermsAPI.list_enrollment_terms method."""
        account_id = None  # Change me!!

        r = self.client.list_enrollment_terms(
            account_id, include=None, workflow_state=None
        )

    def test_retrieve_enrollment_term(self):
        """Integration test for the EnrollmentTermsAPI.retrieve_enrollment_term method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.retrieve_enrollment_term(account_id, id)
