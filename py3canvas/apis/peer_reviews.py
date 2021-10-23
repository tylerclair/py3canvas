"""PeerReviews API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class PeerReviewsAPI(BaseCanvasAPI):
    """PeerReviews API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for PeerReviewsAPI."""
        super(PeerReviewsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.PeerReviewsAPI")

    def get_all_peer_reviews_courses_peer_reviews(self, assignment_id, course_id, include=None):
        """
        Get all Peer Reviews.

        Get a list of all Peer Reviews for this assignment
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


        # OPTIONAL - include
        """
            Associations to include with the peer review.
        """
        if include is not None:
            self._validate_enum(include, ["submission_comments", "user"])
            params["include"] = include


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/peer_reviews".format(**path), data=data, params=params, all_pages=True)

    def get_all_peer_reviews_sections_peer_reviews(self, assignment_id, section_id, include=None):
        """
        Get all Peer Reviews.

        Get a list of all Peer Reviews for this assignment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """
            ID
        """
        path["section_id"] = section_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # OPTIONAL - include
        """
            Associations to include with the peer review.
        """
        if include is not None:
            self._validate_enum(include, ["submission_comments", "user"])
            params["include"] = include


        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/peer_reviews".format(**path), data=data, params=params, all_pages=True)

    def get_all_peer_reviews_courses_submissions(self, assignment_id, course_id, submission_id, include=None):
        """
        Get all Peer Reviews.

        Get a list of all Peer Reviews for this assignment
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


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # OPTIONAL - include
        """
            Associations to include with the peer review.
        """
        if include is not None:
            self._validate_enum(include, ["submission_comments", "user"])
            params["include"] = include


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews".format(**path), data=data, params=params, all_pages=True)

    def get_all_peer_reviews_sections_submissions(self, assignment_id, section_id, submission_id, include=None):
        """
        Get all Peer Reviews.

        Get a list of all Peer Reviews for this assignment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """
            ID
        """
        path["section_id"] = section_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # OPTIONAL - include
        """
            Associations to include with the peer review.
        """
        if include is not None:
            self._validate_enum(include, ["submission_comments", "user"])
            params["include"] = include


        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews".format(**path), data=data, params=params, all_pages=True)

    def create_peer_review_courses(self, assignment_id, course_id, submission_id, user_id):
        """
        Create Peer Review.

        Create a peer review for the assignment
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


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # REQUIRED - user_id
        """
            user_id to assign as reviewer on this assignment
        """
        data["user_id"] = user_id


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews".format(**path), data=data, params=params, single_item=True)

    def create_peer_review_sections(self, assignment_id, section_id, submission_id, user_id):
        """
        Create Peer Review.

        Create a peer review for the assignment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """
            ID
        """
        path["section_id"] = section_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # REQUIRED - user_id
        """
            user_id to assign as reviewer on this assignment
        """
        data["user_id"] = user_id


        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews".format(**path), data=data, params=params, single_item=True)

    def delete_peer_review_courses(self, assignment_id, course_id, submission_id, user_id):
        """
        Delete Peer Review.

        Delete a peer review for the assignment
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


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # REQUIRED - user_id
        """
            user_id to delete as reviewer on this assignment
        """
        params["user_id"] = user_id


        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews".format(**path), data=data, params=params, single_item=True)

    def delete_peer_review_sections(self, assignment_id, section_id, submission_id, user_id):
        """
        Delete Peer Review.

        Delete a peer review for the assignment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """
            ID
        """
        path["section_id"] = section_id


        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # REQUIRED - user_id
        """
            user_id to delete as reviewer on this assignment
        """
        params["user_id"] = user_id


        self.logger.debug("DELETE /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{submission_id}/peer_reviews".format(**path), data=data, params=params, single_item=True)


class Peerreview(BaseModel):
    """Peerreview Model."""

    def __init__(self, assessor_id=None, asset_id=None, asset_type=None, id=None, user_id=None, workflow_state=None, user=None, assessor=None, submission_comments=None):
        """Init method for Peerreview class."""
        self._assessor_id = assessor_id
        self._asset_id = asset_id
        self._asset_type = asset_type
        self._id = id
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._user = user
        self._assessor = assessor
        self._submission_comments = submission_comments

        self.logger = logging.getLogger('py3canvas.Peerreview')

    @property
    def assessor_id(self):
        """The assessors user id."""
        return self._assessor_id

    @assessor_id.setter
    def assessor_id(self, value):
        """Setter for assessor_id property."""
        self.logger.warn("Setting values on assessor_id will NOT update the remote Canvas instance.")
        self._assessor_id = value

    @property
    def asset_id(self):
        """The id for the asset associated with this Peer Review."""
        return self._asset_id

    @asset_id.setter
    def asset_id(self, value):
        """Setter for asset_id property."""
        self.logger.warn("Setting values on asset_id will NOT update the remote Canvas instance.")
        self._asset_id = value

    @property
    def asset_type(self):
        """The type of the asset."""
        return self._asset_type

    @asset_type.setter
    def asset_type(self, value):
        """Setter for asset_type property."""
        self.logger.warn("Setting values on asset_type will NOT update the remote Canvas instance.")
        self._asset_type = value

    @property
    def id(self):
        """The id of the Peer Review."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def user_id(self):
        """The user id for the owner of the asset."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """The state of the Peer Review, either 'assigned' or 'completed'."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def user(self):
        """the User object for the owner of the asset if the user include parameter is provided (see user API) (optional)."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

    @property
    def assessor(self):
        """The User object for the assessor if the user include parameter is provided (see user API) (optional)."""
        return self._assessor

    @assessor.setter
    def assessor(self, value):
        """Setter for assessor property."""
        self.logger.warn("Setting values on assessor will NOT update the remote Canvas instance.")
        self._assessor = value

    @property
    def submission_comments(self):
        """The submission comments associated with this Peer Review if the submission_comment include parameter is provided (see submissions API) (optional)."""
        return self._submission_comments

    @submission_comments.setter
    def submission_comments(self, value):
        """Setter for submission_comments property."""
        self.logger.warn("Setting values on submission_comments will NOT update the remote Canvas instance.")
        self._submission_comments = value

