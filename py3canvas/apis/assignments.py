"""Assignments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class AssignmentsAPI(BaseCanvasAPI):
    """Assignments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AssignmentsAPI."""
        super(AssignmentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AssignmentsAPI")

    def delete_assignment(self, course_id, id):
        """
        Delete an assignment.

        Delete the given assignment.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{id}".format(**path), data=data, params=params, single_item=True)

    def list_assignments_assignments(self, course_id, assignment_ids=None, bucket=None, include=None, needs_grading_count_by_section=None, order_by=None, override_assignment_dates=None, post_to_sis=None, search_term=None):
        """
        List assignments.

        Returns the paginated list of assignments for the current course or assignment group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - include
        """
            Optional information to include with each assignment:
        submission:: The current user's current +Submission+
        assignment_visibility:: An array of ids of students who can see the assignment
        all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an "Everyone" / "Everyone Else" date
        overrides:: An array of +AssignmentOverride+ structures
        observed_users:: An array of submissions for observed users
        can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment.
        score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if 'submission' is also included.
        """
        if include is not None:
            self._validate_enum(include, ["submission", "assignment_visibility", "all_dates", "overrides", "observed_users", "can_edit", "score_statistics"])
            params["include"] = include


        # OPTIONAL - search_term
        """
            The partial title of the assignments to match and return.
        """
        if search_term is not None:
            params["search_term"] = search_term


        # OPTIONAL - override_assignment_dates
        """
            Apply assignment overrides for each assignment, defaults to true.
        """
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates


        # OPTIONAL - needs_grading_count_by_section
        """
            Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false
        """
        if needs_grading_count_by_section is not None:
            params["needs_grading_count_by_section"] = needs_grading_count_by_section


        # OPTIONAL - bucket
        """
            If included, only return certain assignments depending on due date and submission status.
        """
        if bucket is not None:
            self._validate_enum(bucket, ["past", "overdue", "undated", "ungraded", "unsubmitted", "upcoming", "future"])
            params["bucket"] = bucket


        # OPTIONAL - assignment_ids
        """
            if set, return only assignments specified
        """
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids


        # OPTIONAL - order_by
        """
            Determines the order of the assignments. Defaults to "position".
        """
        if order_by is not None:
            self._validate_enum(order_by, ["position", "name", "due_at"])
            params["order_by"] = order_by


        # OPTIONAL - post_to_sis
        """
            Return only assignments that have post_to_sis set or not set.
        """
        if post_to_sis is not None:
            params["post_to_sis"] = post_to_sis


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments".format(**path), data=data, params=params, all_pages=True)

    def list_assignments_assignment_groups(self, assignment_group_id, course_id, assignment_ids=None, bucket=None, include=None, needs_grading_count_by_section=None, order_by=None, override_assignment_dates=None, post_to_sis=None, search_term=None):
        """
        List assignments.

        Returns the paginated list of assignments for the current course or assignment group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_group_id
        """
            ID
        """
        path["assignment_group_id"] = assignment_group_id


        # OPTIONAL - include
        """
            Optional information to include with each assignment:
        submission:: The current user's current +Submission+
        assignment_visibility:: An array of ids of students who can see the assignment
        all_dates:: An array of +AssignmentDate+ structures, one for each override, and also a +base+ if the assignment has an "Everyone" / "Everyone Else" date
        overrides:: An array of +AssignmentOverride+ structures
        observed_users:: An array of submissions for observed users
        can_edit:: an extra Boolean value will be included with each +Assignment+ (and +AssignmentDate+ if +all_dates+ is supplied) to indicate whether the caller can edit the assignment or date. Moderated grading and closed grading periods may restrict a user's ability to edit an assignment.
        score_statistics:: An object containing min, max, and mean score on this assignment. This will not be included for students if there are less than 5 graded assignments or if disabled by the instructor. Only valid if 'submission' is also included.
        """
        if include is not None:
            self._validate_enum(include, ["submission", "assignment_visibility", "all_dates", "overrides", "observed_users", "can_edit", "score_statistics"])
            params["include"] = include


        # OPTIONAL - search_term
        """
            The partial title of the assignments to match and return.
        """
        if search_term is not None:
            params["search_term"] = search_term


        # OPTIONAL - override_assignment_dates
        """
            Apply assignment overrides for each assignment, defaults to true.
        """
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates


        # OPTIONAL - needs_grading_count_by_section
        """
            Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false
        """
        if needs_grading_count_by_section is not None:
            params["needs_grading_count_by_section"] = needs_grading_count_by_section


        # OPTIONAL - bucket
        """
            If included, only return certain assignments depending on due date and submission status.
        """
        if bucket is not None:
            self._validate_enum(bucket, ["past", "overdue", "undated", "ungraded", "unsubmitted", "upcoming", "future"])
            params["bucket"] = bucket


        # OPTIONAL - assignment_ids
        """
            if set, return only assignments specified
        """
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids


        # OPTIONAL - order_by
        """
            Determines the order of the assignments. Defaults to "position".
        """
        if order_by is not None:
            self._validate_enum(order_by, ["position", "name", "due_at"])
            params["order_by"] = order_by


        # OPTIONAL - post_to_sis
        """
            Return only assignments that have post_to_sis set or not set.
        """
        if post_to_sis is not None:
            params["post_to_sis"] = post_to_sis


        self.logger.debug("GET /api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignment_groups/{assignment_group_id}/assignments".format(**path), data=data, params=params, all_pages=True)

    def list_assignments_for_user(self, course_id, user_id):
        """
        List assignments for user.

        Returns the paginated list of assignments for the specified user if the current user has rights to view.
        See {api:AssignmentsApiController#index List assignments} for valid arguments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/users/{user_id}/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/courses/{course_id}/assignments".format(**path), data=data, params=params, no_data=True)

    def duplicate_assignnment(self, assignment_id, course_id, result_type=None):
        """
        Duplicate assignnment.

        Duplicate an assignment and return a json based on result_type argument.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # OPTIONAL - result_type
        """
            Optional information:
        When the root account has the feature `newquizzes_on_quiz_page` enabled
        and this argument is set to "Quiz" the response will be serialized into a
        quiz format({file:doc/api/quizzes.html#Quiz});
        When this argument isn't specified the response will be serialized into an
        assignment format;
        """
        if result_type is not None:
            self._validate_enum(result_type, ["Quiz"])
            data["result_type"] = result_type


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/duplicate with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/duplicate".format(**path), data=data, params=params, single_item=True)

    def get_single_assignment(self, course_id, id, all_dates=None, include=None, needs_grading_count_by_section=None, override_assignment_dates=None):
        """
        Get a single assignment.

        Returns the assignment with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - include
        """
            Associations to include with the assignment. The "assignment_visibility" option
        requires that the Differentiated Assignments course feature be turned on. If
        "observed_users" is passed, submissions for observed users will also be included.
        For "score_statistics" to be included, the "submission" option must also be set.
        """
        if include is not None:
            self._validate_enum(include, ["submission", "assignment_visibility", "overrides", "observed_users", "can_edit", "score_statistics"])
            params["include"] = include


        # OPTIONAL - override_assignment_dates
        """
            Apply assignment overrides to the assignment, defaults to true.
        """
        if override_assignment_dates is not None:
            params["override_assignment_dates"] = override_assignment_dates


        # OPTIONAL - needs_grading_count_by_section
        """
            Split up "needs_grading_count" by sections into the "needs_grading_count_by_section" key, defaults to false
        """
        if needs_grading_count_by_section is not None:
            params["needs_grading_count_by_section"] = needs_grading_count_by_section


        # OPTIONAL - all_dates
        """
            All dates associated with the assignment, if applicable
        """
        if all_dates is not None:
            params["all_dates"] = all_dates


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{id}".format(**path), data=data, params=params, single_item=True)

    def create_assignment(self, assignment_name, course_id, assignment_allowed_attempts=None, assignment_allowed_extensions=None, assignment_annotatable_attachment_id=None, assignment_anonymous_grading=None, assignment_assignment_group_id=None, assignment_assignment_overrides=None, assignment_automatic_peer_reviews=None, assignment_description=None, assignment_due_at=None, assignment_external_tool_tag_attributes=None, assignment_final_grader_id=None, assignment_grade_group_students_individually=None, assignment_grader_comments_visible_to_graders=None, assignment_grader_count=None, assignment_graders_anonymous_to_graders=None, assignment_graders_names_visible_to_final_grader=None, assignment_grading_standard_id=None, assignment_grading_type=None, assignment_group_category_id=None, assignment_integration_data=None, assignment_integration_id=None, assignment_lock_at=None, assignment_moderated_grading=None, assignment_notify_of_update=None, assignment_omit_from_final_grade=None, assignment_only_visible_to_overrides=None, assignment_peer_reviews=None, assignment_points_possible=None, assignment_position=None, assignment_published=None, assignment_quiz_lti=None, assignment_submission_types=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_unlock_at=None, assignment_vericite_enabled=None):
        """
        Create an assignment.

        Create a new assignment for this course. The assignment is created in the
        active state.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - assignment[name]
        """
            The assignment name.
        """
        data["assignment[name]"] = assignment_name


        # OPTIONAL - assignment[position]
        """
            The position of this assignment in the group when displaying
        assignment lists.
        """
        if assignment_position is not None:
            data["assignment[position]"] = assignment_position


        # OPTIONAL - assignment[submission_types]
        """
            List of supported submission types for the assignment.
        Unless the assignment is allowing online submissions, the array should
        only have one element.

        If not allowing online submissions, your options are:
          "online_quiz"
          "none"
          "on_paper"
          "discussion_topic"
          "external_tool"

        If you are allowing online submissions, you can have one or many
        allowed submission types:

          "online_upload"
          "online_text_entry"
          "online_url"
          "media_recording" (Only valid when the Kaltura plugin is enabled)
          "student_annotation"
        """
        if assignment_submission_types is not None:
            self._validate_enum(assignment_submission_types, ["online_quiz", "none", "on_paper", "discussion_topic", "external_tool", "online_upload", "online_text_entry", "online_url", "media_recording", "student_annotation"])
            data["assignment[submission_types]"] = assignment_submission_types


        # OPTIONAL - assignment[allowed_extensions]
        """
            Allowed extensions if submission_types includes "online_upload"

        Example:
          allowed_extensions: ["docx","ppt"]
        """
        if assignment_allowed_extensions is not None:
            data["assignment[allowed_extensions]"] = assignment_allowed_extensions


        # OPTIONAL - assignment[turnitin_enabled]
        """
            Only applies when the Turnitin plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles Turnitin submissions for the assignment.
        Will be ignored if Turnitin is not available for the course.
        """
        if assignment_turnitin_enabled is not None:
            data["assignment[turnitin_enabled]"] = assignment_turnitin_enabled


        # OPTIONAL - assignment[vericite_enabled]
        """
            Only applies when the VeriCite plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles VeriCite submissions for the assignment.
        Will be ignored if VeriCite is not available for the course.
        """
        if assignment_vericite_enabled is not None:
            data["assignment[vericite_enabled]"] = assignment_vericite_enabled


        # OPTIONAL - assignment[turnitin_settings]
        """
            Settings to send along to turnitin. See Assignment object definition for
        format.
        """
        if assignment_turnitin_settings is not None:
            data["assignment[turnitin_settings]"] = assignment_turnitin_settings


        # OPTIONAL - assignment[integration_data]
        """
            Data used for SIS integrations. Requires admin-level token with the "Manage SIS" permission. JSON string required.
        """
        if assignment_integration_data is not None:
            data["assignment[integration_data]"] = assignment_integration_data


        # OPTIONAL - assignment[integration_id]
        """
            Unique ID from third party integrations
        """
        if assignment_integration_id is not None:
            data["assignment[integration_id]"] = assignment_integration_id


        # OPTIONAL - assignment[peer_reviews]
        """
            If submission_types does not include external_tool,discussion_topic,
        online_quiz, or on_paper, determines whether or not peer reviews
        will be turned on for the assignment.
        """
        if assignment_peer_reviews is not None:
            data["assignment[peer_reviews]"] = assignment_peer_reviews


        # OPTIONAL - assignment[automatic_peer_reviews]
        """
            Whether peer reviews will be assigned automatically by Canvas or if
        teachers must manually assign peer reviews. Does not apply if peer reviews
        are not enabled.
        """
        if assignment_automatic_peer_reviews is not None:
            data["assignment[automatic_peer_reviews]"] = assignment_automatic_peer_reviews


        # OPTIONAL - assignment[notify_of_update]
        """
            If true, Canvas will send a notification to students in the class
        notifying them that the content has changed.
        """
        if assignment_notify_of_update is not None:
            data["assignment[notify_of_update]"] = assignment_notify_of_update


        # OPTIONAL - assignment[group_category_id]
        """
            If present, the assignment will become a group assignment assigned
        to the group.
        """
        if assignment_group_category_id is not None:
            data["assignment[group_category_id]"] = assignment_group_category_id


        # OPTIONAL - assignment[grade_group_students_individually]
        """
            If this is a group assignment, teachers have the options to grade
        students individually. If false, Canvas will apply the assignment's
        score to each member of the group. If true, the teacher can manually
        assign scores to each member of the group.
        """
        if assignment_grade_group_students_individually is not None:
            data["assignment[grade_group_students_individually]"] = assignment_grade_group_students_individually


        # OPTIONAL - assignment[external_tool_tag_attributes]
        """
            Hash of external tool parameters if submission_types is ["external_tool"].
        See Assignment object definition for format.
        """
        if assignment_external_tool_tag_attributes is not None:
            data["assignment[external_tool_tag_attributes]"] = assignment_external_tool_tag_attributes


        # OPTIONAL - assignment[points_possible]
        """
            The maximum points possible on the assignment.
        """
        if assignment_points_possible is not None:
            data["assignment[points_possible]"] = assignment_points_possible


        # OPTIONAL - assignment[grading_type]
        """
            The strategy used for grading the assignment.
        The assignment defaults to "points" if this field is omitted.
        """
        if assignment_grading_type is not None:
            self._validate_enum(assignment_grading_type, ["pass_fail", "percent", "letter_grade", "gpa_scale", "points", "not_graded"])
            data["assignment[grading_type]"] = assignment_grading_type


        # OPTIONAL - assignment[due_at]
        """
            The day/time the assignment is due. Must be between the lock dates if there are lock dates.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        """
        if assignment_due_at is not None:
            if issubclass(assignment_due_at.__class__, str):
                assignment_due_at = self._validate_iso8601_string(assignment_due_at)
            elif issubclass(assignment_due_at.__class__, date) or issubclass(assignment_due_at.__class__, datetime):
                assignment_due_at = assignment_due_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment[due_at]"] = assignment_due_at


        # OPTIONAL - assignment[lock_at]
        """
            The day/time the assignment is locked after. Must be after the due date if there is a due date.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        """
        if assignment_lock_at is not None:
            if issubclass(assignment_lock_at.__class__, str):
                assignment_lock_at = self._validate_iso8601_string(assignment_lock_at)
            elif issubclass(assignment_lock_at.__class__, date) or issubclass(assignment_lock_at.__class__, datetime):
                assignment_lock_at = assignment_lock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment[lock_at]"] = assignment_lock_at


        # OPTIONAL - assignment[unlock_at]
        """
            The day/time the assignment is unlocked. Must be before the due date if there is a due date.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        """
        if assignment_unlock_at is not None:
            if issubclass(assignment_unlock_at.__class__, str):
                assignment_unlock_at = self._validate_iso8601_string(assignment_unlock_at)
            elif issubclass(assignment_unlock_at.__class__, date) or issubclass(assignment_unlock_at.__class__, datetime):
                assignment_unlock_at = assignment_unlock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment[unlock_at]"] = assignment_unlock_at


        # OPTIONAL - assignment[description]
        """
            The assignment's description, supports HTML.
        """
        if assignment_description is not None:
            data["assignment[description]"] = assignment_description


        # OPTIONAL - assignment[assignment_group_id]
        """
            The assignment group id to put the assignment in.
        Defaults to the top assignment group in the course.
        """
        if assignment_assignment_group_id is not None:
            data["assignment[assignment_group_id]"] = assignment_assignment_group_id


        # OPTIONAL - assignment[assignment_overrides]
        """
            List of overrides for the assignment.
        """
        if assignment_assignment_overrides is not None:
            data["assignment[assignment_overrides]"] = assignment_assignment_overrides


        # OPTIONAL - assignment[only_visible_to_overrides]
        """
            Whether this assignment is only visible to overrides
        (Only useful if 'differentiated assignments' account setting is on)
        """
        if assignment_only_visible_to_overrides is not None:
            data["assignment[only_visible_to_overrides]"] = assignment_only_visible_to_overrides


        # OPTIONAL - assignment[published]
        """
            Whether this assignment is published.
        (Only useful if 'draft state' account setting is on)
        Unpublished assignments are not visible to students.
        """
        if assignment_published is not None:
            data["assignment[published]"] = assignment_published


        # OPTIONAL - assignment[grading_standard_id]
        """
            The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
        This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'.
        """
        if assignment_grading_standard_id is not None:
            data["assignment[grading_standard_id]"] = assignment_grading_standard_id


        # OPTIONAL - assignment[omit_from_final_grade]
        """
            Whether this assignment is counted towards a student's final grade.
        """
        if assignment_omit_from_final_grade is not None:
            data["assignment[omit_from_final_grade]"] = assignment_omit_from_final_grade


        # OPTIONAL - assignment[quiz_lti]
        """
            Whether this assignment should use the Quizzes 2 LTI tool. Sets the
        submission type to 'external_tool' and configures the external tool
        attributes to use the Quizzes 2 LTI tool configured for this course.
        Has no effect if no Quizzes 2 LTI tool is configured.
        """
        if assignment_quiz_lti is not None:
            data["assignment[quiz_lti]"] = assignment_quiz_lti


        # OPTIONAL - assignment[moderated_grading]
        """
            Whether this assignment is moderated.
        """
        if assignment_moderated_grading is not None:
            data["assignment[moderated_grading]"] = assignment_moderated_grading


        # OPTIONAL - assignment[grader_count]
        """
            The maximum number of provisional graders who may issue grades for this
        assignment. Only relevant for moderated assignments. Must be a positive
        value, and must be set to 1 if the course has fewer than two active
        instructors. Otherwise, the maximum value is the number of active
        instructors in the course minus one, or 10 if the course has more than 11
        active instructors.
        """
        if assignment_grader_count is not None:
            data["assignment[grader_count]"] = assignment_grader_count


        # OPTIONAL - assignment[final_grader_id]
        """
            The user ID of the grader responsible for choosing final grades for this
        assignment. Only relevant for moderated assignments.
        """
        if assignment_final_grader_id is not None:
            data["assignment[final_grader_id]"] = assignment_final_grader_id


        # OPTIONAL - assignment[grader_comments_visible_to_graders]
        """
            Boolean indicating if provisional graders' comments are visible to other
        provisional graders. Only relevant for moderated assignments.
        """
        if assignment_grader_comments_visible_to_graders is not None:
            data["assignment[grader_comments_visible_to_graders]"] = assignment_grader_comments_visible_to_graders


        # OPTIONAL - assignment[graders_anonymous_to_graders]
        """
            Boolean indicating if provisional graders' identities are hidden from
        other provisional graders. Only relevant for moderated assignments.
        """
        if assignment_graders_anonymous_to_graders is not None:
            data["assignment[graders_anonymous_to_graders]"] = assignment_graders_anonymous_to_graders


        # OPTIONAL - assignment[graders_names_visible_to_final_grader]
        """
            Boolean indicating if provisional grader identities are visible to the
        the final grader. Only relevant for moderated assignments.
        """
        if assignment_graders_names_visible_to_final_grader is not None:
            data["assignment[graders_names_visible_to_final_grader]"] = assignment_graders_names_visible_to_final_grader


        # OPTIONAL - assignment[anonymous_grading]
        """
            Boolean indicating if the assignment is graded anonymously. If true,
        graders cannot see student identities.
        """
        if assignment_anonymous_grading is not None:
            data["assignment[anonymous_grading]"] = assignment_anonymous_grading


        # OPTIONAL - assignment[allowed_attempts]
        """
            The number of submission attempts allowed for this assignment. Set to -1 for unlimited attempts.
        """
        if assignment_allowed_attempts is not None:
            data["assignment[allowed_attempts]"] = assignment_allowed_attempts


        # OPTIONAL - assignment[annotatable_attachment_id]
        """
            The Attachment ID of the document being annotated.

        Only applies when submission_types includes "student_annotation".
        """
        if assignment_annotatable_attachment_id is not None:
            data["assignment[annotatable_attachment_id]"] = assignment_annotatable_attachment_id


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments".format(**path), data=data, params=params, single_item=True)

    def edit_assignment(self, course_id, id, assignment_allowed_attempts=None, assignment_allowed_extensions=None, assignment_annotatable_attachment_id=None, assignment_anonymous_grading=None, assignment_assignment_group_id=None, assignment_assignment_overrides=None, assignment_automatic_peer_reviews=None, assignment_description=None, assignment_due_at=None, assignment_external_tool_tag_attributes=None, assignment_final_grader_id=None, assignment_grade_group_students_individually=None, assignment_grader_comments_visible_to_graders=None, assignment_grader_count=None, assignment_graders_anonymous_to_graders=None, assignment_graders_names_visible_to_final_grader=None, assignment_grading_standard_id=None, assignment_grading_type=None, assignment_group_category_id=None, assignment_integration_data=None, assignment_integration_id=None, assignment_lock_at=None, assignment_moderated_grading=None, assignment_name=None, assignment_notify_of_update=None, assignment_omit_from_final_grade=None, assignment_only_visible_to_overrides=None, assignment_peer_reviews=None, assignment_points_possible=None, assignment_position=None, assignment_published=None, assignment_sis_assignment_id=None, assignment_submission_types=None, assignment_submission_types=None, assignment_turnitin_enabled=None, assignment_turnitin_settings=None, assignment_unlock_at=None, assignment_vericite_enabled=None):
        """
        Edit an assignment.

        Modify an existing assignment.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - assignment[name]
        """
            The assignment name.
        """
        if assignment_name is not None:
            data["assignment[name]"] = assignment_name


        # OPTIONAL - assignment[position]
        """
            The position of this assignment in the group when displaying
        assignment lists.
        """
        if assignment_position is not None:
            data["assignment[position]"] = assignment_position


        # OPTIONAL - assignment[submission_types]
        """
            Only applies if the assignment doesn't have student submissions.

        List of supported submission types for the assignment.
        Unless the assignment is allowing online submissions, the array should
        only have one element.

        If not allowing online submissions, your options are:
          "online_quiz"
          "none"
          "on_paper"
          "discussion_topic"
          "external_tool"

        If you are allowing online submissions, you can have one or many
        allowed submission types:

          "online_upload"
          "online_text_entry"
          "online_url"
          "media_recording" (Only valid when the Kaltura plugin is enabled)
          "student_annotation"
        """
        if assignment_submission_types is not None:
            self._validate_enum(assignment_submission_types, ["online_quiz", "none", "on_paper", "discussion_topic", "external_tool", "online_upload", "online_text_entry", "online_url", "media_recording", "student_annotation"])
            data["assignment[submission_types]"] = assignment_submission_types


        # OPTIONAL - assignment[allowed_extensions]
        """
            Allowed extensions if submission_types includes "online_upload"

        Example:
          allowed_extensions: ["docx","ppt"]
        """
        if assignment_allowed_extensions is not None:
            data["assignment[allowed_extensions]"] = assignment_allowed_extensions


        # OPTIONAL - assignment[turnitin_enabled]
        """
            Only applies when the Turnitin plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles Turnitin submissions for the assignment.
        Will be ignored if Turnitin is not available for the course.
        """
        if assignment_turnitin_enabled is not None:
            data["assignment[turnitin_enabled]"] = assignment_turnitin_enabled


        # OPTIONAL - assignment[vericite_enabled]
        """
            Only applies when the VeriCite plugin is enabled for a course and
        the submission_types array includes "online_upload".
        Toggles VeriCite submissions for the assignment.
        Will be ignored if VeriCite is not available for the course.
        """
        if assignment_vericite_enabled is not None:
            data["assignment[vericite_enabled]"] = assignment_vericite_enabled


        # OPTIONAL - assignment[turnitin_settings]
        """
            Settings to send along to turnitin. See Assignment object definition for
        format.
        """
        if assignment_turnitin_settings is not None:
            data["assignment[turnitin_settings]"] = assignment_turnitin_settings


        # OPTIONAL - assignment[sis_assignment_id]
        """
            The sis id of the Assignment
        """
        if assignment_sis_assignment_id is not None:
            data["assignment[sis_assignment_id]"] = assignment_sis_assignment_id


        # OPTIONAL - assignment[integration_data]
        """
            Data used for SIS integrations. Requires admin-level token with the "Manage SIS" permission. JSON string required.
        """
        if assignment_integration_data is not None:
            data["assignment[integration_data]"] = assignment_integration_data


        # OPTIONAL - assignment[integration_id]
        """
            Unique ID from third party integrations
        """
        if assignment_integration_id is not None:
            data["assignment[integration_id]"] = assignment_integration_id


        # OPTIONAL - assignment[peer_reviews]
        """
            If submission_types does not include external_tool,discussion_topic,
        online_quiz, or on_paper, determines whether or not peer reviews
        will be turned on for the assignment.
        """
        if assignment_peer_reviews is not None:
            data["assignment[peer_reviews]"] = assignment_peer_reviews


        # OPTIONAL - assignment[automatic_peer_reviews]
        """
            Whether peer reviews will be assigned automatically by Canvas or if
        teachers must manually assign peer reviews. Does not apply if peer reviews
        are not enabled.
        """
        if assignment_automatic_peer_reviews is not None:
            data["assignment[automatic_peer_reviews]"] = assignment_automatic_peer_reviews


        # OPTIONAL - assignment[notify_of_update]
        """
            If true, Canvas will send a notification to students in the class
        notifying them that the content has changed.
        """
        if assignment_notify_of_update is not None:
            data["assignment[notify_of_update]"] = assignment_notify_of_update


        # OPTIONAL - assignment[group_category_id]
        """
            If present, the assignment will become a group assignment assigned
        to the group.
        """
        if assignment_group_category_id is not None:
            data["assignment[group_category_id]"] = assignment_group_category_id


        # OPTIONAL - assignment[grade_group_students_individually]
        """
            If this is a group assignment, teachers have the options to grade
        students individually. If false, Canvas will apply the assignment's
        score to each member of the group. If true, the teacher can manually
        assign scores to each member of the group.
        """
        if assignment_grade_group_students_individually is not None:
            data["assignment[grade_group_students_individually]"] = assignment_grade_group_students_individually


        # OPTIONAL - assignment[external_tool_tag_attributes]
        """
            Hash of external tool parameters if submission_types is ["external_tool"].
        See Assignment object definition for format.
        """
        if assignment_external_tool_tag_attributes is not None:
            data["assignment[external_tool_tag_attributes]"] = assignment_external_tool_tag_attributes


        # OPTIONAL - assignment[points_possible]
        """
            The maximum points possible on the assignment.
        """
        if assignment_points_possible is not None:
            data["assignment[points_possible]"] = assignment_points_possible


        # OPTIONAL - assignment[grading_type]
        """
            The strategy used for grading the assignment.
        The assignment defaults to "points" if this field is omitted.
        """
        if assignment_grading_type is not None:
            self._validate_enum(assignment_grading_type, ["pass_fail", "percent", "letter_grade", "gpa_scale", "points", "not_graded"])
            data["assignment[grading_type]"] = assignment_grading_type


        # OPTIONAL - assignment[due_at]
        """
            The day/time the assignment is due.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        """
        if assignment_due_at is not None:
            if issubclass(assignment_due_at.__class__, str):
                assignment_due_at = self._validate_iso8601_string(assignment_due_at)
            elif issubclass(assignment_due_at.__class__, date) or issubclass(assignment_due_at.__class__, datetime):
                assignment_due_at = assignment_due_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment[due_at]"] = assignment_due_at


        # OPTIONAL - assignment[lock_at]
        """
            The day/time the assignment is locked after. Must be after the due date if there is a due date.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        """
        if assignment_lock_at is not None:
            if issubclass(assignment_lock_at.__class__, str):
                assignment_lock_at = self._validate_iso8601_string(assignment_lock_at)
            elif issubclass(assignment_lock_at.__class__, date) or issubclass(assignment_lock_at.__class__, datetime):
                assignment_lock_at = assignment_lock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment[lock_at]"] = assignment_lock_at


        # OPTIONAL - assignment[unlock_at]
        """
            The day/time the assignment is unlocked. Must be before the due date if there is a due date.
        Accepts times in ISO 8601 format, e.g. 2014-10-21T18:48:00Z.
        """
        if assignment_unlock_at is not None:
            if issubclass(assignment_unlock_at.__class__, str):
                assignment_unlock_at = self._validate_iso8601_string(assignment_unlock_at)
            elif issubclass(assignment_unlock_at.__class__, date) or issubclass(assignment_unlock_at.__class__, datetime):
                assignment_unlock_at = assignment_unlock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment[unlock_at]"] = assignment_unlock_at


        # OPTIONAL - assignment[description]
        """
            The assignment's description, supports HTML.
        """
        if assignment_description is not None:
            data["assignment[description]"] = assignment_description


        # OPTIONAL - assignment[assignment_group_id]
        """
            The assignment group id to put the assignment in.
        Defaults to the top assignment group in the course.
        """
        if assignment_assignment_group_id is not None:
            data["assignment[assignment_group_id]"] = assignment_assignment_group_id


        # OPTIONAL - assignment[assignment_overrides]
        """
            List of overrides for the assignment.
        If the +assignment[assignment_overrides]+ key is absent, any existing
        overrides are kept as is. If the +assignment[assignment_overrides]+ key is
        present, existing overrides are updated or deleted (and new ones created,
        as necessary) to match the provided list.
        """
        if assignment_assignment_overrides is not None:
            data["assignment[assignment_overrides]"] = assignment_assignment_overrides


        # OPTIONAL - assignment[only_visible_to_overrides]
        """
            Whether this assignment is only visible to overrides
        (Only useful if 'differentiated assignments' account setting is on)
        """
        if assignment_only_visible_to_overrides is not None:
            data["assignment[only_visible_to_overrides]"] = assignment_only_visible_to_overrides


        # OPTIONAL - assignment[published]
        """
            Whether this assignment is published.
        (Only useful if 'draft state' account setting is on)
        Unpublished assignments are not visible to students.
        """
        if assignment_published is not None:
            data["assignment[published]"] = assignment_published


        # OPTIONAL - assignment[grading_standard_id]
        """
            The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
        This will update the grading_type for the course to 'letter_grade' unless it is already 'gpa_scale'.
        """
        if assignment_grading_standard_id is not None:
            data["assignment[grading_standard_id]"] = assignment_grading_standard_id


        # OPTIONAL - assignment[omit_from_final_grade]
        """
            Whether this assignment is counted towards a student's final grade.
        """
        if assignment_omit_from_final_grade is not None:
            data["assignment[omit_from_final_grade]"] = assignment_omit_from_final_grade


        # OPTIONAL - assignment[moderated_grading]
        """
            Whether this assignment is moderated.
        """
        if assignment_moderated_grading is not None:
            data["assignment[moderated_grading]"] = assignment_moderated_grading


        # OPTIONAL - assignment[grader_count]
        """
            The maximum number of provisional graders who may issue grades for this
        assignment. Only relevant for moderated assignments. Must be a positive
        value, and must be set to 1 if the course has fewer than two active
        instructors. Otherwise, the maximum value is the number of active
        instructors in the course minus one, or 10 if the course has more than 11
        active instructors.
        """
        if assignment_grader_count is not None:
            data["assignment[grader_count]"] = assignment_grader_count


        # OPTIONAL - assignment[final_grader_id]
        """
            The user ID of the grader responsible for choosing final grades for this
        assignment. Only relevant for moderated assignments.
        """
        if assignment_final_grader_id is not None:
            data["assignment[final_grader_id]"] = assignment_final_grader_id


        # OPTIONAL - assignment[grader_comments_visible_to_graders]
        """
            Boolean indicating if provisional graders' comments are visible to other
        provisional graders. Only relevant for moderated assignments.
        """
        if assignment_grader_comments_visible_to_graders is not None:
            data["assignment[grader_comments_visible_to_graders]"] = assignment_grader_comments_visible_to_graders


        # OPTIONAL - assignment[graders_anonymous_to_graders]
        """
            Boolean indicating if provisional graders' identities are hidden from
        other provisional graders. Only relevant for moderated assignments.
        """
        if assignment_graders_anonymous_to_graders is not None:
            data["assignment[graders_anonymous_to_graders]"] = assignment_graders_anonymous_to_graders


        # OPTIONAL - assignment[graders_names_visible_to_final_grader]
        """
            Boolean indicating if provisional grader identities are visible to the
        the final grader. Only relevant for moderated assignments.
        """
        if assignment_graders_names_visible_to_final_grader is not None:
            data["assignment[graders_names_visible_to_final_grader]"] = assignment_graders_names_visible_to_final_grader


        # OPTIONAL - assignment[anonymous_grading]
        """
            Boolean indicating if the assignment is graded anonymously. If true,
        graders cannot see student identities.
        """
        if assignment_anonymous_grading is not None:
            data["assignment[anonymous_grading]"] = assignment_anonymous_grading


        # OPTIONAL - assignment[allowed_attempts]
        """
            The number of submission attempts allowed for this assignment. Set to -1 or null for
        unlimited attempts.
        """
        if assignment_allowed_attempts is not None:
            data["assignment[allowed_attempts]"] = assignment_allowed_attempts


        # OPTIONAL - assignment[annotatable_attachment_id]
        """
            The Attachment ID of the document being annotated.

        Only applies when submission_types includes "student_annotation".
        """
        if assignment_annotatable_attachment_id is not None:
            data["assignment[annotatable_attachment_id]"] = assignment_annotatable_attachment_id


        # OPTIONAL - assignment[submission_types]
        """
            Only applies if the assignment doesn't have student submissions.
        """
        if assignment_submission_types is not None:
            data["assignment[submission_types]"] = assignment_submission_types


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{id}".format(**path), data=data, params=params, single_item=True)

    def bulk_update_assignment_dates(self, course_id):
        """
        Bulk update assignment dates.

        Update due dates and availability dates for multiple assignments in a course.
        
        Accepts a JSON array of objects containing two keys each: +id+, the assignment id,
        and +all_dates+, an array of +AssignmentDate+ structures containing the base and/or override
        dates for the assignment, as returned from the {api:AssignmentsApiController#index List assignments}
        endpoint with +include[]=all_dates+.
        
        This endpoint cannot create or destroy assignment overrides; any existing assignment overrides
        that are not referenced in the arguments will be left alone. If an override is given, any dates
        that are not supplied with it will be defaulted. To clear a date, specify null explicitly.
        
        All referenced assignments will be validated before any are saved. A list of errors will
        be returned if any provided dates are invalid, and no changes will be saved.
        
        The bulk update is performed in a background job, use the {api:ProgressController#show Progress API}
        to check its status.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/bulk_update with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/bulk_update".format(**path), data=data, params=params, single_item=True)

    def list_assignment_overrides(self, assignment_id, course_id):
        """
        List assignment overrides.

        Returns the paginated list of overrides for this assignment that target
        sections/groups/students visible to the current user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides".format(**path), data=data, params=params, all_pages=True)

    def get_single_assignment_override(self, assignment_id, course_id, id):
        """
        Get a single assignment override.

        Returns details of the the override with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def redirect_to_assignment_override_for_group(self, assignment_id, group_id):
        """
        Redirect to the assignment override for a group.

        Responds with a redirect to the override for the given group, if any
        (404 otherwise).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        self.logger.debug("GET /api/v1/groups/{group_id}/assignments/{assignment_id}/override with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/assignments/{assignment_id}/override".format(**path), data=data, params=params, no_data=True)

    def redirect_to_assignment_override_for_section(self, assignment_id, course_section_id):
        """
        Redirect to the assignment override for a section.

        Responds with a redirect to the override for the given section, if any
        (404 otherwise).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_section_id
        """
            ID
        """
        path["course_section_id"] = course_section_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        self.logger.debug("GET /api/v1/sections/{course_section_id}/assignments/{assignment_id}/override with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{course_section_id}/assignments/{assignment_id}/override".format(**path), data=data, params=params, no_data=True)

    def create_assignment_override(self, assignment_id, course_id, assignment_override_course_section_id=None, assignment_override_due_at=None, assignment_override_group_id=None, assignment_override_lock_at=None, assignment_override_student_ids=None, assignment_override_title=None, assignment_override_unlock_at=None):
        """
        Create an assignment override.

        One of student_ids, group_id, or course_section_id must be present. At most
        one should be present; if multiple are present only the most specific
        (student_ids first, then group_id, then course_section_id) is used and any
        others are ignored.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # OPTIONAL - assignment_override[student_ids]
        """
            The IDs of
        the override's target students. If present, the IDs must each identify a
        user with an active student enrollment in the course that is not already
        targetted by a different adhoc override.
        """
        if assignment_override_student_ids is not None:
            data["assignment_override[student_ids]"] = assignment_override_student_ids


        # OPTIONAL - assignment_override[title]
        """
            The title of the adhoc
        assignment override. Required if student_ids is present, ignored
        otherwise (the title is set to the name of the targetted group or section
        instead).
        """
        if assignment_override_title is not None:
            data["assignment_override[title]"] = assignment_override_title


        # OPTIONAL - assignment_override[group_id]
        """
            The ID of the
        override's target group. If present, the following conditions must be met
        for the override to be successful:

        1. the assignment MUST be a group assignment (a group_category_id is assigned to it)
        2. the ID must identify an active group in the group set the assignment is in
        3. the ID must not be targetted by a different override

        See {Appendix: Group assignments} for more info.
        """
        if assignment_override_group_id is not None:
            data["assignment_override[group_id]"] = assignment_override_group_id


        # OPTIONAL - assignment_override[course_section_id]
        """
            The ID
        of the override's target section. If present, must identify an active
        section of the assignment's course not already targetted by a different
        override.
        """
        if assignment_override_course_section_id is not None:
            data["assignment_override[course_section_id]"] = assignment_override_course_section_id


        # OPTIONAL - assignment_override[due_at]
        """
            The day/time
        the overridden assignment is due. Accepts times in ISO 8601 format, e.g.
        2014-10-21T18:48:00Z. If absent, this override will not affect due date.
        May be present but null to indicate the override removes any previous due
        date.
        """
        if assignment_override_due_at is not None:
            if issubclass(assignment_override_due_at.__class__, str):
                assignment_override_due_at = self._validate_iso8601_string(assignment_override_due_at)
            elif issubclass(assignment_override_due_at.__class__, date) or issubclass(assignment_override_due_at.__class__, datetime):
                assignment_override_due_at = assignment_override_due_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment_override[due_at]"] = assignment_override_due_at


        # OPTIONAL - assignment_override[unlock_at]
        """
            The day/time
        the overridden assignment becomes unlocked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the unlock date. May be present but null to indicate the override
        removes any previous unlock date.
        """
        if assignment_override_unlock_at is not None:
            if issubclass(assignment_override_unlock_at.__class__, str):
                assignment_override_unlock_at = self._validate_iso8601_string(assignment_override_unlock_at)
            elif issubclass(assignment_override_unlock_at.__class__, date) or issubclass(assignment_override_unlock_at.__class__, datetime):
                assignment_override_unlock_at = assignment_override_unlock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment_override[unlock_at]"] = assignment_override_unlock_at


        # OPTIONAL - assignment_override[lock_at]
        """
            The day/time
        the overridden assignment becomes locked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the lock date. May be present but null to indicate the override
        removes any previous lock date.
        """
        if assignment_override_lock_at is not None:
            if issubclass(assignment_override_lock_at.__class__, str):
                assignment_override_lock_at = self._validate_iso8601_string(assignment_override_lock_at)
            elif issubclass(assignment_override_lock_at.__class__, date) or issubclass(assignment_override_lock_at.__class__, datetime):
                assignment_override_lock_at = assignment_override_lock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment_override[lock_at]"] = assignment_override_lock_at


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides".format(**path), data=data, params=params, single_item=True)

    def update_assignment_override(self, assignment_id, course_id, id, assignment_override_due_at=None, assignment_override_lock_at=None, assignment_override_student_ids=None, assignment_override_title=None, assignment_override_unlock_at=None):
        """
        Update an assignment override.

        All current overridden values must be supplied if they are to be retained;
        e.g. if due_at was overridden, but this PUT omits a value for due_at,
        due_at will no longer be overridden. If the override is adhoc and
        student_ids is not supplied, the target override set is unchanged. Target
        override sets cannot be changed for group or section overrides.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - assignment_override[student_ids]
        """
            The IDs of the
        override's target students. If present, the IDs must each identify a
        user with an active student enrollment in the course that is not already
        targetted by a different adhoc override. Ignored unless the override
        being updated is adhoc.
        """
        if assignment_override_student_ids is not None:
            data["assignment_override[student_ids]"] = assignment_override_student_ids


        # OPTIONAL - assignment_override[title]
        """
            The title of an adhoc
        assignment override. Ignored unless the override being updated is adhoc.
        """
        if assignment_override_title is not None:
            data["assignment_override[title]"] = assignment_override_title


        # OPTIONAL - assignment_override[due_at]
        """
            The day/time
        the overridden assignment is due. Accepts times in ISO 8601 format, e.g.
        2014-10-21T18:48:00Z. If absent, this override will not affect due date.
        May be present but null to indicate the override removes any previous due
        date.
        """
        if assignment_override_due_at is not None:
            if issubclass(assignment_override_due_at.__class__, str):
                assignment_override_due_at = self._validate_iso8601_string(assignment_override_due_at)
            elif issubclass(assignment_override_due_at.__class__, date) or issubclass(assignment_override_due_at.__class__, datetime):
                assignment_override_due_at = assignment_override_due_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment_override[due_at]"] = assignment_override_due_at


        # OPTIONAL - assignment_override[unlock_at]
        """
            The day/time
        the overridden assignment becomes unlocked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the unlock date. May be present but null to indicate the override
        removes any previous unlock date.
        """
        if assignment_override_unlock_at is not None:
            if issubclass(assignment_override_unlock_at.__class__, str):
                assignment_override_unlock_at = self._validate_iso8601_string(assignment_override_unlock_at)
            elif issubclass(assignment_override_unlock_at.__class__, date) or issubclass(assignment_override_unlock_at.__class__, datetime):
                assignment_override_unlock_at = assignment_override_unlock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment_override[unlock_at]"] = assignment_override_unlock_at


        # OPTIONAL - assignment_override[lock_at]
        """
            The day/time
        the overridden assignment becomes locked. Accepts times in ISO 8601
        format, e.g. 2014-10-21T18:48:00Z. If absent, this override will not
        affect the lock date. May be present but null to indicate the override
        removes any previous lock date.
        """
        if assignment_override_lock_at is not None:
            if issubclass(assignment_override_lock_at.__class__, str):
                assignment_override_lock_at = self._validate_iso8601_string(assignment_override_lock_at)
            elif issubclass(assignment_override_lock_at.__class__, date) or issubclass(assignment_override_lock_at.__class__, datetime):
                assignment_override_lock_at = assignment_override_lock_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["assignment_override[lock_at]"] = assignment_override_lock_at


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_assignment_override(self, assignment_id, course_id, id):
        """
        Delete an assignment override.

        Deletes an override and returns its former details.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{assignment_id}/overrides/{id}".format(**path), data=data, params=params, single_item=True)

    def batch_retrieve_overrides_in_course(self, assignment_overrides_assignment_id, assignment_overrides_id, course_id):
        """
        Batch retrieve overrides in a course.

        Returns a list of specified overrides in this course, providing
        they target sections/groups/students visible to the current user.
        Returns null elements in the list for requests that were not found.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - assignment_overrides[id]
        """
            Ids of overrides to retrieve
        """
        params["assignment_overrides[id]"] = assignment_overrides_id


        # REQUIRED - assignment_overrides[assignment_id]
        """
            Ids of assignments for each override
        """
        params["assignment_overrides[assignment_id]"] = assignment_overrides_assignment_id


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/overrides".format(**path), data=data, params=params, all_pages=True)

    def batch_create_overrides_in_course(self, assignment_overrides, course_id):
        """
        Batch create overrides in a course.

        Creates the specified overrides for each assignment.  Handles creation in a
        transaction, so all records are created or none are.
        
        One of student_ids, group_id, or course_section_id must be present. At most
        one should be present; if multiple are present only the most specific
        (student_ids first, then group_id, then course_section_id) is used and any
        others are ignored.
        
        Errors are reported in an errors attribute, an array of errors corresponding
        to inputs.  Global errors will be reported as a single element errors array
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - assignment_overrides
        """
            Attributes for the new assignment overrides.
        See {api:AssignmentOverridesController#create Create an assignment override} for available
        attributes
        """
        data["assignment_overrides"] = assignment_overrides


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/overrides".format(**path), data=data, params=params, all_pages=True)

    def batch_update_overrides_in_course(self, assignment_overrides, course_id):
        """
        Batch update overrides in a course.

        Updates a list of specified overrides for each assignment.  Handles overrides
        in a transaction, so either all updates are applied or none.
        See {api:AssignmentOverridesController#update Update an assignment override} for
        available attributes.
        
        All current overridden values must be supplied if they are to be retained;
        e.g. if due_at was overridden, but this PUT omits a value for due_at,
        due_at will no longer be overridden. If the override is adhoc and
        student_ids is not supplied, the target override set is unchanged. Target
        override sets cannot be changed for group or section overrides.
        
        Errors are reported in an errors attribute, an array of errors corresponding
        to inputs.  Global errors will be reported as a single element errors array
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - assignment_overrides
        """
            Attributes for the updated overrides.
        """
        data["assignment_overrides"] = assignment_overrides


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/overrides with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/overrides".format(**path), data=data, params=params, all_pages=True)


class Externaltooltagattributes(BaseModel):
    """Externaltooltagattributes Model."""

    def __init__(self, url=None, new_tab=None, resource_link_id=None):
        """Init method for Externaltooltagattributes class."""
        self._url = url
        self._new_tab = new_tab
        self._resource_link_id = resource_link_id

        self.logger = logging.getLogger('py3canvas.Externaltooltagattributes')

    @property
    def url(self):
        """URL to the external tool."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def new_tab(self):
        """Whether or not there is a new tab for the external tool."""
        return self._new_tab

    @new_tab.setter
    def new_tab(self, value):
        """Setter for new_tab property."""
        self.logger.warn("Setting values on new_tab will NOT update the remote Canvas instance.")
        self._new_tab = value

    @property
    def resource_link_id(self):
        """the identifier for this tool_tag."""
        return self._resource_link_id

    @resource_link_id.setter
    def resource_link_id(self, value):
        """Setter for resource_link_id property."""
        self.logger.warn("Setting values on resource_link_id will NOT update the remote Canvas instance.")
        self._resource_link_id = value


class Lockinfo(BaseModel):
    """Lockinfo Model."""

    def __init__(self, asset_string=None, unlock_at=None, lock_at=None, context_module=None, manually_locked=None):
        """Init method for Lockinfo class."""
        self._asset_string = asset_string
        self._unlock_at = unlock_at
        self._lock_at = lock_at
        self._context_module = context_module
        self._manually_locked = manually_locked

        self.logger = logging.getLogger('py3canvas.Lockinfo')

    @property
    def asset_string(self):
        """Asset string for the object causing the lock."""
        return self._asset_string

    @asset_string.setter
    def asset_string(self, value):
        """Setter for asset_string property."""
        self.logger.warn("Setting values on asset_string will NOT update the remote Canvas instance.")
        self._asset_string = value

    @property
    def unlock_at(self):
        """(Optional) Time at which this was/will be unlocked. Must be before the due date."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def lock_at(self):
        """(Optional) Time at which this was/will be locked. Must be after the due date."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def context_module(self):
        """(Optional) Context module causing the lock."""
        return self._context_module

    @context_module.setter
    def context_module(self, value):
        """Setter for context_module property."""
        self.logger.warn("Setting values on context_module will NOT update the remote Canvas instance.")
        self._context_module = value

    @property
    def manually_locked(self):
        """manually_locked."""
        return self._manually_locked

    @manually_locked.setter
    def manually_locked(self, value):
        """Setter for manually_locked property."""
        self.logger.warn("Setting values on manually_locked will NOT update the remote Canvas instance.")
        self._manually_locked = value


class Rubricrating(BaseModel):
    """Rubricrating Model."""

    def __init__(self, points=None, id=None, description=None, long_description=None):
        """Init method for Rubricrating class."""
        self._points = points
        self._id = id
        self._description = description
        self._long_description = long_description

        self.logger = logging.getLogger('py3canvas.Rubricrating')

    @property
    def points(self):
        """points."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn("Setting values on points will NOT update the remote Canvas instance.")
        self._points = value

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def long_description(self):
        """long_description."""
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        """Setter for long_description property."""
        self.logger.warn("Setting values on long_description will NOT update the remote Canvas instance.")
        self._long_description = value


class Rubriccriteria(BaseModel):
    """Rubriccriteria Model."""

    def __init__(self, points=None, id=None, learning_outcome_id=None, vendor_guid=None, description=None, long_description=None, criterion_use_range=None, ratings=None, ignore_for_scoring=None):
        """Init method for Rubriccriteria class."""
        self._points = points
        self._id = id
        self._learning_outcome_id = learning_outcome_id
        self._vendor_guid = vendor_guid
        self._description = description
        self._long_description = long_description
        self._criterion_use_range = criterion_use_range
        self._ratings = ratings
        self._ignore_for_scoring = ignore_for_scoring

        self.logger = logging.getLogger('py3canvas.Rubriccriteria')

    @property
    def points(self):
        """points."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn("Setting values on points will NOT update the remote Canvas instance.")
        self._points = value

    @property
    def id(self):
        """The id of rubric criteria."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def learning_outcome_id(self):
        """(Optional) The id of the learning outcome this criteria uses, if any."""
        return self._learning_outcome_id

    @learning_outcome_id.setter
    def learning_outcome_id(self, value):
        """Setter for learning_outcome_id property."""
        self.logger.warn("Setting values on learning_outcome_id will NOT update the remote Canvas instance.")
        self._learning_outcome_id = value

    @property
    def vendor_guid(self):
        """(Optional) The 3rd party vendor's GUID for the outcome this criteria references, if any."""
        return self._vendor_guid

    @vendor_guid.setter
    def vendor_guid(self, value):
        """Setter for vendor_guid property."""
        self.logger.warn("Setting values on vendor_guid will NOT update the remote Canvas instance.")
        self._vendor_guid = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def long_description(self):
        """long_description."""
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        """Setter for long_description property."""
        self.logger.warn("Setting values on long_description will NOT update the remote Canvas instance.")
        self._long_description = value

    @property
    def criterion_use_range(self):
        """criterion_use_range."""
        return self._criterion_use_range

    @criterion_use_range.setter
    def criterion_use_range(self, value):
        """Setter for criterion_use_range property."""
        self.logger.warn("Setting values on criterion_use_range will NOT update the remote Canvas instance.")
        self._criterion_use_range = value

    @property
    def ratings(self):
        """ratings."""
        return self._ratings

    @ratings.setter
    def ratings(self, value):
        """Setter for ratings property."""
        self.logger.warn("Setting values on ratings will NOT update the remote Canvas instance.")
        self._ratings = value

    @property
    def ignore_for_scoring(self):
        """ignore_for_scoring."""
        return self._ignore_for_scoring

    @ignore_for_scoring.setter
    def ignore_for_scoring(self, value):
        """Setter for ignore_for_scoring property."""
        self.logger.warn("Setting values on ignore_for_scoring will NOT update the remote Canvas instance.")
        self._ignore_for_scoring = value


class Assignmentdate(BaseModel):
    """Assignmentdate Model.
    Object representing a due date for an assignment or quiz. If the due date came from an assignment override, it will have an 'id' field."""

    def __init__(self, id=None, base=None, title=None, due_at=None, unlock_at=None, lock_at=None):
        """Init method for Assignmentdate class."""
        self._id = id
        self._base = base
        self._title = title
        self._due_at = due_at
        self._unlock_at = unlock_at
        self._lock_at = lock_at

        self.logger = logging.getLogger('py3canvas.Assignmentdate')

    @property
    def id(self):
        """(Optional, missing if 'base' is present) id of the assignment override this date represents."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def base(self):
        """(Optional, present if 'id' is missing) whether this date represents the assignment's or quiz's default due date."""
        return self._base

    @base.setter
    def base(self, value):
        """Setter for base property."""
        self.logger.warn("Setting values on base will NOT update the remote Canvas instance.")
        self._base = value

    @property
    def title(self):
        """title."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def due_at(self):
        """The due date for the assignment. Must be between the unlock date and the lock date if there are lock dates."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def unlock_at(self):
        """The unlock date for the assignment. Must be before the due date if there is a due date."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def lock_at(self):
        """The lock date for the assignment. Must be after the due date if there is a due date."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value


class Turnitinsettings(BaseModel):
    """Turnitinsettings Model."""

    def __init__(self, originality_report_visibility=None, s_paper_check=None, internet_check=None, journal_check=None, exclude_biblio=None, exclude_quoted=None, exclude_small_matches_type=None, exclude_small_matches_value=None):
        """Init method for Turnitinsettings class."""
        self._originality_report_visibility = originality_report_visibility
        self._s_paper_check = s_paper_check
        self._internet_check = internet_check
        self._journal_check = journal_check
        self._exclude_biblio = exclude_biblio
        self._exclude_quoted = exclude_quoted
        self._exclude_small_matches_type = exclude_small_matches_type
        self._exclude_small_matches_value = exclude_small_matches_value

        self.logger = logging.getLogger('py3canvas.Turnitinsettings')

    @property
    def originality_report_visibility(self):
        """originality_report_visibility."""
        return self._originality_report_visibility

    @originality_report_visibility.setter
    def originality_report_visibility(self, value):
        """Setter for originality_report_visibility property."""
        self.logger.warn("Setting values on originality_report_visibility will NOT update the remote Canvas instance.")
        self._originality_report_visibility = value

    @property
    def s_paper_check(self):
        """s_paper_check."""
        return self._s_paper_check

    @s_paper_check.setter
    def s_paper_check(self, value):
        """Setter for s_paper_check property."""
        self.logger.warn("Setting values on s_paper_check will NOT update the remote Canvas instance.")
        self._s_paper_check = value

    @property
    def internet_check(self):
        """internet_check."""
        return self._internet_check

    @internet_check.setter
    def internet_check(self, value):
        """Setter for internet_check property."""
        self.logger.warn("Setting values on internet_check will NOT update the remote Canvas instance.")
        self._internet_check = value

    @property
    def journal_check(self):
        """journal_check."""
        return self._journal_check

    @journal_check.setter
    def journal_check(self, value):
        """Setter for journal_check property."""
        self.logger.warn("Setting values on journal_check will NOT update the remote Canvas instance.")
        self._journal_check = value

    @property
    def exclude_biblio(self):
        """exclude_biblio."""
        return self._exclude_biblio

    @exclude_biblio.setter
    def exclude_biblio(self, value):
        """Setter for exclude_biblio property."""
        self.logger.warn("Setting values on exclude_biblio will NOT update the remote Canvas instance.")
        self._exclude_biblio = value

    @property
    def exclude_quoted(self):
        """exclude_quoted."""
        return self._exclude_quoted

    @exclude_quoted.setter
    def exclude_quoted(self, value):
        """Setter for exclude_quoted property."""
        self.logger.warn("Setting values on exclude_quoted will NOT update the remote Canvas instance.")
        self._exclude_quoted = value

    @property
    def exclude_small_matches_type(self):
        """exclude_small_matches_type."""
        return self._exclude_small_matches_type

    @exclude_small_matches_type.setter
    def exclude_small_matches_type(self, value):
        """Setter for exclude_small_matches_type property."""
        self.logger.warn("Setting values on exclude_small_matches_type will NOT update the remote Canvas instance.")
        self._exclude_small_matches_type = value

    @property
    def exclude_small_matches_value(self):
        """exclude_small_matches_value."""
        return self._exclude_small_matches_value

    @exclude_small_matches_value.setter
    def exclude_small_matches_value(self, value):
        """Setter for exclude_small_matches_value property."""
        self.logger.warn("Setting values on exclude_small_matches_value will NOT update the remote Canvas instance.")
        self._exclude_small_matches_value = value


class Needsgradingcount(BaseModel):
    """Needsgradingcount Model.
    Used by Assignment model"""

    def __init__(self, section_id=None, needs_grading_count=None):
        """Init method for Needsgradingcount class."""
        self._section_id = section_id
        self._needs_grading_count = needs_grading_count

        self.logger = logging.getLogger('py3canvas.Needsgradingcount')

    @property
    def section_id(self):
        """The section ID."""
        return self._section_id

    @section_id.setter
    def section_id(self, value):
        """Setter for section_id property."""
        self.logger.warn("Setting values on section_id will NOT update the remote Canvas instance.")
        self._section_id = value

    @property
    def needs_grading_count(self):
        """Number of submissions that need grading."""
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, value):
        """Setter for needs_grading_count property."""
        self.logger.warn("Setting values on needs_grading_count will NOT update the remote Canvas instance.")
        self._needs_grading_count = value


class Scorestatistic(BaseModel):
    """Scorestatistic Model.
    Used by Assignment model"""

    def __init__(self, min=None, max=None, mean=None):
        """Init method for Scorestatistic class."""
        self._min = min
        self._max = max
        self._mean = mean

        self.logger = logging.getLogger('py3canvas.Scorestatistic')

    @property
    def min(self):
        """Min score."""
        return self._min

    @min.setter
    def min(self, value):
        """Setter for min property."""
        self.logger.warn("Setting values on min will NOT update the remote Canvas instance.")
        self._min = value

    @property
    def max(self):
        """Max score."""
        return self._max

    @max.setter
    def max(self, value):
        """Setter for max property."""
        self.logger.warn("Setting values on max will NOT update the remote Canvas instance.")
        self._max = value

    @property
    def mean(self):
        """Mean score."""
        return self._mean

    @mean.setter
    def mean(self, value):
        """Setter for mean property."""
        self.logger.warn("Setting values on mean will NOT update the remote Canvas instance.")
        self._mean = value


class Assignment(BaseModel):
    """Assignment Model."""

    def __init__(self, id=None, name=None, description=None, created_at=None, updated_at=None, due_at=None, lock_at=None, unlock_at=None, has_overrides=None, all_dates=None, course_id=None, html_url=None, submissions_download_url=None, assignment_group_id=None, due_date_required=None, allowed_extensions=None, max_name_length=None, turnitin_enabled=None, vericite_enabled=None, turnitin_settings=None, grade_group_students_individually=None, external_tool_tag_attributes=None, peer_reviews=None, automatic_peer_reviews=None, peer_review_count=None, peer_reviews_assign_at=None, intra_group_peer_reviews=None, group_category_id=None, needs_grading_count=None, needs_grading_count_by_section=None, position=None, post_to_sis=None, integration_id=None, integration_data=None, points_possible=None, submission_types=None, has_submitted_submissions=None, grading_type=None, grading_standard_id=None, published=None, unpublishable=None, only_visible_to_overrides=None, locked_for_user=None, lock_info=None, lock_explanation=None, quiz_id=None, anonymous_submissions=None, discussion_topic=None, freeze_on_copy=None, frozen=None, frozen_attributes=None, submission=None, use_rubric_for_grading=None, rubric_settings=None, rubric=None, assignment_visibility=None, overrides=None, omit_from_final_grade=None, moderated_grading=None, grader_count=None, final_grader_id=None, grader_comments_visible_to_graders=None, graders_anonymous_to_graders=None, grader_names_visible_to_final_grader=None, anonymous_grading=None, allowed_attempts=None, post_manually=None, score_statistics=None, can_submit=None):
        """Init method for Assignment class."""
        self._id = id
        self._name = name
        self._description = description
        self._created_at = created_at
        self._updated_at = updated_at
        self._due_at = due_at
        self._lock_at = lock_at
        self._unlock_at = unlock_at
        self._has_overrides = has_overrides
        self._all_dates = all_dates
        self._course_id = course_id
        self._html_url = html_url
        self._submissions_download_url = submissions_download_url
        self._assignment_group_id = assignment_group_id
        self._due_date_required = due_date_required
        self._allowed_extensions = allowed_extensions
        self._max_name_length = max_name_length
        self._turnitin_enabled = turnitin_enabled
        self._vericite_enabled = vericite_enabled
        self._turnitin_settings = turnitin_settings
        self._grade_group_students_individually = grade_group_students_individually
        self._external_tool_tag_attributes = external_tool_tag_attributes
        self._peer_reviews = peer_reviews
        self._automatic_peer_reviews = automatic_peer_reviews
        self._peer_review_count = peer_review_count
        self._peer_reviews_assign_at = peer_reviews_assign_at
        self._intra_group_peer_reviews = intra_group_peer_reviews
        self._group_category_id = group_category_id
        self._needs_grading_count = needs_grading_count
        self._needs_grading_count_by_section = needs_grading_count_by_section
        self._position = position
        self._post_to_sis = post_to_sis
        self._integration_id = integration_id
        self._integration_data = integration_data
        self._points_possible = points_possible
        self._submission_types = submission_types
        self._has_submitted_submissions = has_submitted_submissions
        self._grading_type = grading_type
        self._grading_standard_id = grading_standard_id
        self._published = published
        self._unpublishable = unpublishable
        self._only_visible_to_overrides = only_visible_to_overrides
        self._locked_for_user = locked_for_user
        self._lock_info = lock_info
        self._lock_explanation = lock_explanation
        self._quiz_id = quiz_id
        self._anonymous_submissions = anonymous_submissions
        self._discussion_topic = discussion_topic
        self._freeze_on_copy = freeze_on_copy
        self._frozen = frozen
        self._frozen_attributes = frozen_attributes
        self._submission = submission
        self._use_rubric_for_grading = use_rubric_for_grading
        self._rubric_settings = rubric_settings
        self._rubric = rubric
        self._assignment_visibility = assignment_visibility
        self._overrides = overrides
        self._omit_from_final_grade = omit_from_final_grade
        self._moderated_grading = moderated_grading
        self._grader_count = grader_count
        self._final_grader_id = final_grader_id
        self._grader_comments_visible_to_graders = grader_comments_visible_to_graders
        self._graders_anonymous_to_graders = graders_anonymous_to_graders
        self._grader_names_visible_to_final_grader = grader_names_visible_to_final_grader
        self._anonymous_grading = anonymous_grading
        self._allowed_attempts = allowed_attempts
        self._post_manually = post_manually
        self._score_statistics = score_statistics
        self._can_submit = can_submit

        self.logger = logging.getLogger('py3canvas.Assignment')

    @property
    def id(self):
        """the ID of the assignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def name(self):
        """the name of the assignment."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def description(self):
        """the assignment description, in an HTML fragment."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def created_at(self):
        """The time at which this assignment was originally created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """The time at which this assignment was last modified in any way."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def due_at(self):
        """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def lock_at(self):
        """the lock date (assignment is locked after this date). returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the lock date as it applies to the user requesting information from the API."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

    @property
    def unlock_at(self):
        """the unlock date (assignment is unlocked after this date) returns null if not present NOTE: If this assignment has assignment overrides, this field will be the unlock date as it applies to the user requesting information from the API."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def has_overrides(self):
        """whether this assignment has overrides."""
        return self._has_overrides

    @has_overrides.setter
    def has_overrides(self, value):
        """Setter for has_overrides property."""
        self.logger.warn("Setting values on has_overrides will NOT update the remote Canvas instance.")
        self._has_overrides = value

    @property
    def all_dates(self):
        """(Optional) all dates associated with the assignment, if applicable."""
        return self._all_dates

    @all_dates.setter
    def all_dates(self, value):
        """Setter for all_dates property."""
        self.logger.warn("Setting values on all_dates will NOT update the remote Canvas instance.")
        self._all_dates = value

    @property
    def course_id(self):
        """the ID of the course the assignment belongs to."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def html_url(self):
        """the URL to the assignment's web page."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def submissions_download_url(self):
        """the URL to download all submissions as a zip."""
        return self._submissions_download_url

    @submissions_download_url.setter
    def submissions_download_url(self, value):
        """Setter for submissions_download_url property."""
        self.logger.warn("Setting values on submissions_download_url will NOT update the remote Canvas instance.")
        self._submissions_download_url = value

    @property
    def assignment_group_id(self):
        """the ID of the assignment's group."""
        return self._assignment_group_id

    @assignment_group_id.setter
    def assignment_group_id(self, value):
        """Setter for assignment_group_id property."""
        self.logger.warn("Setting values on assignment_group_id will NOT update the remote Canvas instance.")
        self._assignment_group_id = value

    @property
    def due_date_required(self):
        """Boolean flag indicating whether the assignment requires a due date based on the account level setting."""
        return self._due_date_required

    @due_date_required.setter
    def due_date_required(self, value):
        """Setter for due_date_required property."""
        self.logger.warn("Setting values on due_date_required will NOT update the remote Canvas instance.")
        self._due_date_required = value

    @property
    def allowed_extensions(self):
        """Allowed file extensions, which take effect if submission_types includes 'online_upload'."""
        return self._allowed_extensions

    @allowed_extensions.setter
    def allowed_extensions(self, value):
        """Setter for allowed_extensions property."""
        self.logger.warn("Setting values on allowed_extensions will NOT update the remote Canvas instance.")
        self._allowed_extensions = value

    @property
    def max_name_length(self):
        """An integer indicating the maximum length an assignment's name may be."""
        return self._max_name_length

    @max_name_length.setter
    def max_name_length(self, value):
        """Setter for max_name_length property."""
        self.logger.warn("Setting values on max_name_length will NOT update the remote Canvas instance.")
        self._max_name_length = value

    @property
    def turnitin_enabled(self):
        """Boolean flag indicating whether or not Turnitin has been enabled for the assignment. NOTE: This flag will not appear unless your account has the Turnitin plugin available."""
        return self._turnitin_enabled

    @turnitin_enabled.setter
    def turnitin_enabled(self, value):
        """Setter for turnitin_enabled property."""
        self.logger.warn("Setting values on turnitin_enabled will NOT update the remote Canvas instance.")
        self._turnitin_enabled = value

    @property
    def vericite_enabled(self):
        """Boolean flag indicating whether or not VeriCite has been enabled for the assignment. NOTE: This flag will not appear unless your account has the VeriCite plugin available."""
        return self._vericite_enabled

    @vericite_enabled.setter
    def vericite_enabled(self, value):
        """Setter for vericite_enabled property."""
        self.logger.warn("Setting values on vericite_enabled will NOT update the remote Canvas instance.")
        self._vericite_enabled = value

    @property
    def turnitin_settings(self):
        """Settings to pass along to turnitin to control what kinds of matches should be considered. originality_report_visibility can be 'immediate', 'after_grading', 'after_due_date', or 'never' exclude_small_matches_type can be null, 'percent', 'words' exclude_small_matches_value: - if type is null, this will be null also - if type is 'percent', this will be a number between 0 and 100 representing match size to exclude as a percentage of the document size. - if type is 'words', this will be number > 0 representing how many words a match must contain for it to be considered NOTE: This flag will not appear unless your account has the Turnitin plugin available."""
        return self._turnitin_settings

    @turnitin_settings.setter
    def turnitin_settings(self, value):
        """Setter for turnitin_settings property."""
        self.logger.warn("Setting values on turnitin_settings will NOT update the remote Canvas instance.")
        self._turnitin_settings = value

    @property
    def grade_group_students_individually(self):
        """If this is a group assignment, boolean flag indicating whether or not students will be graded individually."""
        return self._grade_group_students_individually

    @grade_group_students_individually.setter
    def grade_group_students_individually(self, value):
        """Setter for grade_group_students_individually property."""
        self.logger.warn("Setting values on grade_group_students_individually will NOT update the remote Canvas instance.")
        self._grade_group_students_individually = value

    @property
    def external_tool_tag_attributes(self):
        """(Optional) assignment's settings for external tools if submission_types include 'external_tool'. Only url and new_tab are included (new_tab defaults to false).  Use the 'External Tools' API if you need more information about an external tool."""
        return self._external_tool_tag_attributes

    @external_tool_tag_attributes.setter
    def external_tool_tag_attributes(self, value):
        """Setter for external_tool_tag_attributes property."""
        self.logger.warn("Setting values on external_tool_tag_attributes will NOT update the remote Canvas instance.")
        self._external_tool_tag_attributes = value

    @property
    def peer_reviews(self):
        """Boolean indicating if peer reviews are required for this assignment."""
        return self._peer_reviews

    @peer_reviews.setter
    def peer_reviews(self, value):
        """Setter for peer_reviews property."""
        self.logger.warn("Setting values on peer_reviews will NOT update the remote Canvas instance.")
        self._peer_reviews = value

    @property
    def automatic_peer_reviews(self):
        """Boolean indicating peer reviews are assigned automatically. If false, the teacher is expected to manually assign peer reviews."""
        return self._automatic_peer_reviews

    @automatic_peer_reviews.setter
    def automatic_peer_reviews(self, value):
        """Setter for automatic_peer_reviews property."""
        self.logger.warn("Setting values on automatic_peer_reviews will NOT update the remote Canvas instance.")
        self._automatic_peer_reviews = value

    @property
    def peer_review_count(self):
        """Integer representing the amount of reviews each user is assigned. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true."""
        return self._peer_review_count

    @peer_review_count.setter
    def peer_review_count(self, value):
        """Setter for peer_review_count property."""
        self.logger.warn("Setting values on peer_review_count will NOT update the remote Canvas instance.")
        self._peer_review_count = value

    @property
    def peer_reviews_assign_at(self):
        """String representing a date the reviews are due by. Must be a date that occurs after the default due date. If blank, or date is not after the assignment's due date, the assignment's due date will be used. NOTE: This key is NOT present unless you have automatic_peer_reviews set to true."""
        return self._peer_reviews_assign_at

    @peer_reviews_assign_at.setter
    def peer_reviews_assign_at(self, value):
        """Setter for peer_reviews_assign_at property."""
        self.logger.warn("Setting values on peer_reviews_assign_at will NOT update the remote Canvas instance.")
        self._peer_reviews_assign_at = value

    @property
    def intra_group_peer_reviews(self):
        """Boolean representing whether or not members from within the same group on a group assignment can be assigned to peer review their own group's work."""
        return self._intra_group_peer_reviews

    @intra_group_peer_reviews.setter
    def intra_group_peer_reviews(self, value):
        """Setter for intra_group_peer_reviews property."""
        self.logger.warn("Setting values on intra_group_peer_reviews will NOT update the remote Canvas instance.")
        self._intra_group_peer_reviews = value

    @property
    def group_category_id(self):
        """The ID of the assignment’s group set, if this is a group assignment. For group discussions, set group_category_id on the discussion topic, not the linked assignment."""
        return self._group_category_id

    @group_category_id.setter
    def group_category_id(self, value):
        """Setter for group_category_id property."""
        self.logger.warn("Setting values on group_category_id will NOT update the remote Canvas instance.")
        self._group_category_id = value

    @property
    def needs_grading_count(self):
        """if the requesting user has grading rights, the number of submissions that need grading."""
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, value):
        """Setter for needs_grading_count property."""
        self.logger.warn("Setting values on needs_grading_count will NOT update the remote Canvas instance.")
        self._needs_grading_count = value

    @property
    def needs_grading_count_by_section(self):
        """if the requesting user has grading rights and the 'needs_grading_count_by_section' flag is specified, the number of submissions that need grading split out by section. NOTE: This key is NOT present unless you pass the 'needs_grading_count_by_section' argument as true.  ANOTHER NOTE: it's possible to be enrolled in multiple sections, and if a student is setup that way they will show an assignment that needs grading in multiple sections (effectively the count will be duplicated between sections)."""
        return self._needs_grading_count_by_section

    @needs_grading_count_by_section.setter
    def needs_grading_count_by_section(self, value):
        """Setter for needs_grading_count_by_section property."""
        self.logger.warn("Setting values on needs_grading_count_by_section will NOT update the remote Canvas instance.")
        self._needs_grading_count_by_section = value

    @property
    def position(self):
        """the sorting order of the assignment in the group."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn("Setting values on position will NOT update the remote Canvas instance.")
        self._position = value

    @property
    def post_to_sis(self):
        """(optional, present if Sync Grades to SIS feature is enabled)."""
        return self._post_to_sis

    @post_to_sis.setter
    def post_to_sis(self, value):
        """Setter for post_to_sis property."""
        self.logger.warn("Setting values on post_to_sis will NOT update the remote Canvas instance.")
        self._post_to_sis = value

    @property
    def integration_id(self):
        """(optional, Third Party unique identifier for Assignment)."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn("Setting values on integration_id will NOT update the remote Canvas instance.")
        self._integration_id = value

    @property
    def integration_data(self):
        """(optional, Third Party integration data for assignment)."""
        return self._integration_data

    @integration_data.setter
    def integration_data(self, value):
        """Setter for integration_data property."""
        self.logger.warn("Setting values on integration_data will NOT update the remote Canvas instance.")
        self._integration_data = value

    @property
    def points_possible(self):
        """the maximum points possible for the assignment."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

    @property
    def submission_types(self):
        """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'."""
        return self._submission_types

    @submission_types.setter
    def submission_types(self, value):
        """Setter for submission_types property."""
        self.logger.warn("Setting values on submission_types will NOT update the remote Canvas instance.")
        self._submission_types = value

    @property
    def has_submitted_submissions(self):
        """If true, the assignment has been submitted to by at least one student."""
        return self._has_submitted_submissions

    @has_submitted_submissions.setter
    def has_submitted_submissions(self, value):
        """Setter for has_submitted_submissions property."""
        self.logger.warn("Setting values on has_submitted_submissions will NOT update the remote Canvas instance.")
        self._has_submitted_submissions = value

    @property
    def grading_type(self):
        """The type of grading the assignment receives; one of 'pass_fail', 'percent', 'letter_grade', 'gpa_scale', 'points'."""
        return self._grading_type

    @grading_type.setter
    def grading_type(self, value):
        """Setter for grading_type property."""
        self.logger.warn("Setting values on grading_type will NOT update the remote Canvas instance.")
        self._grading_type = value

    @property
    def grading_standard_id(self):
        """The id of the grading standard being applied to this assignment. Valid if grading_type is 'letter_grade' or 'gpa_scale'."""
        return self._grading_standard_id

    @grading_standard_id.setter
    def grading_standard_id(self, value):
        """Setter for grading_standard_id property."""
        self.logger.warn("Setting values on grading_standard_id will NOT update the remote Canvas instance.")
        self._grading_standard_id = value

    @property
    def published(self):
        """Whether the assignment is published."""
        return self._published

    @published.setter
    def published(self, value):
        """Setter for published property."""
        self.logger.warn("Setting values on published will NOT update the remote Canvas instance.")
        self._published = value

    @property
    def unpublishable(self):
        """Whether the assignment's 'published' state can be changed to false. Will be false if there are student submissions for the assignment."""
        return self._unpublishable

    @unpublishable.setter
    def unpublishable(self, value):
        """Setter for unpublishable property."""
        self.logger.warn("Setting values on unpublishable will NOT update the remote Canvas instance.")
        self._unpublishable = value

    @property
    def only_visible_to_overrides(self):
        """Whether the assignment is only visible to overrides."""
        return self._only_visible_to_overrides

    @only_visible_to_overrides.setter
    def only_visible_to_overrides(self, value):
        """Setter for only_visible_to_overrides property."""
        self.logger.warn("Setting values on only_visible_to_overrides will NOT update the remote Canvas instance.")
        self._only_visible_to_overrides = value

    @property
    def locked_for_user(self):
        """Whether or not this is locked for the user."""
        return self._locked_for_user

    @locked_for_user.setter
    def locked_for_user(self, value):
        """Setter for locked_for_user property."""
        self.logger.warn("Setting values on locked_for_user will NOT update the remote Canvas instance.")
        self._locked_for_user = value

    @property
    def lock_info(self):
        """(Optional) Information for the user about the lock. Present when locked_for_user is true."""
        return self._lock_info

    @lock_info.setter
    def lock_info(self, value):
        """Setter for lock_info property."""
        self.logger.warn("Setting values on lock_info will NOT update the remote Canvas instance.")
        self._lock_info = value

    @property
    def lock_explanation(self):
        """(Optional) An explanation of why this is locked for the user. Present when locked_for_user is true."""
        return self._lock_explanation

    @lock_explanation.setter
    def lock_explanation(self, value):
        """Setter for lock_explanation property."""
        self.logger.warn("Setting values on lock_explanation will NOT update the remote Canvas instance.")
        self._lock_explanation = value

    @property
    def quiz_id(self):
        """(Optional) id of the associated quiz (applies only when submission_types is ['online_quiz'])."""
        return self._quiz_id

    @quiz_id.setter
    def quiz_id(self, value):
        """Setter for quiz_id property."""
        self.logger.warn("Setting values on quiz_id will NOT update the remote Canvas instance.")
        self._quiz_id = value

    @property
    def anonymous_submissions(self):
        """(Optional) whether anonymous submissions are accepted (applies only to quiz assignments)."""
        return self._anonymous_submissions

    @anonymous_submissions.setter
    def anonymous_submissions(self, value):
        """Setter for anonymous_submissions property."""
        self.logger.warn("Setting values on anonymous_submissions will NOT update the remote Canvas instance.")
        self._anonymous_submissions = value

    @property
    def discussion_topic(self):
        """(Optional) the DiscussionTopic associated with the assignment, if applicable."""
        return self._discussion_topic

    @discussion_topic.setter
    def discussion_topic(self, value):
        """Setter for discussion_topic property."""
        self.logger.warn("Setting values on discussion_topic will NOT update the remote Canvas instance.")
        self._discussion_topic = value

    @property
    def freeze_on_copy(self):
        """(Optional) Boolean indicating if assignment will be frozen when it is copied. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account."""
        return self._freeze_on_copy

    @freeze_on_copy.setter
    def freeze_on_copy(self, value):
        """Setter for freeze_on_copy property."""
        self.logger.warn("Setting values on freeze_on_copy will NOT update the remote Canvas instance.")
        self._freeze_on_copy = value

    @property
    def frozen(self):
        """(Optional) Boolean indicating if assignment is frozen for the calling user. NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account."""
        return self._frozen

    @frozen.setter
    def frozen(self, value):
        """Setter for frozen property."""
        self.logger.warn("Setting values on frozen will NOT update the remote Canvas instance.")
        self._frozen = value

    @property
    def frozen_attributes(self):
        """(Optional) Array of frozen attributes for the assignment. Only account administrators currently have permission to change an attribute in this list. Will be empty if no attributes are frozen for this assignment. Possible frozen attributes are: title, description, lock_at, points_possible, grading_type, submission_types, assignment_group_id, allowed_extensions, group_category_id, notify_of_update, peer_reviews NOTE: This field will only be present if the AssignmentFreezer plugin is available for your account."""
        return self._frozen_attributes

    @frozen_attributes.setter
    def frozen_attributes(self, value):
        """Setter for frozen_attributes property."""
        self.logger.warn("Setting values on frozen_attributes will NOT update the remote Canvas instance.")
        self._frozen_attributes = value

    @property
    def submission(self):
        """(Optional) If 'submission' is included in the 'include' parameter, includes a Submission object that represents the current user's (user who is requesting information from the api) current submission for the assignment. See the Submissions API for an example response. If the user does not have a submission, this key will be absent."""
        return self._submission

    @submission.setter
    def submission(self, value):
        """Setter for submission property."""
        self.logger.warn("Setting values on submission will NOT update the remote Canvas instance.")
        self._submission = value

    @property
    def use_rubric_for_grading(self):
        """(Optional) If true, the rubric is directly tied to grading the assignment. Otherwise, it is only advisory. Included if there is an associated rubric."""
        return self._use_rubric_for_grading

    @use_rubric_for_grading.setter
    def use_rubric_for_grading(self, value):
        """Setter for use_rubric_for_grading property."""
        self.logger.warn("Setting values on use_rubric_for_grading will NOT update the remote Canvas instance.")
        self._use_rubric_for_grading = value

    @property
    def rubric_settings(self):
        """(Optional) An object describing the basic attributes of the rubric, including the point total. Included if there is an associated rubric."""
        return self._rubric_settings

    @rubric_settings.setter
    def rubric_settings(self, value):
        """Setter for rubric_settings property."""
        self.logger.warn("Setting values on rubric_settings will NOT update the remote Canvas instance.")
        self._rubric_settings = value

    @property
    def rubric(self):
        """(Optional) A list of scoring criteria and ratings for each rubric criterion. Included if there is an associated rubric."""
        return self._rubric

    @rubric.setter
    def rubric(self, value):
        """Setter for rubric property."""
        self.logger.warn("Setting values on rubric will NOT update the remote Canvas instance.")
        self._rubric = value

    @property
    def assignment_visibility(self):
        """(Optional) If 'assignment_visibility' is included in the 'include' parameter, includes an array of student IDs who can see this assignment."""
        return self._assignment_visibility

    @assignment_visibility.setter
    def assignment_visibility(self, value):
        """Setter for assignment_visibility property."""
        self.logger.warn("Setting values on assignment_visibility will NOT update the remote Canvas instance.")
        self._assignment_visibility = value

    @property
    def overrides(self):
        """(Optional) If 'overrides' is included in the 'include' parameter, includes an array of assignment override objects."""
        return self._overrides

    @overrides.setter
    def overrides(self, value):
        """Setter for overrides property."""
        self.logger.warn("Setting values on overrides will NOT update the remote Canvas instance.")
        self._overrides = value

    @property
    def omit_from_final_grade(self):
        """(Optional) If true, the assignment will be omitted from the student's final grade."""
        return self._omit_from_final_grade

    @omit_from_final_grade.setter
    def omit_from_final_grade(self, value):
        """Setter for omit_from_final_grade property."""
        self.logger.warn("Setting values on omit_from_final_grade will NOT update the remote Canvas instance.")
        self._omit_from_final_grade = value

    @property
    def moderated_grading(self):
        """Boolean indicating if the assignment is moderated."""
        return self._moderated_grading

    @moderated_grading.setter
    def moderated_grading(self, value):
        """Setter for moderated_grading property."""
        self.logger.warn("Setting values on moderated_grading will NOT update the remote Canvas instance.")
        self._moderated_grading = value

    @property
    def grader_count(self):
        """The maximum number of provisional graders who may issue grades for this assignment. Only relevant for moderated assignments. Must be a positive value, and must be set to 1 if the course has fewer than two active instructors. Otherwise, the maximum value is the number of active instructors in the course minus one, or 10 if the course has more than 11 active instructors."""
        return self._grader_count

    @grader_count.setter
    def grader_count(self, value):
        """Setter for grader_count property."""
        self.logger.warn("Setting values on grader_count will NOT update the remote Canvas instance.")
        self._grader_count = value

    @property
    def final_grader_id(self):
        """The user ID of the grader responsible for choosing final grades for this assignment. Only relevant for moderated assignments."""
        return self._final_grader_id

    @final_grader_id.setter
    def final_grader_id(self, value):
        """Setter for final_grader_id property."""
        self.logger.warn("Setting values on final_grader_id will NOT update the remote Canvas instance.")
        self._final_grader_id = value

    @property
    def grader_comments_visible_to_graders(self):
        """Boolean indicating if provisional graders' comments are visible to other provisional graders. Only relevant for moderated assignments."""
        return self._grader_comments_visible_to_graders

    @grader_comments_visible_to_graders.setter
    def grader_comments_visible_to_graders(self, value):
        """Setter for grader_comments_visible_to_graders property."""
        self.logger.warn("Setting values on grader_comments_visible_to_graders will NOT update the remote Canvas instance.")
        self._grader_comments_visible_to_graders = value

    @property
    def graders_anonymous_to_graders(self):
        """Boolean indicating if provisional graders' identities are hidden from other provisional graders. Only relevant for moderated assignments with grader_comments_visible_to_graders set to true."""
        return self._graders_anonymous_to_graders

    @graders_anonymous_to_graders.setter
    def graders_anonymous_to_graders(self, value):
        """Setter for graders_anonymous_to_graders property."""
        self.logger.warn("Setting values on graders_anonymous_to_graders will NOT update the remote Canvas instance.")
        self._graders_anonymous_to_graders = value

    @property
    def grader_names_visible_to_final_grader(self):
        """Boolean indicating if provisional grader identities are visible to the final grader. Only relevant for moderated assignments."""
        return self._grader_names_visible_to_final_grader

    @grader_names_visible_to_final_grader.setter
    def grader_names_visible_to_final_grader(self, value):
        """Setter for grader_names_visible_to_final_grader property."""
        self.logger.warn("Setting values on grader_names_visible_to_final_grader will NOT update the remote Canvas instance.")
        self._grader_names_visible_to_final_grader = value

    @property
    def anonymous_grading(self):
        """Boolean indicating if the assignment is graded anonymously. If true, graders cannot see student identities."""
        return self._anonymous_grading

    @anonymous_grading.setter
    def anonymous_grading(self, value):
        """Setter for anonymous_grading property."""
        self.logger.warn("Setting values on anonymous_grading will NOT update the remote Canvas instance.")
        self._anonymous_grading = value

    @property
    def allowed_attempts(self):
        """The number of submission attempts a student can make for this assignment. -1 is considered unlimited."""
        return self._allowed_attempts

    @allowed_attempts.setter
    def allowed_attempts(self, value):
        """Setter for allowed_attempts property."""
        self.logger.warn("Setting values on allowed_attempts will NOT update the remote Canvas instance.")
        self._allowed_attempts = value

    @property
    def post_manually(self):
        """Whether the assignment has manual posting enabled. Only relevant for courses using New Gradebook."""
        return self._post_manually

    @post_manually.setter
    def post_manually(self, value):
        """Setter for post_manually property."""
        self.logger.warn("Setting values on post_manually will NOT update the remote Canvas instance.")
        self._post_manually = value

    @property
    def score_statistics(self):
        """(Optional) If 'score_statistics' and 'submission' are included in the 'include' parameter and statistics are available, includes the min, max, and mode for this assignment."""
        return self._score_statistics

    @score_statistics.setter
    def score_statistics(self, value):
        """Setter for score_statistics property."""
        self.logger.warn("Setting values on score_statistics will NOT update the remote Canvas instance.")
        self._score_statistics = value

    @property
    def can_submit(self):
        """(Optional) If retrieving a single assignment and 'can_submit' is included in the 'include' parameter, flags whether user has the right to submit the assignment (i.e. checks enrollment dates, submission types, locked status, attempts remaining, etc...). Including 'can submit' automatically includes 'submission' in the include parameter. Not available when observed_users are included."""
        return self._can_submit

    @can_submit.setter
    def can_submit(self, value):
        """Setter for can_submit property."""
        self.logger.warn("Setting values on can_submit will NOT update the remote Canvas instance.")
        self._can_submit = value


class Assignmentoverride(BaseModel):
    """Assignmentoverride Model."""

    def __init__(self, id=None, assignment_id=None, student_ids=None, group_id=None, course_section_id=None, title=None, due_at=None, all_day=None, all_day_date=None, unlock_at=None, lock_at=None):
        """Init method for Assignmentoverride class."""
        self._id = id
        self._assignment_id = assignment_id
        self._student_ids = student_ids
        self._group_id = group_id
        self._course_section_id = course_section_id
        self._title = title
        self._due_at = due_at
        self._all_day = all_day
        self._all_day_date = all_day_date
        self._unlock_at = unlock_at
        self._lock_at = lock_at

        self.logger = logging.getLogger('py3canvas.Assignmentoverride')

    @property
    def id(self):
        """the ID of the assignment override."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def assignment_id(self):
        """the ID of the assignment the override applies to."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn("Setting values on assignment_id will NOT update the remote Canvas instance.")
        self._assignment_id = value

    @property
    def student_ids(self):
        """the IDs of the override's target students (present if the override targets an ad-hoc set of students)."""
        return self._student_ids

    @student_ids.setter
    def student_ids(self, value):
        """Setter for student_ids property."""
        self.logger.warn("Setting values on student_ids will NOT update the remote Canvas instance.")
        self._student_ids = value

    @property
    def group_id(self):
        """the ID of the override's target group (present if the override targets a group and the assignment is a group assignment)."""
        return self._group_id

    @group_id.setter
    def group_id(self, value):
        """Setter for group_id property."""
        self.logger.warn("Setting values on group_id will NOT update the remote Canvas instance.")
        self._group_id = value

    @property
    def course_section_id(self):
        """the ID of the overrides's target section (present if the override targets a section)."""
        return self._course_section_id

    @course_section_id.setter
    def course_section_id(self, value):
        """Setter for course_section_id property."""
        self.logger.warn("Setting values on course_section_id will NOT update the remote Canvas instance.")
        self._course_section_id = value

    @property
    def title(self):
        """the title of the override."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def due_at(self):
        """the overridden due at (present if due_at is overridden)."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn("Setting values on due_at will NOT update the remote Canvas instance.")
        self._due_at = value

    @property
    def all_day(self):
        """the overridden all day flag (present if due_at is overridden)."""
        return self._all_day

    @all_day.setter
    def all_day(self, value):
        """Setter for all_day property."""
        self.logger.warn("Setting values on all_day will NOT update the remote Canvas instance.")
        self._all_day = value

    @property
    def all_day_date(self):
        """the overridden all day date (present if due_at is overridden)."""
        return self._all_day_date

    @all_day_date.setter
    def all_day_date(self, value):
        """Setter for all_day_date property."""
        self.logger.warn("Setting values on all_day_date will NOT update the remote Canvas instance.")
        self._all_day_date = value

    @property
    def unlock_at(self):
        """the overridden unlock at (present if unlock_at is overridden)."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn("Setting values on unlock_at will NOT update the remote Canvas instance.")
        self._unlock_at = value

    @property
    def lock_at(self):
        """the overridden lock at, if any (present if lock_at is overridden)."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn("Setting values on lock_at will NOT update the remote Canvas instance.")
        self._lock_at = value

