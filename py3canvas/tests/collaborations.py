"""Collaborations API Tests for Version 1.0.

This is a testing template for the generated CollaborationsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.collaborations import CollaborationsAPI
from py3canvas.apis.collaborations import Collaboration
from py3canvas.apis.collaborations import Collaborator


class TestCollaborationsAPI(unittest.TestCase):
    """Tests for the CollaborationsAPI."""

    def setUp(self):
        self.client = CollaborationsAPI(secrets.instance_address, secrets.access_token)

    def test_list_collaborations_courses(self):
        """Integration test for the CollaborationsAPI.list_collaborations_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_collaborations_courses(course_id)

    def test_list_collaborations_groups(self):
        """Integration test for the CollaborationsAPI.list_collaborations_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_collaborations_groups(group_id)

    def test_list_members_of_collaboration(self):
        """Integration test for the CollaborationsAPI.list_members_of_collaboration method."""
        id = None  # Change me!!

        r = self.client.list_members_of_collaboration(id, include=None)

    def test_list_potential_members_courses(self):
        """Integration test for the CollaborationsAPI.list_potential_members_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_potential_members_courses(course_id)

    def test_list_potential_members_groups(self):
        """Integration test for the CollaborationsAPI.list_potential_members_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_potential_members_groups(group_id)

