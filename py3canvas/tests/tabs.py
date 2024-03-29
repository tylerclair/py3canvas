"""Tabs API Tests for Version 1.0.

This is a testing template for the generated TabsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.tabs import TabsAPI
from py3canvas.apis.tabs import Tab


class TestTabsAPI(unittest.TestCase):
    """Tests for the TabsAPI."""

    def setUp(self):
        self.client = TabsAPI(secrets.instance_address, secrets.access_token)

    def test_list_available_tabs_for_course_or_group_accounts(self):
        """Integration test for the TabsAPI.list_available_tabs_for_course_or_group_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_available_tabs_for_course_or_group_accounts(
            account_id, include=None
        )

    def test_list_available_tabs_for_course_or_group_courses(self):
        """Integration test for the TabsAPI.list_available_tabs_for_course_or_group_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_available_tabs_for_course_or_group_courses(
            course_id, include=None
        )

    def test_list_available_tabs_for_course_or_group_groups(self):
        """Integration test for the TabsAPI.list_available_tabs_for_course_or_group_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_available_tabs_for_course_or_group_groups(
            group_id, include=None
        )

    def test_list_available_tabs_for_course_or_group_users(self):
        """Integration test for the TabsAPI.list_available_tabs_for_course_or_group_users method."""
        user_id = None  # Change me!!

        r = self.client.list_available_tabs_for_course_or_group_users(
            user_id, include=None
        )

    def test_update_tab_for_course(self):
        """Integration test for the TabsAPI.update_tab_for_course method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass
