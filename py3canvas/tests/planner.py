"""Planner API Tests for Version 1.0.

This is a testing template for the generated PlannerAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.planner import PlannerAPI
from py3canvas.apis.planner import Plannernote
from py3canvas.apis.planner import Planneroverride


class TestPlannerAPI(unittest.TestCase):
    """Tests for the PlannerAPI."""

    def setUp(self):
        self.client = PlannerAPI(secrets.instance_address, secrets.access_token)

    def test_list_planner_items_planner(self):
        """Integration test for the PlannerAPI.list_planner_items_planner method."""

        r = self.client.list_planner_items_planner(context_codes=None, end_date=None, filter=None, start_date=None)

    def test_list_planner_items_users(self):
        """Integration test for the PlannerAPI.list_planner_items_users method."""
        user_id = None  # Change me!!

        r = self.client.list_planner_items_users(user_id, context_codes=None, end_date=None, filter=None, start_date=None)

    def test_list_planner_notes(self):
        """Integration test for the PlannerAPI.list_planner_notes method."""

        r = self.client.list_planner_notes(context_codes=None, end_date=None, start_date=None)

    def test_show_planner_note(self):
        """Integration test for the PlannerAPI.show_planner_note method."""
        id = None  # Change me!!

        r = self.client.show_planner_note(id)

    def test_update_planner_note(self):
        """Integration test for the PlannerAPI.update_planner_note method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_planner_note(self):
        """Integration test for the PlannerAPI.create_planner_note method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_planner_note(self):
        """Integration test for the PlannerAPI.delete_planner_note method."""
        id = None  # Change me!!

        r = self.client.delete_planner_note(id)

    def test_list_planner_overrides(self):
        """Integration test for the PlannerAPI.list_planner_overrides method."""

        r = self.client.list_planner_overrides()

    def test_show_planner_override(self):
        """Integration test for the PlannerAPI.show_planner_override method."""
        id = None  # Change me!!

        r = self.client.show_planner_override(id)

    def test_update_planner_override(self):
        """Integration test for the PlannerAPI.update_planner_override method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_planner_override(self):
        """Integration test for the PlannerAPI.create_planner_override method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_planner_override(self):
        """Integration test for the PlannerAPI.delete_planner_override method."""
        id = None  # Change me!!

        r = self.client.delete_planner_override(id)

