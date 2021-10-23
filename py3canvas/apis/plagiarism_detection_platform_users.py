"""PlagiarismDetectionPlatformUsers API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class PlagiarismDetectionPlatformUsersAPI(BaseCanvasAPI):
    """PlagiarismDetectionPlatformUsers API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PlagiarismDetectionPlatformUsersAPI."""
        super(PlagiarismDetectionPlatformUsersAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PlagiarismDetectionPlatformUsersAPI")

    def get_single_user_lti(self, id):
        """
        Get a single user (lti).

        Get a single Canvas user by Canvas id or LTI id. Tool providers may only access
        users that have been assigned an assignment associated with their tool.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/lti/users/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/users/{id}".format(**path), data=data, params=params, single_item=True)

    def get_all_users_in_group_lti(self, group_id):
        """
        Get all users in a group (lti).

        Get all Canvas users in a group. Tool providers may only access
        groups that belong to the context the tool is installed in.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        self.logger.debug("GET /api/lti/groups/{group_id}/users with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/groups/{group_id}/users".format(**path), data=data, params=params, all_pages=True)

