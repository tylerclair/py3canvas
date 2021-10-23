"""ModeratedGrading API Tests for Version 1.0.

This is a testing template for the generated ModeratedGradingAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.moderated_grading import ModeratedGradingAPI
from py3canvas.apis.moderated_grading import Provisionalgrade


class TestModeratedGradingAPI(unittest.TestCase):
    """Tests for the ModeratedGradingAPI."""

    def setUp(self):
        self.client = ModeratedGradingAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_list_students_selected_for_moderation(self):
        """Integration test for the ModeratedGradingAPI.list_students_selected_for_moderation method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.list_students_selected_for_moderation(assignment_id, course_id)

    def test_select_students_for_moderation(self):
        """Integration test for the ModeratedGradingAPI.select_students_for_moderation method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_bulk_select_provisional_grades(self):
        """Integration test for the ModeratedGradingAPI.bulk_select_provisional_grades method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_provisional_grade_status_for_student(self):
        """Integration test for the ModeratedGradingAPI.show_provisional_grade_status_for_student method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.show_provisional_grade_status_for_student(
            assignment_id, course_id, student_id=None
        )

    def test_select_provisional_grade(self):
        """Integration test for the ModeratedGradingAPI.select_provisional_grade method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_publish_provisional_grades_for_assignment(self):
        """Integration test for the ModeratedGradingAPI.publish_provisional_grades_for_assignment method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_provisional_grade_status_for_student(self):
        """Integration test for the ModeratedGradingAPI.show_provisional_grade_status_for_student method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.show_provisional_grade_status_for_student(
            assignment_id, course_id, anonymous_id=None
        )
