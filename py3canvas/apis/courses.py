"""Courses API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class CoursesAPI(BaseCanvasAPI):
    """Courses API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CoursesAPI."""
        super(CoursesAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.CoursesAPI")

    def list_your_courses(
        self,
        enrollment_role=None,
        enrollment_role_id=None,
        enrollment_state=None,
        enrollment_type=None,
        exclude_blueprint_courses=None,
        include=None,
        state=None,
    ):
        """
        List your courses.

        Returns the paginated list of active courses for the current user.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - enrollment_type
        """
            When set, only return courses where the user is enrolled as this type. For
        example, set to "teacher" to return only courses where the user is
        enrolled as a Teacher.  This argument is ignored if enrollment_role is given.
        """
        if enrollment_type is not None:
            self._validate_enum(
                enrollment_type, ["teacher", "student", "ta", "observer", "designer"]
            )
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - enrollment_role
        """
            Deprecated
        When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a base role type of
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'.
        """
        if enrollment_role is not None:
            params["enrollment_role"] = enrollment_role

        # OPTIONAL - enrollment_role_id
        """
            When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a built_in role type of
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'.
        """
        if enrollment_role_id is not None:
            params["enrollment_role_id"] = enrollment_role_id

        # OPTIONAL - enrollment_state
        """
            When set, only return courses where the user has an enrollment with the given state.
        This will respect section/course/term date overrides.
        """
        if enrollment_state is not None:
            self._validate_enum(
                enrollment_state, ["active", "invited_or_pending", "completed"]
            )
            params["enrollment_state"] = enrollment_state

        # OPTIONAL - exclude_blueprint_courses
        """
            When set, only return courses that are not configured as blueprint courses.
        """
        if exclude_blueprint_courses is not None:
            params["exclude_blueprint_courses"] = exclude_blueprint_courses

        # OPTIONAL - include
        """
            - "needs_grading_count": Optional information to include with each Course.
          When needs_grading_count is given, and the current user has grading
          rights, the total number of submissions needing grading for all
          assignments is returned.
        - "syllabus_body": Optional information to include with each Course.
          When syllabus_body is given the user-generated html for the course
          syllabus is returned.
        - "public_description": Optional information to include with each Course.
          When public_description is given the user-generated text for the course
          public description is returned.
        - "total_scores": Optional information to include with each Course.
          When total_scores is given, any student enrollments will also
          include the fields 'computed_current_score', 'computed_final_score',
          'computed_current_grade', and 'computed_final_grade', as well as (if
          the user has permission) 'unposted_current_score',
          'unposted_final_score', 'unposted_current_grade', and
          'unposted_final_grade' (see Enrollment documentation for more
          information on these fields). This argument is ignored if the course is
          configured to hide final grades.
        - "current_grading_period_scores": Optional information to include with
          each Course. When current_grading_period_scores is given and total_scores
          is given, any student enrollments will also include the fields
          'has_grading_periods',
          'totals_for_all_grading_periods_option', 'current_grading_period_title',
          'current_grading_period_id', current_period_computed_current_score',
          'current_period_computed_final_score',
          'current_period_computed_current_grade', and
          'current_period_computed_final_grade', as well as (if the user has permission)
          'current_period_unposted_current_score',
          'current_period_unposted_final_score',
          'current_period_unposted_current_grade', and
          'current_period_unposted_final_grade' (see Enrollment documentation for
          more information on these fields). In addition, when this argument is
          passed, the course will have a 'has_grading_periods' attribute
          on it. This argument is ignored if the total_scores argument is not
          included. If the course is configured to hide final grades, the
          following fields are not returned:
          'totals_for_all_grading_periods_option',
          'current_period_computed_current_score',
          'current_period_computed_final_score',
          'current_period_computed_current_grade',
          'current_period_computed_final_grade',
          'current_period_unposted_current_score',
          'current_period_unposted_final_score',
          'current_period_unposted_current_grade', and
          'current_period_unposted_final_grade'
        - "grading_periods": Optional information to include with each Course. When
          grading_periods is given, a list of the grading periods associated with
          each course is returned.
        - "term": Optional information to include with each Course. When
          term is given, the information for the enrollment term for each course
          is returned.
        - "account": Optional information to include with each Course. When
          account is given, the account json for each course is returned.
        - "course_progress": Optional information to include with each Course.
          When course_progress is given, each course will include a
          'course_progress' object with the fields: 'requirement_count', an integer
          specifying the total number of requirements in the course,
          'requirement_completed_count', an integer specifying the total number of
          requirements in this course that have been completed, and
          'next_requirement_url', a string url to the next requirement item, and
          'completed_at', the date the course was completed (null if incomplete).
          'next_requirement_url' will be null if all requirements have been
          completed or the current module does not require sequential progress.
          "course_progress" will return an error message if the course is not
          module based or the user is not enrolled as a student in the course.
        - "sections": Section enrollment information to include with each Course.
          Returns an array of hashes containing the section ID (id), section name
          (name), start and end dates (start_at, end_at), as well as the enrollment
          type (enrollment_role, e.g. 'StudentEnrollment').
        - "storage_quota_used_mb": The amount of storage space used by the files in this course
        - "total_students": Optional information to include with each Course.
          Returns an integer for the total amount of active and invited students.
        - "passback_status": Include the grade passback_status
        - "favorites": Optional information to include with each Course.
          Indicates if the user has marked the course as a favorite course.
        - "teachers": Teacher information to include with each Course.
          Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information
          for each teacher in the course.
        - "observed_users": Optional information to include with each Course.
          Will include data for observed users if the current user has an
          observer enrollment.
        - "tabs": Optional information to include with each Course.
          Will include the list of tabs configured for each course.  See the
          {api:TabsController#index List available tabs API} for more information.
        - "course_image": Optional course image data for when there is a course image
          and the course image feature flag has been enabled
        - "concluded": Optional information to include with each Course. Indicates whether
          the course has been concluded, taking course and term dates into account.
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "needs_grading_count",
                    "syllabus_body",
                    "public_description",
                    "total_scores",
                    "current_grading_period_scores",
                    "grading_periods",
                    "term",
                    "account",
                    "course_progress",
                    "sections",
                    "storage_quota_used_mb",
                    "total_students",
                    "passback_status",
                    "favorites",
                    "teachers",
                    "observed_users",
                    "course_image",
                    "concluded",
                ],
            )
            params["include"] = include

        # OPTIONAL - state
        """
            If set, only return courses that are in the given state(s).
        By default, "available" is returned for students and observers, and
        anything except "deleted", for all other enrollment types
        """
        if state is not None:
            self._validate_enum(
                state, ["unpublished", "available", "completed", "deleted"]
            )
            params["state"] = state

        self.logger.debug(
            "GET /api/v1/courses with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_courses_for_user(
        self, user_id, enrollment_state=None, homeroom=None, include=None, state=None
    ):
        """
        List courses for a user.

        Returns a paginated list of active courses for this user. To view the course list for a user other than yourself, you must be either an observer of that user or an administrator.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        # OPTIONAL - include
        """
            - "needs_grading_count": Optional information to include with each Course.
          When needs_grading_count is given, and the current user has grading
          rights, the total number of submissions needing grading for all
          assignments is returned.
        - "syllabus_body": Optional information to include with each Course.
          When syllabus_body is given the user-generated html for the course
          syllabus is returned.
        - "public_description": Optional information to include with each Course.
          When public_description is given the user-generated text for the course
          public description is returned.
        - "total_scores": Optional information to include with each Course.
          When total_scores is given, any student enrollments will also
          include the fields 'computed_current_score', 'computed_final_score',
          'computed_current_grade', and 'computed_final_grade' (see Enrollment
          documentation for more information on these fields). This argument
          is ignored if the course is configured to hide final grades.
        - "current_grading_period_scores": Optional information to include with
          each Course. When current_grading_period_scores is given and total_scores
          is given, any student enrollments will also include the fields
          'has_grading_periods',
          'totals_for_all_grading_periods_option', 'current_grading_period_title',
          'current_grading_period_id', current_period_computed_current_score',
          'current_period_computed_final_score',
          'current_period_computed_current_grade', and
          'current_period_computed_final_grade', as well as (if the user has permission)
          'current_period_unposted_current_score',
          'current_period_unposted_final_score',
          'current_period_unposted_current_grade', and
          'current_period_unposted_final_grade' (see Enrollment documentation for
          more information on these fields). In addition, when this argument is
          passed, the course will have a 'has_grading_periods' attribute
          on it. This argument is ignored if the course is configured to hide final
          grades or if the total_scores argument is not included.
        - "grading_periods": Optional information to include with each Course. When
          grading_periods is given, a list of the grading periods associated with
          each course is returned.
        - "term": Optional information to include with each Course. When
          term is given, the information for the enrollment term for each course
          is returned.
        - "account": Optional information to include with each Course. When
          account is given, the account json for each course is returned.
        - "course_progress": Optional information to include with each Course.
          When course_progress is given, each course will include a
          'course_progress' object with the fields: 'requirement_count', an integer
          specifying the total number of requirements in the course,
          'requirement_completed_count', an integer specifying the total number of
          requirements in this course that have been completed, and
          'next_requirement_url', a string url to the next requirement item, and
          'completed_at', the date the course was completed (null if incomplete).
          'next_requirement_url' will be null if all requirements have been
          completed or the current module does not require sequential progress.
          "course_progress" will return an error message if the course is not
          module based or the user is not enrolled as a student in the course.
        - "sections": Section enrollment information to include with each Course.
          Returns an array of hashes containing the section ID (id), section name
          (name), start and end dates (start_at, end_at), as well as the enrollment
          type (enrollment_role, e.g. 'StudentEnrollment').
        - "storage_quota_used_mb": The amount of storage space used by the files in this course
        - "total_students": Optional information to include with each Course.
          Returns an integer for the total amount of active and invited students.
        - "passback_status": Include the grade passback_status
        - "favorites": Optional information to include with each Course.
          Indicates if the user has marked the course as a favorite course.
        - "teachers": Teacher information to include with each Course.
          Returns an array of hashes containing the {api:Users:UserDisplay UserDisplay} information
          for each teacher in the course.
        - "observed_users": Optional information to include with each Course.
          Will include data for observed users if the current user has an
          observer enrollment.
        - "tabs": Optional information to include with each Course.
          Will include the list of tabs configured for each course.  See the
          {api:TabsController#index List available tabs API} for more information.
        - "course_image": Optional course image data for when there is a course image
          and the course image feature flag has been enabled
        - "concluded": Optional information to include with each Course. Indicates whether
          the course has been concluded, taking course and term dates into account.
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "needs_grading_count",
                    "syllabus_body",
                    "public_description",
                    "total_scores",
                    "current_grading_period_scores",
                    "grading_periods",
                    "term",
                    "account",
                    "course_progress",
                    "sections",
                    "storage_quota_used_mb",
                    "total_students",
                    "passback_status",
                    "favorites",
                    "teachers",
                    "observed_users",
                    "course_image",
                    "concluded",
                ],
            )
            params["include"] = include

        # OPTIONAL - state
        """
            If set, only return courses that are in the given state(s).
        By default, "available" is returned for students and observers, and
        anything except "deleted", for all other enrollment types
        """
        if state is not None:
            self._validate_enum(
                state, ["unpublished", "available", "completed", "deleted"]
            )
            params["state"] = state

        # OPTIONAL - enrollment_state
        """
            When set, only return courses where the user has an enrollment with the given state.
        This will respect section/course/term date overrides.
        """
        if enrollment_state is not None:
            self._validate_enum(
                enrollment_state, ["active", "invited_or_pending", "completed"]
            )
            params["enrollment_state"] = enrollment_state

        # OPTIONAL - homeroom
        """
            If set, only return homeroom courses.
        """
        if homeroom is not None:
            params["homeroom"] = homeroom

        self.logger.debug(
            "GET /api/v1/users/{user_id}/courses with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/users/{user_id}/courses".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def get_user_progress(self, course_id, user_id):
        """
        Get user progress.

        Return progress information for the user and course

        You can supply +self+ as the user_id to query your own progress in a course. To query another user's progress,
        you must be a teacher in the course, an administrator, or a linked observer of the user.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/users/{user_id}/progress with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/users/{user_id}/progress".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def create_new_course(
        self,
        account_id,
        course_allow_student_forum_attachments=None,
        course_allow_student_wiki_edits=None,
        course_allow_wiki_comments=None,
        course_apply_assignment_group_weights=None,
        course_course_code=None,
        course_course_format=None,
        course_default_view=None,
        course_end_at=None,
        course_grade_passback_setting=None,
        course_grading_standard_id=None,
        course_hide_final_grades=None,
        course_integration_id=None,
        course_is_public=None,
        course_is_public_to_auth_users=None,
        course_license=None,
        course_name=None,
        course_open_enrollment=None,
        course_public_description=None,
        course_public_syllabus=None,
        course_public_syllabus_to_auth=None,
        course_restrict_enrollments_to_course_dates=None,
        course_self_enrollment=None,
        course_sis_course_id=None,
        course_start_at=None,
        course_syllabus_body=None,
        course_term_id=None,
        course_time_zone=None,
        enable_sis_reactivation=None,
        enroll_me=None,
        offer=None,
    ):
        """
        Create a new course.

        Create a new course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - course[name]
        """
            The name of the course. If omitted, the course will be named "Unnamed
        Course."
        """
        if course_name is not None:
            data["course[name]"] = course_name

        # OPTIONAL - course[course_code]
        """
            The course code for the course.
        """
        if course_course_code is not None:
            data["course[course_code]"] = course_course_code

        # OPTIONAL - course[start_at]
        """
            Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true.
        """
        if course_start_at is not None:
            if issubclass(course_start_at.__class__, str):
                course_start_at = self._validate_iso8601_string(course_start_at)
            elif issubclass(course_start_at.__class__, date) or issubclass(
                course_start_at.__class__, datetime
            ):
                course_start_at = course_start_at.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            data["course[start_at]"] = course_start_at

        # OPTIONAL - course[end_at]
        """
            Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true.
        """
        if course_end_at is not None:
            if issubclass(course_end_at.__class__, str):
                course_end_at = self._validate_iso8601_string(course_end_at)
            elif issubclass(course_end_at.__class__, date) or issubclass(
                course_end_at.__class__, datetime
            ):
                course_end_at = course_end_at.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            data["course[end_at]"] = course_end_at

        # OPTIONAL - course[license]
        """
            The name of the licensing. Should be one of the following abbreviations
        (a descriptive name is included in parenthesis for reference):
        - 'private' (Private Copyrighted)
        - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives)
        - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike)
        - 'cc_by_nc' (CC Attribution Non-Commercial)
        - 'cc_by_nd' (CC Attribution No Derivatives)
        - 'cc_by_sa' (CC Attribution Share Alike)
        - 'cc_by' (CC Attribution)
        - 'public_domain' (Public Domain).
        """
        if course_license is not None:
            data["course[license]"] = course_license

        # OPTIONAL - course[is_public]
        """
            Set to true if course is public to both authenticated and unauthenticated users.
        """
        if course_is_public is not None:
            data["course[is_public]"] = course_is_public

        # OPTIONAL - course[is_public_to_auth_users]
        """
            Set to true if course is public only to authenticated users.
        """
        if course_is_public_to_auth_users is not None:
            data["course[is_public_to_auth_users]"] = course_is_public_to_auth_users

        # OPTIONAL - course[public_syllabus]
        """
            Set to true to make the course syllabus public.
        """
        if course_public_syllabus is not None:
            data["course[public_syllabus]"] = course_public_syllabus

        # OPTIONAL - course[public_syllabus_to_auth]
        """
            Set to true to make the course syllabus public for authenticated users.
        """
        if course_public_syllabus_to_auth is not None:
            data["course[public_syllabus_to_auth]"] = course_public_syllabus_to_auth

        # OPTIONAL - course[public_description]
        """
            A publicly visible description of the course.
        """
        if course_public_description is not None:
            data["course[public_description]"] = course_public_description

        # OPTIONAL - course[allow_student_wiki_edits]
        """
            If true, students will be able to modify the course wiki.
        """
        if course_allow_student_wiki_edits is not None:
            data["course[allow_student_wiki_edits]"] = course_allow_student_wiki_edits

        # OPTIONAL - course[allow_wiki_comments]
        """
            If true, course members will be able to comment on wiki pages.
        """
        if course_allow_wiki_comments is not None:
            data["course[allow_wiki_comments]"] = course_allow_wiki_comments

        # OPTIONAL - course[allow_student_forum_attachments]
        """
            If true, students can attach files to forum posts.
        """
        if course_allow_student_forum_attachments is not None:
            data[
                "course[allow_student_forum_attachments]"
            ] = course_allow_student_forum_attachments

        # OPTIONAL - course[open_enrollment]
        """
            Set to true if the course is open enrollment.
        """
        if course_open_enrollment is not None:
            data["course[open_enrollment]"] = course_open_enrollment

        # OPTIONAL - course[self_enrollment]
        """
            Set to true if the course is self enrollment.
        """
        if course_self_enrollment is not None:
            data["course[self_enrollment]"] = course_self_enrollment

        # OPTIONAL - course[restrict_enrollments_to_course_dates]
        """
            Set to true to restrict user enrollments to the start and end dates of the
        course. This parameter is required when using the API, as this option is
        not displayed in the Course Settings page. This value must be set to true
        in order to specify a course start date and/or end date.
        """
        if course_restrict_enrollments_to_course_dates is not None:
            data[
                "course[restrict_enrollments_to_course_dates]"
            ] = course_restrict_enrollments_to_course_dates

        # OPTIONAL - course[term_id]
        """
            The unique ID of the term to create to course in.
        """
        if course_term_id is not None:
            data["course[term_id]"] = course_term_id

        # OPTIONAL - course[sis_course_id]
        """
            The unique SIS identifier.
        """
        if course_sis_course_id is not None:
            data["course[sis_course_id]"] = course_sis_course_id

        # OPTIONAL - course[integration_id]
        """
            The unique Integration identifier.
        """
        if course_integration_id is not None:
            data["course[integration_id]"] = course_integration_id

        # OPTIONAL - course[hide_final_grades]
        """
            If this option is set to true, the totals in student grades summary will
        be hidden.
        """
        if course_hide_final_grades is not None:
            data["course[hide_final_grades]"] = course_hide_final_grades

        # OPTIONAL - course[apply_assignment_group_weights]
        """
            Set to true to weight final grade based on assignment groups percentages.
        """
        if course_apply_assignment_group_weights is not None:
            data[
                "course[apply_assignment_group_weights]"
            ] = course_apply_assignment_group_weights

        # OPTIONAL - course[time_zone]
        """
            The time zone for the course. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        """
        if course_time_zone is not None:
            data["course[time_zone]"] = course_time_zone

        # OPTIONAL - offer
        """
            If this option is set to true, the course will be available to students
        immediately.
        """
        if offer is not None:
            data["offer"] = offer

        # OPTIONAL - enroll_me
        """
            Set to true to enroll the current user as the teacher.
        """
        if enroll_me is not None:
            data["enroll_me"] = enroll_me

        # OPTIONAL - course[default_view]
        """
            The type of page that users will see when they first visit the course
        * 'feed' Recent Activity Dashboard
        * 'modules' Course Modules/Sections Page
        * 'assignments' Course Assignments List
        * 'syllabus' Course Syllabus Page
        other types may be added in the future
        """
        if course_default_view is not None:
            self._validate_enum(
                course_default_view,
                ["feed", "wiki", "modules", "syllabus", "assignments"],
            )
            data["course[default_view]"] = course_default_view

        # OPTIONAL - course[syllabus_body]
        """
            The syllabus body for the course
        """
        if course_syllabus_body is not None:
            data["course[syllabus_body]"] = course_syllabus_body

        # OPTIONAL - course[grading_standard_id]
        """
            The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
        """
        if course_grading_standard_id is not None:
            data["course[grading_standard_id]"] = course_grading_standard_id

        # OPTIONAL - course[grade_passback_setting]
        """
            Optional. The grade_passback_setting for the course. Only 'nightly_sync', 'disabled', and '' are allowed
        """
        if course_grade_passback_setting is not None:
            data["course[grade_passback_setting]"] = course_grade_passback_setting

        # OPTIONAL - course[course_format]
        """
            Optional. Specifies the format of the course. (Should be 'on_campus', 'online', or 'blended')
        """
        if course_course_format is not None:
            data["course[course_format]"] = course_course_format

        # OPTIONAL - enable_sis_reactivation
        """
            When true, will first try to re-activate a deleted course with matching sis_course_id if possible.
        """
        if enable_sis_reactivation is not None:
            data["enable_sis_reactivation"] = enable_sis_reactivation

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/courses with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/courses".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def upload_file(self, course_id):
        """
        Upload a file.

        Upload a file to the course.

        This API endpoint is the first step in uploading a file to a course.
        See the {file:file_uploads.html File Upload Documentation} for details on
        the file upload workflow.

        Only those with the "Manage Files" permission on a course can upload files
        to the course. By default, this is Teachers, TAs and Designers.
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
            "POST /api/v1/courses/{course_id}/files with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/files".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_students(self, course_id):
        """
        List students.

        Returns the paginated list of students enrolled in this course.

        DEPRECATED: Please use the {api:CoursesController#users course users} endpoint
        and pass "student" as the enrollment_type.
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
            "GET /api/v1/courses/{course_id}/students with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/students".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_users_in_course_users(
        self,
        course_id,
        enrollment_role=None,
        enrollment_role_id=None,
        enrollment_state=None,
        enrollment_type=None,
        include=None,
        search_term=None,
        sort=None,
        user_id=None,
        user_ids=None,
    ):
        """
        List users in course.

        Returns the paginated list of users in this course. And optionally the user's enrollments in the course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - search_term
        """
            The partial name or full ID of the users to match and return in the results list.
        """
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - sort
        """
            When set, sort the results of the search based on the given field.
        """
        if sort is not None:
            self._validate_enum(sort, ["username", "last_login", "email", "sis_id"])
            params["sort"] = sort

        # OPTIONAL - enrollment_type
        """
            When set, only return users where the user is enrolled as this type.
        "student_view" implies include[]=test_student.
        This argument is ignored if enrollment_role is given.
        """
        if enrollment_type is not None:
            self._validate_enum(
                enrollment_type,
                ["teacher", "student", "student_view", "ta", "observer", "designer"],
            )
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - enrollment_role
        """
            Deprecated
        When set, only return users enrolled with the specified course-level role.  This can be
        a role created with the {api:RoleOverridesController#add_role Add Role API} or a
        base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'ObserverEnrollment', or 'DesignerEnrollment'.
        """
        if enrollment_role is not None:
            params["enrollment_role"] = enrollment_role

        # OPTIONAL - enrollment_role_id
        """
            When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'.
        """
        if enrollment_role_id is not None:
            params["enrollment_role_id"] = enrollment_role_id

        # OPTIONAL - include
        """
            - "enrollments":
        Optionally include with each Course the user's current and invited
        enrollments. If the user is enrolled as a student, and the account has
        permission to manage or view all grades, each enrollment will include a
        'grades' key with 'current_score', 'final_score', 'current_grade' and
        'final_grade' values.
        - "locked": Optionally include whether an enrollment is locked.
        - "avatar_url": Optionally include avatar_url.
        - "bio": Optionally include each user's bio.
        - "test_student": Optionally include the course's Test Student,
        if present. Default is to not include Test Student.
        - "custom_links": Optionally include plugin-supplied custom links for each student,
        such as analytics information
        - "current_grading_period_scores": if enrollments is included as
        well as this directive, the scores returned in the enrollment
        will be for the current grading period if there is one. A
        'grading_period_id' value will also be included with the
        scores. if grading_period_id is nil there is no current grading
        period and the score is a total score.
        - "uuid": Optionally include the users uuid
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "enrollments",
                    "locked",
                    "avatar_url",
                    "test_student",
                    "bio",
                    "custom_links",
                    "current_grading_period_scores",
                    "uuid",
                ],
            )
            params["include"] = include

        # OPTIONAL - user_id
        """
            If this parameter is given and it corresponds to a user in the course,
        the +page+ parameter will be ignored and the page containing the specified user
        will be returned instead.
        """
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - user_ids
        """
            If included, the course users set will only include users with IDs
        specified by the param. Note: this will not work in conjunction
        with the "user_id" argument but multiple user_ids can be included.
        """
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - enrollment_state
        """
            When set, only return users where the enrollment workflow state is of one of the given types.
        "active" and "invited" enrollments are returned by default.
        """
        if enrollment_state is not None:
            self._validate_enum(
                enrollment_state,
                ["active", "invited", "rejected", "completed", "inactive"],
            )
            params["enrollment_state"] = enrollment_state

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/users with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/users".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_users_in_course_search_users(
        self,
        course_id,
        enrollment_role=None,
        enrollment_role_id=None,
        enrollment_state=None,
        enrollment_type=None,
        include=None,
        search_term=None,
        sort=None,
        user_id=None,
        user_ids=None,
    ):
        """
        List users in course.

        Returns the paginated list of users in this course. And optionally the user's enrollments in the course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - search_term
        """
            The partial name or full ID of the users to match and return in the results list.
        """
        if search_term is not None:
            params["search_term"] = search_term

        # OPTIONAL - sort
        """
            When set, sort the results of the search based on the given field.
        """
        if sort is not None:
            self._validate_enum(sort, ["username", "last_login", "email", "sis_id"])
            params["sort"] = sort

        # OPTIONAL - enrollment_type
        """
            When set, only return users where the user is enrolled as this type.
        "student_view" implies include[]=test_student.
        This argument is ignored if enrollment_role is given.
        """
        if enrollment_type is not None:
            self._validate_enum(
                enrollment_type,
                ["teacher", "student", "student_view", "ta", "observer", "designer"],
            )
            params["enrollment_type"] = enrollment_type

        # OPTIONAL - enrollment_role
        """
            Deprecated
        When set, only return users enrolled with the specified course-level role.  This can be
        a role created with the {api:RoleOverridesController#add_role Add Role API} or a
        base role type of 'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment',
        'ObserverEnrollment', or 'DesignerEnrollment'.
        """
        if enrollment_role is not None:
            params["enrollment_role"] = enrollment_role

        # OPTIONAL - enrollment_role_id
        """
            When set, only return courses where the user is enrolled with the specified
        course-level role.  This can be a role created with the
        {api:RoleOverridesController#add_role Add Role API} or a built_in role id with type
        'StudentEnrollment', 'TeacherEnrollment', 'TaEnrollment', 'ObserverEnrollment',
        or 'DesignerEnrollment'.
        """
        if enrollment_role_id is not None:
            params["enrollment_role_id"] = enrollment_role_id

        # OPTIONAL - include
        """
            - "enrollments":
        Optionally include with each Course the user's current and invited
        enrollments. If the user is enrolled as a student, and the account has
        permission to manage or view all grades, each enrollment will include a
        'grades' key with 'current_score', 'final_score', 'current_grade' and
        'final_grade' values.
        - "locked": Optionally include whether an enrollment is locked.
        - "avatar_url": Optionally include avatar_url.
        - "bio": Optionally include each user's bio.
        - "test_student": Optionally include the course's Test Student,
        if present. Default is to not include Test Student.
        - "custom_links": Optionally include plugin-supplied custom links for each student,
        such as analytics information
        - "current_grading_period_scores": if enrollments is included as
        well as this directive, the scores returned in the enrollment
        will be for the current grading period if there is one. A
        'grading_period_id' value will also be included with the
        scores. if grading_period_id is nil there is no current grading
        period and the score is a total score.
        - "uuid": Optionally include the users uuid
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "enrollments",
                    "locked",
                    "avatar_url",
                    "test_student",
                    "bio",
                    "custom_links",
                    "current_grading_period_scores",
                    "uuid",
                ],
            )
            params["include"] = include

        # OPTIONAL - user_id
        """
            If this parameter is given and it corresponds to a user in the course,
        the +page+ parameter will be ignored and the page containing the specified user
        will be returned instead.
        """
        if user_id is not None:
            params["user_id"] = user_id

        # OPTIONAL - user_ids
        """
            If included, the course users set will only include users with IDs
        specified by the param. Note: this will not work in conjunction
        with the "user_id" argument but multiple user_ids can be included.
        """
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - enrollment_state
        """
            When set, only return users where the enrollment workflow state is of one of the given types.
        "active" and "invited" enrollments are returned by default.
        """
        if enrollment_state is not None:
            self._validate_enum(
                enrollment_state,
                ["active", "invited", "rejected", "completed", "inactive"],
            )
            params["enrollment_state"] = enrollment_state

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/search_users with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/search_users".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def list_recently_logged_in_students(self, course_id):
        """
        List recently logged in students.

        Returns the paginated list of users in this course, ordered by how recently they have
        logged in. The records include the 'last_login' field which contains
        a timestamp of the last time that user logged into canvas.  The querying
        user must have the 'View usage reports' permission.
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
            "GET /api/v1/courses/{course_id}/recent_students with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/recent_students".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def get_single_user(self, course_id, id):
        """
        Get single user.

        Return information on a single user.

        Accepts the same include[] parameters as the :users: action, and returns a
        single user with the same fields as that action.
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

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/users/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/users/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def search_for_content_share_users(self, course_id, search_term):
        """
        Search for content share users.

        Returns a paginated list of users you can share content with.  Requires the content share
        feature and the user must have the manage content permission for the course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - search_term
        """
            Term used to find users.  Will search available share users with the search term in their name.
        """
        params["search_term"] = search_term

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/content_share_users with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/content_share_users".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def preview_processed_html(self, course_id, html=None):
        """
        Preview processed html.

        Preview html content processed for this course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - html
        """
            The html content to process
        """
        if html is not None:
            data["html"] = html

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/preview_html with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/preview_html".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def course_activity_stream(self, course_id):
        """
        Course activity stream.

        Returns the current user's course-specific activity stream, paginated.

        For full documentation, see the API documentation for the user activity
        stream, in the user api.
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
            "GET /api/v1/courses/{course_id}/activity_stream with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/activity_stream".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def course_activity_stream_summary(self, course_id):
        """
        Course activity stream summary.

        Returns a summary of the current user's course-specific activity stream.

        For full documentation, see the API documentation for the user activity
        stream summary, in the user api.
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
            "GET /api/v1/courses/{course_id}/activity_stream/summary with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/activity_stream/summary".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def course_todo_items(self, course_id):
        """
        Course TODO items.

        Returns the current user's course-specific todo items.

        For full documentation, see the API documentation for the user todo items, in the user api.
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
            "GET /api/v1/courses/{course_id}/todo with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/todo".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def delete_conclude_course(self, event, id):
        """
        Delete/Conclude a course.

        Delete or conclude an existing course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # REQUIRED - event
        """
            The action to take on the course.
        """
        self._validate_enum(event, ["delete", "conclude"])
        params["event"] = event

        self.logger.debug(
            "DELETE /api/v1/courses/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/courses/{id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_course_settings(self, course_id):
        """
        Get course settings.

        Returns some of a course's settings.
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
            "GET /api/v1/courses/{course_id}/settings with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/settings".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def update_course_settings(
        self,
        course_id,
        allow_student_discussion_editing=None,
        allow_student_discussion_topics=None,
        allow_student_forum_attachments=None,
        allow_student_organized_groups=None,
        filter_speed_grader_by_student_group=None,
        hide_distribution_graphs=None,
        hide_final_grades=None,
        hide_sections_on_course_users_page=None,
        home_page_announcement_limit=None,
        lock_all_announcements=None,
        restrict_student_future_view=None,
        restrict_student_past_view=None,
        show_announcements_on_home_page=None,
        syllabus_course_summary=None,
        usage_rights_required=None,
    ):
        """
        Update course settings.

        Can update the following course settings:
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - allow_student_discussion_topics
        """
            Let students create discussion topics
        """
        if allow_student_discussion_topics is not None:
            data["allow_student_discussion_topics"] = allow_student_discussion_topics

        # OPTIONAL - allow_student_forum_attachments
        """
            Let students attach files to discussions
        """
        if allow_student_forum_attachments is not None:
            data["allow_student_forum_attachments"] = allow_student_forum_attachments

        # OPTIONAL - allow_student_discussion_editing
        """
            Let students edit or delete their own discussion posts
        """
        if allow_student_discussion_editing is not None:
            data["allow_student_discussion_editing"] = allow_student_discussion_editing

        # OPTIONAL - allow_student_organized_groups
        """
            Let students organize their own groups
        """
        if allow_student_organized_groups is not None:
            data["allow_student_organized_groups"] = allow_student_organized_groups

        # OPTIONAL - filter_speed_grader_by_student_group
        """
            Filter SpeedGrader to only the selected student group
        """
        if filter_speed_grader_by_student_group is not None:
            data[
                "filter_speed_grader_by_student_group"
            ] = filter_speed_grader_by_student_group

        # OPTIONAL - hide_final_grades
        """
            Hide totals in student grades summary
        """
        if hide_final_grades is not None:
            data["hide_final_grades"] = hide_final_grades

        # OPTIONAL - hide_distribution_graphs
        """
            Hide grade distribution graphs from students
        """
        if hide_distribution_graphs is not None:
            data["hide_distribution_graphs"] = hide_distribution_graphs

        # OPTIONAL - hide_sections_on_course_users_page
        """
            Disallow students from viewing students in sections they do not belong to
        """
        if hide_sections_on_course_users_page is not None:
            data[
                "hide_sections_on_course_users_page"
            ] = hide_sections_on_course_users_page

        # OPTIONAL - lock_all_announcements
        """
            Disable comments on announcements
        """
        if lock_all_announcements is not None:
            data["lock_all_announcements"] = lock_all_announcements

        # OPTIONAL - usage_rights_required
        """
            Copyright and license information must be provided for files before they are published.
        """
        if usage_rights_required is not None:
            data["usage_rights_required"] = usage_rights_required

        # OPTIONAL - restrict_student_past_view
        """
            Restrict students from viewing courses after end date
        """
        if restrict_student_past_view is not None:
            data["restrict_student_past_view"] = restrict_student_past_view

        # OPTIONAL - restrict_student_future_view
        """
            Restrict students from viewing courses before start date
        """
        if restrict_student_future_view is not None:
            data["restrict_student_future_view"] = restrict_student_future_view

        # OPTIONAL - show_announcements_on_home_page
        """
            Show the most recent announcements on the Course home page (if a Wiki, defaults to five announcements, configurable via home_page_announcement_limit).
        Canvas for Elementary subjects ignore this setting.
        """
        if show_announcements_on_home_page is not None:
            data["show_announcements_on_home_page"] = show_announcements_on_home_page

        # OPTIONAL - home_page_announcement_limit
        """
            Limit the number of announcements on the home page if enabled via show_announcements_on_home_page
        """
        if home_page_announcement_limit is not None:
            data["home_page_announcement_limit"] = home_page_announcement_limit

        # OPTIONAL - syllabus_course_summary
        """
            Show the course summary (list of assignments and calendar events) on the syllabus page. Default is true.
        """
        if syllabus_course_summary is not None:
            data["syllabus_course_summary"] = syllabus_course_summary

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/settings with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/settings".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def return_test_student_for_course(self, course_id):
        """
        Return test student for course.

        Returns information for a test student in this course. Creates a test
        student if one does not already exist for the course. The caller must have
        permission to access the course's student view.
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
            "GET /api/v1/courses/{course_id}/student_view_student with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/student_view_student".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_single_course_courses(self, id, include=None, teacher_limit=None):
        """
        Get a single course.

        Return information on a single course.

        Accepts the same include[] parameters as the list action plus:
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
            - "all_courses": Also search recently deleted courses.
        - "permissions": Include permissions the current user has
          for the course.
        - "observed_users": include observed users in the enrollments
        - "course_image": Optional course image data for when there is a course image
          and the course image feature flag has been enabled
        - "concluded": Optional information to include with each Course. Indicates whether
          the course has been concluded, taking course and term dates into account.
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "needs_grading_count",
                    "syllabus_body",
                    "public_description",
                    "total_scores",
                    "current_grading_period_scores",
                    "term",
                    "account",
                    "course_progress",
                    "sections",
                    "storage_quota_used_mb",
                    "total_students",
                    "passback_status",
                    "favorites",
                    "teachers",
                    "observed_users",
                    "all_courses",
                    "permissions",
                    "observed_users",
                    "course_image",
                    "concluded",
                ],
            )
            params["include"] = include

        # OPTIONAL - teacher_limit
        """
            The maximum number of teacher enrollments to show.
        If the course contains more teachers than this, instead of giving the teacher
        enrollments, the count of teachers will be given under a _teacher_count_ key.
        """
        if teacher_limit is not None:
            params["teacher_limit"] = teacher_limit

        self.logger.debug(
            "GET /api/v1/courses/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_single_course_accounts(
        self, account_id, id, include=None, teacher_limit=None
    ):
        """
        Get a single course.

        Return information on a single course.

        Accepts the same include[] parameters as the list action plus:
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

        # OPTIONAL - include
        """
            - "all_courses": Also search recently deleted courses.
        - "permissions": Include permissions the current user has
          for the course.
        - "observed_users": include observed users in the enrollments
        - "course_image": Optional course image data for when there is a course image
          and the course image feature flag has been enabled
        - "concluded": Optional information to include with each Course. Indicates whether
          the course has been concluded, taking course and term dates into account.
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "needs_grading_count",
                    "syllabus_body",
                    "public_description",
                    "total_scores",
                    "current_grading_period_scores",
                    "term",
                    "account",
                    "course_progress",
                    "sections",
                    "storage_quota_used_mb",
                    "total_students",
                    "passback_status",
                    "favorites",
                    "teachers",
                    "observed_users",
                    "all_courses",
                    "permissions",
                    "observed_users",
                    "course_image",
                    "concluded",
                ],
            )
            params["include"] = include

        # OPTIONAL - teacher_limit
        """
            The maximum number of teacher enrollments to show.
        If the course contains more teachers than this, instead of giving the teacher
        enrollments, the count of teachers will be given under a _teacher_count_ key.
        """
        if teacher_limit is not None:
            params["teacher_limit"] = teacher_limit

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/courses/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/courses/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_course(
        self,
        id,
        course_account_id=None,
        course_allow_student_forum_attachments=None,
        course_allow_student_wiki_edits=None,
        course_allow_wiki_comments=None,
        course_apply_assignment_group_weights=None,
        course_blueprint=None,
        course_blueprint_restrictions=None,
        course_blueprint_restrictions_by_object_type=None,
        course_course_code=None,
        course_course_color=None,
        course_course_format=None,
        course_default_view=None,
        course_enable_pace_plans=None,
        course_end_at=None,
        course_event=None,
        course_friendly_name=None,
        course_grade_passback_setting=None,
        course_grading_standard_id=None,
        course_hide_final_grades=None,
        course_homeroom_course=None,
        course_homeroom_course_id=None,
        course_image_id=None,
        course_image_url=None,
        course_integration_id=None,
        course_is_public=None,
        course_is_public_to_auth_users=None,
        course_license=None,
        course_name=None,
        course_open_enrollment=None,
        course_public_description=None,
        course_public_syllabus=None,
        course_public_syllabus_to_auth=None,
        course_remove_banner_image=None,
        course_remove_image=None,
        course_restrict_enrollments_to_course_dates=None,
        course_self_enrollment=None,
        course_sis_course_id=None,
        course_start_at=None,
        course_storage_quota_mb=None,
        course_syllabus_body=None,
        course_syllabus_course_summary=None,
        course_sync_enrollments_from_homeroom=None,
        course_template=None,
        course_term_id=None,
        course_time_zone=None,
        course_use_blueprint_restrictions_by_object_type=None,
        offer=None,
    ):
        """
        Update a course.

        Update an existing course.

        Arguments are the same as Courses#create, with a few exceptions (enroll_me).

        If a user has content management rights, but not full course editing rights, the only attribute
        editable through this endpoint will be "syllabus_body"
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        # OPTIONAL - course[account_id]
        """
            The unique ID of the account to move the course to.
        """
        if course_account_id is not None:
            data["course[account_id]"] = course_account_id

        # OPTIONAL - course[name]
        """
            The name of the course. If omitted, the course will be named "Unnamed
        Course."
        """
        if course_name is not None:
            data["course[name]"] = course_name

        # OPTIONAL - course[course_code]
        """
            The course code for the course.
        """
        if course_course_code is not None:
            data["course[course_code]"] = course_course_code

        # OPTIONAL - course[start_at]
        """
            Course start date in ISO8601 format, e.g. 2011-01-01T01:00Z
        This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true,
        or the course is already published.
        """
        if course_start_at is not None:
            if issubclass(course_start_at.__class__, str):
                course_start_at = self._validate_iso8601_string(course_start_at)
            elif issubclass(course_start_at.__class__, date) or issubclass(
                course_start_at.__class__, datetime
            ):
                course_start_at = course_start_at.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            data["course[start_at]"] = course_start_at

        # OPTIONAL - course[end_at]
        """
            Course end date in ISO8601 format. e.g. 2011-01-01T01:00Z
        This value is ignored unless 'restrict_enrollments_to_course_dates' is set to true.
        """
        if course_end_at is not None:
            if issubclass(course_end_at.__class__, str):
                course_end_at = self._validate_iso8601_string(course_end_at)
            elif issubclass(course_end_at.__class__, date) or issubclass(
                course_end_at.__class__, datetime
            ):
                course_end_at = course_end_at.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            data["course[end_at]"] = course_end_at

        # OPTIONAL - course[license]
        """
            The name of the licensing. Should be one of the following abbreviations
        (a descriptive name is included in parenthesis for reference):
        - 'private' (Private Copyrighted)
        - 'cc_by_nc_nd' (CC Attribution Non-Commercial No Derivatives)
        - 'cc_by_nc_sa' (CC Attribution Non-Commercial Share Alike)
        - 'cc_by_nc' (CC Attribution Non-Commercial)
        - 'cc_by_nd' (CC Attribution No Derivatives)
        - 'cc_by_sa' (CC Attribution Share Alike)
        - 'cc_by' (CC Attribution)
        - 'public_domain' (Public Domain).
        """
        if course_license is not None:
            data["course[license]"] = course_license

        # OPTIONAL - course[is_public]
        """
            Set to true if course is public to both authenticated and unauthenticated users.
        """
        if course_is_public is not None:
            data["course[is_public]"] = course_is_public

        # OPTIONAL - course[is_public_to_auth_users]
        """
            Set to true if course is public only to authenticated users.
        """
        if course_is_public_to_auth_users is not None:
            data["course[is_public_to_auth_users]"] = course_is_public_to_auth_users

        # OPTIONAL - course[public_syllabus]
        """
            Set to true to make the course syllabus public.
        """
        if course_public_syllabus is not None:
            data["course[public_syllabus]"] = course_public_syllabus

        # OPTIONAL - course[public_syllabus_to_auth]
        """
            Set to true to make the course syllabus to public for authenticated users.
        """
        if course_public_syllabus_to_auth is not None:
            data["course[public_syllabus_to_auth]"] = course_public_syllabus_to_auth

        # OPTIONAL - course[public_description]
        """
            A publicly visible description of the course.
        """
        if course_public_description is not None:
            data["course[public_description]"] = course_public_description

        # OPTIONAL - course[allow_student_wiki_edits]
        """
            If true, students will be able to modify the course wiki.
        """
        if course_allow_student_wiki_edits is not None:
            data["course[allow_student_wiki_edits]"] = course_allow_student_wiki_edits

        # OPTIONAL - course[allow_wiki_comments]
        """
            If true, course members will be able to comment on wiki pages.
        """
        if course_allow_wiki_comments is not None:
            data["course[allow_wiki_comments]"] = course_allow_wiki_comments

        # OPTIONAL - course[allow_student_forum_attachments]
        """
            If true, students can attach files to forum posts.
        """
        if course_allow_student_forum_attachments is not None:
            data[
                "course[allow_student_forum_attachments]"
            ] = course_allow_student_forum_attachments

        # OPTIONAL - course[open_enrollment]
        """
            Set to true if the course is open enrollment.
        """
        if course_open_enrollment is not None:
            data["course[open_enrollment]"] = course_open_enrollment

        # OPTIONAL - course[self_enrollment]
        """
            Set to true if the course is self enrollment.
        """
        if course_self_enrollment is not None:
            data["course[self_enrollment]"] = course_self_enrollment

        # OPTIONAL - course[restrict_enrollments_to_course_dates]
        """
            Set to true to restrict user enrollments to the start and end dates of the
        course. This parameter is required when using the API, as this option is
        not displayed in the Course Settings page. Setting this value to false will
        remove the course end date (if it exists), as well as the course start date
        (if the course is unpublished).
        """
        if course_restrict_enrollments_to_course_dates is not None:
            data[
                "course[restrict_enrollments_to_course_dates]"
            ] = course_restrict_enrollments_to_course_dates

        # OPTIONAL - course[term_id]
        """
            The unique ID of the term to create to course in.
        """
        if course_term_id is not None:
            data["course[term_id]"] = course_term_id

        # OPTIONAL - course[sis_course_id]
        """
            The unique SIS identifier.
        """
        if course_sis_course_id is not None:
            data["course[sis_course_id]"] = course_sis_course_id

        # OPTIONAL - course[integration_id]
        """
            The unique Integration identifier.
        """
        if course_integration_id is not None:
            data["course[integration_id]"] = course_integration_id

        # OPTIONAL - course[hide_final_grades]
        """
            If this option is set to true, the totals in student grades summary will
        be hidden.
        """
        if course_hide_final_grades is not None:
            data["course[hide_final_grades]"] = course_hide_final_grades

        # OPTIONAL - course[time_zone]
        """
            The time zone for the course. Allowed time zones are
        {http://www.iana.org/time-zones IANA time zones} or friendlier
        {http://api.rubyonrails.org/classes/ActiveSupport/TimeZone.html Ruby on Rails time zones}.
        """
        if course_time_zone is not None:
            data["course[time_zone]"] = course_time_zone

        # OPTIONAL - course[apply_assignment_group_weights]
        """
            Set to true to weight final grade based on assignment groups percentages.
        """
        if course_apply_assignment_group_weights is not None:
            data[
                "course[apply_assignment_group_weights]"
            ] = course_apply_assignment_group_weights

        # OPTIONAL - course[storage_quota_mb]
        """
            Set the storage quota for the course, in megabytes. The caller must have
        the "Manage storage quotas" account permission.
        """
        if course_storage_quota_mb is not None:
            data["course[storage_quota_mb]"] = course_storage_quota_mb

        # OPTIONAL - offer
        """
            If this option is set to true, the course will be available to students
        immediately.
        """
        if offer is not None:
            data["offer"] = offer

        # OPTIONAL - course[event]
        """
            The action to take on each course.
        * 'claim' makes a course no longer visible to students. This action is also called "unpublish" on the web site.
          A course cannot be unpublished if students have received graded submissions.
        * 'offer' makes a course visible to students. This action is also called "publish" on the web site.
        * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears
          in prior-enrollment lists.
        * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists).
          All enrollments are deleted. Course content may be physically deleted at a future date.
        * 'undelete' attempts to recover a course that has been deleted. This action requires account administrative rights.
          (Recovery is not guaranteed; please conclude rather than delete a course if there is any possibility the course
          will be used again.) The recovered course will be unpublished. Deleted enrollments will not be recovered.
        """
        if course_event is not None:
            self._validate_enum(
                course_event, ["claim", "offer", "conclude", "delete", "undelete"]
            )
            data["course[event]"] = course_event

        # OPTIONAL - course[default_view]
        """
            The type of page that users will see when they first visit the course
        * 'feed' Recent Activity Dashboard
        * 'wiki' Wiki Front Page
        * 'modules' Course Modules/Sections Page
        * 'assignments' Course Assignments List
        * 'syllabus' Course Syllabus Page
        other types may be added in the future
        """
        if course_default_view is not None:
            self._validate_enum(
                course_default_view,
                ["feed", "wiki", "modules", "syllabus", "assignments"],
            )
            data["course[default_view]"] = course_default_view

        # OPTIONAL - course[syllabus_body]
        """
            The syllabus body for the course
        """
        if course_syllabus_body is not None:
            data["course[syllabus_body]"] = course_syllabus_body

        # OPTIONAL - course[syllabus_course_summary]
        """
            Optional. Indicates whether the Course Summary (consisting of the course's assignments and calendar events) is displayed on the syllabus page. Defaults to +true+.
        """
        if course_syllabus_course_summary is not None:
            data["course[syllabus_course_summary]"] = course_syllabus_course_summary

        # OPTIONAL - course[grading_standard_id]
        """
            The grading standard id to set for the course.  If no value is provided for this argument the current grading_standard will be un-set from this course.
        """
        if course_grading_standard_id is not None:
            data["course[grading_standard_id]"] = course_grading_standard_id

        # OPTIONAL - course[grade_passback_setting]
        """
            Optional. The grade_passback_setting for the course. Only 'nightly_sync' and '' are allowed
        """
        if course_grade_passback_setting is not None:
            data["course[grade_passback_setting]"] = course_grade_passback_setting

        # OPTIONAL - course[course_format]
        """
            Optional. Specifies the format of the course. (Should be either 'on_campus' or 'online')
        """
        if course_course_format is not None:
            data["course[course_format]"] = course_course_format

        # OPTIONAL - course[image_id]
        """
            This is a file ID corresponding to an image file in the course that will
        be used as the course image.
        This will clear the course's image_url setting if set.  If you attempt
        to provide image_url and image_id in a request it will fail.
        """
        if course_image_id is not None:
            data["course[image_id]"] = course_image_id

        # OPTIONAL - course[image_url]
        """
            This is a URL to an image to be used as the course image.
        This will clear the course's image_id setting if set.  If you attempt
        to provide image_url and image_id in a request it will fail.
        """
        if course_image_url is not None:
            data["course[image_url]"] = course_image_url

        # OPTIONAL - course[remove_image]
        """
            If this option is set to true, the course image url and course image
        ID are both set to nil
        """
        if course_remove_image is not None:
            data["course[remove_image]"] = course_remove_image

        # OPTIONAL - course[remove_banner_image]
        """
            If this option is set to true, the course banner image url and course
        banner image ID are both set to nil
        """
        if course_remove_banner_image is not None:
            data["course[remove_banner_image]"] = course_remove_banner_image

        # OPTIONAL - course[blueprint]
        """
            Sets the course as a blueprint course.
        """
        if course_blueprint is not None:
            data["course[blueprint]"] = course_blueprint

        # OPTIONAL - course[blueprint_restrictions]
        """
            Sets a default set to apply to blueprint course objects when restricted,
        unless _use_blueprint_restrictions_by_object_type_ is enabled.
        See the {api:Blueprint_Courses:BlueprintRestriction Blueprint Restriction} documentation
        """
        if course_blueprint_restrictions is not None:
            data["course[blueprint_restrictions]"] = course_blueprint_restrictions

        # OPTIONAL - course[use_blueprint_restrictions_by_object_type]
        """
            When enabled, the _blueprint_restrictions_ parameter will be ignored in favor of
        the _blueprint_restrictions_by_object_type_ parameter
        """
        if course_use_blueprint_restrictions_by_object_type is not None:
            data[
                "course[use_blueprint_restrictions_by_object_type]"
            ] = course_use_blueprint_restrictions_by_object_type

        # OPTIONAL - course[blueprint_restrictions_by_object_type]
        """
            Allows setting multiple {api:Blueprint_Courses:BlueprintRestriction Blueprint Restriction}
        to apply to blueprint course objects of the matching type when restricted.
        The possible object types are "assignment", "attachment", "discussion_topic", "quiz" and "wiki_page".
        Example usage:
          course[blueprint_restrictions_by_object_type][assignment][content]=1
        """
        if course_blueprint_restrictions_by_object_type is not None:
            data[
                "course[blueprint_restrictions_by_object_type]"
            ] = course_blueprint_restrictions_by_object_type

        # OPTIONAL - course[homeroom_course]
        """
            Sets the course as a homeroom course. The setting takes effect only when the course is associated
        with a Canvas for Elementary-enabled account.
        """
        if course_homeroom_course is not None:
            data["course[homeroom_course]"] = course_homeroom_course

        # OPTIONAL - course[sync_enrollments_from_homeroom]
        """
            Syncs enrollments from the homeroom that is set in homeroom_course_id. The setting only takes effect when the
        course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled.
        """
        if course_sync_enrollments_from_homeroom is not None:
            data[
                "course[sync_enrollments_from_homeroom]"
            ] = course_sync_enrollments_from_homeroom

        # OPTIONAL - course[homeroom_course_id]
        """
            Sets the Homeroom Course id to be used with sync_enrollments_from_homeroom. The setting only takes effect when the
        course is associated with a Canvas for Elementary-enabled account and sync_enrollments_from_homeroom is enabled.
        """
        if course_homeroom_course_id is not None:
            data["course[homeroom_course_id]"] = course_homeroom_course_id

        # OPTIONAL - course[template]
        """
            Enable or disable the course as a template that can be selected by an account
        """
        if course_template is not None:
            data["course[template]"] = course_template

        # OPTIONAL - course[course_color]
        """
            Sets a color in hex code format to be associated with the course. The setting takes effect only when the course
        is associated with a Canvas for Elementary-enabled account.
        """
        if course_course_color is not None:
            data["course[course_color]"] = course_course_color

        # OPTIONAL - course[friendly_name]
        """
            Set a friendly name for the course. If this is provided and the course is associated with a Canvas for
        Elementary account, it will be shown instead of the course name. This setting takes priority over
        course nicknames defined by individual users.
        """
        if course_friendly_name is not None:
            data["course[friendly_name]"] = course_friendly_name

        # OPTIONAL - course[enable_pace_plans]
        """
            Enable or disable Pace Plans for the course. This setting only has an effect when the Pace Plans feature flag is
        enabled for the sub-account. Otherwise, Pace Plans are always disabled.
          Note: Pace Plans is in active development.
        """
        if course_enable_pace_plans is not None:
            data["course[enable_pace_plans]"] = course_enable_pace_plans

        self.logger.debug(
            "PUT /api/v1/courses/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def update_courses(self, account_id, course_ids, event):
        """
        Update courses.

        Update multiple courses in an account.  Operates asynchronously; use the {api:ProgressController#show progress endpoint}
        to query the status of an operation.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - course_ids
        """
            List of ids of courses to update. At most 500 courses may be updated in one call.
        """
        data["course_ids"] = course_ids

        # REQUIRED - event
        """
            The action to take on each course.  Must be one of 'offer', 'conclude', 'delete', or 'undelete'.
        * 'offer' makes a course visible to students. This action is also called "publish" on the web site.
        * 'conclude' prevents future enrollments and makes a course read-only for all participants. The course still appears
          in prior-enrollment lists.
        * 'delete' completely removes the course from the web site (including course menus and prior-enrollment lists).
          All enrollments are deleted. Course content may be physically deleted at a future date.
        * 'undelete' attempts to recover a course that has been deleted. (Recovery is not guaranteed; please conclude
          rather than delete a course if there is any possibility the course will be used again.) The recovered course
          will be unpublished. Deleted enrollments will not be recovered.
        """
        self._validate_enum(event, ["offer", "conclude", "delete", "undelete"])
        data["event"] = event

        self.logger.debug(
            "PUT /api/v1/accounts/{account_id}/courses with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/courses".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def reset_course(self, course_id):
        """
        Reset a course.

        Deletes the current course, and creates a new equivalent course with
        no content, but all sections and users moved over.
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
            "POST /api/v1/courses/{course_id}/reset_content with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/reset_content".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_effective_due_dates(self, course_id, assignment_ids=None):
        """
        Get effective due dates.

        For each assignment in the course, returns each assigned student's ID
        and their corresponding due date along with some grading period data.
        Returns a collection with keys representing assignment IDs and values as a
        collection containing keys representing student IDs and values representing
        the student's effective due_at, the grading_period_id of which the due_at falls
        in, and whether or not the grading period is closed (in_closed_grading_period)

        The list of assignment IDs for which effective student due dates are
        requested. If not provided, all assignments in the course will be used.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - assignment_ids
        """
            no description
        """
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/effective_due_dates with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/effective_due_dates".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def permissions(self, course_id, permissions=None):
        """
        Permissions.

        Returns permission information for the calling user in the given course.
        See also the {api:AccountsController#permissions Account} and
        {api:GroupsController#permissions Group} counterparts.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - permissions
        """
            List of permissions to check against the authenticated user.
        Permission names are documented in the {api:RoleOverridesController#add_role Create a role} endpoint.
        """
        if permissions is not None:
            params["permissions"] = permissions

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/permissions with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/permissions".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_bulk_user_progress(self, course_id):
        """
        Get bulk user progress.

        Returns progress information for all users enrolled in the given course.

        You must be a user who has permission to view all grades in the course (such as a teacher or administrator).
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
            "GET /api/v1/courses/{course_id}/bulk_user_progress with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/bulk_user_progress".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_course_copy_status(self, course_id, id):
        """
        Get course copy status.

        DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}

        Retrieve the status of a course copy
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

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/course_copy/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/course_copy/{id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    # def copy_course_content(self, course_id, except=None, only=None, source_course=None):
    #     """
    #     Copy course content.

    #     DEPRECATED: Please use the {api:ContentMigrationsController#create Content Migrations API}

    #     Copies content from one course into another. The default is to copy all course
    #     content. You can control specific types to copy by using either the 'except' option
    #     or the 'only' option.

    #     The response is the same as the course copy status endpoint
    #     """
    #     path = {}
    #     data = {}
    #     params = {}

    #     # REQUIRED - PATH - course_id
    #     """
    #         ID
    #     """
    #     path["course_id"] = course_id

    #     # OPTIONAL - source_course
    #     """
    #         ID or SIS-ID of the course to copy the content from
    #     """
    #     if source_course is not None:
    #         data["source_course"] = source_course

    #     # OPTIONAL - except
    #     """
    #         A list of the course content types to exclude, all areas not listed will
    #     be copied.
    #     """
    #     if except is not None:
    #         self._validate_enum(except, ["course_settings", "assignments", "external_tools", "files", "topics", "calendar_events", "quizzes", "wiki_pages", "modules", "outcomes"])
    #         data["except"] = except

    #     # OPTIONAL - only
    #     """
    #         A list of the course content types to copy, all areas not listed will not
    #     be copied.
    #     """
    #     if only is not None:
    #         self._validate_enum(only, ["course_settings", "assignments", "external_tools", "files", "topics", "calendar_events", "quizzes", "wiki_pages", "modules", "outcomes"])
    #         data["only"] = only

    #     self.logger.debug("POST /api/v1/courses/{course_id}/course_copy with query params: {params} and form data: {data}".format(params=params, data=data, **path))
    #     return self.generic_request("POST", "/api/v1/courses/{course_id}/course_copy".format(**path), data=data, params=params, no_data=True)


class Term(BaseModel):
    """Term Model."""

    def __init__(self, id=None, name=None, start_at=None, end_at=None):
        """Init method for Term class."""
        self._id = id
        self._name = name
        self._start_at = start_at
        self._end_at = end_at

        self.logger = logging.getLogger("py3canvas.Term")

    @property
    def id(self):
        """id."""
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
        """name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def start_at(self):
        """start_at."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn(
            "Setting values on start_at will NOT update the remote Canvas instance."
        )
        self._start_at = value

    @property
    def end_at(self):
        """end_at."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn(
            "Setting values on end_at will NOT update the remote Canvas instance."
        )
        self._end_at = value


class Courseprogress(BaseModel):
    """Courseprogress Model."""

    def __init__(
        self,
        requirement_count=None,
        requirement_completed_count=None,
        next_requirement_url=None,
        completed_at=None,
    ):
        """Init method for Courseprogress class."""
        self._requirement_count = requirement_count
        self._requirement_completed_count = requirement_completed_count
        self._next_requirement_url = next_requirement_url
        self._completed_at = completed_at

        self.logger = logging.getLogger("py3canvas.Courseprogress")

    @property
    def requirement_count(self):
        """total number of requirements from all modules."""
        return self._requirement_count

    @requirement_count.setter
    def requirement_count(self, value):
        """Setter for requirement_count property."""
        self.logger.warn(
            "Setting values on requirement_count will NOT update the remote Canvas instance."
        )
        self._requirement_count = value

    @property
    def requirement_completed_count(self):
        """total number of requirements the user has completed from all modules."""
        return self._requirement_completed_count

    @requirement_completed_count.setter
    def requirement_completed_count(self, value):
        """Setter for requirement_completed_count property."""
        self.logger.warn(
            "Setting values on requirement_completed_count will NOT update the remote Canvas instance."
        )
        self._requirement_completed_count = value

    @property
    def next_requirement_url(self):
        """url to next module item that has an unmet requirement. null if the user has completed the course or the current module does not require sequential progress."""
        return self._next_requirement_url

    @next_requirement_url.setter
    def next_requirement_url(self, value):
        """Setter for next_requirement_url property."""
        self.logger.warn(
            "Setting values on next_requirement_url will NOT update the remote Canvas instance."
        )
        self._next_requirement_url = value

    @property
    def completed_at(self):
        """date the course was completed. null if the course has not been completed by this user."""
        return self._completed_at

    @completed_at.setter
    def completed_at(self, value):
        """Setter for completed_at property."""
        self.logger.warn(
            "Setting values on completed_at will NOT update the remote Canvas instance."
        )
        self._completed_at = value


class Course(BaseModel):
    """Course Model."""

    def __init__(
        self,
        id=None,
        sis_course_id=None,
        uuid=None,
        integration_id=None,
        sis_import_id=None,
        name=None,
        course_code=None,
        workflow_state=None,
        account_id=None,
        root_account_id=None,
        enrollment_term_id=None,
        grading_periods=None,
        grading_standard_id=None,
        grade_passback_setting=None,
        created_at=None,
        start_at=None,
        end_at=None,
        locale=None,
        enrollments=None,
        total_students=None,
        calendar=None,
        default_view=None,
        syllabus_body=None,
        needs_grading_count=None,
        term=None,
        course_progress=None,
        apply_assignment_group_weights=None,
        permissions=None,
        is_public=None,
        is_public_to_auth_users=None,
        public_syllabus=None,
        public_syllabus_to_auth=None,
        public_description=None,
        storage_quota_mb=None,
        storage_quota_used_mb=None,
        hide_final_grades=None,
        license=None,
        allow_student_assignment_edits=None,
        allow_wiki_comments=None,
        allow_student_forum_attachments=None,
        open_enrollment=None,
        self_enrollment=None,
        restrict_enrollments_to_course_dates=None,
        course_format=None,
        access_restricted_by_date=None,
        time_zone=None,
        blueprint=None,
        blueprint_restrictions=None,
        blueprint_restrictions_by_object_type=None,
        template=None,
    ):
        """Init method for Course class."""
        self._id = id
        self._sis_course_id = sis_course_id
        self._uuid = uuid
        self._integration_id = integration_id
        self._sis_import_id = sis_import_id
        self._name = name
        self._course_code = course_code
        self._workflow_state = workflow_state
        self._account_id = account_id
        self._root_account_id = root_account_id
        self._enrollment_term_id = enrollment_term_id
        self._grading_periods = grading_periods
        self._grading_standard_id = grading_standard_id
        self._grade_passback_setting = grade_passback_setting
        self._created_at = created_at
        self._start_at = start_at
        self._end_at = end_at
        self._locale = locale
        self._enrollments = enrollments
        self._total_students = total_students
        self._calendar = calendar
        self._default_view = default_view
        self._syllabus_body = syllabus_body
        self._needs_grading_count = needs_grading_count
        self._term = term
        self._course_progress = course_progress
        self._apply_assignment_group_weights = apply_assignment_group_weights
        self._permissions = permissions
        self._is_public = is_public
        self._is_public_to_auth_users = is_public_to_auth_users
        self._public_syllabus = public_syllabus
        self._public_syllabus_to_auth = public_syllabus_to_auth
        self._public_description = public_description
        self._storage_quota_mb = storage_quota_mb
        self._storage_quota_used_mb = storage_quota_used_mb
        self._hide_final_grades = hide_final_grades
        self._license = license
        self._allow_student_assignment_edits = allow_student_assignment_edits
        self._allow_wiki_comments = allow_wiki_comments
        self._allow_student_forum_attachments = allow_student_forum_attachments
        self._open_enrollment = open_enrollment
        self._self_enrollment = self_enrollment
        self._restrict_enrollments_to_course_dates = (
            restrict_enrollments_to_course_dates
        )
        self._course_format = course_format
        self._access_restricted_by_date = access_restricted_by_date
        self._time_zone = time_zone
        self._blueprint = blueprint
        self._blueprint_restrictions = blueprint_restrictions
        self._blueprint_restrictions_by_object_type = (
            blueprint_restrictions_by_object_type
        )
        self._template = template

        self.logger = logging.getLogger("py3canvas.Course")

    @property
    def id(self):
        """the unique identifier for the course."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def sis_course_id(self):
        """the SIS identifier for the course, if defined. This field is only included if the user has permission to view SIS information."""
        return self._sis_course_id

    @sis_course_id.setter
    def sis_course_id(self, value):
        """Setter for sis_course_id property."""
        self.logger.warn(
            "Setting values on sis_course_id will NOT update the remote Canvas instance."
        )
        self._sis_course_id = value

    @property
    def uuid(self):
        """the UUID of the course."""
        return self._uuid

    @uuid.setter
    def uuid(self, value):
        """Setter for uuid property."""
        self.logger.warn(
            "Setting values on uuid will NOT update the remote Canvas instance."
        )
        self._uuid = value

    @property
    def integration_id(self):
        """the integration identifier for the course, if defined. This field is only included if the user has permission to view SIS information."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn(
            "Setting values on integration_id will NOT update the remote Canvas instance."
        )
        self._integration_id = value

    @property
    def sis_import_id(self):
        """the unique identifier for the SIS import. This field is only included if the user has permission to manage SIS information."""
        return self._sis_import_id

    @sis_import_id.setter
    def sis_import_id(self, value):
        """Setter for sis_import_id property."""
        self.logger.warn(
            "Setting values on sis_import_id will NOT update the remote Canvas instance."
        )
        self._sis_import_id = value

    @property
    def name(self):
        """the full name of the course."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def course_code(self):
        """the course code."""
        return self._course_code

    @course_code.setter
    def course_code(self, value):
        """Setter for course_code property."""
        self.logger.warn(
            "Setting values on course_code will NOT update the remote Canvas instance."
        )
        self._course_code = value

    @property
    def workflow_state(self):
        """the current state of the course one of 'unpublished', 'available', 'completed', or 'deleted'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def account_id(self):
        """the account associated with the course."""
        return self._account_id

    @account_id.setter
    def account_id(self, value):
        """Setter for account_id property."""
        self.logger.warn(
            "Setting values on account_id will NOT update the remote Canvas instance."
        )
        self._account_id = value

    @property
    def root_account_id(self):
        """the root account associated with the course."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn(
            "Setting values on root_account_id will NOT update the remote Canvas instance."
        )
        self._root_account_id = value

    @property
    def enrollment_term_id(self):
        """the enrollment term associated with the course."""
        return self._enrollment_term_id

    @enrollment_term_id.setter
    def enrollment_term_id(self, value):
        """Setter for enrollment_term_id property."""
        self.logger.warn(
            "Setting values on enrollment_term_id will NOT update the remote Canvas instance."
        )
        self._enrollment_term_id = value

    @property
    def grading_periods(self):
        """A list of grading periods associated with the course."""
        return self._grading_periods

    @grading_periods.setter
    def grading_periods(self, value):
        """Setter for grading_periods property."""
        self.logger.warn(
            "Setting values on grading_periods will NOT update the remote Canvas instance."
        )
        self._grading_periods = value

    @property
    def grading_standard_id(self):
        """the grading standard associated with the course."""
        return self._grading_standard_id

    @grading_standard_id.setter
    def grading_standard_id(self, value):
        """Setter for grading_standard_id property."""
        self.logger.warn(
            "Setting values on grading_standard_id will NOT update the remote Canvas instance."
        )
        self._grading_standard_id = value

    @property
    def grade_passback_setting(self):
        """the grade_passback_setting set on the course."""
        return self._grade_passback_setting

    @grade_passback_setting.setter
    def grade_passback_setting(self, value):
        """Setter for grade_passback_setting property."""
        self.logger.warn(
            "Setting values on grade_passback_setting will NOT update the remote Canvas instance."
        )
        self._grade_passback_setting = value

    @property
    def created_at(self):
        """the date the course was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def start_at(self):
        """the start date for the course, if applicable."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn(
            "Setting values on start_at will NOT update the remote Canvas instance."
        )
        self._start_at = value

    @property
    def end_at(self):
        """the end date for the course, if applicable."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn(
            "Setting values on end_at will NOT update the remote Canvas instance."
        )
        self._end_at = value

    @property
    def locale(self):
        """the course-set locale, if applicable."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn(
            "Setting values on locale will NOT update the remote Canvas instance."
        )
        self._locale = value

    @property
    def enrollments(self):
        """A list of enrollments linking the current user to the course. for student enrollments, grading information may be included if include[]=total_scores."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn(
            "Setting values on enrollments will NOT update the remote Canvas instance."
        )
        self._enrollments = value

    @property
    def total_students(self):
        """optional: the total number of active and invited students in the course."""
        return self._total_students

    @total_students.setter
    def total_students(self, value):
        """Setter for total_students property."""
        self.logger.warn(
            "Setting values on total_students will NOT update the remote Canvas instance."
        )
        self._total_students = value

    @property
    def calendar(self):
        """course calendar."""
        return self._calendar

    @calendar.setter
    def calendar(self, value):
        """Setter for calendar property."""
        self.logger.warn(
            "Setting values on calendar will NOT update the remote Canvas instance."
        )
        self._calendar = value

    @property
    def default_view(self):
        """the type of page that users will see when they first visit the course - 'feed': Recent Activity Dashboard - 'wiki': Wiki Front Page - 'modules': Course Modules/Sections Page - 'assignments': Course Assignments List - 'syllabus': Course Syllabus Page other types may be added in the future."""
        return self._default_view

    @default_view.setter
    def default_view(self, value):
        """Setter for default_view property."""
        self.logger.warn(
            "Setting values on default_view will NOT update the remote Canvas instance."
        )
        self._default_view = value

    @property
    def syllabus_body(self):
        """optional: user-generated HTML for the course syllabus."""
        return self._syllabus_body

    @syllabus_body.setter
    def syllabus_body(self, value):
        """Setter for syllabus_body property."""
        self.logger.warn(
            "Setting values on syllabus_body will NOT update the remote Canvas instance."
        )
        self._syllabus_body = value

    @property
    def needs_grading_count(self):
        """optional: the number of submissions needing grading returned only if the current user has grading rights and include[]=needs_grading_count."""
        return self._needs_grading_count

    @needs_grading_count.setter
    def needs_grading_count(self, value):
        """Setter for needs_grading_count property."""
        self.logger.warn(
            "Setting values on needs_grading_count will NOT update the remote Canvas instance."
        )
        self._needs_grading_count = value

    @property
    def term(self):
        """optional: the enrollment term object for the course returned only if include[]=term."""
        return self._term

    @term.setter
    def term(self, value):
        """Setter for term property."""
        self.logger.warn(
            "Setting values on term will NOT update the remote Canvas instance."
        )
        self._term = value

    @property
    def course_progress(self):
        """optional: information on progress through the course returned only if include[]=course_progress."""
        return self._course_progress

    @course_progress.setter
    def course_progress(self, value):
        """Setter for course_progress property."""
        self.logger.warn(
            "Setting values on course_progress will NOT update the remote Canvas instance."
        )
        self._course_progress = value

    @property
    def apply_assignment_group_weights(self):
        """weight final grade based on assignment group percentages."""
        return self._apply_assignment_group_weights

    @apply_assignment_group_weights.setter
    def apply_assignment_group_weights(self, value):
        """Setter for apply_assignment_group_weights property."""
        self.logger.warn(
            "Setting values on apply_assignment_group_weights will NOT update the remote Canvas instance."
        )
        self._apply_assignment_group_weights = value

    @property
    def permissions(self):
        """optional: the permissions the user has for the course. returned only for a single course and include[]=permissions."""
        return self._permissions

    @permissions.setter
    def permissions(self, value):
        """Setter for permissions property."""
        self.logger.warn(
            "Setting values on permissions will NOT update the remote Canvas instance."
        )
        self._permissions = value

    @property
    def is_public(self):
        """is_public."""
        return self._is_public

    @is_public.setter
    def is_public(self, value):
        """Setter for is_public property."""
        self.logger.warn(
            "Setting values on is_public will NOT update the remote Canvas instance."
        )
        self._is_public = value

    @property
    def is_public_to_auth_users(self):
        """is_public_to_auth_users."""
        return self._is_public_to_auth_users

    @is_public_to_auth_users.setter
    def is_public_to_auth_users(self, value):
        """Setter for is_public_to_auth_users property."""
        self.logger.warn(
            "Setting values on is_public_to_auth_users will NOT update the remote Canvas instance."
        )
        self._is_public_to_auth_users = value

    @property
    def public_syllabus(self):
        """public_syllabus."""
        return self._public_syllabus

    @public_syllabus.setter
    def public_syllabus(self, value):
        """Setter for public_syllabus property."""
        self.logger.warn(
            "Setting values on public_syllabus will NOT update the remote Canvas instance."
        )
        self._public_syllabus = value

    @property
    def public_syllabus_to_auth(self):
        """public_syllabus_to_auth."""
        return self._public_syllabus_to_auth

    @public_syllabus_to_auth.setter
    def public_syllabus_to_auth(self, value):
        """Setter for public_syllabus_to_auth property."""
        self.logger.warn(
            "Setting values on public_syllabus_to_auth will NOT update the remote Canvas instance."
        )
        self._public_syllabus_to_auth = value

    @property
    def public_description(self):
        """optional: the public description of the course."""
        return self._public_description

    @public_description.setter
    def public_description(self, value):
        """Setter for public_description property."""
        self.logger.warn(
            "Setting values on public_description will NOT update the remote Canvas instance."
        )
        self._public_description = value

    @property
    def storage_quota_mb(self):
        """storage_quota_mb."""
        return self._storage_quota_mb

    @storage_quota_mb.setter
    def storage_quota_mb(self, value):
        """Setter for storage_quota_mb property."""
        self.logger.warn(
            "Setting values on storage_quota_mb will NOT update the remote Canvas instance."
        )
        self._storage_quota_mb = value

    @property
    def storage_quota_used_mb(self):
        """storage_quota_used_mb."""
        return self._storage_quota_used_mb

    @storage_quota_used_mb.setter
    def storage_quota_used_mb(self, value):
        """Setter for storage_quota_used_mb property."""
        self.logger.warn(
            "Setting values on storage_quota_used_mb will NOT update the remote Canvas instance."
        )
        self._storage_quota_used_mb = value

    @property
    def hide_final_grades(self):
        """hide_final_grades."""
        return self._hide_final_grades

    @hide_final_grades.setter
    def hide_final_grades(self, value):
        """Setter for hide_final_grades property."""
        self.logger.warn(
            "Setting values on hide_final_grades will NOT update the remote Canvas instance."
        )
        self._hide_final_grades = value

    @property
    def license(self):
        """license."""
        return self._license

    @license.setter
    def license(self, value):
        """Setter for license property."""
        self.logger.warn(
            "Setting values on license will NOT update the remote Canvas instance."
        )
        self._license = value

    @property
    def allow_student_assignment_edits(self):
        """allow_student_assignment_edits."""
        return self._allow_student_assignment_edits

    @allow_student_assignment_edits.setter
    def allow_student_assignment_edits(self, value):
        """Setter for allow_student_assignment_edits property."""
        self.logger.warn(
            "Setting values on allow_student_assignment_edits will NOT update the remote Canvas instance."
        )
        self._allow_student_assignment_edits = value

    @property
    def allow_wiki_comments(self):
        """allow_wiki_comments."""
        return self._allow_wiki_comments

    @allow_wiki_comments.setter
    def allow_wiki_comments(self, value):
        """Setter for allow_wiki_comments property."""
        self.logger.warn(
            "Setting values on allow_wiki_comments will NOT update the remote Canvas instance."
        )
        self._allow_wiki_comments = value

    @property
    def allow_student_forum_attachments(self):
        """allow_student_forum_attachments."""
        return self._allow_student_forum_attachments

    @allow_student_forum_attachments.setter
    def allow_student_forum_attachments(self, value):
        """Setter for allow_student_forum_attachments property."""
        self.logger.warn(
            "Setting values on allow_student_forum_attachments will NOT update the remote Canvas instance."
        )
        self._allow_student_forum_attachments = value

    @property
    def open_enrollment(self):
        """open_enrollment."""
        return self._open_enrollment

    @open_enrollment.setter
    def open_enrollment(self, value):
        """Setter for open_enrollment property."""
        self.logger.warn(
            "Setting values on open_enrollment will NOT update the remote Canvas instance."
        )
        self._open_enrollment = value

    @property
    def self_enrollment(self):
        """self_enrollment."""
        return self._self_enrollment

    @self_enrollment.setter
    def self_enrollment(self, value):
        """Setter for self_enrollment property."""
        self.logger.warn(
            "Setting values on self_enrollment will NOT update the remote Canvas instance."
        )
        self._self_enrollment = value

    @property
    def restrict_enrollments_to_course_dates(self):
        """restrict_enrollments_to_course_dates."""
        return self._restrict_enrollments_to_course_dates

    @restrict_enrollments_to_course_dates.setter
    def restrict_enrollments_to_course_dates(self, value):
        """Setter for restrict_enrollments_to_course_dates property."""
        self.logger.warn(
            "Setting values on restrict_enrollments_to_course_dates will NOT update the remote Canvas instance."
        )
        self._restrict_enrollments_to_course_dates = value

    @property
    def course_format(self):
        """course_format."""
        return self._course_format

    @course_format.setter
    def course_format(self, value):
        """Setter for course_format property."""
        self.logger.warn(
            "Setting values on course_format will NOT update the remote Canvas instance."
        )
        self._course_format = value

    @property
    def access_restricted_by_date(self):
        """optional: this will be true if this user is currently prevented from viewing the course because of date restriction settings."""
        return self._access_restricted_by_date

    @access_restricted_by_date.setter
    def access_restricted_by_date(self, value):
        """Setter for access_restricted_by_date property."""
        self.logger.warn(
            "Setting values on access_restricted_by_date will NOT update the remote Canvas instance."
        )
        self._access_restricted_by_date = value

    @property
    def time_zone(self):
        """The course's IANA time zone name."""
        return self._time_zone

    @time_zone.setter
    def time_zone(self, value):
        """Setter for time_zone property."""
        self.logger.warn(
            "Setting values on time_zone will NOT update the remote Canvas instance."
        )
        self._time_zone = value

    @property
    def blueprint(self):
        """optional: whether the course is set as a Blueprint Course (blueprint fields require the Blueprint Courses feature)."""
        return self._blueprint

    @blueprint.setter
    def blueprint(self, value):
        """Setter for blueprint property."""
        self.logger.warn(
            "Setting values on blueprint will NOT update the remote Canvas instance."
        )
        self._blueprint = value

    @property
    def blueprint_restrictions(self):
        """optional: Set of restrictions applied to all locked course objects."""
        return self._blueprint_restrictions

    @blueprint_restrictions.setter
    def blueprint_restrictions(self, value):
        """Setter for blueprint_restrictions property."""
        self.logger.warn(
            "Setting values on blueprint_restrictions will NOT update the remote Canvas instance."
        )
        self._blueprint_restrictions = value

    @property
    def blueprint_restrictions_by_object_type(self):
        """optional: Sets of restrictions differentiated by object type applied to locked course objects."""
        return self._blueprint_restrictions_by_object_type

    @blueprint_restrictions_by_object_type.setter
    def blueprint_restrictions_by_object_type(self, value):
        """Setter for blueprint_restrictions_by_object_type property."""
        self.logger.warn(
            "Setting values on blueprint_restrictions_by_object_type will NOT update the remote Canvas instance."
        )
        self._blueprint_restrictions_by_object_type = value

    @property
    def template(self):
        """optional: whether the course is set as a template (requires the Course Templates feature)."""
        return self._template

    @template.setter
    def template(self, value):
        """Setter for template property."""
        self.logger.warn(
            "Setting values on template will NOT update the remote Canvas instance."
        )
        self._template = value


class Calendarlink(BaseModel):
    """Calendarlink Model."""

    def __init__(self, ics=None):
        """Init method for Calendarlink class."""
        self._ics = ics

        self.logger = logging.getLogger("py3canvas.Calendarlink")

    @property
    def ics(self):
        """The URL of the calendar in ICS format."""
        return self._ics

    @ics.setter
    def ics(self, value):
        """Setter for ics property."""
        self.logger.warn(
            "Setting values on ics will NOT update the remote Canvas instance."
        )
        self._ics = value
