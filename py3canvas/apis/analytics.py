"""Analytics API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI


class AnalyticsAPI(BaseCanvasAPI):
    """Analytics API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AnalyticsAPI."""
        super(AnalyticsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AnalyticsAPI")

    def get_department_level_participation_data_terms(self, account_id, term_id):
        """
        Get department-level participation data.

        Returns page view hits summed across all courses in the department. Two
        groupings of these counts are returned; one by day (+by_date+), the other
        by category (+by_category+). The possible categories are announcements,
        assignments, collaborations, conferences, discussions, files, general,
        grades, groups, modules, other, pages, and quizzes.

        This and the other department-level endpoints have three variations which
        all return the same style of data but for different subsets of courses. All
        share the prefix /api/v1/accounts/<account_id>/analytics. The possible
        suffixes are:

         * /current: includes all available courses in the default term
         * /completed: includes all concluded courses in the default term
         * /terms/<term_id>: includes all available or concluded courses in the
           given term.

        Courses not yet offered or which have been deleted are never included.

        /current and /completed are intended for use when the account has only one
        term. /terms/<term_id> is intended for use when the account has multiple
        terms.

        The action follows the suffix.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - term_id
        """
            ID
        """
        path["term_id"] = term_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/terms/{term_id}/activity with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/activity".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_participation_data_current(self, account_id):
        """
        Get department-level participation data.

        Returns page view hits summed across all courses in the department. Two
        groupings of these counts are returned; one by day (+by_date+), the other
        by category (+by_category+). The possible categories are announcements,
        assignments, collaborations, conferences, discussions, files, general,
        grades, groups, modules, other, pages, and quizzes.

        This and the other department-level endpoints have three variations which
        all return the same style of data but for different subsets of courses. All
        share the prefix /api/v1/accounts/<account_id>/analytics. The possible
        suffixes are:

         * /current: includes all available courses in the default term
         * /completed: includes all concluded courses in the default term
         * /terms/<term_id>: includes all available or concluded courses in the
           given term.

        Courses not yet offered or which have been deleted are never included.

        /current and /completed are intended for use when the account has only one
        term. /terms/<term_id> is intended for use when the account has multiple
        terms.

        The action follows the suffix.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/current/activity with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/current/activity".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_participation_data_completed(self, account_id):
        """
        Get department-level participation data.

        Returns page view hits summed across all courses in the department. Two
        groupings of these counts are returned; one by day (+by_date+), the other
        by category (+by_category+). The possible categories are announcements,
        assignments, collaborations, conferences, discussions, files, general,
        grades, groups, modules, other, pages, and quizzes.

        This and the other department-level endpoints have three variations which
        all return the same style of data but for different subsets of courses. All
        share the prefix /api/v1/accounts/<account_id>/analytics. The possible
        suffixes are:

         * /current: includes all available courses in the default term
         * /completed: includes all concluded courses in the default term
         * /terms/<term_id>: includes all available or concluded courses in the
           given term.

        Courses not yet offered or which have been deleted are never included.

        /current and /completed are intended for use when the account has only one
        term. /terms/<term_id> is intended for use when the account has multiple
        terms.

        The action follows the suffix.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/completed/activity with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/completed/activity".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_grade_data_terms(self, account_id, term_id):
        """
        Get department-level grade data.

        Returns the distribution of grades for students in courses in the
        department.  Each data point is one student's current grade in one course;
        if a student is in multiple courses, he contributes one value per course,
        but if he's enrolled multiple times in the same course (e.g. a lecture
        section and a lab section), he only constributes on value for that course.

        Grades are binned to the nearest integer score; anomalous grades outside
        the 0 to 100 range are ignored. The raw counts are returned, not yet
        normalized by the total count.

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - term_id
        """
            ID
        """
        path["term_id"] = term_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/terms/{term_id}/grades with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/grades".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_grade_data_current(self, account_id):
        """
        Get department-level grade data.

        Returns the distribution of grades for students in courses in the
        department.  Each data point is one student's current grade in one course;
        if a student is in multiple courses, he contributes one value per course,
        but if he's enrolled multiple times in the same course (e.g. a lecture
        section and a lab section), he only constributes on value for that course.

        Grades are binned to the nearest integer score; anomalous grades outside
        the 0 to 100 range are ignored. The raw counts are returned, not yet
        normalized by the total count.

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/current/grades with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/current/grades".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_grade_data_completed(self, account_id):
        """
        Get department-level grade data.

        Returns the distribution of grades for students in courses in the
        department.  Each data point is one student's current grade in one course;
        if a student is in multiple courses, he contributes one value per course,
        but if he's enrolled multiple times in the same course (e.g. a lecture
        section and a lab section), he only constributes on value for that course.

        Grades are binned to the nearest integer score; anomalous grades outside
        the 0 to 100 range are ignored. The raw counts are returned, not yet
        normalized by the total count.

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/completed/grades with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/completed/grades".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_statistics_terms(self, account_id, term_id):
        """
        Get department-level statistics.

        Returns numeric statistics about the department and term (or filter).

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - term_id
        """
            ID
        """
        path["term_id"] = term_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/terms/{term_id}/statistics with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/statistics".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_statistics_current(self, account_id):
        """
        Get department-level statistics.

        Returns numeric statistics about the department and term (or filter).

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/current/statistics with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/current/statistics".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_statistics_completed(self, account_id):
        """
        Get department-level statistics.

        Returns numeric statistics about the department and term (or filter).

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/completed/statistics with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/completed/statistics".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_statistics_broken_down_by_subaccount_terms(
        self, account_id, term_id
    ):
        """
        Get department-level statistics, broken down by subaccount.

        Returns numeric statistics about the department subaccounts and term (or filter).

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - term_id
        """
            ID
        """
        path["term_id"] = term_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/terms/{term_id}/statistics_by_subaccount with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/terms/{term_id}/statistics_by_subaccount".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_statistics_broken_down_by_subaccount_current(
        self, account_id
    ):
        """
        Get department-level statistics, broken down by subaccount.

        Returns numeric statistics about the department subaccounts and term (or filter).

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/current/statistics_by_subaccount with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/current/statistics_by_subaccount".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_department_level_statistics_broken_down_by_subaccount_completed(
        self, account_id
    ):
        """
        Get department-level statistics, broken down by subaccount.

        Returns numeric statistics about the department subaccounts and term (or filter).

        Shares the same variations on endpoint as the participation data.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/analytics/completed/statistics_by_subaccount with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/analytics/completed/statistics_by_subaccount".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_course_level_participation_data(self, course_id):
        """
        Get course-level participation data.

        Returns page view hits and participation numbers grouped by day through the
        entire history of the course. Page views is returned as a hash, where the
        hash keys are dates in the format "YYYY-MM-DD". The page_views result set
        includes page views broken out by access category. Participations is
        returned as an array of dates in the format "YYYY-MM-DD".
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
            "GET /api/v1/courses/{course_id}/analytics/activity with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/analytics/activity".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_course_level_assignment_data(self, course_id, async=None):
        """
        Get course-level assignment data.

        Returns a list of assignments for the course sorted by due date. For
        each assignment returns basic assignment information, the grade breakdown,
        and a breakdown of on-time/late status of homework submissions.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - async
        """
            If async is true, then the course_assignments call can happen asynch-
        ronously and MAY return a response containing a progress_url key instead
        of an assignments array. If it does, then it is the caller's
        responsibility to poll the API again to see if the progress is complete.
        If the data is ready (possibly even on the first async call) then it
        will be passed back normally, as documented in the example response.
        """
        if async is not None:
            params["async"] = async

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/analytics/assignments with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/analytics/assignments".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_course_level_student_summary_data(
        self, course_id, sort_column=None, student_id=None
    ):
        """
        Get course-level student summary data.

        Returns a summary of per-user access information for all students in
        a course. This includes total page views, total participations, and a
        breakdown of on-time/late status for all homework submissions in the course.

        Each student's summary also includes the maximum number of page views and
        participations by any student in the course, which may be useful for some
        visualizations (since determining maximums client side can be tricky with
        pagination).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - sort_column
        """
            The order results in which results are returned.  Defaults to "name".
        """
        if sort_column is not None:
            self._validate_enum(
                sort_column,
                [
                    "name",
                    "name_descending",
                    "score",
                    "score_descending",
                    "participations",
                    "participations_descending",
                    "page_views",
                    "page_views_descending",
                ],
            )
            params["sort_column"] = sort_column

        # OPTIONAL - student_id
        """
            If set, returns only the specified student.
        """
        if student_id is not None:
            params["student_id"] = student_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/analytics/student_summaries with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/analytics/student_summaries".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_user_in_a_course_level_participation_data(self, course_id, student_id):
        """
        Get user-in-a-course-level participation data.

        Returns page view hits grouped by hour, and participation details through the
        entire history of the course.

        `page_views` are returned as a hash, where the keys are iso8601 dates, bucketed by the hour.
        `participations` are returned as an array of hashes, sorted oldest to newest.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - student_id
        """
            ID
        """
        path["student_id"] = student_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/analytics/users/{student_id}/activity with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/analytics/users/{student_id}/activity".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_user_in_a_course_level_assignment_data(self, course_id, student_id):
        """
        Get user-in-a-course-level assignment data.

        Returns a list of assignments for the course sorted by due date. For
        each assignment returns basic assignment information, the grade breakdown
        (including the student's actual grade), and the basic submission
        information for the student's submission if it exists.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - student_id
        """
            ID
        """
        path["student_id"] = student_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/analytics/users/{student_id}/assignments with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/analytics/users/{student_id}/assignments".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def get_user_in_a_course_level_messaging_data(self, course_id, student_id):
        """
        Get user-in-a-course-level messaging data.

        Returns messaging "hits" grouped by day through the entire history of the
        course. Returns a hash containing the number of instructor-to-student messages,
        and student-to-instructor messages, where the hash keys are dates
        in the format "YYYY-MM-DD". Message hits include Conversation messages and
        comments on homework submissions.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - student_id
        """
            ID
        """
        path["student_id"] = student_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/analytics/users/{student_id}/communication with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/analytics/users/{student_id}/communication".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )
