"""Result API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ResultAPI(BaseCanvasAPI):
    """Result API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ResultAPI."""
        super(ResultAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ResultAPI")

    def show_collection_of_results(self, course_id, line_item_id):
        """
        Show a collection of Results.

        Show existing Results of a line item. Can be used to retrieve a specific student's
        result by adding the user_id (defined as the lti_user_id or the Canvas user_id) as
        a query parameter (i.e. user_id=1000). If user_id is included, it will return only
        one Result in the collection if the result exists, otherwise it will be empty. May
        also limit number of results by adding the limit query param (i.e. limit=100)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - line_item_id
        """
            ID
        """
        path["line_item_id"] = line_item_id

        self.logger.debug(
            "GET /api/lti/courses/{course_id}/line_items/{line_item_id}/results with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/lti/courses/{course_id}/line_items/{line_item_id}/results".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def show_result(self, course_id, id, line_item_id):
        """
        Show a Result.

        Show existing Result of a line item.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - line_item_id
        """
            ID
        """
        path["line_item_id"] = line_item_id

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/lti/courses/{course_id}/line_items/{line_item_id}/results/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/lti/courses/{course_id}/line_items/{line_item_id}/results/{id}".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )


class Result(BaseModel):
    """Result Model."""

    def __init__(
        self,
        id=None,
        userId=None,
        resultScore=None,
        resultMaximum=None,
        comment=None,
        scoreOf=None,
    ):
        """Init method for Result class."""
        self._id = id
        self._userId = userId
        self._resultScore = resultScore
        self._resultMaximum = resultMaximum
        self._comment = comment
        self._scoreOf = scoreOf

        self.logger = logging.getLogger("py3canvas.Result")

    @property
    def id(self):
        """The fully qualified URL for showing the Result."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def userId(self):
        """The lti_user_id or the Canvas user_id."""
        return self._userId

    @userId.setter
    def userId(self, value):
        """Setter for userId property."""
        self.logger.warn(
            "Setting values on userId will NOT update the remote Canvas instance."
        )
        self._userId = value

    @property
    def resultScore(self):
        """The score of the result as defined by Canvas, scaled to the resultMaximum."""
        return self._resultScore

    @resultScore.setter
    def resultScore(self, value):
        """Setter for resultScore property."""
        self.logger.warn(
            "Setting values on resultScore will NOT update the remote Canvas instance."
        )
        self._resultScore = value

    @property
    def resultMaximum(self):
        """Maximum possible score for this result; 1 is the default value and will be assumed if not specified otherwise. Minimum value of 0 required."""
        return self._resultMaximum

    @resultMaximum.setter
    def resultMaximum(self, value):
        """Setter for resultMaximum property."""
        self.logger.warn(
            "Setting values on resultMaximum will NOT update the remote Canvas instance."
        )
        self._resultMaximum = value

    @property
    def comment(self):
        """Comment visible to the student about the result."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Setter for comment property."""
        self.logger.warn(
            "Setting values on comment will NOT update the remote Canvas instance."
        )
        self._comment = value

    @property
    def scoreOf(self):
        """URL of the line item this belongs to."""
        return self._scoreOf

    @scoreOf.setter
    def scoreOf(self, value):
        """Setter for scoreOf property."""
        self.logger.warn(
            "Setting values on scoreOf will NOT update the remote Canvas instance."
        )
        self._scoreOf = value
