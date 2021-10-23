"""Assignments API Tests for Version 1.0.

This is a testing template for the generated AssignmentsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.assignments import AssignmentsAPI
from py3canvas.apis.assignments import Externaltooltagattributes
from py3canvas.apis.assignments import Lockinfo
from py3canvas.apis.assignments import Rubricrating
from py3canvas.apis.assignments import Rubriccriteria
from py3canvas.apis.assignments import Assignmentdate
from py3canvas.apis.assignments import Turnitinsettings
from py3canvas.apis.assignments import Needsgradingcount
from py3canvas.apis.assignments import Scorestatistic
from py3canvas.apis.assignments import Assignment
from py3canvas.apis.assignments import Assignmentoverride


class TestAssignmentsAPI(unittest.TestCase):
    """Tests for the AssignmentsAPI."""

    def setUp(self):
        self.client = AssignmentsAPI(secrets.instance_address, secrets.access_token)

    def test_delete_assignment(self):
        """Integration test for the AssignmentsAPI.delete_assignment method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_assignment(course_id, id)

    def test_list_assignments_assignments(self):
        """Integration test for the AssignmentsAPI.list_assignments_assignments method."""
        course_id = None  # Change me!!

        r = self.client.list_assignments_assignments(course_id, assignment_ids=None, bucket=None, include=None, needs_grading_count_by_section=None, order_by=None, override_assignment_dates=None, post_to_sis=None, search_term=None)

    def test_list_assignments_assignment_groups(self):
        """Integration test for the AssignmentsAPI.list_assignments_assignment_groups method."""
        course_id = None  # Change me!!
        assignment_group_id = None  # Change me!!

        r = self.client.list_assignments_assignment_groups(assignment_group_id, course_id, assignment_ids=None, bucket=None, include=None, needs_grading_count_by_section=None, order_by=None, override_assignment_dates=None, post_to_sis=None, search_term=None)

    def test_list_assignments_for_user(self):
        """Integration test for the AssignmentsAPI.list_assignments_for_user method."""
        user_id = None  # Change me!!
        course_id = None  # Change me!!

        r = self.client.list_assignments_for_user(course_id, user_id)

    def test_duplicate_assignnment(self):
        """Integration test for the AssignmentsAPI.duplicate_assignnment method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_single_assignment(self):
        """Integration test for the AssignmentsAPI.get_single_assignment method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_assignment(course_id, id, all_dates=None, include=None, needs_grading_count_by_section=None, override_assignment_dates=None)

    def test_create_assignment(self):
        """Integration test for the AssignmentsAPI.create_assignment method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_edit_assignment(self):
        """Integration test for the AssignmentsAPI.edit_assignment method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_bulk_update_assignment_dates(self):
        """Integration test for the AssignmentsAPI.bulk_update_assignment_dates method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_assignment_overrides(self):
        """Integration test for the AssignmentsAPI.list_assignment_overrides method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.list_assignment_overrides(assignment_id, course_id)

    def test_get_single_assignment_override(self):
        """Integration test for the AssignmentsAPI.get_single_assignment_override method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_single_assignment_override(assignment_id, course_id, id)

    def test_redirect_to_assignment_override_for_group(self):
        """Integration test for the AssignmentsAPI.redirect_to_assignment_override_for_group method."""
        group_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.redirect_to_assignment_override_for_group(assignment_id, group_id)

    def test_redirect_to_assignment_override_for_section(self):
        """Integration test for the AssignmentsAPI.redirect_to_assignment_override_for_section method."""
        course_section_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.redirect_to_assignment_override_for_section(assignment_id, course_section_id)

    def test_create_assignment_override(self):
        """Integration test for the AssignmentsAPI.create_assignment_override method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_assignment_override(self):
        """Integration test for the AssignmentsAPI.update_assignment_override method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_assignment_override(self):
        """Integration test for the AssignmentsAPI.delete_assignment_override method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_assignment_override(assignment_id, course_id, id)

    def test_batch_retrieve_overrides_in_course(self):
        """Integration test for the AssignmentsAPI.batch_retrieve_overrides_in_course method."""
        course_id = None  # Change me!!
        assignment_overrides[id] = None  # Change me!!
        assignment_overrides[assignment_id] = None  # Change me!!

        r = self.client.batch_retrieve_overrides_in_course(assignment_overrides_assignment_id, assignment_overrides_id, course_id)

    def test_batch_create_overrides_in_course(self):
        """Integration test for the AssignmentsAPI.batch_create_overrides_in_course method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_batch_update_overrides_in_course(self):
        """Integration test for the AssignmentsAPI.batch_update_overrides_in_course method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

