"""AssignmentExtensions API Tests for Version 1.0.

This is a testing template for the generated AssignmentExtensionsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.assignment_extensions import AssignmentExtensionsAPI
from py3canvas.apis.assignment_extensions import Assignmentextension


class TestAssignmentExtensionsAPI(unittest.TestCase):
    """Tests for the AssignmentExtensionsAPI."""

    def setUp(self):
        self.client = AssignmentExtensionsAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_set_extensions_for_student_assignment_submissions(self):
        """Integration test for the AssignmentExtensionsAPI.set_extensions_for_student_assignment_submissions method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
