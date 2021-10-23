"""NamesAndRole API Tests for Version 1.0.

This is a testing template for the generated NamesAndRoleAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.names_and_role import NamesAndRoleAPI
from py3canvas.apis.names_and_role import Namesandrolecontext
from py3canvas.apis.names_and_role import Namesandrolemessage
from py3canvas.apis.names_and_role import Namesandrolemembership
from py3canvas.apis.names_and_role import Namesandrolememberships


class TestNamesAndRoleAPI(unittest.TestCase):
    """Tests for the NamesAndRoleAPI."""

    def setUp(self):
        self.client = NamesAndRoleAPI(secrets.instance_address, secrets.access_token)

    def test_list_course_memberships(self):
        """Integration test for the NamesAndRoleAPI.list_course_memberships method."""
        course_id = None  # Change me!!

        r = self.client.list_course_memberships(course_id, limit=None, rlid=None, role=None)

    def test_list_group_memberships(self):
        """Integration test for the NamesAndRoleAPI.list_group_memberships method."""
        group_id = None  # Change me!!

        r = self.client.list_group_memberships(group_id, `rlid`=None, limit=None, role=None)

