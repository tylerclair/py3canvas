"""SisIntegration API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class SisIntegrationAPI(BaseCanvasAPI):
    """SisIntegration API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SisIntegrationAPI."""
        super(SisIntegrationAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SisIntegrationAPI")

    def retrieve_assignments_enabled_for_grade_export_to_sis_accounts(self, account_id, course_id=None, ends_after=None, include=None, starts_before=None):
        """
        Retrieve assignments enabled for grade export to SIS.

        Retrieve a list of published assignments flagged as "post_to_sis". Assignment group and section information are
        included for convenience.
        
        Each section includes course information for the origin course and the cross-listed course, if applicable. The
        `origin_course` is the course to which the section belongs or the course from which the section was cross-listed.
        Generally, the `origin_course` should be preferred when performing integration work. The `xlist_course` is provided
        for consistency and is only present when the section has been cross-listed.
        
        The `override` is only provided if the Differentiated Assignments course feature is turned on and the assignment
        has an override for that section. When there is an override for the assignment the override object's keys/values can
        be merged with the top level assignment object to create a view of the assignment object specific to that section.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """The ID of the account to query."""
        path["account_id"] = account_id

        # OPTIONAL - course_id
        """The ID of the course to query."""
        if course_id is not None:
            params["course_id"] = course_id

        # OPTIONAL - starts_before
        """When searching on an account, restricts to courses that start before
        this date (if they have a start date)"""
        if starts_before is not None:
            if issubclass(starts_before.__class__, str):
                starts_before = self._validate_iso8601_string(starts_before)
            elif issubclass(starts_before.__class__, date) or issubclass(starts_before.__class__, datetime):
                starts_before = starts_before.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["starts_before"] = starts_before

        # OPTIONAL - ends_after
        """When searching on an account, restricts to courses that end after this
        date (if they have an end date)"""
        if ends_after is not None:
            if issubclass(ends_after.__class__, str):
                ends_after = self._validate_iso8601_string(ends_after)
            elif issubclass(ends_after.__class__, date) or issubclass(ends_after.__class__, datetime):
                ends_after = ends_after.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["ends_after"] = ends_after

        # OPTIONAL - include
        """Array of additional information to include.
        
        "student_overrides":: returns individual student override information"""
        if include is not None:
            self._validate_enum(include, ["student_overrides"])
            params["include"] = include

        self.logger.debug("GET /api/sis/accounts/{account_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/sis/accounts/{account_id}/assignments".format(**path), data=data, params=params, no_data=True)

    def retrieve_assignments_enabled_for_grade_export_to_sis_courses(self, course_id, account_id=None, ends_after=None, include=None, starts_before=None):
        """
        Retrieve assignments enabled for grade export to SIS.

        Retrieve a list of published assignments flagged as "post_to_sis". Assignment group and section information are
        included for convenience.
        
        Each section includes course information for the origin course and the cross-listed course, if applicable. The
        `origin_course` is the course to which the section belongs or the course from which the section was cross-listed.
        Generally, the `origin_course` should be preferred when performing integration work. The `xlist_course` is provided
        for consistency and is only present when the section has been cross-listed.
        
        The `override` is only provided if the Differentiated Assignments course feature is turned on and the assignment
        has an override for that section. When there is an override for the assignment the override object's keys/values can
        be merged with the top level assignment object to create a view of the assignment object specific to that section.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - account_id
        """The ID of the account to query."""
        if account_id is not None:
            params["account_id"] = account_id

        # REQUIRED - PATH - course_id
        """The ID of the course to query."""
        path["course_id"] = course_id

        # OPTIONAL - starts_before
        """When searching on an account, restricts to courses that start before
        this date (if they have a start date)"""
        if starts_before is not None:
            if issubclass(starts_before.__class__, str):
                starts_before = self._validate_iso8601_string(starts_before)
            elif issubclass(starts_before.__class__, date) or issubclass(starts_before.__class__, datetime):
                starts_before = starts_before.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["starts_before"] = starts_before

        # OPTIONAL - ends_after
        """When searching on an account, restricts to courses that end after this
        date (if they have an end date)"""
        if ends_after is not None:
            if issubclass(ends_after.__class__, str):
                ends_after = self._validate_iso8601_string(ends_after)
            elif issubclass(ends_after.__class__, date) or issubclass(ends_after.__class__, datetime):
                ends_after = ends_after.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["ends_after"] = ends_after

        # OPTIONAL - include
        """Array of additional information to include.
        
        "student_overrides":: returns individual student override information"""
        if include is not None:
            self._validate_enum(include, ["student_overrides"])
            params["include"] = include

        self.logger.debug("GET /api/sis/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/sis/courses/{course_id}/assignments".format(**path), data=data, params=params, no_data=True)

    def disable_assignments_currently_enabled_for_grade_export_to_sis(self, course_id, grading_period_id=None):
        """
        Disable assignments currently enabled for grade export to SIS.

        Disable all assignments flagged as "post_to_sis", with the option of making it
        specific to a grading period, in a course.
        
        On success, the response will be 204 No Content with an empty body.
        
        On failure, the response will be 400 Bad Request with a body of a specific
        message.
        
        For disabling assignments in a specific grading period
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """The ID of the course."""
        path["course_id"] = course_id

        # OPTIONAL - grading_period_id
        """The ID of the grading period."""
        if grading_period_id is not None:
            data["grading_period_id"] = grading_period_id

        self.logger.debug("PUT /api/sis/courses/{course_id}/disable_post_to_sis with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/sis/courses/{course_id}/disable_post_to_sis".format(**path), data=data, params=params, no_data=True)

