"""PlannerNote API Tests for Version 1.0.

This is a testing template for the generated PlannerNoteAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.planner_note import PlannerNoteAPI
from py3canvas.apis.planner_note import Plannernote


class TestPlannerNoteAPI(unittest.TestCase):
    """Tests for the PlannerNoteAPI."""

    def setUp(self):
        self.client = PlannerNoteAPI(secrets.instance_address, secrets.access_token)

    def test_list_planner_notes(self):
        """Integration test for the PlannerNoteAPI.list_planner_notes method."""

        r = self.client.list_planner_notes()

    def test_show_plannernote(self):
        """Integration test for the PlannerNoteAPI.show_plannernote method."""
        id = None  # Change me!!

        r = self.client.show_plannernote(id)

    def test_update_plannernote(self):
        """Integration test for the PlannerNoteAPI.update_plannernote method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_planner_note(self):
        """Integration test for the PlannerNoteAPI.create_planner_note method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_planner_note(self):
        """Integration test for the PlannerNoteAPI.delete_planner_note method."""
        id = None  # Change me!!

        r = self.client.delete_planner_note(id)

