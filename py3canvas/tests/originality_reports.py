"""OriginalityReports API Tests for Version 1.0.

This is a testing template for the generated OriginalityReportsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.originality_reports import OriginalityReportsAPI
from py3canvas.apis.originality_reports import Toolsetting
from py3canvas.apis.originality_reports import Originalityreport


class TestOriginalityReportsAPI(unittest.TestCase):
    """Tests for the OriginalityReportsAPI."""

    def setUp(self):
        self.client = OriginalityReportsAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_create_originality_report(self):
        """Integration test for the OriginalityReportsAPI.create_originality_report method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_originality_report_submissions(self):
        """Integration test for the OriginalityReportsAPI.edit_originality_report_submissions method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_originality_report_files(self):
        """Integration test for the OriginalityReportsAPI.edit_originality_report_files method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_originality_report_submissions(self):
        """Integration test for the OriginalityReportsAPI.show_originality_report_submissions method."""
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_originality_report_submissions(
            assignment_id, id, submission_id
        )

    def test_show_originality_report_files(self):
        """Integration test for the OriginalityReportsAPI.show_originality_report_files method."""
        assignment_id = None  # Change me!!
        file_id = None  # Change me!!

        r = self.client.show_originality_report_files(assignment_id, file_id)
