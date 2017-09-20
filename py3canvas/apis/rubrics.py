"""Rubrics API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class RubricsAPI(BaseCanvasAPI):
    """Rubrics API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for RubricsAPI."""
        super(RubricsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.RubricsAPI")

    def list_rubrics_accounts(self, account_id):
        """
        List rubrics.

        Returns the paginated list of active rubrics for the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        self.logger.debug("GET /api/v1/accounts/{account_id}/rubrics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/rubrics".format(**path), data=data, params=params, no_data=True)

    def list_rubrics_courses(self, course_id):
        """
        List rubrics.

        Returns the paginated list of active rubrics for the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        self.logger.debug("GET /api/v1/courses/{course_id}/rubrics with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/rubrics".format(**path), data=data, params=params, no_data=True)

    def get_single_rubric_accounts(self, id, account_id, include=None, style=None):
        """
        Get a single rubric.

        Returns the rubric with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """ID"""
        path["account_id"] = account_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """If included, the type of associated rubric assessments to return. If not included, assessments will be omitted."""
        if include is not None:
            self._validate_enum(include, ["assessments", "graded_assessments", "peer_assessments"])
            params["include"] = include

        # OPTIONAL - style
        """Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted."""
        if style is not None:
            self._validate_enum(style, ["full", "comments_only"])
            params["style"] = style

        self.logger.debug("GET /api/v1/accounts/{account_id}/rubrics/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/rubrics/{id}".format(**path), data=data, params=params, single_item=True)

    def get_single_rubric_courses(self, id, course_id, include=None, style=None):
        """
        Get a single rubric.

        Returns the rubric with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """ID"""
        path["course_id"] = course_id

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - include
        """If included, the type of associated rubric assessments to return. If not included, assessments will be omitted."""
        if include is not None:
            self._validate_enum(include, ["assessments", "graded_assessments", "peer_assessments"])
            params["include"] = include

        # OPTIONAL - style
        """Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted."""
        if style is not None:
            self._validate_enum(style, ["full", "comments_only"])
            params["style"] = style

        self.logger.debug("GET /api/v1/courses/{course_id}/rubrics/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/rubrics/{id}".format(**path), data=data, params=params, single_item=True)


class Rubricassessment(BaseModel):
    """Rubricassessment Model."""

    def __init__(self, artifact_id=None, artifact_attempt=None, assessment_type=None, comments=None, data=None, score=None, rubric_association_id=None, artifact_type=None, assessor_id=None, rubric_id=None, id=None):
        """Init method for Rubricassessment class."""
        self._artifact_id = artifact_id
        self._artifact_attempt = artifact_attempt
        self._assessment_type = assessment_type
        self._comments = comments
        self._data = data
        self._score = score
        self._rubric_association_id = rubric_association_id
        self._artifact_type = artifact_type
        self._assessor_id = assessor_id
        self._rubric_id = rubric_id
        self._id = id

        self.logger = logging.getLogger('py3canvas.Rubricassessment')

    @property
    def artifact_id(self):
        """the id of the object of the assessment."""
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, value):
        """Setter for artifact_id property."""
        self.logger.warn("Setting values on artifact_id will NOT update the remote Canvas instance.")
        self._artifact_id = value

    @property
    def artifact_attempt(self):
        """the current number of attempts made on the object of the assessment."""
        return self._artifact_attempt

    @artifact_attempt.setter
    def artifact_attempt(self, value):
        """Setter for artifact_attempt property."""
        self.logger.warn("Setting values on artifact_attempt will NOT update the remote Canvas instance.")
        self._artifact_attempt = value

    @property
    def assessment_type(self):
        """the type of assessment. values will be either 'grading', 'peer_review', or 'provisional_grade'."""
        return self._assessment_type

    @assessment_type.setter
    def assessment_type(self, value):
        """Setter for assessment_type property."""
        self.logger.warn("Setting values on assessment_type will NOT update the remote Canvas instance.")
        self._assessment_type = value

    @property
    def comments(self):
        """(Optional) If 'comments_only' is included in the 'style' parameter, returned assessments will include only the comments portion of their data hash. If the user does not request a style, this key will be absent."""
        return self._comments

    @comments.setter
    def comments(self, value):
        """Setter for comments property."""
        self.logger.warn("Setting values on comments will NOT update the remote Canvas instance.")
        self._comments = value

    @property
    def data(self):
        """(Optional) If 'full' is included in the 'style' parameter, returned assessments will have their full details contained in their data hash. If the user does not request a style, this key will be absent."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn("Setting values on data will NOT update the remote Canvas instance.")
        self._data = value

    @property
    def score(self):
        """score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def rubric_association_id(self):
        """rubric_association_id."""
        return self._rubric_association_id

    @rubric_association_id.setter
    def rubric_association_id(self, value):
        """Setter for rubric_association_id property."""
        self.logger.warn("Setting values on rubric_association_id will NOT update the remote Canvas instance.")
        self._rubric_association_id = value

    @property
    def artifact_type(self):
        """the object of the assessment."""
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, value):
        """Setter for artifact_type property."""
        self.logger.warn("Setting values on artifact_type will NOT update the remote Canvas instance.")
        self._artifact_type = value

    @property
    def assessor_id(self):
        """user id of the person who made the assessment."""
        return self._assessor_id

    @assessor_id.setter
    def assessor_id(self, value):
        """Setter for assessor_id property."""
        self.logger.warn("Setting values on assessor_id will NOT update the remote Canvas instance.")
        self._assessor_id = value

    @property
    def rubric_id(self):
        """the rubric the assessment belongs to."""
        return self._rubric_id

    @rubric_id.setter
    def rubric_id(self, value):
        """Setter for rubric_id property."""
        self.logger.warn("Setting values on rubric_id will NOT update the remote Canvas instance.")
        self._rubric_id = value

    @property
    def id(self):
        """the ID of the rubric."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value


