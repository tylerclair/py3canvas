"""Submissions API Tests for Version 1.0.

This is a testing template for the generated SubmissionsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.submissions import SubmissionsAPI
from py3canvas.apis.submissions import Mediacomment
from py3canvas.apis.submissions import Submissioncomment
from py3canvas.apis.submissions import Submission


class TestSubmissionsAPI(unittest.TestCase):
    """Tests for the SubmissionsAPI."""

    def setUp(self):
        self.client = SubmissionsAPI(secrets.instance_address, secrets.access_token)

    def test_submit_assignment_courses(self):
        """Integration test for the SubmissionsAPI.submit_assignment_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_submit_assignment_sections(self):
        """Integration test for the SubmissionsAPI.submit_assignment_sections method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_assignment_submissions_courses(self):
        """Integration test for the SubmissionsAPI.list_assignment_submissions_courses method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.list_assignment_submissions_courses(
            assignment_id, course_id, grouped=None, include=None
        )

    def test_list_assignment_submissions_sections(self):
        """Integration test for the SubmissionsAPI.list_assignment_submissions_sections method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.list_assignment_submissions_sections(
            assignment_id, section_id, grouped=None, include=None
        )

    def test_list_submissions_for_multiple_assignments_courses(self):
        """Integration test for the SubmissionsAPI.list_submissions_for_multiple_assignments_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_submissions_for_multiple_assignments_courses(
            course_id,
            assignment_ids=None,
            enrollment_state=None,
            graded_since=None,
            grading_period_id=None,
            grouped=None,
            include=None,
            order=None,
            order_direction=None,
            post_to_sis=None,
            state_based_on_date=None,
            student_ids=None,
            submitted_since=None,
            workflow_state=None,
        )

    def test_list_submissions_for_multiple_assignments_sections(self):
        """Integration test for the SubmissionsAPI.list_submissions_for_multiple_assignments_sections method."""
        section_id = None  # Change me!!

        r = self.client.list_submissions_for_multiple_assignments_sections(
            section_id,
            assignment_ids=None,
            enrollment_state=None,
            graded_since=None,
            grading_period_id=None,
            grouped=None,
            include=None,
            order=None,
            order_direction=None,
            post_to_sis=None,
            state_based_on_date=None,
            student_ids=None,
            submitted_since=None,
            workflow_state=None,
        )

    def test_get_single_submission_courses(self):
        """Integration test for the SubmissionsAPI.get_single_submission_courses method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.get_single_submission_courses(
            assignment_id, course_id, user_id, include=None
        )

    def test_get_single_submission_sections(self):
        """Integration test for the SubmissionsAPI.get_single_submission_sections method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.get_single_submission_sections(
            assignment_id, section_id, user_id, include=None
        )

    def test_upload_file_courses(self):
        """Integration test for the SubmissionsAPI.upload_file_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_upload_file_sections(self):
        """Integration test for the SubmissionsAPI.upload_file_sections method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_grade_or_comment_on_submission_courses(self):
        """Integration test for the SubmissionsAPI.grade_or_comment_on_submission_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_grade_or_comment_on_submission_sections(self):
        """Integration test for the SubmissionsAPI.grade_or_comment_on_submission_sections method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_gradeable_students(self):
        """Integration test for the SubmissionsAPI.list_gradeable_students method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.list_gradeable_students(assignment_id, course_id)

    def test_list_multiple_assignments_gradeable_students(self):
        """Integration test for the SubmissionsAPI.list_multiple_assignments_gradeable_students method."""
        course_id = None  # Change me!!

        r = self.client.list_multiple_assignments_gradeable_students(
            course_id, assignment_ids=None
        )

    def test_grade_or_comment_on_multiple_submissions_courses_submissions(self):
        """Integration test for the SubmissionsAPI.grade_or_comment_on_multiple_submissions_courses_submissions method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_grade_or_comment_on_multiple_submissions_courses_assignments(self):
        """Integration test for the SubmissionsAPI.grade_or_comment_on_multiple_submissions_courses_assignments method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_grade_or_comment_on_multiple_submissions_sections_submissions(self):
        """Integration test for the SubmissionsAPI.grade_or_comment_on_multiple_submissions_sections_submissions method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_grade_or_comment_on_multiple_submissions_sections_assignments(self):
        """Integration test for the SubmissionsAPI.grade_or_comment_on_multiple_submissions_sections_assignments method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_submission_as_read_courses(self):
        """Integration test for the SubmissionsAPI.mark_submission_as_read_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_submission_as_read_sections(self):
        """Integration test for the SubmissionsAPI.mark_submission_as_read_sections method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_submission_as_unread_courses(self):
        """Integration test for the SubmissionsAPI.mark_submission_as_unread_courses method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.mark_submission_as_unread_courses(
            assignment_id, course_id, user_id
        )

    def test_mark_submission_as_unread_sections(self):
        """Integration test for the SubmissionsAPI.mark_submission_as_unread_sections method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.mark_submission_as_unread_sections(
            assignment_id, section_id, user_id
        )

    def test_submission_summary_courses(self):
        """Integration test for the SubmissionsAPI.submission_summary_courses method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.submission_summary_courses(
            assignment_id, course_id, grouped=None
        )

    def test_submission_summary_sections(self):
        """Integration test for the SubmissionsAPI.submission_summary_sections method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.submission_summary_sections(
            assignment_id, section_id, grouped=None
        )
