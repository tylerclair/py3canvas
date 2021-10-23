"""ContentSecurityPolicySettings API Tests for Version 1.0.

This is a testing template for the generated ContentSecurityPolicySettingsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.content_security_policy_settings import ContentSecurityPolicySettingsAPI


class TestContentSecurityPolicySettingsAPI(unittest.TestCase):
    """Tests for the ContentSecurityPolicySettingsAPI."""

    def setUp(self):
        self.client = ContentSecurityPolicySettingsAPI(secrets.instance_address, secrets.access_token)

    def test_get_current_settings_for_account_or_course_courses(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.get_current_settings_for_account_or_course_courses method."""
        course_id = None  # Change me!!

        r = self.client.get_current_settings_for_account_or_course_courses(course_id)

    def test_get_current_settings_for_account_or_course_accounts(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.get_current_settings_for_account_or_course_accounts method."""
        account_id = None  # Change me!!

        r = self.client.get_current_settings_for_account_or_course_accounts(account_id)

    def test_enable_disable_or_clear_explicit_csp_setting_courses(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.enable_disable_or_clear_explicit_csp_setting_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_enable_disable_or_clear_explicit_csp_setting_accounts(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.enable_disable_or_clear_explicit_csp_setting_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_lock_or_unlock_current_csp_settings_for_sub_accounts_and_courses(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.lock_or_unlock_current_csp_settings_for_sub_accounts_and_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_add_allowed_domain_to_account(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.add_allowed_domain_to_account method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_add_multiple_allowed_domains_to_account(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.add_multiple_allowed_domains_to_account method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_retrieve_reported_csp_violations_for_account(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.retrieve_reported_csp_violations_for_account method."""
        account_id = None  # Change me!!

        r = self.client.retrieve_reported_csp_violations_for_account(account_id)

    def test_remove_domain_from_account(self):
        """Integration test for the ContentSecurityPolicySettingsAPI.remove_domain_from_account method."""
        account_id = None  # Change me!!
        domain = None  # Change me!!

        r = self.client.remove_domain_from_account(account_id, domain)

