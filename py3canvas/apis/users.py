"""Users API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class UsersAPI(BaseCanvasAPI):
    """Users API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for UsersAPI."""
        super(UsersAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.UsersAPI")

    def list_users_in_account(
        self, account_id, enrollment_type=None, order=None, search_term=None, sort=None
    ):
        """
        List users in account.

        A paginated list of of users associated with this account.
        
         @example_request
           curl https://<canvas>/api/v1/accounts/self/users?search_term=<search value> \
              -X GET \
              -H 'Authorization: Bearer <token>'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - search_term
        """
            The partial name or full ID of the users to match and return in the
        results list. Must be at least 3 characters.

        Note that the API will prefer matching on canonical user ID if the ID has
        a numeric form. It will only search against other fields if non-numeric
        in form, or if the numeric value doesn't yield any matches. Queries by
        administrative users will search on SIS ID, login ID, name, or email
        address
        """
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - enrollment_type
        """
            When set, only return users enrolled with the specified course-level base role.
        This can be a base role type of 'student', 'teacher',
        'ta', 'observer', or 'designer'.
        """
        if enrollment_type is not None:
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - sort
        """
            The column to sort results by.
        """
        if sort is not None:
            self._validate_enum(sort, ["username", "email", "sis_id", "last_login"])
            params["sort"] = sort

        # OPTIONAL - order
        """
            The order to sort the given column by.
        """
        if order is not None:
            self._validate_enum(order, ["asc", "desc"])
            params["order"] = order

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/users with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/users".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_activity_stream_self(self, only_active_courses=None):
        """
        List the activity stream.

        Returns the current user's global activity stream, paginated.

        There are many types of objects that can be returned in the activity
        stream. All object types have the same basic set of shared attributes:
          !!!javascript
          {
            'created_at': '2011-07-13T09:12:00Z',
            'updated_at': '2011-07-25T08:52:41Z',
            'id': 1234,
            'title': 'Stream Item Subject',
            'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
            'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
            'read_state': false,
            'context_type': 'course', // course|group
            'course_id': 1,
            'group_id': null,
            'html_url': "http://..." // URL to the Canvas web UI for this stream item
          }

        In addition, each item type has its own set of attributes available.

        DiscussionTopic:

          !!!javascript
          {
            'type': 'DiscussionTopic',
            'discussion_topic_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': true,
            'root_discussion_entries': {
              ...
            }
          }

        For DiscussionTopic, the message is truncated at 4kb.

        Announcement:

          !!!javascript
          {
            'type': 'Announcement',
            'announcement_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': null,
            'root_discussion_entries': {
              ...
            }
          }

        For Announcement, the message is truncated at 4kb.

        Conversation:

          !!!javascript
          {
            'type': 'Conversation',
            'conversation_id': 1234,
            'private': false,
            'participant_count': 3,
          }

        Message:

          !!!javascript
          {
            'type': 'Message',
            'message_id': 1234,
            'notification_category': 'Assignment Graded'
          }

        Submission:

        Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.

        Conference:

          !!!javascript
          {
            'type': 'Conference',
            'web_conference_id': 1234
          }

        Collaboration:

          !!!javascript
          {
            'type': 'Collaboration',
            'collaboration_id': 1234
          }

        AssessmentRequest:

          !!!javascript
          {
            'type': 'AssessmentRequest',
            'assessment_request_id': 1234
          }
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - only_active_courses
        """
            If true, will only return objects for courses the user is actively participating in
        """
        if only_active_courses is not None:
            params["only_active_courses"] = only_active_courses

        self.logger.debug(
            "GET /api/v1/users/self/activity_stream with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/activity_stream".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_activity_stream_activity_stream(self, only_active_courses=None):
        """
        List the activity stream.

        Returns the current user's global activity stream, paginated.

        There are many types of objects that can be returned in the activity
        stream. All object types have the same basic set of shared attributes:
          !!!javascript
          {
            'created_at': '2011-07-13T09:12:00Z',
            'updated_at': '2011-07-25T08:52:41Z',
            'id': 1234,
            'title': 'Stream Item Subject',
            'message': 'This is the body text of the activity stream item. It is plain-text, and can be multiple paragraphs.',
            'type': 'DiscussionTopic|Conversation|Message|Submission|Conference|Collaboration|AssessmentRequest...',
            'read_state': false,
            'context_type': 'course', // course|group
            'course_id': 1,
            'group_id': null,
            'html_url': "http://..." // URL to the Canvas web UI for this stream item
          }

        In addition, each item type has its own set of attributes available.

        DiscussionTopic:

          !!!javascript
          {
            'type': 'DiscussionTopic',
            'discussion_topic_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': true,
            'root_discussion_entries': {
              ...
            }
          }

        For DiscussionTopic, the message is truncated at 4kb.

        Announcement:

          !!!javascript
          {
            'type': 'Announcement',
            'announcement_id': 1234,
            'total_root_discussion_entries': 5,
            'require_initial_post': true,
            'user_has_posted': null,
            'root_discussion_entries': {
              ...
            }
          }

        For Announcement, the message is truncated at 4kb.

        Conversation:

          !!!javascript
          {
            'type': 'Conversation',
            'conversation_id': 1234,
            'private': false,
            'participant_count': 3,
          }

        Message:

          !!!javascript
          {
            'type': 'Message',
            'message_id': 1234,
            'notification_category': 'Assignment Graded'
          }

        Submission:

        Returns an {api:Submissions:Submission Submission} with its Course and Assignment data.

        Conference:

          !!!javascript
          {
            'type': 'Conference',
            'web_conference_id': 1234
          }

        Collaboration:

          !!!javascript
          {
            'type': 'Collaboration',
            'collaboration_id': 1234
          }

        AssessmentRequest:

          !!!javascript
          {
            'type': 'AssessmentRequest',
            'assessment_request_id': 1234
          }
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - only_active_courses
        """
            If true, will only return objects for courses the user is actively participating in
        """
        if only_active_courses is not None:
            params["only_active_courses"] = only_active_courses

        self.logger.debug(
            "GET /api/v1/users/activity_stream with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/activity_stream".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def activity_stream_summary(self):
        """
        Activity stream summary.

        Returns a summary of the current user's global activity stream.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/users/self/activity_stream/summary with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/activity_stream/summary".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_todo_items(self, include=None):
        """
        List the TODO items.

        A paginated list of the current user's list of todo items.

        There is a limit to the number of items returned.

        The `ignore` and `ignore_permanently` URLs can be used to update the user's
        preferences on what items will be displayed.
        Performing a DELETE request against the `ignore` URL will hide that item
        from future todo item requests, until the item changes.
        Performing a DELETE request against the `ignore_permanently` URL will hide
        that item forever.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - include
        """
            "ungraded_quizzes":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.
                             These will be returned under a +quiz+ key instead of an +assignment+ key in response elements.
        """
        if include is not None:
            self._validate_enum(include, ["ungraded_quizzes"])
            params["include"] = include

        self.logger.debug(
            "GET /api/v1/users/self/todo with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/todo".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_counts_for_todo_items(self, include=None):
        """
        List counts for todo items.

        Counts of different todo items such as the number of assignments needing grading as well as the number of assignments needing submitting.

        There is a limit to the number of todo items this endpoint will count.
        It will only look at the first 100 todo items for the user. If the user has more than 100 todo items this count may not be reliable.
        The largest reliable number for both counts is 100.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - include
        """
            "ungraded_quizzes":: Optionally include ungraded quizzes (such as practice quizzes and surveys) in the list.
                             These will be returned under a +quiz+ key instead of an +assignment+ key in response elements.
        """
        if include is not None:
            self._validate_enum(include, ["ungraded_quizzes"])
            params["include"] = include

        self.logger.debug(
            "GET /api/v1/users/self/todo_item_count with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/todo_item_count".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_upcoming_assignments_calendar_events(self):
        """
        List upcoming assignments, calendar events.

        A paginated list of the current user's upcoming events.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/users/self/upcoming_events with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/upcoming_events".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_missing_submissions(
        self, user_id, course_ids=None, filter=None, include=None
    ):
        """
        List Missing Submissions.

        A paginated list of past-due assignments for which the student does not have a submission.
        The user sending the request must either be the student, an admin or a parent observer using the parent app
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            the student's ID
        """
        path["user_id"] = user_id

        # OPTIONAL - include
        """
            "planner_overrides":: Optionally include the assignment's associated planner override, if it exists, for the current user.
                              These will be returned under a +planner_override+ key
        "course":: Optionally include the assignments' courses
        """
        if include is not None:
            self._validate_enum(include, ["planner_overrides", "course"])
            params["include"] = include

        # OPTIONAL - filter
        """
            "submittable":: Only return assignments that the current user can submit (i.e. filter out locked assignments)
        """
        if filter is not None:
            self._validate_enum(filter, ["submittable"])
            params["filter"] = filter

        # OPTIONAL - course_ids
        """
            Optionally restricts the list of past-due assignments to only those associated with the specified
        course IDs.
        """
        if course_ids is not None:
            params["course_ids"] = course_ids

        self.logger.debug(
            "GET /api/v1/users/{user_id}/missing_submissions with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/missing_submissions".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def hide_stream_item(self, id):
        """
        Hide a stream item.

        Hide the given stream item.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "DELETE /api/v1/users/self/activity_stream/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/users/self/activity_stream/{id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def hide_all_stream_items(self):
        """
        Hide all stream items.

        Hide all stream items for the user
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "DELETE /api/v1/users/self/activity_stream with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/users/self/activity_stream".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def upload_file(self, user_id):
        """
        Upload a file.

        Upload a file to the user's personal files section.

        This API endpoint is the first step in uploading a file to a user's files.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow.

        Note that typically users will only be able to upload files to their
        own files section. Passing a user_id of +self+ is an easy shortcut
        to specify the current user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        self.logger.debug(
            "POST /api/v1/users/{user_id}/files with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/users/{user_id}/files".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def show_user_details(self, id, include=None):
        """
        Show user details.

        Shows details for user.

        Also includes an attribute "permissions", a non-comprehensive list of permissions for the user.
        Example:
          !!!javascript
          "permissions": {
           "can_update_name": true, // Whether the user can update their name.
           "can_update_avatar": false, // Whether the user can update their avatar.
           "limit_parent_app_web_access": false // Whether the user can interact with Canvas web from the Canvas Parent app.
          }
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # OPTIONAL - include
        """
            Array of additional information to include on the user record.
        "locale", "avatar_url", "permissions", "email", and "effective_locale"
        will always be returned
        """
        if include is not None:
            self._validate_enum(include, ["uuid", "last_login"])
            params["include"] = include

        self.logger.debug(
            "GET /api/v1/users/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def create_user(
        self,
        account_id,
        pseudonym_unique_id,
        communication_channel_address=None,
        communication_channel_confirmation_url=None,
        communication_channel_skip_confirmation=None,
        communication_channel_type=None,
        destination=None,
        enable_sis_reactivation=None,
        force_validations=None,
        initial_enrollment_type=None,
        pairing_code_code=None,
        pseudonym_authentication_provider_id=None,
        pseudonym_force_self_registration=None,
        pseudonym_integration_id=None,
        pseudonym_password=None,
        pseudonym_send_confirmation=None,
        pseudonym_sis_user_id=None,
        user_locale=None,
        user_name=None,
        user_short_name=None,
        user_skip_registration=None,
        user_sortable_name=None,
        user_terms_of_use=None,
        user_time_zone=None,
    ):
        """
        Create a user.

        Create and return a new user and pseudonym for an account.

        [DEPRECATED (for self-registration only)] If you don't have the "Modify
        login details for users" permission, but self-registration is enabled
        on the account, you can still use this endpoint to register new users.
        Certain fields will be required, and others will be ignored (see below).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - user[name]
        """
            The full name of the user. This name will be used by teacher for grading.
        Required if this is a self-registration.
        """
        if user_name is not None:
            data["user[name]"] = user_name

        # OPTIONAL - user[short_name]
        """
            User's name as it will be displayed in discussions, messages, and comments.
        """
        if user_short_name is not None:
            data["user[short_name]"] = user_short_name

        # OPTIONAL - user[sortable_name]
        """
            User's name as used to sort alphabetically in lists.
        """
        if user_sortable_name is not None:
            data["user[sortable_name]"] = user_sortable_name

        # OPTIONAL - user[time_zone]
        """
            The time zone for the user. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        """
        if user_time_zone is not None:
            data["user[time_zone]"] = user_time_zone

        # OPTIONAL - user[locale]
        """
            The user's preferred language, from the list of languages Canvas supports.
        This is in RFC-5646 format.
        """
        if user_locale is not None:
            data["user[locale]"] = user_locale

        # OPTIONAL - user[terms_of_use]
        """
            Whether the user accepts the terms of use. Required if this is a
        self-registration and this canvas instance requires users to accept
        the terms (on by default).

        If this is true, it will mark the user as having accepted the terms of use.
        """
        if user_terms_of_use is not None:
            data["user[terms_of_use]"] = user_terms_of_use

        # OPTIONAL - user[skip_registration]
        """
            Automatically mark the user as registered.

        If this is true, it is recommended to set <tt>"pseudonym[send_confirmation]"</tt> to true as well.
        Otherwise, the user will not receive any messages about their account creation.

        The users communication channel confirmation can be skipped by setting
        <tt>"communication_channel[skip_confirmation]"</tt> to true as well.
        """
        if user_skip_registration is not None:
            data["user[skip_registration]"] = user_skip_registration

        # REQUIRED - pseudonym[unique_id]
        """
            User's login ID. If this is a self-registration, it must be a valid
        email address.
        """
        data["pseudonym[unique_id]"] = pseudonym_unique_id

        # OPTIONAL - pseudonym[password]
        """
            User's password. Cannot be set during self-registration.
        """
        if pseudonym_password is not None:
            data["pseudonym[password]"] = pseudonym_password

        # OPTIONAL - pseudonym[sis_user_id]
        """
            SIS ID for the user's account. To set this parameter, the caller must be
        able to manage SIS permissions.
        """
        if pseudonym_sis_user_id is not None:
            data["pseudonym[sis_user_id]"] = pseudonym_sis_user_id

        # OPTIONAL - pseudonym[integration_id]
        """
            Integration ID for the login. To set this parameter, the caller must be able to
        manage SIS permissions. The Integration ID is a secondary
        identifier useful for more complex SIS integrations.
        """
        if pseudonym_integration_id is not None:
            data["pseudonym[integration_id]"] = pseudonym_integration_id

        # OPTIONAL - pseudonym[send_confirmation]
        """
            Send user notification of account creation if true.
        Automatically set to true during self-registration.
        """
        if pseudonym_send_confirmation is not None:
            data["pseudonym[send_confirmation]"] = pseudonym_send_confirmation

        # OPTIONAL - pseudonym[force_self_registration]
        """
            Send user a self-registration style email if true.
        Setting it means the users will get a notification asking them
        to "complete the registration process" by clicking it, setting
        a password, and letting them in.  Will only be executed on
        if the user does not need admin approval.
        Defaults to false unless explicitly provided.
        """
        if pseudonym_force_self_registration is not None:
            data[
                "pseudonym[force_self_registration]"
            ] = pseudonym_force_self_registration

        # OPTIONAL - pseudonym[authentication_provider_id]
        """
            The authentication provider this login is associated with. Logins
        associated with a specific provider can only be used with that provider.
        Legacy providers (LDAP, CAS, SAML) will search for logins associated with
        them, or unassociated logins. New providers will only search for logins
        explicitly associated with them. This can be the integer ID of the
        provider, or the type of the provider (in which case, it will find the
        first matching provider).
        """
        if pseudonym_authentication_provider_id is not None:
            data[
                "pseudonym[authentication_provider_id]"
            ] = pseudonym_authentication_provider_id

        # OPTIONAL - communication_channel[type]
        """
            The communication channel type, e.g. 'email' or 'sms'.
        """
        if communication_channel_type is not None:
            data["communication_channel[type]"] = communication_channel_type

        # OPTIONAL - communication_channel[address]
        """
            The communication channel address, e.g. the user's email address.
        """
        if communication_channel_address is not None:
            data["communication_channel[address]"] = communication_channel_address

        # OPTIONAL - communication_channel[confirmation_url]
        """
            Only valid for account admins. If true, returns the new user account
        confirmation URL in the response.
        """
        if communication_channel_confirmation_url is not None:
            data[
                "communication_channel[confirmation_url]"
            ] = communication_channel_confirmation_url

        # OPTIONAL - communication_channel[skip_confirmation]
        """
            Only valid for site admins and account admins making requests; If true, the channel is
        automatically validated and no confirmation email or SMS is sent.
        Otherwise, the user must respond to a confirmation message to confirm the
        channel.

        If this is true, it is recommended to set <tt>"pseudonym[send_confirmation]"</tt> to true as well.
        Otherwise, the user will not receive any messages about their account creation.
        """
        if communication_channel_skip_confirmation is not None:
            data[
                "communication_channel[skip_confirmation]"
            ] = communication_channel_skip_confirmation

        # OPTIONAL - force_validations
        """
            If true, validations are performed on the newly created user (and their associated pseudonym)
        even if the request is made by a privileged user like an admin. When set to false,
        or not included in the request parameters, any newly created users are subject to
        validations unless the request is made by a user with a 'manage_user_logins' right.
        In which case, certain validations such as 'require_acceptance_of_terms' and
        'require_presence_of_name' are not enforced. Use this parameter to return helpful json
        errors while building users with an admin request.
        """
        if force_validations is not None:
            data["force_validations"] = force_validations

        # OPTIONAL - enable_sis_reactivation
        """
            When true, will first try to re-activate a deleted user with matching sis_user_id if possible.
        This is commonly done with user[skip_registration] and communication_channel[skip_confirmation]
        so that the default communication_channel is also restored.
        """
        if enable_sis_reactivation is not None:
            data["enable_sis_reactivation"] = enable_sis_reactivation

        # OPTIONAL - destination
        """
            If you're setting the password for the newly created user, you can provide this param
        with a valid URL pointing into this Canvas installation, and the response will include
        a destination field that's a URL that you can redirect a browser to and have the newly
        created user automatically logged in. The URL is only valid for a short time, and must
        match the domain this request is directed to, and be for a well-formed path that Canvas
        can recognize.
        """
        if destination is not None:
            data["destination"] = destination

        # OPTIONAL - initial_enrollment_type
        """
            `observer` if doing a self-registration with a pairing code. This allows setting the
        password during user creation.
        """
        if initial_enrollment_type is not None:
            data["initial_enrollment_type"] = initial_enrollment_type

        # OPTIONAL - pairing_code[code]
        """
            If provided and valid, will link the new user as an observer to the student's whose
        pairing code is given.
        """
        if pairing_code_code is not None:
            data["pairing_code[code]"] = pairing_code_code

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/users with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/users".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def deprecated_self_register_user(
        self,
        account_id,
        pseudonym_unique_id,
        user_name,
        user_terms_of_use,
        communication_channel_address=None,
        communication_channel_type=None,
        user_locale=None,
        user_short_name=None,
        user_sortable_name=None,
        user_time_zone=None,
    ):
        """
        [DEPRECATED] Self register a user.

        Self register and return a new user and pseudonym for an account.

        If self-registration is enabled on the account, you can use this
        endpoint to self register new users.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - user[name]
        """
            The full name of the user. This name will be used by teacher for grading.
        """
        data["user[name]"] = user_name

        # OPTIONAL - user[short_name]
        """
            User's name as it will be displayed in discussions, messages, and comments.
        """
        if user_short_name is not None:
            data["user[short_name]"] = user_short_name

        # OPTIONAL - user[sortable_name]
        """
            User's name as used to sort alphabetically in lists.
        """
        if user_sortable_name is not None:
            data["user[sortable_name]"] = user_sortable_name

        # OPTIONAL - user[time_zone]
        """
            The time zone for the user. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        """
        if user_time_zone is not None:
            data["user[time_zone]"] = user_time_zone

        # OPTIONAL - user[locale]
        """
            The user's preferred language, from the list of languages Canvas supports.
        This is in RFC-5646 format.
        """
        if user_locale is not None:
            data["user[locale]"] = user_locale

        # REQUIRED - user[terms_of_use]
        """
            Whether the user accepts the terms of use.
        """
        data["user[terms_of_use]"] = user_terms_of_use

        # REQUIRED - pseudonym[unique_id]
        """
            User's login ID. Must be a valid email address.
        """
        data["pseudonym[unique_id]"] = pseudonym_unique_id

        # OPTIONAL - communication_channel[type]
        """
            The communication channel type, e.g. 'email' or 'sms'.
        """
        if communication_channel_type is not None:
            data["communication_channel[type]"] = communication_channel_type

        # OPTIONAL - communication_channel[address]
        """
            The communication channel address, e.g. the user's email address.
        """
        if communication_channel_address is not None:
            data["communication_channel[address]"] = communication_channel_address

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/self_registration with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/self_registration".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_user_settings(
        self,
        id,
        collapse_global_nav=None,
        comment_library_suggestions_enabled=None,
        elementary_dashboard_disabled=None,
        hide_dashcard_color_overlays=None,
        manual_mark_as_read=None,
        release_notes_badge_disabled=None,
    ):
        """
        Update user settings.

        Update an existing user's settings.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # OPTIONAL - manual_mark_as_read
        """
            If true, require user to manually mark discussion posts as read (don't
        auto-mark as read).
        """
        if manual_mark_as_read is not None:
            params["manual_mark_as_read"] = manual_mark_as_read

        # OPTIONAL - release_notes_badge_disabled
        """
            If true, hide the badge for new release notes.
        """
        if release_notes_badge_disabled is not None:
            params["release_notes_badge_disabled"] = release_notes_badge_disabled

        # OPTIONAL - collapse_global_nav
        """
            If true, the user's page loads with the global navigation collapsed
        """
        if collapse_global_nav is not None:
            params["collapse_global_nav"] = collapse_global_nav

        # OPTIONAL - hide_dashcard_color_overlays
        """
            If true, images on course cards will be presented without being tinted
        to match the course color.
        """
        if hide_dashcard_color_overlays is not None:
            params["hide_dashcard_color_overlays"] = hide_dashcard_color_overlays

        # OPTIONAL - comment_library_suggestions_enabled
        """
            If true, suggestions within the comment library will be shown.
        """
        if comment_library_suggestions_enabled is not None:
            params[
                "comment_library_suggestions_enabled"
            ] = comment_library_suggestions_enabled

        # OPTIONAL - elementary_dashboard_disabled
        """
            If true, will display the user's preferred class Canvas dashboard
        view instead of the canvas for elementary view.
        """
        if elementary_dashboard_disabled is not None:
            params["elementary_dashboard_disabled"] = elementary_dashboard_disabled

        self.logger.debug(
            "GET /api/v1/users/{id}/settings with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{id}/settings".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_custom_colors(self, id):
        """
        Get custom colors.

        Returns all custom colors that have been saved for a user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/v1/users/{id}/colors with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{id}/colors".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_custom_color(self, asset_string, id):
        """
        Get custom color.

        Returns the custom colors that have been saved for a user for a given context.

        The asset_string parameter should be in the format 'context_id', for example
        'course_42'.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # REQUIRED - PATH - asset_string
        """
            ID
        """
        path["asset_string"] = asset_string

        self.logger.debug(
            "GET /api/v1/users/{id}/colors/{asset_string} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{id}/colors/{asset_string}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def update_custom_color(self, asset_string, id, hexcode=None):
        """
        Update custom color.

        Updates a custom color for a user for a given context.  This allows
        colors for the calendar and elsewhere to be customized on a user basis.

        The asset string parameter should be in the format 'context_id', for example
        'course_42'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # REQUIRED - PATH - asset_string
        """
            ID
        """
        path["asset_string"] = asset_string

        # OPTIONAL - hexcode
        """
            The hexcode of the color to set for the context, if you choose to pass the
        hexcode as a query parameter rather than in the request body you should
        NOT include the '#' unless you escape it first.
        """
        if hexcode is not None:
            data["hexcode"] = hexcode

        self.logger.debug(
            "PUT /api/v1/users/{id}/colors/{asset_string} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/{id}/colors/{asset_string}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_dashboard_positions(self, id):
        """
        Get dashboard positions.

        Returns all dashboard positions that have been saved for a user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/v1/users/{id}/dashboard_positions with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{id}/dashboard_positions".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def update_dashboard_positions(self, id):
        """
        Update dashboard positions.

        Updates the dashboard positions for a user for a given context.  This allows
        positions for the dashboard cards and elsewhere to be customized on a per
        user basis.

        The asset string parameter should be in the format 'context_id', for example
        'course_42'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "PUT /api/v1/users/{id}/dashboard_positions with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/{id}/dashboard_positions".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def edit_user(
        self,
        id,
        user_avatar_token=None,
        user_avatar_url=None,
        user_bio=None,
        user_email=None,
        user_event=None,
        user_locale=None,
        user_name=None,
        user_pronouns=None,
        user_short_name=None,
        user_sortable_name=None,
        user_time_zone=None,
        user_title=None,
    ):
        """
        Edit a user.

        Modify an existing user. To modify a user's login, see the documentation for logins.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # OPTIONAL - user[name]
        """
            The full name of the user. This name will be used by teacher for grading.
        """
        if user_name is not None:
            data["user[name]"] = user_name

        # OPTIONAL - user[short_name]
        """
            User's name as it will be displayed in discussions, messages, and comments.
        """
        if user_short_name is not None:
            data["user[short_name]"] = user_short_name

        # OPTIONAL - user[sortable_name]
        """
            User's name as used to sort alphabetically in lists.
        """
        if user_sortable_name is not None:
            data["user[sortable_name]"] = user_sortable_name

        # OPTIONAL - user[time_zone]
        """
            The time zone for the user. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        """
        if user_time_zone is not None:
            data["user[time_zone]"] = user_time_zone

        # OPTIONAL - user[email]
        """
            The default email address of the user.
        """
        if user_email is not None:
            data["user[email]"] = user_email

        # OPTIONAL - user[locale]
        """
            The user's preferred language, from the list of languages Canvas supports.
        This is in RFC-5646 format.
        """
        if user_locale is not None:
            data["user[locale]"] = user_locale

        # OPTIONAL - user[avatar][token]
        """
            A unique representation of the avatar record to assign as the user's
        current avatar. This token can be obtained from the user avatars endpoint.
        This supersedes the user [avatar] [url] argument, and if both are included
        the url will be ignored. Note: this is an internal representation and is
        subject to change without notice. It should be consumed with this api
        endpoint and used in the user update endpoint, and should not be
        constructed by the client.
        """
        if user_avatar_token is not None:
            data["user[avatar][token]"] = user_avatar_token

        # OPTIONAL - user[avatar][url]
        """
            To set the user's avatar to point to an external url, do not include a
        token and instead pass the url here. Warning: For maximum compatibility,
        please use 128 px square images.
        """
        if user_avatar_url is not None:
            data["user[avatar][url]"] = user_avatar_url

        # OPTIONAL - user[title]
        """
            Sets a title on the user profile. (See {api:ProfileController#settings Get user profile}.)
        Profiles must be enabled on the root account.
        """
        if user_title is not None:
            data["user[title]"] = user_title

        # OPTIONAL - user[bio]
        """
            Sets a bio on the user profile. (See {api:ProfileController#settings Get user profile}.)
        Profiles must be enabled on the root account.
        """
        if user_bio is not None:
            data["user[bio]"] = user_bio

        # OPTIONAL - user[pronouns]
        """
            Sets pronouns on the user profile.
        Passing an empty string will empty the user's pronouns
        Only Available Pronouns set on the root account are allowed
        Adding and changing pronouns must be enabled on the root account.
        """
        if user_pronouns is not None:
            data["user[pronouns]"] = user_pronouns

        # OPTIONAL - user[event]
        """
            suspends or unsuspends all logins for this user that the calling user
        has permission to
        """
        if user_event is not None:
            self._validate_enum(user_event, ["suspend", "unsuspend"])
            data["user[event]"] = user_event

        self.logger.debug(
            "PUT /api/v1/users/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def merge_user_into_another_user_destination_user_id(self, destination_user_id, id):
        """
        Merge user into another user.

        Merge a user into another user.
        To merge users, the caller must have permissions to manage both users. This
        should be considered irreversible. This will delete the user and move all
        the data into the destination user.

        User merge details and caveats:
        The from_user is the user that was deleted in the user_merge process.
        The destination_user is the user that remains, that is being split.

        Avatars:
        When both users have avatars, only the destination_users avatar will remain.
        When one user has an avatar, will it will end up on the destination_user.

        Terms of Use:
        If either user has accepted terms of use, it will be be left as accepted.

        Communication Channels:
        All unique communication channels moved to the destination_user.
        All notification preferences are moved to the destination_user.

        Enrollments:
        All unique enrollments are moved to the destination_user.
        When there is an enrollment that would end up making it so that a user would
        be observing themselves, the enrollment is not moved over.
        Everything that is tied to the from_user at the course level relating to the
        enrollment is also moved to the destination_user.

        Submissions:
        All submissions are moved to the destination_user. If there are enrollments
        for both users in the same course, we prefer submissions that have grades
        then submissions that have work in them, and if there are no grades or no
        work, they are not moved.

        Other notes:
        Access Tokens are moved on merge.
        Conversations are moved on merge.
        Favorites are moved on merge.
        Courses will commonly use LTI tools. LTI tools reference the user with IDs
        that are stored on a user object. Merging users deletes one user and moves
        all records from the deleted user to the destination_user. These IDs are
        kept for all enrollments, group_membership, and account_users for the
        from_user at the time of the merge. When the destination_user launches an
        LTI tool from a course that used to be the from_user's, it doesn't appear as
        a new user to the tool provider. Instead it will send the stored ids. The
        destination_user's LTI IDs remain as they were for the courses that they
        originally had. Future enrollments for the destination_user will use the IDs
        that are on the destination_user object. LTI IDs that are kept and tracked
        per context include lti_context_id, lti_id and uuid. APIs that return the
        LTI ids will return the one for the context that it is called for, except
        for the user uuid. The user UUID will display the destination_users uuid,
        and when getting the uuid from an api that is in a context that was
        recorded from a merge event, an additional attribute is added as past_uuid.

        When finding users by SIS ids in different accounts the
        destination_account_id is required.

        The account can also be identified by passing the domain in destination_account_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # REQUIRED - PATH - destination_user_id
        """
            ID
        """
        path["destination_user_id"] = destination_user_id

        self.logger.debug(
            "PUT /api/v1/users/{id}/merge_into/{destination_user_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/{id}/merge_into/{destination_user_id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def merge_user_into_another_user_accounts(
        self, destination_account_id, destination_user_id, id
    ):
        """
        Merge user into another user.

        Merge a user into another user.
        To merge users, the caller must have permissions to manage both users. This
        should be considered irreversible. This will delete the user and move all
        the data into the destination user.

        User merge details and caveats:
        The from_user is the user that was deleted in the user_merge process.
        The destination_user is the user that remains, that is being split.

        Avatars:
        When both users have avatars, only the destination_users avatar will remain.
        When one user has an avatar, will it will end up on the destination_user.

        Terms of Use:
        If either user has accepted terms of use, it will be be left as accepted.

        Communication Channels:
        All unique communication channels moved to the destination_user.
        All notification preferences are moved to the destination_user.

        Enrollments:
        All unique enrollments are moved to the destination_user.
        When there is an enrollment that would end up making it so that a user would
        be observing themselves, the enrollment is not moved over.
        Everything that is tied to the from_user at the course level relating to the
        enrollment is also moved to the destination_user.

        Submissions:
        All submissions are moved to the destination_user. If there are enrollments
        for both users in the same course, we prefer submissions that have grades
        then submissions that have work in them, and if there are no grades or no
        work, they are not moved.

        Other notes:
        Access Tokens are moved on merge.
        Conversations are moved on merge.
        Favorites are moved on merge.
        Courses will commonly use LTI tools. LTI tools reference the user with IDs
        that are stored on a user object. Merging users deletes one user and moves
        all records from the deleted user to the destination_user. These IDs are
        kept for all enrollments, group_membership, and account_users for the
        from_user at the time of the merge. When the destination_user launches an
        LTI tool from a course that used to be the from_user's, it doesn't appear as
        a new user to the tool provider. Instead it will send the stored ids. The
        destination_user's LTI IDs remain as they were for the courses that they
        originally had. Future enrollments for the destination_user will use the IDs
        that are on the destination_user object. LTI IDs that are kept and tracked
        per context include lti_context_id, lti_id and uuid. APIs that return the
        LTI ids will return the one for the context that it is called for, except
        for the user uuid. The user UUID will display the destination_users uuid,
        and when getting the uuid from an api that is in a context that was
        recorded from a merge event, an additional attribute is added as past_uuid.

        When finding users by SIS ids in different accounts the
        destination_account_id is required.

        The account can also be identified by passing the domain in destination_account_id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # REQUIRED - PATH - destination_account_id
        """
            ID
        """
        path["destination_account_id"] = destination_account_id

        # REQUIRED - PATH - destination_user_id
        """
            ID
        """
        path["destination_user_id"] = destination_user_id

        self.logger.debug(
            "PUT /api/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/{id}/merge_into/accounts/{destination_account_id}/users/{destination_user_id}".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def split_merged_users_into_separate_users(self, id):
        """
        Split merged users into separate users.

        Merged users cannot be fully restored to their previous state, but this will
        attempt to split as much as possible to the previous state.
        To split a merged user, the caller must have permissions to manage all of
        the users logins. If there are multiple users that have been merged into one
        user it will split each merge into a separate user.
        A split can only happen within 180 days of a user merge. A user merge deletes
        the previous user and may be permanently deleted. In this scenario we create
        a new user object and proceed to move as much as possible to the new user.
        The user object will not have preserved the name or settings from the
        previous user. Some items may have been deleted during a user_merge that
        cannot be restored, and/or the data has become stale because of other
        changes to the objects since the time of the user_merge.

        Split users details and caveats:

        The from_user is the user that was deleted in the user_merge process.
        The destination_user is the user that remains, that is being split.

        Avatars:
        When both users had avatars, both will be remain.
        When from_user had an avatar and destination_user did not have an avatar,
        the destination_user's avatar will be deleted if it still matches what was
        there are the time of the merge.
        If the destination_user's avatar was changed at anytime after the merge, it
        will remain on the destination user.
        If the from_user had an avatar it will be there after split.

        Terms of Use:
        If from_user had not accepted terms of use, they will be prompted again
        to accept terms of use after the split.
        If the destination_user had not accepted terms of use, hey will be prompted
        again to accept terms of use after the split.
        If neither user had accepted the terms of use, but since the time of the
        merge had accepted, both will be prompted to accept terms of use.
        If both had accepted terms of use, this will remain.

        Communication Channels:
        All communication channels are restored to what they were prior to the
        merge. If a communication channel was added after the merge, it will remain
        on the destination_user.
        Notification preferences remain with the communication channels.

        Enrollments:
        All enrollments from the time of the merge will be moved back to where they
        were. Enrollments created since the time of the merge that were created by
        sis_import will go to the user that owns that sis_id used for the import.
        Other new enrollments will remain on the destination_user.
        Everything that is tied to the destination_user at the course level relating
        to an enrollment is moved to the from_user. When both users are in the same
        course prior to merge this can cause some unexpected items to move.

        Submissions:
        Unlike other items tied to a course, submissions are explicitly recorded to
        avoid problems with grades.
        All submissions were moved are restored to the spot prior to merge.
        All submission that were created in a course that was moved in enrollments
        are moved over to the from_user.

        Other notes:
        Access Tokens are moved back on split.
        Conversations are moved back on split.
        Favorites that existing at the time of merge are moved back on split.
        LTI ids are restored to how they were prior to merge.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "POST /api/v1/users/{id}/split with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/users/{id}/split".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def get_pandata_events_jwt_token_and_its_expiration_date(self, app_key=None):
        """
        Get a Pandata Events jwt token and its expiration date.

        Returns a jwt auth and props token that can be used to send events to
        Pandata.

        NOTE: This is currently only available to the mobile developer keys.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - app_key
        """
            The pandata events appKey for this mobile app
        """
        if app_key is not None:
            data["app_key"] = app_key

        self.logger.debug(
            "POST /api/v1/users/self/pandata_events_token with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/users/self/pandata_events_token".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_users_most_recently_graded_submissions(
        self,
        id,
        include=None,
        only_current_enrollments=None,
        only_published_assignments=None,
    ):
        """
        Get a users most recently graded submissions.


        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # OPTIONAL - include
        """
            Associations to include with the group
        """
        if include is not None:
            self._validate_enum(include, ["assignment"])
            params["include"] = include

        # OPTIONAL - only_current_enrollments
        """
            Returns submissions for only currently active enrollments
        """
        if only_current_enrollments is not None:
            params["only_current_enrollments"] = only_current_enrollments

        # OPTIONAL - only_published_assignments
        """
            Returns submissions for only published assignments
        """
        if only_published_assignments is not None:
            params["only_published_assignments"] = only_published_assignments

        self.logger.debug(
            "GET /api/v1/users/{id}/graded_submissions with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{id}/graded_submissions".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def get_user_profile(self, user_id):
        """
        Get user profile.

        Returns user profile data, including user id, name, and profile pic.

        When requesting the profile for the user accessing the API, the user's
        calendar feed URL and LTI user id will be returned as well.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        self.logger.debug(
            "GET /api/v1/users/{user_id}/profile with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/profile".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def list_avatar_options(self, user_id):
        """
        List avatar options.

        A paginated list of the possible user avatar options that can be set with the user update endpoint. The response will be an array of avatar records. If the 'type' field is 'attachment', the record will include all the normal attachment json fields; otherwise it will include only the 'url' and 'display_name' fields. Additionally, all records will include a 'type' field and a 'token' field. The following explains each field in more detail
        type:: ["gravatar"|"attachment"|"no_pic"] The type of avatar record, for categorization purposes.
        url:: The url of the avatar
        token:: A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client.
        display_name:: A textual description of the avatar record
        id:: ['attachment' type only] the internal id of the attachment
        content-type:: ['attachment' type only] the content-type of the attachment
        filename:: ['attachment' type only] the filename of the attachment
        size:: ['attachment' type only] the size of the attachment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        self.logger.debug(
            "GET /api/v1/users/{user_id}/avatars with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/avatars".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_user_page_views(self, user_id, end_time=None, start_time=None):
        """
        List user page views.

        Return a paginated list of the user's page view history in json format,
        similar to the available CSV download. Page views are returned in
        descending order, newest to oldest.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        # OPTIONAL - start_time
        """
            The beginning of the time range from which you want page views.
        """
        if start_time is not None:
            if issubclass(start_time.__class__, str):
                start_time = self._validate_iso8601_string(start_time)
            elif issubclass(start_time.__class__, date) or issubclass(
                start_time.__class__, datetime
            ):
                start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """
            The end of the time range from which you want page views.
        """
        if end_time is not None:
            if issubclass(end_time.__class__, str):
                end_time = self._validate_iso8601_string(end_time)
            elif issubclass(end_time.__class__, date) or issubclass(
                end_time.__class__, datetime
            ):
                end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_time"] = end_time

        self.logger.debug(
            "GET /api/v1/users/{user_id}/page_views with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/page_views".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def store_custom_data(self, data, ns, user_id):
        """
        Store custom data.

        Store arbitrary user data as JSON.
        
        Arbitrary JSON data can be stored for a User.
        A typical scenario would be an external site/service that registers users in Canvas
        and wants to capture additional info about them.  The part of the URL that follows
        +/custom_data/+ defines the scope of the request, and it reflects the structure of
        the JSON data to be stored or retrieved.
        
        The value +self+ may be used for +user_id+ to store data associated with the calling user.
        In order to access another user's custom data, you must be an account administrator with
        permission to manage users.
        
        A namespace parameter, +ns+, is used to prevent custom_data collisions between
        different apps.  This parameter is required for all custom_data requests.
        
        A request with Content-Type multipart/form-data or Content-Type
        application/x-www-form-urlencoded can only be used to store strings.
        
        Example PUT with multipart/form-data data:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/telephone' \
            -X PUT \
            -F 'ns=com.my-organization.canvas-app' \
            -F 'data=555-1234' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "555-1234"
          }
        
        Subscopes (or, generated scopes) can also be specified by passing values to
        +data+[+subscope+].
        
        Example PUT specifying subscopes:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements' \
            -X PUT \
            -F 'ns=com.my-organization.canvas-app' \
            -F 'data[waist]=32in' \
            -F 'data[inseam]=34in' \
            -F 'data[chest]=40in' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "chest": "40in",
              "waist": "32in",
              "inseam": "34in"
            }
          }
        
        Following such a request, subsets of the stored data to be retrieved directly from a subscope.
        
        Example {api:UsersController#get_custom_data GET} from a generated scope
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/body/measurements/chest' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "40in"
          }
        
        If you want to store more than just strings (i.e. numbers, arrays, hashes, true, false,
        and/or null), you must make a request with Content-Type application/json as in the following
        example.
        
        Example PUT with JSON data:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -H 'Content-Type: application/json' \
            -X PUT \
            -d '{
                  "ns": "com.my-organization.canvas-app",
                  "data": {
                    "a-number": 6.02e23,
                    "a-bool": true,
                    "a-string": "true",
                    "a-hash": {"a": {"b": "ohai"}},
                    "an-array": [1, "two", null, false]
                  }
                }' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "a-number": 6.02e+23,
              "a-bool": true,
              "a-string": "true",
              "a-hash": {
                "a": {
                  "b": "ohai"
                }
              },
              "an-array": [1, "two", null, false]
            }
          }
        
        If the data is an Object (as it is in the above example), then subsets of the data can
        be accessed by including the object's (possibly nested) keys in the scope of a GET request.
        
        Example {api:UsersController#get_custom_data GET} with a generated scope:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/a-hash/a/b' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "ohai"
          }
        
        
        On success, this endpoint returns an object containing the data that was stored.
        
        Responds with status code 200 if the scope already contained data, and it was overwritten
        by the data specified in the request.
        
        Responds with status code 201 if the scope was previously empty, and the data specified
        in the request was successfully stored there.
        
        Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid, or if
        the +data+ parameter is missing.
        
        Responds with status code 409 if the requested scope caused a conflict and data was not stored.
        This happens when storing data at the requested scope would cause data at an outer scope
        to be lost.  e.g., if +/custom_data+ was +{"fashion_app": {"hair": "blonde"}}+, but
        you tried to +`PUT /custom_data/fashion_app/hair/style -F data=buzz`+, then for the request
        to succeed,the value of +/custom_data/fashion_app/hair+ would have to become a hash, and its
        old string value would be lost.  In this situation, an error object is returned with the
        following format:
        
          !!!javascript
          {
            "message": "write conflict for custom_data hash",
            "conflict_scope": "fashion_app/hair",
            "type_at_conflict": "String",
            "value_at_conflict": "blonde"
          }
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        # REQUIRED - ns
        """
            The namespace under which to store the data.  This should be something other
        Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        """
        data["ns"] = ns

        # REQUIRED - data
        """
            The data you want to store for the user, at the specified scope.  If the data is
        composed of (possibly nested) JSON objects, scopes will be generated for the (nested)
        keys (see examples).
        """
        data["data"] = data

        self.logger.debug(
            "PUT /api/v1/users/{user_id}/custom_data with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/{user_id}/custom_data".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def load_custom_data(self, ns, user_id):
        """
        Load custom data.

        Load custom user data.

        Arbitrary JSON data can be stored for a User.  This API call
        retrieves that data for a (optional) given scope.
        See {api:UsersController#set_custom_data Store Custom Data} for details and
        examples.

        On success, this endpoint returns an object containing the data that was requested.

        Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
        or if the specified scope does not contain any data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        # REQUIRED - ns
        """
            The namespace from which to retrieve the data.  This should be something other
        Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        """
        params["ns"] = ns

        self.logger.debug(
            "GET /api/v1/users/{user_id}/custom_data with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/custom_data".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def delete_custom_data(self, ns, user_id):
        """
        Delete custom data.

        Delete custom user data.
        
        Arbitrary JSON data can be stored for a User.  This API call
        deletes that data for a given scope.  Without a scope, all custom_data is deleted.
        See {api:UsersController#set_custom_data Store Custom Data} for details and
        examples of storage and retrieval.
        
        As an example, we'll store some data, then delete a subset of it.
        
        Example {api:UsersController#set_custom_data PUT} with valid JSON data:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -X PUT \
            -F 'ns=com.my-organization.canvas-app' \
            -F 'data[fruit][apple]=so tasty' \
            -F 'data[fruit][kiwi]=a bit sour' \
            -F 'data[veggies][root][onion]=tear-jerking' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "fruit": {
                "apple": "so tasty",
                "kiwi": "a bit sour"
              },
              "veggies": {
                "root": {
                  "onion": "tear-jerking"
                }
              }
            }
          }
        
        Example DELETE:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/fruit/kiwi' \
            -X DELETE \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "a bit sour"
          }
        
        Example {api:UsersController#get_custom_data GET} following the above DELETE:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "fruit": {
                "apple": "so tasty"
              },
              "veggies": {
                "root": {
                  "onion": "tear-jerking"
                }
              }
            }
          }
        
        Note that hashes left empty after a DELETE will get removed from the custom_data store.
        For example, following the previous commands, if we delete /custom_data/veggies/root/onion,
        then the entire /custom_data/veggies scope will be removed.
        
        Example DELETE that empties a parent scope:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data/veggies/root/onion' \
            -X DELETE \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": "tear-jerking"
          }
        
        Example {api:UsersController#get_custom_data GET} following the above DELETE:
          curl 'https://<canvas>/api/v1/users/<user_id>/custom_data' \
            -X GET \
            -F 'ns=com.my-organization.canvas-app' \
            -H 'Authorization: Bearer <token>'
        
        Response:
          !!!javascript
          {
            "data": {
              "fruit": {
                "apple": "so tasty"
              }
            }
          }
        
        On success, this endpoint returns an object containing the data that was deleted.
        
        Responds with status code 400 if the namespace parameter, +ns+, is missing or invalid,
        or if the specified scope does not contain any data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        # REQUIRED - ns
        """
            The namespace from which to delete the data.  This should be something other
        Canvas API apps aren't likely to use, such as a reverse DNS for your organization.
        """
        params["ns"] = ns

        self.logger.debug(
            "DELETE /api/v1/users/{user_id}/custom_data with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/users/{user_id}/custom_data".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_course_nicknames(self):
        """
        List course nicknames.

        Returns all course nicknames you have set.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "GET /api/v1/users/self/course_nicknames with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/course_nicknames".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def get_course_nickname(self, course_id):
        """
        Get course nickname.

        Returns the nickname for a specific course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        self.logger.debug(
            "GET /api/v1/users/self/course_nicknames/{course_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/self/course_nicknames/{course_id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def set_course_nickname(self, course_id, nickname):
        """
        Set course nickname.

        Set a nickname for the given course. This will replace the course's name
        in output of API calls you make subsequently, as well as in selected
        places in the Canvas web user interface.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - nickname
        """
            The nickname to set.  It must be non-empty and shorter than 60 characters.
        """
        data["nickname"] = nickname

        self.logger.debug(
            "PUT /api/v1/users/self/course_nicknames/{course_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/users/self/course_nicknames/{course_id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def remove_course_nickname(self, course_id):
        """
        Remove course nickname.

        Remove the nickname for the given course.
        Subsequent course API calls will return the actual name for the course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        self.logger.debug(
            "DELETE /api/v1/users/self/course_nicknames/{course_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/users/self/course_nicknames/{course_id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def clear_course_nicknames(self):
        """
        Clear course nicknames.

        Remove all stored course nicknames.
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug(
            "DELETE /api/v1/users/self/course_nicknames with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/users/self/course_nicknames".format(**path),
            data=data,
            params=params,
            no_data=True,
        )


class Userdisplay(BaseModel):
    """Userdisplay Model.
    This mini-object is used for secondary user responses, when we just want to provide enough information to display a user."""

    def __init__(self, id=None, short_name=None, avatar_image_url=None, html_url=None):
        """Init method for Userdisplay class."""
        self._id = id
        self._short_name = short_name
        self._avatar_image_url = avatar_image_url
        self._html_url = html_url

        self.logger = logging.getLogger("py3canvas.Userdisplay")

    @property
    def id(self):
        """The ID of the user."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def short_name(self):
        """A short name the user has selected, for use in conversations or other less formal places through the site."""
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        """Setter for short_name property."""
        self.logger.warn(
            "Setting values on short_name will NOT update the remote Canvas instance."
        )
        self._short_name = value

    @property
    def avatar_image_url(self):
        """If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar."""
        return self._avatar_image_url

    @avatar_image_url.setter
    def avatar_image_url(self, value):
        """Setter for avatar_image_url property."""
        self.logger.warn(
            "Setting values on avatar_image_url will NOT update the remote Canvas instance."
        )
        self._avatar_image_url = value

    @property
    def html_url(self):
        """URL to access user, either nested to a context or directly."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn(
            "Setting values on html_url will NOT update the remote Canvas instance."
        )
        self._html_url = value


class Anonymoususerdisplay(BaseModel):
    """Anonymoususerdisplay Model.
    This mini-object is returned in place of UserDisplay when returning student data for anonymous assignments, and includes an anonymous ID to identify a user within the scope of a single assignment."""

    def __init__(self, anonymous_id=None, avatar_image_url=None):
        """Init method for Anonymoususerdisplay class."""
        self._anonymous_id = anonymous_id
        self._avatar_image_url = avatar_image_url

        self.logger = logging.getLogger("py3canvas.Anonymoususerdisplay")

    @property
    def anonymous_id(self):
        """A unique short ID identifying this user within the scope of a particular assignment."""
        return self._anonymous_id

    @anonymous_id.setter
    def anonymous_id(self, value):
        """Setter for anonymous_id property."""
        self.logger.warn(
            "Setting values on anonymous_id will NOT update the remote Canvas instance."
        )
        self._anonymous_id = value

    @property
    def avatar_image_url(self):
        """A URL to retrieve a generic avatar."""
        return self._avatar_image_url

    @avatar_image_url.setter
    def avatar_image_url(self, value):
        """Setter for avatar_image_url property."""
        self.logger.warn(
            "Setting values on avatar_image_url will NOT update the remote Canvas instance."
        )
        self._avatar_image_url = value


class User(BaseModel):
    """User Model.
    A Canvas user, e.g. a student, teacher, administrator, observer, etc."""

    def __init__(
        self,
        id,
        name=None,
        sortable_name=None,
        short_name=None,
        sis_user_id=None,
        sis_import_id=None,
        integration_id=None,
        login_id=None,
        avatar_url=None,
        enrollments=None,
        email=None,
        locale=None,
        last_login=None,
        time_zone=None,
        bio=None,
    ):
        """Init method for User class."""
        self._id = id
        self._name = name
        self._sortable_name = sortable_name
        self._short_name = short_name
        self._sis_user_id = sis_user_id
        self._sis_import_id = sis_import_id
        self._integration_id = integration_id
        self._login_id = login_id
        self._avatar_url = avatar_url
        self._enrollments = enrollments
        self._email = email
        self._locale = locale
        self._last_login = last_login
        self._time_zone = time_zone
        self._bio = bio

        self.logger = logging.getLogger("py3canvas.User")

    @property
    def id(self):
        """The ID of the user."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def name(self):
        """The name of the user."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def sortable_name(self):
        """The name of the user that is should be used for sorting groups of users, such as in the gradebook."""
        return self._sortable_name

    @sortable_name.setter
    def sortable_name(self, value):
        """Setter for sortable_name property."""
        self.logger.warn(
            "Setting values on sortable_name will NOT update the remote Canvas instance."
        )
        self._sortable_name = value

    @property
    def short_name(self):
        """A short name the user has selected, for use in conversations or other less formal places through the site."""
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        """Setter for short_name property."""
        self.logger.warn(
            "Setting values on short_name will NOT update the remote Canvas instance."
        )
        self._short_name = value

    @property
    def sis_user_id(self):
        """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn(
            "Setting values on sis_user_id will NOT update the remote Canvas instance."
        )
        self._sis_user_id = value

    @property
    def sis_import_id(self):
        """The id of the SIS import.  This field is only included if the user came from a SIS import and has permissions to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn(
            "Setting values on sis_import_id will NOT update the remote Canvas instance."
        )
        self._sis_import_id = value

    @property
    def integration_id(self):
        """The integration_id associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn(
            "Setting values on integration_id will NOT update the remote Canvas instance."
        )
        self._integration_id = value

    @property
    def login_id(self):
        """The unique login id for the user.  This is what the user uses to log in to Canvas."""
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        """Setter for login_id property."""
        self.logger.warn(
            "Setting values on login_id will NOT update the remote Canvas instance."
        )
        self._login_id = value

    @property
    def avatar_url(self):
        """If avatars are enabled, this field will be included and contain a url to retrieve the user's avatar."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        """Setter for avatar_url property."""
        self.logger.warn(
            "Setting values on avatar_url will NOT update the remote Canvas instance."
        )
        self._avatar_url = value

    @property
    def enrollments(self):
        """Optional: This field can be requested with certain API calls, and will return a list of the users active enrollments. See the List enrollments API for more details about the format of these records."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn(
            "Setting values on enrollments will NOT update the remote Canvas instance."
        )
        self._enrollments = value

    @property
    def email(self):
        """Optional: This field can be requested with certain API calls, and will return the users primary email address."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email property."""
        self.logger.warn(
            "Setting values on email will NOT update the remote Canvas instance."
        )
        self._email = value

    @property
    def locale(self):
        """Optional: This field can be requested with certain API calls, and will return the users locale in RFC 5646 format."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn(
            "Setting values on locale will NOT update the remote Canvas instance."
        )
        self._locale = value

    @property
    def last_login(self):
        """Optional: This field is only returned in certain API calls, and will return a timestamp representing the last time the user logged in to canvas."""
        return self._last_login

    @last_login.setter
    def last_login(self, value):
        """Setter for last_login property."""
        self.logger.warn(
            "Setting values on last_login will NOT update the remote Canvas instance."
        )
        self._last_login = value

    @property
    def time_zone(self):
        """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone."""
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """Setter for time_zone property."""
        self.logger.warn(
            "Setting values on time_zone will NOT update the remote Canvas instance."
        )
        self._time_zone = value

    @property
    def bio(self):
        """Optional: The user's bio."""
        return self._bio

    @bio.setter
    def bio(self, value):
        """Setter for bio property."""
        self.logger.warn(
            "Setting values on bio will NOT update the remote Canvas instance."
        )
        self._bio = value


class Profile(BaseModel):
    """Profile Model.
    Profile details for a Canvas user."""

    def __init__(
        self,
        id=None,
        name=None,
        short_name=None,
        sortable_name=None,
        title=None,
        bio=None,
        primary_email=None,
        login_id=None,
        sis_user_id=None,
        lti_user_id=None,
        avatar_url=None,
        calendar=None,
        time_zone=None,
        locale=None,
        k5_user=None,
    ):
        """Init method for Profile class."""
        self._id = id
        self._name = name
        self._short_name = short_name
        self._sortable_name = sortable_name
        self._title = title
        self._bio = bio
        self._primary_email = primary_email
        self._login_id = login_id
        self._sis_user_id = sis_user_id
        self._lti_user_id = lti_user_id
        self._avatar_url = avatar_url
        self._calendar = calendar
        self._time_zone = time_zone
        self._locale = locale
        self._k5_user = k5_user

        self.logger = logging.getLogger("py3canvas.Profile")

    @property
    def id(self):
        """The ID of the user."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def name(self):
        """Sample User."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def short_name(self):
        """Sample User."""
        return self._short_name

    @short_name.setter
    def short_name(self, value):
        """Setter for short_name property."""
        self.logger.warn(
            "Setting values on short_name will NOT update the remote Canvas instance."
        )
        self._short_name = value

    @property
    def sortable_name(self):
        """user, sample."""
        return self._sortable_name

    @sortable_name.setter
    def sortable_name(self, value):
        """Setter for sortable_name property."""
        self.logger.warn(
            "Setting values on sortable_name will NOT update the remote Canvas instance."
        )
        self._sortable_name = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn(
            "Setting values on title will NOT update the remote Canvas instance."
        )
        self._title = value

    @property
    def bio(self):
        """bio."""
        return self._bio

    @bio.setter
    def bio(self, value):
        """Setter for bio property."""
        self.logger.warn(
            "Setting values on bio will NOT update the remote Canvas instance."
        )
        self._bio = value

    @property
    def primary_email(self):
        """sample_user@example.com."""
        return self._primary_email

    @primary_email.setter
    def primary_email(self, value):
        """Setter for primary_email property."""
        self.logger.warn(
            "Setting values on primary_email will NOT update the remote Canvas instance."
        )
        self._primary_email = value

    @property
    def login_id(self):
        """sample_user@example.com."""
        return self._login_id

    @login_id.setter
    def login_id(self, value):
        """Setter for login_id property."""
        self.logger.warn(
            "Setting values on login_id will NOT update the remote Canvas instance."
        )
        self._login_id = value

    @property
    def sis_user_id(self):
        """sis1."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn(
            "Setting values on sis_user_id will NOT update the remote Canvas instance."
        )
        self._sis_user_id = value

    @property
    def lti_user_id(self):
        """lti_user_id."""
        return self._lti_user_id

    @lti_user_id.setter
    def lti_user_id(self, value):
        """Setter for lti_user_id property."""
        self.logger.warn(
            "Setting values on lti_user_id will NOT update the remote Canvas instance."
        )
        self._lti_user_id = value

    @property
    def avatar_url(self):
        """The avatar_url can change over time, so we recommend not caching it for more than a few hours."""
        return self._avatar_url

    @avatar_url.setter
    def avatar_url(self, value):
        """Setter for avatar_url property."""
        self.logger.warn(
            "Setting values on avatar_url will NOT update the remote Canvas instance."
        )
        self._avatar_url = value

    @property
    def calendar(self):
        """calendar."""
        return self._calendar

    @calendar.setter
    def calendar(self, value):
        """Setter for calendar property."""
        self.logger.warn(
            "Setting values on calendar will NOT update the remote Canvas instance."
        )
        self._calendar = value

    @property
    def time_zone(self):
        """Optional: This field is only returned in certain API calls, and will return the IANA time zone name of the user's preferred timezone."""
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """Setter for time_zone property."""
        self.logger.warn(
            "Setting values on time_zone will NOT update the remote Canvas instance."
        )
        self._time_zone = value

    @property
    def locale(self):
        """The users locale."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn(
            "Setting values on locale will NOT update the remote Canvas instance."
        )
        self._locale = value

    @property
    def k5_user(self):
        """Optional: Whether or not the user is a K5 user. This field is nil if the user settings are not for the user making the request."""
        return self._k5_user

    @k5_user.setter
    def k5_user(self, value):
        """Setter for k5_user property."""
        self.logger.warn(
            "Setting values on k5_user will NOT update the remote Canvas instance."
        )
        self._k5_user = value


class Avatar(BaseModel):
    """Avatar Model.
    Possible avatar for a user."""

    def __init__(
        self,
        type,
        url,
        token,
        display_name,
        id=None,
        content_type=None,
        filename=None,
        size=None,
    ):
        """Init method for Avatar class."""
        self._type = type
        self._url = url
        self._token = token
        self._display_name = display_name
        self._id = id
        self._content_type = content_type
        self._filename = filename
        self._size = size

        self.logger = logging.getLogger("py3canvas.Avatar")

    @property
    def type(self):
        """['gravatar'|'attachment'|'no_pic'] The type of avatar record, for categorization purposes."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn(
            "Setting values on type will NOT update the remote Canvas instance."
        )
        self._type = value

    @property
    def url(self):
        """The url of the avatar."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn(
            "Setting values on url will NOT update the remote Canvas instance."
        )
        self._url = value

    @property
    def token(self):
        """A unique representation of the avatar record which can be used to set the avatar with the user update endpoint. Note: this is an internal representation and is subject to change without notice. It should be consumed with this api endpoint and used in the user update endpoint, and should not be constructed by the client."""
        return self._token

    @token.setter
    def token(self, value):
        """Setter for token property."""
        self.logger.warn(
            "Setting values on token will NOT update the remote Canvas instance."
        )
        self._token = value

    @property
    def display_name(self):
        """A textual description of the avatar record."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn(
            "Setting values on display_name will NOT update the remote Canvas instance."
        )
        self._display_name = value

    @property
    def id(self):
        """['attachment' type only] the internal id of the attachment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def content_type(self):
        """['attachment' type only] the content-type of the attachment."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn(
            "Setting values on content_type will NOT update the remote Canvas instance."
        )
        self._content_type = value

    @property
    def filename(self):
        """['attachment' type only] the filename of the attachment."""
        return self._filename

    @filename.setter
    def filename(self, value):
        """Setter for filename property."""
        self.logger.warn(
            "Setting values on filename will NOT update the remote Canvas instance."
        )
        self._filename = value

    @property
    def size(self):
        """['attachment' type only] the size of the attachment."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter for size property."""
        self.logger.warn(
            "Setting values on size will NOT update the remote Canvas instance."
        )
        self._size = value


