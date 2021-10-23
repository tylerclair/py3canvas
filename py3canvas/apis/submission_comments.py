"""SubmissionComments API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class SubmissionCommentsAPI(BaseCanvasAPI):
    """SubmissionComments API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SubmissionCommentsAPI."""
        super(SubmissionCommentsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SubmissionCommentsAPI")

    def edit_submission_comment(self, assignment_id, course_id, id, user_id, comment=None):
        """
        Edit a submission comment.

        Edit the given submission comment.
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - comment
        """
            If this argument is present, edit the text of a comment.
        """
        if comment is not None:
            data["comment"] = comment


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id}".format(**path), data=data, params=params, single_item=True)

    def delete_submission_comment(self, assignment_id, course_id, id, user_id):
        """
        Delete a submission comment.

        Delete the given submission comment.
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/{id}".format(**path), data=data, params=params, single_item=True)

    def upload_file(self, assignment_id, course_id, user_id):
        """
        Upload a file.

        Upload a file to attach to a submission comment
        
        See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        
        The final step of the file upload workflow will return the attachment data,
        including the new file id. The caller can then PUT the file_id to the
        submission API to attach it to a comment
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/comments/files".format(**path), data=data, params=params, no_data=True)

