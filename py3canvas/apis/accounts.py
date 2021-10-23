"""Accounts API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class AccountsAPI(BaseCanvasAPI):
    """Accounts API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AccountsAPI."""
        super(AccountsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AccountsAPI")

    def list_accounts(self, include=None):
        """
        List accounts.

        A paginated list of accounts that the current user can view or manage.
        Typically, students and even teachers will get an empty list in response,
        only account admins can view the accounts that they are in.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - include
        """
            Array of additional information to include.

        "lti_guid":: the 'tool_consumer_instance_guid' that will be sent for this account on LTI launches
        "registration_settings":: returns info about the privacy policy and terms of use
        "services":: returns services and whether they are enabled (requires account management permissions)
        """
        if include is not None:
            self._validate_enum(include, ["lti_guid", "registration_settings", "services"])
            params["include"] = include


        self.logger.debug("GET /api/v1/accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts".format(**path), data=data, params=params, all_pages=True)

    def get_accounts_that_admins_can_manage(self):
        """
        Get accounts that admins can manage.

        A paginated list of accounts where the current user has permission to create
        or manage courses. List will be empty for students and teachers as only admins
        can view which accounts they are in.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/manageable_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/manageable_accounts".format(**path), data=data, params=params, all_pages=True)

    def list_accounts_for_course_admins(self):
        """
        List accounts for course admins.

        A paginated list of accounts that the current user can view through their
        admin course enrollments. (Teacher, TA, or designer enrollments).
        Only returns "id", "name", "workflow_state", "root_account_id" and "parent_account_id"
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/v1/course_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/course_accounts".format(**path), data=data, params=params, all_pages=True)

    def get_single_account(self, id):
        """
        Get a single account.

        Retrieve information on an individual account, given by id or sis
        sis_account_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/accounts/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{id}".format(**path), data=data, params=params, single_item=True)

    def settings(self, account_id):
        """
        Settings.

        Returns all of the settings for the specified account as a JSON object. The caller must be an Account
        admin with the manage_account_settings permission.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/settings with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/settings".format(**path), data=data, params=params, no_data=True)

    def permissions(self, account_id, permissions=None):
        """
        Permissions.

        Returns permission information for the calling user and the given account.
        You may use `self` as the account id to check permissions against the domain root account.
        The caller must have an account role or admin (teacher/TA/designer) enrollment in a course
        in the account.
        
        See also the {api:CoursesController#permissions Course} and {api:GroupsController#permissions Group}
        counterparts.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # OPTIONAL - permissions
        """
            List of permissions to check against the authenticated user.
        Permission names are documented in the {api:RoleOverridesController#add_role Create a role} endpoint.
        """
        if permissions is not None:
            params["permissions"] = permissions


        self.logger.debug("GET /api/v1/accounts/{account_id}/permissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/permissions".format(**path), data=data, params=params, no_data=True)

    def get_sub_accounts_of_account(self, account_id, recursive=None):
        """
        Get the sub-accounts of an account.

        List accounts that are sub-accounts of the given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # OPTIONAL - recursive
        """
            If true, the entire account tree underneath
        this account will be returned (though still paginated). If false, only
        direct sub-accounts of this account will be returned. Defaults to false.
        """
        if recursive is not None:
            params["recursive"] = recursive


        self.logger.debug("GET /api/v1/accounts/{account_id}/sub_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/sub_accounts".format(**path), data=data, params=params, all_pages=True)

    def get_terms_of_service(self, account_id):
        """
        Get the Terms of Service.

        Returns the terms of service for that account
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/terms_of_service with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/terms_of_service".format(**path), data=data, params=params, single_item=True)

    def get_help_links(self, account_id):
        """
        Get help links.

        Returns the help links for that account
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/help_links with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/help_links".format(**path), data=data, params=params, single_item=True)

    def list_active_courses_in_account(self, account_id, blueprint=None, blueprint_associated=None, by_subaccounts=None, by_teachers=None, completed=None, ends_after=None, enrollment_term_id=None, enrollment_type=None, hide_enrollmentless_courses=None, homeroom=None, include=None, order=None, published=None, search_by=None, search_term=None, sort=None, starts_before=None, state=None, with_enrollments=None):
        """
        List active courses in an account.

        Retrieve a paginated list of courses in this account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # OPTIONAL - with_enrollments
        """
            If true, include only courses with at least one enrollment.  If false,
        include only courses with no enrollments.  If not present, do not filter
        on course enrollment status.
        """
        if with_enrollments is not None:
            params["with_enrollments"] = with_enrollments


        # OPTIONAL - enrollment_type
        """
            If set, only return courses that have at least one user enrolled in
        in the course with one of the specified enrollment types.
        """
        if enrollment_type is not None:
            self._validate_enum(enrollment_type, ["teacher", "student", "ta", "observer", "designer"])
            params["enrollment_type"] = enrollment_type


        # OPTIONAL - published
        """
            If true, include only published courses.  If false, exclude published
        courses.  If not present, do not filter on published status.
        """
        if published is not None:
            params["published"] = published


        # OPTIONAL - completed
        """
            If true, include only completed courses (these may be in state
        'completed', or their enrollment term may have ended).  If false, exclude
        completed courses.  If not present, do not filter on completed status.
        """
        if completed is not None:
            params["completed"] = completed


        # OPTIONAL - blueprint
        """
            If true, include only blueprint courses. If false, exclude them.
        If not present, do not filter on this basis.
        """
        if blueprint is not None:
            params["blueprint"] = blueprint


        # OPTIONAL - blueprint_associated
        """
            If true, include only courses that inherit content from a blueprint course.
        If false, exclude them. If not present, do not filter on this basis.
        """
        if blueprint_associated is not None:
            params["blueprint_associated"] = blueprint_associated


        # OPTIONAL - by_teachers
        """
            List of User IDs of teachers; if supplied, include only courses taught by
        one of the referenced users.
        """
        if by_teachers is not None:
            params["by_teachers"] = by_teachers


        # OPTIONAL - by_subaccounts
        """
            List of Account IDs; if supplied, include only courses associated with one
        of the referenced subaccounts.
        """
        if by_subaccounts is not None:
            params["by_subaccounts"] = by_subaccounts


        # OPTIONAL - hide_enrollmentless_courses
        """
            If present, only return courses that have at least one enrollment.
        Equivalent to 'with_enrollments=true'; retained for compatibility.
        """
        if hide_enrollmentless_courses is not None:
            params["hide_enrollmentless_courses"] = hide_enrollmentless_courses


        # OPTIONAL - state
        """
            If set, only return courses that are in the given state(s). By default,
        all states but "deleted" are returned.
        """
        if state is not None:
            self._validate_enum(state, ["created", "claimed", "available", "completed", "deleted", "all"])
            params["state"] = state


        # OPTIONAL - enrollment_term_id
        """
            If set, only includes courses from the specified term.
        """
        if enrollment_term_id is not None:
            params["enrollment_term_id"] = enrollment_term_id


        # OPTIONAL - search_term
        """
            The partial course name, code, or full ID to match and return in the results list. Must be at least 3 characters.
        """
        if search_term is not None:
            params["search_term"] = search_term


        # OPTIONAL - include
        """
            - All explanations can be seen in the {api:CoursesController#index Course API index documentation}
        - "sections", "needs_grading_count" and "total_scores" are not valid options at the account level
        """
        if include is not None:
            self._validate_enum(include, ["syllabus_body", "term", "course_progress", "storage_quota_used_mb", "total_students", "teachers", "account_name", "concluded"])
            params["include"] = include


        # OPTIONAL - sort
        """
            The column to sort results by.
        """
        if sort is not None:
            self._validate_enum(sort, ["course_name", "sis_course_id", "teacher", "account_name"])
            params["sort"] = sort


        # OPTIONAL - order
        """
            The order to sort the given column by.
        """
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order


        # OPTIONAL - search_by
        """
            The filter to search by. "course" searches for course names, course codes,
        and SIS IDs. "teacher" searches for teacher names
        """
        if search_by is not None:
            self._validate_enum(search_by, ["course", "teacher"])
            params["search_by"] = search_by


        # OPTIONAL - starts_before
        """
            If set, only return courses that start before the value (inclusive)
        or their enrollment term starts before the value (inclusive)
        or both the course's start_at and the enrollment term's start_at are set to null.
        The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if starts_before is not None:
            params["starts_before"] = starts_before


        # OPTIONAL - ends_after
        """
            If set, only return courses that end after the value (inclusive)
        or their enrollment term ends after the value (inclusive)
        or both the course's end_at and the enrollment term's end_at are set to null.
        The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if ends_after is not None:
            params["ends_after"] = ends_after


        # OPTIONAL - homeroom
        """
            If set, only return homeroom courses.
        """
        if homeroom is not None:
            params["homeroom"] = homeroom


        self.logger.debug("GET /api/v1/accounts/{account_id}/courses with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/courses".format(**path), data=data, params=params, all_pages=True)

    def update_account(self, id, account_course_template_id=None, account_default_group_storage_quota_mb=None, account_default_storage_quota_mb=None, account_default_time_zone=None, account_default_user_storage_quota_mb=None, account_lock_outcome_proficiency_locked=None, account_lock_proficiency_calculation_locked=None, account_name=None, account_services=None, account_settings_lock_all_announcements_locked=None, account_settings_lock_all_announcements_value=None, account_settings_lock_outcome_proficiency_value=None, account_settings_lock_proficiency_calculation_value=None, account_settings_microsoft_sync_enabled=None, account_settings_microsoft_sync_login_attribute=None, account_settings_microsoft_sync_login_attribute_suffix=None, account_settings_microsoft_sync_remote_attribute=None, account_settings_microsoft_sync_tenant=None, account_settings_restrict_student_future_listing_locked=None, account_settings_restrict_student_future_listing_value=None, account_settings_restrict_student_future_view_locked=None, account_settings_restrict_student_future_view_value=None, account_settings_restrict_student_past_view_locked=None, account_settings_restrict_student_past_view_value=None, account_settings_usage_rights_required_locked=None, account_settings_usage_rights_required_value=None, account_sis_account_id=None):
        """
        Update an account.

        Update an existing account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - account[name]
        """
            Updates the account name
        """
        if account_name is not None:
            data["account[name]"] = account_name


        # OPTIONAL - account[sis_account_id]
        """
            Updates the account sis_account_id
        Must have manage_sis permission and must not be a root_account.
        """
        if account_sis_account_id is not None:
            data["account[sis_account_id]"] = account_sis_account_id


        # OPTIONAL - account[default_time_zone]
        """
            The default time zone of the account. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        """
        if account_default_time_zone is not None:
            data["account[default_time_zone]"] = account_default_time_zone


        # OPTIONAL - account[default_storage_quota_mb]
        """
            The default course storage quota to be used, if not otherwise specified.
        """
        if account_default_storage_quota_mb is not None:
            data["account[default_storage_quota_mb]"] = account_default_storage_quota_mb


        # OPTIONAL - account[default_user_storage_quota_mb]
        """
            The default user storage quota to be used, if not otherwise specified.
        """
        if account_default_user_storage_quota_mb is not None:
            data["account[default_user_storage_quota_mb]"] = account_default_user_storage_quota_mb


        # OPTIONAL - account[default_group_storage_quota_mb]
        """
            The default group storage quota to be used, if not otherwise specified.
        """
        if account_default_group_storage_quota_mb is not None:
            data["account[default_group_storage_quota_mb]"] = account_default_group_storage_quota_mb


        # OPTIONAL - account[course_template_id]
        """
            The ID of a course to be used as a template for all newly created courses.
        Empty means to inherit the setting from parent account, 0 means to not
        use a template even if a parent account has one set. The course must be
        marked as a template.
        """
        if account_course_template_id is not None:
            data["account[course_template_id]"] = account_course_template_id


        # OPTIONAL - account[settings][restrict_student_past_view][value]
        """
            Restrict students from viewing courses after end date
        """
        if account_settings_restrict_student_past_view_value is not None:
            data["account[settings][restrict_student_past_view][value]"] = account_settings_restrict_student_past_view_value


        # OPTIONAL - account[settings][restrict_student_past_view][locked]
        """
            Lock this setting for sub-accounts and courses
        """
        if account_settings_restrict_student_past_view_locked is not None:
            data["account[settings][restrict_student_past_view][locked]"] = account_settings_restrict_student_past_view_locked


        # OPTIONAL - account[settings][restrict_student_future_view][value]
        """
            Restrict students from viewing courses before start date
        """
        if account_settings_restrict_student_future_view_value is not None:
            data["account[settings][restrict_student_future_view][value]"] = account_settings_restrict_student_future_view_value


        # OPTIONAL - account[settings][microsoft_sync_enabled]
        """
            Determines whether this account has Microsoft Teams Sync enabled or not.

        Note that if you are altering Microsoft Teams sync settings you must enable
        the Microsoft Group enrollment syncing feature flag. In addition, if you are enabling
        Microsoft Teams sync, you must also specify a tenant, login attribute, and a remote attribute.
        Specifying a suffix to use is optional.
        """
        if account_settings_microsoft_sync_enabled is not None:
            data["account[settings][microsoft_sync_enabled]"] = account_settings_microsoft_sync_enabled


        # OPTIONAL - account[settings][microsoft_sync_tenant]
        """
            The tenant this account should use when using Microsoft Teams Sync.
        This should be an Azure Active Directory domain name.
        """
        if account_settings_microsoft_sync_tenant is not None:
            data["account[settings][microsoft_sync_tenant]"] = account_settings_microsoft_sync_tenant


        # OPTIONAL - account[settings][microsoft_sync_login_attribute]
        """
            The attribute this account should use to lookup users when using Microsoft Teams Sync.
        Must be one of "sub", "email", "oid", "preferred_username", or "integration_id".
        """
        if account_settings_microsoft_sync_login_attribute is not None:
            data["account[settings][microsoft_sync_login_attribute]"] = account_settings_microsoft_sync_login_attribute


        # OPTIONAL - account[settings][microsoft_sync_login_attribute_suffix]
        """
            A suffix that will be appended to the result of the login attribute when associating
        Canvas users with Microsoft users. Must be under 255 characters and contain no whitespace.
        This field is optional.
        """
        if account_settings_microsoft_sync_login_attribute_suffix is not None:
            data["account[settings][microsoft_sync_login_attribute_suffix]"] = account_settings_microsoft_sync_login_attribute_suffix


        # OPTIONAL - account[settings][microsoft_sync_remote_attribute]
        """
            The Active Directory attribute to use when associating Canvas users with Microsoft users.
        Must be one of "mail", "mailNickname", or "userPrincipalName".
        """
        if account_settings_microsoft_sync_remote_attribute is not None:
            data["account[settings][microsoft_sync_remote_attribute]"] = account_settings_microsoft_sync_remote_attribute


        # OPTIONAL - account[settings][restrict_student_future_view][locked]
        """
            Lock this setting for sub-accounts and courses
        """
        if account_settings_restrict_student_future_view_locked is not None:
            data["account[settings][restrict_student_future_view][locked]"] = account_settings_restrict_student_future_view_locked


        # OPTIONAL - account[settings][lock_all_announcements][value]
        """
            Disable comments on announcements
        """
        if account_settings_lock_all_announcements_value is not None:
            data["account[settings][lock_all_announcements][value]"] = account_settings_lock_all_announcements_value


        # OPTIONAL - account[settings][lock_all_announcements][locked]
        """
            Lock this setting for sub-accounts and courses
        """
        if account_settings_lock_all_announcements_locked is not None:
            data["account[settings][lock_all_announcements][locked]"] = account_settings_lock_all_announcements_locked


        # OPTIONAL - account[settings][usage_rights_required][value]
        """
            Copyright and license information must be provided for files before they are published.
        """
        if account_settings_usage_rights_required_value is not None:
            data["account[settings][usage_rights_required][value]"] = account_settings_usage_rights_required_value


        # OPTIONAL - account[settings][usage_rights_required][locked]
        """
            Lock this setting for sub-accounts and courses
        """
        if account_settings_usage_rights_required_locked is not None:
            data["account[settings][usage_rights_required][locked]"] = account_settings_usage_rights_required_locked


        # OPTIONAL - account[settings][restrict_student_future_listing][value]
        """
            Restrict students from viewing future enrollments in course list
        """
        if account_settings_restrict_student_future_listing_value is not None:
            data["account[settings][restrict_student_future_listing][value]"] = account_settings_restrict_student_future_listing_value


        # OPTIONAL - account[settings][restrict_student_future_listing][locked]
        """
            Lock this setting for sub-accounts and courses
        """
        if account_settings_restrict_student_future_listing_locked is not None:
            data["account[settings][restrict_student_future_listing][locked]"] = account_settings_restrict_student_future_listing_locked


        # OPTIONAL - account[settings][lock_outcome_proficiency][value]
        """
            [DEPRECATED] Restrict instructors from changing mastery scale
        """
        if account_settings_lock_outcome_proficiency_value is not None:
            data["account[settings][lock_outcome_proficiency][value]"] = account_settings_lock_outcome_proficiency_value


        # OPTIONAL - account[lock_outcome_proficiency][locked]
        """
            [DEPRECATED] Lock this setting for sub-accounts and courses
        """
        if account_lock_outcome_proficiency_locked is not None:
            data["account[lock_outcome_proficiency][locked]"] = account_lock_outcome_proficiency_locked


        # OPTIONAL - account[settings][lock_proficiency_calculation][value]
        """
            [DEPRECATED] Restrict instructors from changing proficiency calculation method
        """
        if account_settings_lock_proficiency_calculation_value is not None:
            data["account[settings][lock_proficiency_calculation][value]"] = account_settings_lock_proficiency_calculation_value


        # OPTIONAL - account[lock_proficiency_calculation][locked]
        """
            [DEPRECATED] Lock this setting for sub-accounts and courses
        """
        if account_lock_proficiency_calculation_locked is not None:
            data["account[lock_proficiency_calculation][locked]"] = account_lock_proficiency_calculation_locked


        # OPTIONAL - account[services]
        """
            Give this a set of keys and boolean values to enable or disable services matching the keys
        """
        if account_services is not None:
            data["account[services]"] = account_services


        self.logger.debug("PUT /api/v1/accounts/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_user_from_root_account(self, account_id, user_id):
        """
        Delete a user from the root account.

        Delete a user record from a Canvas root account. If a user is associated
        with multiple root accounts (in a multi-tenant instance of Canvas), this
        action will NOT remove them from the other accounts.
        
        WARNING: This API will allow a user to remove themselves from the account.
        If they do this, they won't be able to make API calls or log into Canvas at
        that account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("DELETE /api/v1/accounts/{account_id}/users/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/users/{user_id}".format(**path), data=data, params=params, single_item=True)

    def create_new_sub_account(self, account_id, account_name, account_default_group_storage_quota_mb=None, account_default_storage_quota_mb=None, account_default_user_storage_quota_mb=None, account_sis_account_id=None):
        """
        Create a new sub-account.

        Add a new sub-account to a given account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - account[name]
        """
            The name of the new sub-account.
        """
        data["account[name]"] = account_name


        # OPTIONAL - account[sis_account_id]
        """
            The account's identifier in the Student Information System.
        """
        if account_sis_account_id is not None:
            data["account[sis_account_id]"] = account_sis_account_id


        # OPTIONAL - account[default_storage_quota_mb]
        """
            The default course storage quota to be used, if not otherwise specified.
        """
        if account_default_storage_quota_mb is not None:
            data["account[default_storage_quota_mb]"] = account_default_storage_quota_mb


        # OPTIONAL - account[default_user_storage_quota_mb]
        """
            The default user storage quota to be used, if not otherwise specified.
        """
        if account_default_user_storage_quota_mb is not None:
            data["account[default_user_storage_quota_mb]"] = account_default_user_storage_quota_mb


        # OPTIONAL - account[default_group_storage_quota_mb]
        """
            The default group storage quota to be used, if not otherwise specified.
        """
        if account_default_group_storage_quota_mb is not None:
            data["account[default_group_storage_quota_mb]"] = account_default_group_storage_quota_mb


        self.logger.debug("POST /api/v1/accounts/{account_id}/sub_accounts with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/sub_accounts".format(**path), data=data, params=params, single_item=True)

    def delete_sub_account(self, account_id, id):
        """
        Delete a sub-account.

        Cannot delete an account with active courses or active sub_accounts.
        Cannot delete a root_account
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/v1/accounts/{account_id}/sub_accounts/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/sub_accounts/{id}".format(**path), data=data, params=params, single_item=True)


class Account(BaseModel):
    """Account Model."""

    def __init__(self, id=None, name=None, uuid=None, parent_account_id=None, root_account_id=None, default_storage_quota_mb=None, default_user_storage_quota_mb=None, default_group_storage_quota_mb=None, default_time_zone=None, sis_account_id=None, integration_id=None, sis_import_id=None, lti_guid=None, workflow_state=None):
        """Init method for Account class."""
        self._id = id
        self._name = name
        self._uuid = uuid
        self._parent_account_id = parent_account_id
        self._root_account_id = root_account_id
        self._default_storage_quota_mb = default_storage_quota_mb
        self._default_user_storage_quota_mb = default_user_storage_quota_mb
        self._default_group_storage_quota_mb = default_group_storage_quota_mb
        self._default_time_zone = default_time_zone
        self._sis_account_id = sis_account_id
        self._integration_id = integration_id
        self._sis_import_id = sis_import_id
        self._lti_guid = lti_guid
        self._workflow_state = workflow_state

        self.logger = logging.getLogger('py3canvas.Account')

    @property
    def id(self):
        """the ID of the Account object."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """The display name of the account."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def uuid(self):
        """The UUID of the account."""
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """Setter for uuid property."""
        self.logger.warn("Setting values on uuid will NOT update the remote Canvas instance.")
        self._uuid = value

    @property
    def parent_account_id(self):
        """The account's parent ID, or null if this is the root account."""
        return self._parent_account_id

    @parent_account_id.setter
    def parent_account_id(self, value):
        """Setter for parent_account_id property."""
        self.logger.warn("Setting values on parent_account_id will NOT update the remote Canvas instance.")
        self._parent_account_id = value

    @property
    def root_account_id(self):
        """The ID of the root account, or null if this is the root account."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn("Setting values on root_account_id will NOT update the remote Canvas instance.")
        self._root_account_id = value

    @property
    def default_storage_quota_mb(self):
        """The storage quota for the account in megabytes, if not otherwise specified."""
        return self._default_storage_quota_mb

    @default_storage_quota_mb.setter
    def default_storage_quota_mb(self, value):
        """Setter for default_storage_quota_mb property."""
        self.logger.warn("Setting values on default_storage_quota_mb will NOT update the remote Canvas instance.")
        self._default_storage_quota_mb = value

    @property
    def default_user_storage_quota_mb(self):
        """The storage quota for a user in the account in megabytes, if not otherwise specified."""
        return self._default_user_storage_quota_mb

    @default_user_storage_quota_mb.setter
    def default_user_storage_quota_mb(self, value):
        """Setter for default_user_storage_quota_mb property."""
        self.logger.warn("Setting values on default_user_storage_quota_mb will NOT update the remote Canvas instance.")
        self._default_user_storage_quota_mb = value

    @property
    def default_group_storage_quota_mb(self):
        """The storage quota for a group in the account in megabytes, if not otherwise specified."""
        return self._default_group_storage_quota_mb

    @default_group_storage_quota_mb.setter
    def default_group_storage_quota_mb(self, value):
        """Setter for default_group_storage_quota_mb property."""
        self.logger.warn("Setting values on default_group_storage_quota_mb will NOT update the remote Canvas instance.")
        self._default_group_storage_quota_mb = value

    @property
    def default_time_zone(self):
        """The default time zone of the account. Allowed time zones are {http://www.iana.org/time-zones IANA time zones} or friendlier {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}."""
        return self._default_time_zone

    @default_time_zone.setter
    def default_time_zone(self, value):
        """Setter for default_time_zone property."""
        self.logger.warn("Setting values on default_time_zone will NOT update the remote Canvas instance.")
        self._default_time_zone = value

    @property
    def sis_account_id(self):
        """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information."""
        return self._sis_account_id

    @sis_account_id.setter
    def sis_account_id(self, value):
        """Setter for sis_account_id property."""
        self.logger.warn("Setting values on sis_account_id will NOT update the remote Canvas instance.")
        self._sis_account_id = value

    @property
    def integration_id(self):
        """The account's identifier in the Student Information System. Only included if the user has permission to view SIS information."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn("Setting values on integration_id will NOT update the remote Canvas instance.")
        self._integration_id = value

    @property
    def sis_import_id(self):
        """The id of the SIS import if created through SIS. Only included if the user has permission to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn("Setting values on sis_import_id will NOT update the remote Canvas instance.")
        self._sis_import_id = value

    @property
    def lti_guid(self):
        """The account's identifier that is sent as context_id in LTI launches."""
        return self._lti_guid

    @lti_guid.setter
    def lti_guid(self, value):
        """Setter for lti_guid property."""
        self.logger.warn("Setting values on lti_guid will NOT update the remote Canvas instance.")
        self._lti_guid = value

    @property
    def workflow_state(self):
        """The state of the account. Can be 'active' or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value


class Termsofservice(BaseModel):
    """Termsofservice Model."""

    def __init__(self, id=None, terms_type=None, passive=None, account_id=None, content=None, self_registration_type=None):
        """Init method for Termsofservice class."""
        self._id = id
        self._terms_type = terms_type
        self._passive = passive
        self._account_id = account_id
        self._content = content
        self._self_registration_type = self_registration_type

        self.logger = logging.getLogger('py3canvas.Termsofservice')

    @property
    def id(self):
        """Terms Of Service id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def terms_type(self):
        """The given type for the Terms of Service."""
        return self._terms_type

    @terms_type.setter
    def terms_type(self, value):
        """Setter for terms_type property."""
        self.logger.warn("Setting values on terms_type will NOT update the remote Canvas instance.")
        self._terms_type = value

    @property
    def passive(self):
        """Boolean dictating if the user must accept Terms of Service."""
        return self._passive

    @passive.setter
    def passive(self, value):
        """Setter for passive property."""
        self.logger.warn("Setting values on passive will NOT update the remote Canvas instance.")
        self._passive = value

    @property
    def account_id(self):
        """The id of the root account that owns the Terms of Service."""
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        """Setter for account_id property."""
        self.logger.warn("Setting values on account_id will NOT update the remote Canvas instance.")
        self._account_id = value

    @property
    def content(self):
        """Content of the Terms of Service."""
        return self._content

    @content.setter
    def content(self, value):
        """Setter for content property."""
        self.logger.warn("Setting values on content will NOT update the remote Canvas instance.")
        self._content = value

    @property
    def self_registration_type(self):
        """The type of self registration allowed."""
        return self._self_registration_type

    @self_registration_type.setter
    def self_registration_type(self, value):
        """Setter for self_registration_type property."""
        self.logger.warn("Setting values on self_registration_type will NOT update the remote Canvas instance.")
        self._self_registration_type = value


class Helplink(BaseModel):
    """Helplink Model."""

    def __init__(self, id=None, text=None, subtext=None, url=None, type=None, available_to=None):
        """Init method for Helplink class."""
        self._id = id
        self._text = text
        self._subtext = subtext
        self._url = url
        self._type = type
        self._available_to = available_to

        self.logger = logging.getLogger('py3canvas.Helplink')

    @property
    def id(self):
        """The ID of the help link."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def text(self):
        """The name of the help link."""
        return self._text

    @text.setter
    def text(self, value):
        """Setter for text property."""
        self.logger.warn("Setting values on text will NOT update the remote Canvas instance.")
        self._text = value

    @property
    def subtext(self):
        """The description of the help link."""
        return self._subtext

    @subtext.setter
    def subtext(self, value):
        """Setter for subtext property."""
        self.logger.warn("Setting values on subtext will NOT update the remote Canvas instance.")
        self._subtext = value

    @property
    def url(self):
        """The URL of the help link."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def type(self):
        """The type of the help link."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def available_to(self):
        """The roles that have access to this help link."""
        return self._available_to

    @available_to.setter
    def available_to(self, value):
        """Setter for available_to property."""
        self.logger.warn("Setting values on available_to will NOT update the remote Canvas instance.")
        self._available_to = value


class Helplinks(BaseModel):
    """Helplinks Model."""

    def __init__(self, help_link_name=None, help_link_icon=None, custom_help_links=None, default_help_links=None):
        """Init method for Helplinks class."""
        self._help_link_name = help_link_name
        self._help_link_icon = help_link_icon
        self._custom_help_links = custom_help_links
        self._default_help_links = default_help_links

        self.logger = logging.getLogger('py3canvas.Helplinks')

    @property
    def help_link_name(self):
        """Help link button title."""
        return self._help_link_name

    @help_link_name.setter
    def help_link_name(self, value):
        """Setter for help_link_name property."""
        self.logger.warn("Setting values on help_link_name will NOT update the remote Canvas instance.")
        self._help_link_name = value

    @property
    def help_link_icon(self):
        """Help link button icon."""
        return self._help_link_icon

    @help_link_icon.setter
    def help_link_icon(self, value):
        """Setter for help_link_icon property."""
        self.logger.warn("Setting values on help_link_icon will NOT update the remote Canvas instance.")
        self._help_link_icon = value

    @property
    def custom_help_links(self):
        """Help links defined by the account. Could include default help links."""
        return self._custom_help_links

    @custom_help_links.setter
    def custom_help_links(self, value):
        """Setter for custom_help_links property."""
        self.logger.warn("Setting values on custom_help_links will NOT update the remote Canvas instance.")
        self._custom_help_links = value

    @property
    def default_help_links(self):
        """Default help links provided when account has not set help links of their own."""
        return self._default_help_links

    @default_help_links.setter
    def default_help_links(self, value):
        """Setter for default_help_links property."""
        self.logger.warn("Setting values on default_help_links will NOT update the remote Canvas instance.")
        self._default_help_links = value

