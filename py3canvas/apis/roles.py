"""Roles API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class RolesAPI(BaseCanvasAPI):
    """Roles API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for RolesAPI."""
        super(RolesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.RolesAPI")

    def list_roles(self, account_id, show_inherited=None, state=None):
        """
        List roles.

        A paginated list of the roles available to an account.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            The id of the account to retrieve roles for.
        """
        path["account_id"] = account_id


        # OPTIONAL - state
        """
            Filter by role state. If this argument is omitted, only 'active' roles are
        returned.
        """
        if state is not None:
            self._validate_enum(state, ["active", "inactive"])
            params["state"] = state


        # OPTIONAL - show_inherited
        """
            If this argument is true, all roles inherited from parent accounts will
        be included.
        """
        if show_inherited is not None:
            params["show_inherited"] = show_inherited


        self.logger.debug("GET /api/v1/accounts/{account_id}/roles with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/roles".format(**path), data=data, params=params, all_pages=True)

    def get_single_role(self, account_id, id, role_id, role=None):
        """
        Get a single role.

        Retrieve information about a single role
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # REQUIRED - PATH - account_id
        """
            The id of the account containing the role
        """
        path["account_id"] = account_id


        # REQUIRED - role_id
        """
            The unique identifier for the role
        """
        params["role_id"] = role_id


        # OPTIONAL - role
        """
            The name for the role
        """
        if role is not None:
            params["role"] = role


        self.logger.debug("GET /api/v1/accounts/{account_id}/roles/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/roles/{id}".format(**path), data=data, params=params, single_item=True)

    def create_new_role(self, account_id, label, base_role_type=None, permissions_<X>_applies_to_descendants=None, permissions_<X>_applies_to_self=None, permissions_<X>_enabled=None, permissions_<X>_explicit=None, permissions_<X>_locked=None, role=None):
        """
        Create a new role.

        Create a new course-level or account-level role.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - label
        """
            Label for the role.
        """
        data["label"] = label


        # OPTIONAL - role
        """
            Deprecated alias for label.
        """
        if role is not None:
            data["role"] = role


        # OPTIONAL - base_role_type
        """
            Specifies the role type that will be used as a base
        for the permissions granted to this role.

        Defaults to 'AccountMembership' if absent
        """
        if base_role_type is not None:
            self._validate_enum(base_role_type, ["AccountMembership", "StudentEnrollment", "TeacherEnrollment", "TaEnrollment", "ObserverEnrollment", "DesignerEnrollment"])
            data["base_role_type"] = base_role_type


        # OPTIONAL - permissions[<X>][explicit]
        """
            no description
        """
        if permissions_<X>_explicit is not None:
            data["permissions[<X>][explicit]"] = permissions_<X>_explicit


        # OPTIONAL - permissions[<X>][enabled]
        """
            If explicit is 1 and enabled is 1, permission <X> will be explicitly
        granted to this role. If explicit is 1 and enabled has any other value
        (typically 0), permission <X> will be explicitly denied to this role. If
        explicit is any other value (typically 0) or absent, or if enabled is
        absent, the value for permission <X> will be inherited from upstream.
        Ignored if permission <X> is locked upstream (in an ancestor account).

        May occur multiple times with unique values for <X>. Recognized
        permission names for <X> are:

          [For Account-Level Roles Only]
          become_user                      -- Users - act as
          import_sis                       -- SIS Data - import
          manage_account_memberships       -- Admins - add / remove
          manage_account_settings          -- Account-level settings - manage
          manage_alerts                    -- Global announcements - add / edit / delete
          manage_catalog                   -- Catalog - manage
          Manage Course Templates granular permissions
              add_course_template          -- Course Templates - add
              delete_course_template       -- Course Templates - delete
              edit_course_template         -- Course Templates - edit
          manage_courses_add               -- Courses - add
          manage_courses_admin             -- Courses - manage / update
          manage_developer_keys            -- Developer keys - manage
          manage_feature_flags             -- Feature Previews - enable / disable
          manage_master_courses            -- Blueprint Courses - add / edit / associate / delete
          manage_role_overrides            -- Permissions - manage
          manage_storage_quotas            -- Storage Quotas - manage
          manage_sis                       -- SIS data - manage
          manage_user_logins               -- Users - manage login details
          manage_user_observers            -- Users - manage observers
          moderate_user_content            -- Users - moderate content
          read_course_content              -- Course Content - view
          read_course_list                 -- Courses - view list
          view_course_changes              -- Courses - view change logs
          view_feature_flags               -- Feature Previews - view
          view_grade_changes               -- Grades - view change logs
          view_notifications               -- Notifications - view
          view_quiz_answer_audits          -- Quizzes - view submission log
          view_statistics                  -- Statistics - view
          undelete_courses                 -- Courses - undelete

          [For both Account-Level and Course-Level roles]
           Note: Applicable enrollment types for course-level roles are given in brackets:
                 S = student, T = teacher (instructor), A = TA, D = designer, O = observer.
                 Lower-case letters indicate permissions that are off by default.
                 A missing letter indicates the permission cannot be enabled for the role
                 or any derived custom roles.
          allow_course_admin_actions       -- [ Tad ] Users - allow administrative actions in courses
          create_collaborations            -- [STADo] Student Collaborations - create
          create_conferences               -- [STADo] Web conferences - create
          create_forum                     -- [STADo] Discussions - create
          generate_observer_pairing_code   -- [ tado] Users - Generate observer pairing codes for students
          import_outcomes                  -- [ TaDo] Learning Outcomes - import
          lti_add_edit                     -- [ TAD ] LTI - add / edit / delete
          manage_account_banks             -- [ td  ] Item Banks - manage account
          manage_assignments               -- [ TADo] Assignments and Quizzes - add / edit / delete (deprecated)
          Manage Assignments and Quizzes granular permissions
              manage_assignments_add       -- [ TADo] Assignments and Quizzes - add
              manage_assignments_edit      -- [ TADo] Assignments and Quizzes - edit / manage
              manage_assignments_delete    -- [ TADo] Assignments and Quizzes - delete
          manage_calendar                  -- [sTADo] Course Calendar - add / edit / delete
          manage_content                   -- [ TADo] Course Content - add / edit / delete
          manage_course_visibility         -- [ TAD ] Course - change visibility
          Manage Courses granular permissions
              manage_courses_conclude      -- [ TaD ] Courses - conclude
              manage_courses_delete        -- [ TaD ] Courses - delete
              manage_courses_publish       -- [ TaD ] Courses - publish
              manage_courses_reset         -- [ TaD ] Courses - reset
          Manage Files granular permissions
              manage_files_add             -- [ TADo] Course Files - add
              manage_files_edit            -- [ TADo] Course Files - edit
              manage_files_delete          -- [ TADo] Course Files - delete
          manage_grades                    -- [ TA  ] Grades - edit
          Manage Groups granular permissions
              manage_groups_add            -- [ TAD ] Groups - add
              manage_groups_delete         -- [ TAD ] Groups - delete
              manage_groups_manage         -- [ TAD ] Groups - manage
          manage_interaction_alerts        -- [ Ta  ] Alerts - add / edit / delete
          manage_outcomes                  -- [sTaDo] Learning Outcomes - add / edit / delete
          manage_proficiency_calculations  -- [ t d ] Outcome Proficiency Calculations - add / edit / delete
          manage_proficiency_scales        -- [ t d ] Outcome Proficiency/Mastery Scales - add / edit / delete
          Manage Sections granular permissions
              manage_sections_add          -- [ TaD ] Course Sections - add
              manage_sections_edit         -- [ TaD ] Course Sections - edit
              manage_sections_delete       -- [ TaD ] Course Sections - delete
          manage_students                  -- [ TAD ] Users - manage students in courses
          manage_user_notes                -- [ TA  ] Faculty Journal - manage entries
          manage_rubrics                   -- [ TAD ] Rubrics - add / edit / delete
          Manage Pages granular permissions
              manage_wiki_create           -- [ TADo] Pages - create
              manage_wiki_delete           -- [ TADo] Pages - delete
              manage_wiki_update           -- [ TADo] Pages - update
          moderate_forum                   -- [sTADo] Discussions - moderate
          post_to_forum                    -- [STADo] Discussions - post
          read_announcements               -- [STADO] Announcements - view
          read_email_addresses             -- [sTAdo] Users - view primary email address
          read_forum                       -- [STADO] Discussions - view
          read_question_banks              -- [ TADo] Question banks - view and link
          read_reports                     -- [ TAD ] Courses - view usage reports
          read_roster                      -- [STADo] Users - view list
          read_sis                         -- [sTa  ] SIS Data - read
          select_final_grade               -- [ TA  ] Grades - select final grade for moderation
          send_messages                    -- [STADo] Conversations - send messages to individual course members
          send_messages_all                -- [sTADo] Conversations - send messages to entire class
          Users - Teacher granular permissions
              add_teacher_to_course        -- [ Tad ] Add a teacher enrollment to a course
              remove_teacher_from_course   -- [ Tad ] Remove a Teacher enrollment from a course
          Users - TA granular permissions
              add_ta_to_course             -- [ Tad ] Add a TA enrollment to a course
              remove_ta_from_course        -- [ Tad ] Remove a TA enrollment from a course
          Users - Designer granular permissions
              add_designer_to_course       -- [ Tad ] Add a designer enrollment to a course
              remove_designer_from_course  -- [ Tad ] Remove a designer enrollment from a course
          Users - Observer granular permissions
              add_observer_to_course       -- [ Tad ] Add an observer enrollment to a course
              remove_observer_from_course  -- [ Tad ] Remove an observer enrollment from a course
          Users - Student granular permissions
              add_student_to_course        -- [ Tad ] Add a student enrollment to a course
              remove_student_from_course   -- [ Tad ] Remove a student enrollment from a course
          view_all_grades                  -- [ TAd ] Grades - view all grades
          view_analytics                   -- [sTA  ] Analytics - view pages
          view_audit_trail                 -- [ t   ] Grades - view audit trail
          view_group_pages                 -- [sTADo] Groups - view all student groups
          view_user_logins                 -- [ TA  ] Users - view login IDs

        Some of these permissions are applicable only for roles on the site admin
        account, on a root account, or for course-level roles with a particular base role type;
        if a specified permission is inapplicable, it will be ignored.

        Additional permissions may exist based on installed plugins.

        A comprehensive list of all permissions are available:

        Course Permissions PDF: http://bit.ly/cnvs-course-permissions

        Account Permissions PDF: http://bit.ly/cnvs-acct-permissions
        """
        if permissions_<X>_enabled is not None:
            data["permissions[<X>][enabled]"] = permissions_<X>_enabled


        # OPTIONAL - permissions[<X>][locked]
        """
            If the value is 1, permission <X> will be locked downstream (new roles in
        subaccounts cannot override the setting). For any other value, permission
        <X> is left unlocked. Ignored if permission <X> is already locked
        upstream. May occur multiple times with unique values for <X>.
        """
        if permissions_<X>_locked is not None:
            data["permissions[<X>][locked]"] = permissions_<X>_locked


        # OPTIONAL - permissions[<X>][applies_to_self]
        """
            If the value is 1, permission <X> applies to the account this role is in.
        The default value is 1. Must be true if applies_to_descendants is false.
        This value is only returned if enabled is true.
        """
        if permissions_<X>_applies_to_self is not None:
            data["permissions[<X>][applies_to_self]"] = permissions_<X>_applies_to_self


        # OPTIONAL - permissions[<X>][applies_to_descendants]
        """
            If the value is 1, permission <X> cascades down to sub accounts of the
        account this role is in. The default value is 1.  Must be true if
        applies_to_self is false.This value is only returned if enabled is true.
        """
        if permissions_<X>_applies_to_descendants is not None:
            data["permissions[<X>][applies_to_descendants]"] = permissions_<X>_applies_to_descendants


        self.logger.debug("POST /api/v1/accounts/{account_id}/roles with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/roles".format(**path), data=data, params=params, single_item=True)

    def deactivate_role(self, account_id, id, role_id, role=None):
        """
        Deactivate a role.

        Deactivates a custom role.  This hides it in the user interface and prevents it
        from being assigned to new users.  Existing users assigned to the role will
        continue to function with the same permissions they had previously.
        Built-in roles cannot be deactivated.
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


        # REQUIRED - role_id
        """
            The unique identifier for the role
        """
        params["role_id"] = role_id


        # OPTIONAL - role
        """
            The name for the role
        """
        if role is not None:
            params["role"] = role


        self.logger.debug("DELETE /api/v1/accounts/{account_id}/roles/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/accounts/{account_id}/roles/{id}".format(**path), data=data, params=params, single_item=True)

    def activate_role(self, account_id, id, role_id, role=None):
        """
        Activate a role.

        Re-activates an inactive role (allowing it to be assigned to new users)
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


        # REQUIRED - role_id
        """
            The unique identifier for the role
        """
        data["role_id"] = role_id


        # OPTIONAL - role
        """
            The name for the role
        """
        if role is not None:
            data["role"] = role


        self.logger.debug("POST /api/v1/accounts/{account_id}/roles/{id}/activate with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/roles/{id}/activate".format(**path), data=data, params=params, single_item=True)

    def update_role(self, account_id, id, label=None, permissions_<X>_applies_to_descendants=None, permissions_<X>_applies_to_self=None, permissions_<X>_enabled=None, permissions_<X>_explicit=None):
        """
        Update a role.

        Update permissions for an existing role.
        
        Recognized roles are:
        * TeacherEnrollment
        * StudentEnrollment
        * TaEnrollment
        * ObserverEnrollment
        * DesignerEnrollment
        * AccountAdmin
        * Any previously created custom role
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


        # OPTIONAL - label
        """
            The label for the role. Can only change the label of a custom role that belongs directly to the account.
        """
        if label is not None:
            data["label"] = label


        # OPTIONAL - permissions[<X>][explicit]
        """
            no description
        """
        if permissions_<X>_explicit is not None:
            data["permissions[<X>][explicit]"] = permissions_<X>_explicit


        # OPTIONAL - permissions[<X>][enabled]
        """
            These arguments are described in the documentation for the
        {api:RoleOverridesController#add_role add_role method}.
        """
        if permissions_<X>_enabled is not None:
            data["permissions[<X>][enabled]"] = permissions_<X>_enabled


        # OPTIONAL - permissions[<X>][applies_to_self]
        """
            If the value is 1, permission <X> applies to the account this role is in.
        The default value is 1. Must be true if applies_to_descendants is false.
        This value is only returned if enabled is true.
        """
        if permissions_<X>_applies_to_self is not None:
            data["permissions[<X>][applies_to_self]"] = permissions_<X>_applies_to_self


        # OPTIONAL - permissions[<X>][applies_to_descendants]
        """
            If the value is 1, permission <X> cascades down to sub accounts of the
        account this role is in. The default value is 1.  Must be true if
        applies_to_self is false.This value is only returned if enabled is true.
        """
        if permissions_<X>_applies_to_descendants is not None:
            data["permissions[<X>][applies_to_descendants]"] = permissions_<X>_applies_to_descendants


        self.logger.debug("PUT /api/v1/accounts/{account_id}/roles/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/roles/{id}".format(**path), data=data, params=params, single_item=True)


