"""Announcements API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class AnnouncementsAPI(BaseCanvasAPI):
    """Announcements API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AnnouncementsAPI."""
        super(AnnouncementsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AnnouncementsAPI")

    def list_announcements(self, context_codes, active_only=None, end_date=None, include=None, latest_only=None, start_date=None):
        """
        List announcements.

        Returns the paginated list of announcements for the given courses and date range.  Note that
        a +context_code+ field is added to the responses so you can tell which course each announcement
        belongs to.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - context_codes
        """
            List of context_codes to retrieve announcements for (for example, +course_123+). Only courses
        are presently supported. The call will fail unless the caller has View Announcements permission
        in all listed courses.
        """
        params["context_codes"] = context_codes


        # OPTIONAL - start_date
        """
            Only return announcements posted since the start_date (inclusive).
        Defaults to 14 days ago. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if start_date is not None:
            params["start_date"] = start_date


        # OPTIONAL - end_date
        """
            Only return announcements posted before the end_date (inclusive).
        Defaults to 28 days from start_date. The value should be formatted as: yyyy-mm-dd or ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        Announcements scheduled for future posting will only be returned to course administrators.
        """
        if end_date is not None:
            params["end_date"] = end_date


        # OPTIONAL - active_only
        """
            Only return active announcements that have been published.
        Applies only to requesting users that have permission to view
        unpublished items.
        Defaults to false for users with access to view unpublished items,
        otherwise true and unmodifiable.
        """
        if active_only is not None:
            params["active_only"] = active_only


        # OPTIONAL - latest_only
        """
            Only return the latest announcement for each associated context.
        The response will include at most one announcement for each
        specified context in the context_codes[] parameter.
        Defaults to false.
        """
        if latest_only is not None:
            params["latest_only"] = latest_only


        # OPTIONAL - include
        """
            Optional list of resources to include with the response. May include
        a string of the name of the resource. Possible values are:
        "sections", "sections_user_count"
        if "sections" is passed, includes the course sections that are associated
        with the topic, if the topic is specific to certain sections of the course.
        If "sections_user_count" is passed, then:
          (a) If sections were asked for *and* the topic is specific to certain
              course sections sections, includes the number of users in each
              section. (as part of the section json asked for above)
          (b) Else, includes at the root level the total number of users in the
              topic's context (group or course) that the topic applies to.
        """
        if include is not None:
            params["include"] = include


        self.logger.debug("GET /api/v1/announcements with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/announcements".format(**path), data=data, params=params, all_pages=True)

