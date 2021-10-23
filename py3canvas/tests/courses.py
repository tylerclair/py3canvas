"""Courses API Tests for Version 1.0.

This is a testing template for the generated CoursesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.courses import CoursesAPI
from py3canvas.apis.courses import Term
from py3canvas.apis.courses import Courseprogress
from py3canvas.apis.courses import Course
from py3canvas.apis.courses import Calendarlink


class TestCoursesAPI(unittest.TestCase):
    """Tests for the CoursesAPI."""

    def setUp(self):
        self.client = CoursesAPI(secrets.instance_address, secrets.access_token)

    def test_list_your_courses(self):
        """Integration test for the CoursesAPI.list_your_courses method."""

        r = self.client.list_your_courses(enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, exclude_blueprint_courses=None, include=None, state=None)

    def test_list_courses_for_user(self):
        """Integration test for the CoursesAPI.list_courses_for_user method."""
        user_id = None  # Change me!!

        r = self.client.list_courses_for_user(user_id, enrollment_state=None, homeroom=None, include=None, state=None)

    def test_get_user_progress(self):
        """Integration test for the CoursesAPI.get_user_progress method."""
        course_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.get_user_progress(course_id, user_id)

    def test_create_new_course(self):
        """Integration test for the CoursesAPI.create_new_course method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_upload_file(self):
        """Integration test for the CoursesAPI.upload_file method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_students(self):
        """Integration test for the CoursesAPI.list_students method."""
        course_id = None  # Change me!!

        r = self.client.list_students(course_id)

    def test_list_users_in_course_users(self):
        """Integration test for the CoursesAPI.list_users_in_course_users method."""
        course_id = None  # Change me!!

        r = self.client.list_users_in_course_users(course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, search_term=None, sort=None, user_id=None, user_ids=None)

    def test_list_users_in_course_search_users(self):
        """Integration test for the CoursesAPI.list_users_in_course_search_users method."""
        course_id = None  # Change me!!

        r = self.client.list_users_in_course_search_users(course_id, enrollment_role=None, enrollment_role_id=None, enrollment_state=None, enrollment_type=None, include=None, search_term=None, sort=None, user_id=None, user_ids=None)

    def test_list_recently_logged_in_students(self):
        """Integration test for the CoursesAPI.list_recently_logged_in_students method."""
        course_id = None  # Change me!!

        r = self.client.list_recently_logged_in_students(course_id)

    def test_get_single_user(self):
        """Integration test for the CoursesAPI.get_single_user method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_user(course_id, id)

    def test_search_for_content_share_users(self):
        """Integration test for the CoursesAPI.search_for_content_share_users method."""
        course_id = None  # Change me!!
        search_term = None  # Change me!!

        r = self.client.search_for_content_share_users(course_id, search_term)

    def test_preview_processed_html(self):
        """Integration test for the CoursesAPI.preview_processed_html method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_course_activity_stream(self):
        """Integration test for the CoursesAPI.course_activity_stream method."""
        course_id = None  # Change me!!

        r = self.client.course_activity_stream(course_id)

    def test_course_activity_stream_summary(self):
        """Integration test for the CoursesAPI.course_activity_stream_summary method."""
        course_id = None  # Change me!!

        r = self.client.course_activity_stream_summary(course_id)

    def test_course_todo_items(self):
        """Integration test for the CoursesAPI.course_todo_items method."""
        course_id = None  # Change me!!

        r = self.client.course_todo_items(course_id)

    def test_delete_conclude_course(self):
        """Integration test for the CoursesAPI.delete_conclude_course method."""
        id = None  # Change me!!
        event = None  # Change me!!

        r = self.client.delete_conclude_course(event, id)

    def test_get_course_settings(self):
        """Integration test for the CoursesAPI.get_course_settings method."""
        course_id = None  # Change me!!

        r = self.client.get_course_settings(course_id)

    def test_update_course_settings(self):
        """Integration test for the CoursesAPI.update_course_settings method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_return_test_student_for_course(self):
        """Integration test for the CoursesAPI.return_test_student_for_course method."""
        course_id = None  # Change me!!

        r = self.client.return_test_student_for_course(course_id)

    def test_get_single_course_courses(self):
        """Integration test for the CoursesAPI.get_single_course_courses method."""
        id = None  # Change me!!

        r = self.client.get_single_course_courses(id, include=None, teacher_limit=None)

    def test_get_single_course_accounts(self):
        """Integration test for the CoursesAPI.get_single_course_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_course_accounts(account_id, id, include=None, teacher_limit=None)

    def test_update_course(self):
        """Integration test for the CoursesAPI.update_course method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_courses(self):
        """Integration test for the CoursesAPI.update_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_reset_course(self):
        """Integration test for the CoursesAPI.reset_course method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_effective_due_dates(self):
        """Integration test for the CoursesAPI.get_effective_due_dates method."""
        course_id = None  # Change me!!

        r = self.client.get_effective_due_dates(course_id, assignment_ids=None)

    def test_permissions(self):
        """Integration test for the CoursesAPI.permissions method."""
        course_id = None  # Change me!!

        r = self.client.permissions(course_id, permissions=None)

    def test_get_bulk_user_progress(self):
        """Integration test for the CoursesAPI.get_bulk_user_progress method."""
        course_id = None  # Change me!!

        r = self.client.get_bulk_user_progress(course_id)

    def test_get_course_copy_status(self):
        """Integration test for the CoursesAPI.get_course_copy_status method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_course_copy_status(course_id, id)

    def test_copy_course_content(self):
        """Integration test for the CoursesAPI.copy_course_content method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