class Pageview(BaseModel):
    """Pageview Model.
    The record of a user page view access in Canvas"""

    def __init__(
        self,
        id,
        app_name=None,
        url=None,
        context_type=None,
        asset_type=None,
        controller=None,
        action=None,
        contributed=None,
        interaction_seconds=None,
        created_at=None,
        user_request=None,
        render_time=None,
        user_agent=None,
        participated=None,
        http_method=None,
        remote_ip=None,
        links=None,
    ):
        """Init method for Pageview class."""
        self._id = id
        self._app_name = app_name
        self._url = url
        self._context_type = context_type
        self._asset_type = asset_type
        self._controller = controller
        self._action = action
        self._contributed = contributed
        self._interaction_seconds = interaction_seconds
        self._created_at = created_at
        self._user_request = user_request
        self._render_time = render_time
        self._user_agent = user_agent
        self._participated = participated
        self._http_method = http_method
        self._remote_ip = remote_ip
        self._links = links

        self.logger = logging.getLogger("py3canvas.Pageview")

    @property
    def id(self):
        """A UUID representing the page view.  This is also the unique request id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def app_name(self):
        """If the request is from an API request, the app that generated the access token."""
        return self._app_name

    @app_name.setter
    def app_name(self, value):
        """Setter for app_name property."""
        self.logger.warn(
            "Setting values on app_name will NOT update the remote Canvas instance."
        )
        self._app_name = value

    @property
    def url(self):
        """The URL requested."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn(
            "Setting values on url will NOT update the remote Canvas instance."
        )
        self._url = value

    @property
    def context_type(self):
        """The type of context for the request."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn(
            "Setting values on context_type will NOT update the remote Canvas instance."
        )
        self._context_type = value

    @property
    def asset_type(self):
        """The type of asset in the context for the request, if any."""
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        """Setter for asset_type property."""
        self.logger.warn(
            "Setting values on asset_type will NOT update the remote Canvas instance."
        )
        self._asset_type = value

    @property
    def controller(self):
        """The rails controller that handled the request."""
        return self._controller

    @controller.setter
    def controller(self, value):
        """Setter for controller property."""
        self.logger.warn(
            "Setting values on controller will NOT update the remote Canvas instance."
        )
        self._controller = value

    @property
    def action(self):
        """The rails action that handled the request."""
        return self._action

    @action.setter
    def action(self, value):
        """Setter for action property."""
        self.logger.warn(
            "Setting values on action will NOT update the remote Canvas instance."
        )
        self._action = value

    @property
    def contributed(self):
        """This field is deprecated, and will always be false."""
        return self._contributed

    @contributed.setter
    def contributed(self, value):
        """Setter for contributed property."""
        self.logger.warn(
            "Setting values on contributed will NOT update the remote Canvas instance."
        )
        self._contributed = value

    @property
    def interaction_seconds(self):
        """An approximation of how long the user spent on the page, in seconds."""
        return self._interaction_seconds

    @interaction_seconds.setter
    def interaction_seconds(self, value):
        """Setter for interaction_seconds property."""
        self.logger.warn(
            "Setting values on interaction_seconds will NOT update the remote Canvas instance."
        )
        self._interaction_seconds = value

    @property
    def created_at(self):
        """When the request was made."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def user_request(self):
        """A flag indicating whether the request was user-initiated, or automatic (such as an AJAX call)."""
        return self._user_request

    @user_request.setter
    def user_request(self, value):
        """Setter for user_request property."""
        self.logger.warn(
            "Setting values on user_request will NOT update the remote Canvas instance."
        )
        self._user_request = value

    @property
    def render_time(self):
        """How long the response took to render, in seconds."""
        return self._render_time

    @render_time.setter
    def render_time(self, value):
        """Setter for render_time property."""
        self.logger.warn(
            "Setting values on render_time will NOT update the remote Canvas instance."
        )
        self._render_time = value

    @property
    def user_agent(self):
        """The user-agent of the browser or program that made the request."""
        return self._user_agent

    @user_agent.setter
    def user_agent(self, value):
        """Setter for user_agent property."""
        self.logger.warn(
            "Setting values on user_agent will NOT update the remote Canvas instance."
        )
        self._user_agent = value

    @property
    def participated(self):
        """True if the request counted as participating, such as submitting homework."""
        return self._participated

    @participated.setter
    def participated(self, value):
        """Setter for participated property."""
        self.logger.warn(
            "Setting values on participated will NOT update the remote Canvas instance."
        )
        self._participated = value

    @property
    def http_method(self):
        """The HTTP method such as GET or POST."""
        return self._http_method

    @http_method.setter
    def http_method(self, value):
        """Setter for http_method property."""
        self.logger.warn(
            "Setting values on http_method will NOT update the remote Canvas instance."
        )
        self._http_method = value

    @property
    def remote_ip(self):
        """The origin IP address of the request."""
        return self._remote_ip

    @remote_ip.setter
    def remote_ip(self, value):
        """Setter for remote_ip property."""
        self.logger.warn(
            "Setting values on remote_ip will NOT update the remote Canvas instance."
        )
        self._remote_ip = value

    @property
    def links(self):
        """The page view links to define the relationships."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn(
            "Setting values on links will NOT update the remote Canvas instance."
        )
        self._links = value


class Pageviewlinks(BaseModel):
    """Pageviewlinks Model.
    The links of a page view access in Canvas"""

    def __init__(
        self, user=None, context=None, asset=None, real_user=None, account=None
    ):
        """Init method for Pageviewlinks class."""
        self._user = user
        self._context = context
        self._asset = asset
        self._real_user = real_user
        self._account = account

        self.logger = logging.getLogger("py3canvas.Pageviewlinks")

    @property
    def user(self):
        """The ID of the user for this page view."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn(
            "Setting values on user will NOT update the remote Canvas instance."
        )
        self._user = value

    @property
    def context(self):
        """The ID of the context for the request (course id if context_type is Course, etc)."""
        return self._context

    @context.setter
    def context(self, value):
        """Setter for context property."""
        self.logger.warn(
            "Setting values on context will NOT update the remote Canvas instance."
        )
        self._context = value

    @property
    def asset(self):
        """The ID of the asset for the request, if any."""
        return self._asset

    @asset.setter
    def asset(self, value):
        """Setter for asset property."""
        self.logger.warn(
            "Setting values on asset will NOT update the remote Canvas instance."
        )
        self._asset = value

    @property
    def real_user(self):
        """The ID of the actual user who made this request, if the request was made by a user who was masquerading."""
        return self._real_user

    @real_user.setter
    def real_user(self, value):
        """Setter for real_user property."""
        self.logger.warn(
            "Setting values on real_user will NOT update the remote Canvas instance."
        )
        self._real_user = value

    @property
    def account(self):
        """The ID of the account context for this page view."""
        return self._account

    @account.setter
    def account(self, value):
        """Setter for account property."""
        self.logger.warn(
            "Setting values on account will NOT update the remote Canvas instance."
        )
        self._account = value


class Coursenickname(BaseModel):
    """Coursenickname Model."""

    def __init__(self, course_id=None, name=None, nickname=None):
        """Init method for Coursenickname class."""
        self._course_id = course_id
        self._name = name
        self._nickname = nickname

        self.logger = logging.getLogger("py3canvas.Coursenickname")

    @property
    def course_id(self):
        """the ID of the course."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn(
            "Setting values on course_id will NOT update the remote Canvas instance."
        )
        self._course_id = value

    @property
    def name(self):
        """the actual name of the course."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def nickname(self):
        """the calling user's nickname for the course."""
        return self._nickname

    @nickname.setter
    def nickname(self, value):
        """Setter for nickname property."""
        self.logger.warn(
            "Setting values on nickname will NOT update the remote Canvas instance."
        )
        self._nickname = value