class Rubric(BaseModel):
    """Rubric Model."""

    def __init__(self, read_only=None, title=None, context_type=None, context_id=None, points_possible=None, free_form_criterion_comments=None, hide_score_total=None, assessments=None, id=None, reusable=None):
        """Init method for Rubric class."""
        self._read_only = read_only
        self._title = title
        self._context_type = context_type
        self._context_id = context_id
        self._points_possible = points_possible
        self._free_form_criterion_comments = free_form_criterion_comments
        self._hide_score_total = hide_score_total
        self._assessments = assessments
        self._id = id
        self._reusable = reusable

        self.logger = logging.getLogger('py3canvas.Rubric')

    @property
    def read_only(self):
        """read_only."""
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """Setter for read_only property."""
        self.logger.warn("Setting values on read_only will NOT update the remote Canvas instance.")
        self._read_only = value

    @property
    def title(self):
        """title of the rubric."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value

    @property
    def context_type(self):
        """context_type."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn("Setting values on context_type will NOT update the remote Canvas instance.")
        self._context_type = value

    @property
    def context_id(self):
        """the context owning the rubric."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn("Setting values on context_id will NOT update the remote Canvas instance.")
        self._context_id = value

    @property
    def points_possible(self):
        """points_possible."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn("Setting values on points_possible will NOT update the remote Canvas instance.")
        self._points_possible = value

    @property
    def free_form_criterion_comments(self):
        """whether or not free-form comments are used."""
        return self._free_form_criterion_comments

    @free_form_criterion_comments.setter
    def free_form_criterion_comments(self, value):
        """Setter for free_form_criterion_comments property."""
        self.logger.warn("Setting values on free_form_criterion_comments will NOT update the remote Canvas instance.")
        self._free_form_criterion_comments = value

    @property
    def hide_score_total(self):
        """hide_score_total."""
        return self._hide_score_total

    @hide_score_total.setter
    def hide_score_total(self, value):
        """Setter for hide_score_total property."""
        self.logger.warn("Setting values on hide_score_total will NOT update the remote Canvas instance.")
        self._hide_score_total = value

    @property
    def assessments(self):
        """If an assessment type is included in the 'include' parameter, includes an array of rubric assessment objects for a given rubric, based on the assessment type requested. If the user does not request an assessment type this key will be absent."""
        return self._assessments

    @assessments.setter
    def assessments(self, value):
        """Setter for assessments property."""
        self.logger.warn("Setting values on assessments will NOT update the remote Canvas instance.")
        self._assessments = value

    @property
    def id(self):
        """the ID of the rubric."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def reusable(self):
        """reusable."""
        return self._reusable

    @reusable.setter
    def reusable(self, value):
        """Setter for reusable property."""
        self.logger.warn("Setting values on reusable will NOT update the remote Canvas instance.")
        self._reusable = value