class Rolepermissions(BaseModel):
    """Rolepermissions Model."""

    def __init__(self, enabled=None, locked=False, applies_to_self=True, applies_to_descendants=True, readonly=False, explicit=False, prior_default=None):
        """Init method for Rolepermissions class."""
        self._enabled = enabled
        self._locked = locked
        self._applies_to_self = applies_to_self
        self._applies_to_descendants = applies_to_descendants
        self._readonly = readonly
        self._explicit = explicit
        self._prior_default = prior_default

        self.logger = logging.getLogger('py3canvas.Rolepermissions')

    @property
    def enabled(self):
        """Whether the role has the permission."""
        return self._enabled

    @enabled.setter
    def enabled(self, value):
        """Setter for enabled property."""
        self.logger.warn("Setting values on enabled will NOT update the remote Canvas instance.")
        self._enabled = value

    @property
    def locked(self):
        """Whether the permission is locked by this role."""
        return self._locked

    @locked.setter
    def locked(self, value):
        """Setter for locked property."""
        self.logger.warn("Setting values on locked will NOT update the remote Canvas instance.")
        self._locked = value

    @property
    def applies_to_self(self):
        """Whether the permission applies to the account this role is in. Only present if enabled is true."""
        return self._applies_to_self

    @applies_to_self.setter
    def applies_to_self(self, value):
        """Setter for applies_to_self property."""
        self.logger.warn("Setting values on applies_to_self will NOT update the remote Canvas instance.")
        self._applies_to_self = value

    @property
    def applies_to_descendants(self):
        """Whether the permission cascades down to sub accounts of the account this role is in. Only present if enabled is true."""
        return self._applies_to_descendants

    @applies_to_descendants.setter
    def applies_to_descendants(self, value):
        """Setter for applies_to_descendants property."""
        self.logger.warn("Setting values on applies_to_descendants will NOT update the remote Canvas instance.")
        self._applies_to_descendants = value

    @property
    def readonly(self):
        """Whether the permission can be modified in this role (i.e. whether the permission is locked by an upstream role)."""
        return self._readonly

    @readonly.setter
    def readonly(self, value):
        """Setter for readonly property."""
        self.logger.warn("Setting values on readonly will NOT update the remote Canvas instance.")
        self._readonly = value

    @property
    def explicit(self):
        """Whether the value of enabled is specified explicitly by this role, or inherited from an upstream role."""
        return self._explicit

    @explicit.setter
    def explicit(self, value):
        """Setter for explicit property."""
        self.logger.warn("Setting values on explicit will NOT update the remote Canvas instance.")
        self._explicit = value

    @property
    def prior_default(self):
        """The value that would have been inherited from upstream if the role had not explicitly set a value. Only present if explicit is true."""
        return self._prior_default

    @prior_default.setter
    def prior_default(self, value):
        """Setter for prior_default property."""
        self.logger.warn("Setting values on prior_default will NOT update the remote Canvas instance.")
        self._prior_default = value


