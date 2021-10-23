"""PlannerOverride API Tests for Version 1.0.

This is a testing template for the generated PlannerOverrideAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.planner_override import PlannerOverrideAPI
from py3canvas.apis.planner_override import Planneroverride


class TestPlannerOverrideAPI(unittest.TestCase):
    """Tests for the PlannerOverrideAPI."""

    def setUp(self):
        self.client = PlannerOverrideAPI(secrets.instance_address, secrets.access_token)

    def test_list_planner_items(self):
        """Integration test for the PlannerOverrideAPI.list_planner_items method."""

        r = self.client.list_planner_items(end_date=None, filter=None, start_date=None)

    def test_list_planner_overrides(self):
        """Integration test for the PlannerOverrideAPI.list_planner_overrides method."""

        r = self.client.list_planner_overrides()

    def test_show_planner_override(self):
        """Integration test for the PlannerOverrideAPI.show_planner_override method."""
        id = None  # Change me!!

        r = self.client.show_planner_override(id)

    def test_update_planner_override(self):
        """Integration test for the PlannerOverrideAPI.update_planner_override method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_planner_override(self):
        """Integration test for the PlannerOverrideAPI.create_planner_override method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_planner_override(self):
        """Integration test for the PlannerOverrideAPI.delete_planner_override method."""
        id = None  # Change me!!

        r = self.client.delete_planner_override(id)

