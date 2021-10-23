"""Analytics API Tests for Version 1.0.

This is a testing template for the generated AnalyticsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.analytics import AnalyticsAPI


class TestAnalyticsAPI(unittest.TestCase):
    """Tests for the AnalyticsAPI."""

    def setUp(self):
        self.client = AnalyticsAPI(secrets.instance_address, secrets.access_token)

    def test_get_department_level_participation_data_terms(self):
        """Integration test for the AnalyticsAPI.get_department_level_participation_data_terms method."""
        account_id = None  # Change me!!
        term_id = None  # Change me!!

        r = self.client.get_department_level_participation_data_terms(
            account_id, term_id
        )

    def test_get_department_level_participation_data_current(self):
        """Integration test for the AnalyticsAPI.get_department_level_participation_data_current method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_participation_data_current(account_id)

    def test_get_department_level_participation_data_completed(self):
        """Integration test for the AnalyticsAPI.get_department_level_participation_data_completed method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_participation_data_completed(account_id)

    def test_get_department_level_grade_data_terms(self):
        """Integration test for the AnalyticsAPI.get_department_level_grade_data_terms method."""
        account_id = None  # Change me!!
        term_id = None  # Change me!!

        r = self.client.get_department_level_grade_data_terms(account_id, term_id)

    def test_get_department_level_grade_data_current(self):
        """Integration test for the AnalyticsAPI.get_department_level_grade_data_current method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_grade_data_current(account_id)

    def test_get_department_level_grade_data_completed(self):
        """Integration test for the AnalyticsAPI.get_department_level_grade_data_completed method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_grade_data_completed(account_id)

    def test_get_department_level_statistics_terms(self):
        """Integration test for the AnalyticsAPI.get_department_level_statistics_terms method."""
        account_id = None  # Change me!!
        term_id = None  # Change me!!

        r = self.client.get_department_level_statistics_terms(account_id, term_id)

    def test_get_department_level_statistics_current(self):
        """Integration test for the AnalyticsAPI.get_department_level_statistics_current method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_statistics_current(account_id)

    def test_get_department_level_statistics_completed(self):
        """Integration test for the AnalyticsAPI.get_department_level_statistics_completed method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_statistics_completed(account_id)

    def test_get_department_level_statistics_broken_down_by_subaccount_terms(self):
        """Integration test for the AnalyticsAPI.get_department_level_statistics_broken_down_by_subaccount_terms method."""
        account_id = None  # Change me!!
        term_id = None  # Change me!!

        r = self.client.get_department_level_statistics_broken_down_by_subaccount_terms(
            account_id, term_id
        )

    def test_get_department_level_statistics_broken_down_by_subaccount_current(self):
        """Integration test for the AnalyticsAPI.get_department_level_statistics_broken_down_by_subaccount_current method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_statistics_broken_down_by_subaccount_current(
            account_id
        )

    def test_get_department_level_statistics_broken_down_by_subaccount_completed(self):
        """Integration test for the AnalyticsAPI.get_department_level_statistics_broken_down_by_subaccount_completed method."""
        account_id = None  # Change me!!

        r = self.client.get_department_level_statistics_broken_down_by_subaccount_completed(
            account_id
        )

    def test_get_course_level_participation_data(self):
        """Integration test for the AnalyticsAPI.get_course_level_participation_data method."""
        course_id = None  # Change me!!

        r = self.client.get_course_level_participation_data(course_id)

    def test_get_course_level_assignment_data(self):
        """Integration test for the AnalyticsAPI.get_course_level_assignment_data method."""
        course_id = None  # Change me!!

        r = self.client.get_course_level_assignment_data(course_id, async=None)

    def test_get_course_level_student_summary_data(self):
        """Integration test for the AnalyticsAPI.get_course_level_student_summary_data method."""
        course_id = None  # Change me!!

        r = self.client.get_course_level_student_summary_data(
            course_id, sort_column=None, student_id=None
        )

    def test_get_user_in_a_course_level_participation_data(self):
        """Integration test for the AnalyticsAPI.get_user_in_a_course_level_participation_data method."""
        course_id = None  # Change me!!
        student_id = None  # Change me!!

        r = self.client.get_user_in_a_course_level_participation_data(
            course_id, student_id
        )

    def test_get_user_in_a_course_level_assignment_data(self):
        """Integration test for the AnalyticsAPI.get_user_in_a_course_level_assignment_data method."""
        course_id = None  # Change me!!
        student_id = None  # Change me!!

        r = self.client.get_user_in_a_course_level_assignment_data(
            course_id, student_id
        )

    def test_get_user_in_a_course_level_messaging_data(self):
        """Integration test for the AnalyticsAPI.get_user_in_a_course_level_messaging_data method."""
        course_id = None  # Change me!!
        student_id = None  # Change me!!

        r = self.client.get_user_in_a_course_level_messaging_data(course_id, student_id)