class Role(BaseModel):
    """Role Model."""

    def __init__(self, label=None, role=None, base_role_type=None, account=None, workflow_state=None, permissions=None):
        """Init method for Role class."""
        self._label = label
        self._role = role
        self._base_role_type = base_role_type
        self._account = account
        self._workflow_state = workflow_state
        self._permissions = permissions

        self.logger = logging.getLogger('py3canvas.Role')

    @property
    def label(self):
        """The label of the role."""
        return self._label

    @label.setter
    def label(self, value):
        """Setter for label property."""
        self.logger.warn("Setting values on label will NOT update the remote Canvas instance.")
        self._label = value

    @property
    def role(self):
        """The label of the role. (Deprecated alias for 'label')."""
        return self._role

    @role.setter
    def role(self, value):
        """Setter for role property."""
        self.logger.warn("Setting values on role will NOT update the remote Canvas instance.")
        self._role = value

    @property
    def base_role_type(self):
        """The role type that is being used as a base for this role. For account-level roles, this is 'AccountMembership'. For course-level roles, it is an enrollment type."""
        return self._base_role_type

    @base_role_type.setter
    def base_role_type(self, value):
        """Setter for base_role_type property."""
        self.logger.warn("Setting values on base_role_type will NOT update the remote Canvas instance.")
        self._base_role_type = value

    @property
    def account(self):
        """JSON representation of the account the role is in."""
        return self._account

    @account.setter
    def account(self, value):
        """Setter for account property."""
        self.logger.warn("Setting values on account will NOT update the remote Canvas instance.")
        self._account = value

    @property
    def workflow_state(self):
        """The state of the role: 'active', 'inactive', or 'built_in'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def permissions(self):
        """A dictionary of permissions keyed by name (see permissions input parameter in the 'Create a role' API)."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn("Setting values on permissions will NOT update the remote Canvas instance.")
        self._permissions = value

