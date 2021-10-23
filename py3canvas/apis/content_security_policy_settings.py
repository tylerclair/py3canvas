"""ContentSecurityPolicySettings API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class ContentSecurityPolicySettingsAPI(BaseCanvasAPI):
    """ContentSecurityPolicySettings API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ContentSecurityPolicySettingsAPI."""
        super(ContentSecurityPolicySettingsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ContentSecurityPolicySettingsAPI")

    def get_current_settings_for_account_or_course_courses(self, course_id):
        """
        Get current settings for account or course.

        Update multiple modules in an account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/courses/{course_id}/csp_settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/csp_settings".format(**path), data=data, params=params, no_data=True)

    def get_current_settings_for_account_or_course_accounts(self, account_id):
        """
        Get current settings for account or course.

        Update multiple modules in an account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/csp_settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/csp_settings".format(**path), data=data, params=params, no_data=True)

    def enable_disable_or_clear_explicit_csp_setting_courses(self, course_id, status):
        """
        Enable, disable, or clear explicit CSP setting.

        Either explicitly sets CSP to be on or off for courses and sub-accounts,
        or clear the explicit settings to default to those set by a parent account
        
        Note: If "inherited" and "settings_locked" are both true for this account or course,
        then the CSP setting cannot be modified.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - status
        """
            If set to "enabled" for an account, CSP will be enabled for all its courses and sub-accounts (that
        have not explicitly enabled or disabled it), using the allowed domains set on this account.
        If set to "disabled", CSP will be disabled for this account or course and for all sub-accounts
        that have not explicitly re-enabled it.
        If set to "inherited", this account or course will reset to the default state where CSP settings
        are inherited from the first parent account to have them explicitly set.
        """
        self._validate_enum(status, ["enabled", "disabled", "inherited"])
        data["status"] = status


        self.logger.debug("PUT /api/v1/courses/{course_id}/csp_settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/csp_settings".format(**path), data=data, params=params, no_data=True)

    def enable_disable_or_clear_explicit_csp_setting_accounts(self, account_id, status):
        """
        Enable, disable, or clear explicit CSP setting.

        Either explicitly sets CSP to be on or off for courses and sub-accounts,
        or clear the explicit settings to default to those set by a parent account
        
        Note: If "inherited" and "settings_locked" are both true for this account or course,
        then the CSP setting cannot be modified.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - status
        """
            If set to "enabled" for an account, CSP will be enabled for all its courses and sub-accounts (that
        have not explicitly enabled or disabled it), using the allowed domains set on this account.
        If set to "disabled", CSP will be disabled for this account or course and for all sub-accounts
        that have not explicitly re-enabled it.
        If set to "inherited", this account or course will reset to the default state where CSP settings
        are inherited from the first parent account to have them explicitly set.
        """
        self._validate_enum(status, ["enabled", "disabled", "inherited"])
        data["status"] = status


        self.logger.debug("PUT /api/v1/accounts/{account_id}/csp_settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/csp_settings".format(**path), data=data, params=params, no_data=True)

    def lock_or_unlock_current_csp_settings_for_sub_accounts_and_courses(self, account_id, settings_locked):
        """
        Lock or unlock current CSP settings for sub-accounts and courses.

        Can only be set if CSP is explicitly enabled or disabled on this account (i.e. "inherited" is false).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - settings_locked
        """
            Whether sub-accounts and courses will be prevented from overriding settings inherited from this account.
        """
        data["settings_locked"] = settings_locked


        self.logger.debug("PUT /api/v1/accounts/{account_id}/csp_settings/lock with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/csp_settings/lock".format(**path), data=data, params=params, no_data=True)

    def add_allowed_domain_to_account(self, account_id, domain):
        """
        Add an allowed domain to account.

        Adds an allowed domain for the current account. Note: this will not take effect
        unless CSP is explicitly enabled on this account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - domain
        """
            no description
        """
        data["domain"] = domain


        self.logger.debug("POST /api/v1/accounts/{account_id}/csp_settings/domains with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/csp_settings/domains".format(**path), data=data, params=params, no_data=True)

    def add_multiple_allowed_domains_to_account(self, account_id, domains):
        """
        Add multiple allowed domains to an account.

        Adds multiple allowed domains for the current account. Note: this will not take effect
        unless CSP is explicitly enabled on this account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - domains
        """
            no description
        """
        data["domains"] = domains


        self.logger.debug("POST /api/v1/accounts/{account_id}/csp_settings/domains/batch_create with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/csp_settings/domains/batch_create".format(**path), data=data, params=params, no_data=True)

    def retrieve_reported_csp_violations_for_account(self, account_id):
        """
        Retrieve reported CSP Violations for account.

        Must be called on a root account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/csp_log with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/csp_log".format(**path), data=data, params=params, no_data=True)

    def remove_domain_from_account(self, account_id, domain):
        """
        Remove a domain from account.

        Removes an allowed domain from the current account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - domain
        """
            no description
        """
        params["domain"] = domain


        self.logger.debug("DELETE /api/v1/accounts/{account_id}/csp_settings/domains with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/csp_settings/domains".format(**path), data=data, params=params, no_data=True)

