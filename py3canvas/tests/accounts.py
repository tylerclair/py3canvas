"""Accounts API Tests for Version 1.0.

This is a testing template for the generated AccountsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.accounts import AccountsAPI
from py3canvas.apis.accounts import Account
from py3canvas.apis.accounts import Termsofservice
from py3canvas.apis.accounts import Helplink
from py3canvas.apis.accounts import Helplinks


class TestAccountsAPI(unittest.TestCase):
    """Tests for the AccountsAPI."""

    def setUp(self):
        self.client = AccountsAPI(secrets.instance_address, secrets.access_token)

    def test_list_accounts(self):
        """Integration test for the AccountsAPI.list_accounts method."""

        r = self.client.list_accounts(include=None)

    def test_get_accounts_that_admins_can_manage(self):
        """Integration test for the AccountsAPI.get_accounts_that_admins_can_manage method."""

        r = self.client.get_accounts_that_admins_can_manage()

    def test_list_accounts_for_course_admins(self):
        """Integration test for the AccountsAPI.list_accounts_for_course_admins method."""

        r = self.client.list_accounts_for_course_admins()

    def test_get_single_account(self):
        """Integration test for the AccountsAPI.get_single_account method."""
        id = None  # Change me!!

        r = self.client.get_single_account(id)

    def test_settings(self):
        """Integration test for the AccountsAPI.settings method."""
        account_id = None  # Change me!!

        r = self.client.settings(account_id)

    def test_permissions(self):
        """Integration test for the AccountsAPI.permissions method."""
        account_id = None  # Change me!!

        r = self.client.permissions(account_id, permissions=None)

    def test_get_sub_accounts_of_account(self):
        """Integration test for the AccountsAPI.get_sub_accounts_of_account method."""
        account_id = None  # Change me!!

        r = self.client.get_sub_accounts_of_account(account_id, recursive=None)

    def test_get_terms_of_service(self):
        """Integration test for the AccountsAPI.get_terms_of_service method."""
        account_id = None  # Change me!!

        r = self.client.get_terms_of_service(account_id)

    def test_get_help_links(self):
        """Integration test for the AccountsAPI.get_help_links method."""
        account_id = None  # Change me!!

        r = self.client.get_help_links(account_id)

    def test_list_active_courses_in_account(self):
        """Integration test for the AccountsAPI.list_active_courses_in_account method."""
        account_id = None  # Change me!!

        r = self.client.list_active_courses_in_account(account_id, blueprint=None, blueprint_associated=None, by_subaccounts=None, by_teachers=None, completed=None, ends_after=None, enrollment_term_id=None, enrollment_type=None, hide_enrollmentless_courses=None, homeroom=None, include=None, order=None, published=None, search_by=None, search_term=None, sort=None, starts_before=None, state=None, with_enrollments=None)

    def test_update_account(self):
        """Integration test for the AccountsAPI.update_account method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_user_from_root_account(self):
        """Integration test for the AccountsAPI.delete_user_from_root_account method."""
        account_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.delete_user_from_root_account(account_id, user_id)

    def test_create_new_sub_account(self):
        """Integration test for the AccountsAPI.create_new_sub_account method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_sub_account(self):
        """Integration test for the AccountsAPI.delete_sub_account method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_sub_account(account_id, id)

