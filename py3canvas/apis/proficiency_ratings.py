"""ProficiencyRatings API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ProficiencyRatingsAPI(BaseCanvasAPI):
    """ProficiencyRatings API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ProficiencyRatingsAPI."""
        super(ProficiencyRatingsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ProficiencyRatingsAPI")

    def create_update_proficiency_ratings_accounts(self, account_id, ratings_color=None, ratings_description=None, ratings_mastery=None, ratings_points=None):
        """
        Create/update proficiency ratings.

        Create or update account-level proficiency ratings. These ratings will apply to all
        sub-accounts, unless they have their own account-level proficiency ratings defined.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # OPTIONAL - ratings[description]
        """
            The description of the rating level.
        """
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description


        # OPTIONAL - ratings[points]
        """
            The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value.
        """
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points


        # OPTIONAL - ratings[mastery]
        """
            Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery.
        """
        if ratings_mastery is not None:
            data["ratings[mastery]"] = ratings_mastery


        # OPTIONAL - ratings[color]
        """
            The color associated with the rating level. Should be a hex color code like '00FFFF'.
        """
        if ratings_color is not None:
            data["ratings[color]"] = ratings_color


        self.logger.debug("POST /api/v1/accounts/{account_id}/outcome_proficiency with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/outcome_proficiency".format(**path), data=data, params=params, single_item=True)

    def create_update_proficiency_ratings_courses(self, course_id, ratings_color=None, ratings_description=None, ratings_mastery=None, ratings_points=None):
        """
        Create/update proficiency ratings.

        Create or update account-level proficiency ratings. These ratings will apply to all
        sub-accounts, unless they have their own account-level proficiency ratings defined.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - ratings[description]
        """
            The description of the rating level.
        """
        if ratings_description is not None:
            data["ratings[description]"] = ratings_description


        # OPTIONAL - ratings[points]
        """
            The non-negative number of points of the rating level. Points across ratings should be strictly decreasing in value.
        """
        if ratings_points is not None:
            data["ratings[points]"] = ratings_points


        # OPTIONAL - ratings[mastery]
        """
            Indicates the rating level where mastery is first achieved. Only one rating in a proficiency should be marked for mastery.
        """
        if ratings_mastery is not None:
            data["ratings[mastery]"] = ratings_mastery


        # OPTIONAL - ratings[color]
        """
            The color associated with the rating level. Should be a hex color code like '00FFFF'.
        """
        if ratings_color is not None:
            data["ratings[color]"] = ratings_color


        self.logger.debug("POST /api/v1/courses/{course_id}/outcome_proficiency with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/outcome_proficiency".format(**path), data=data, params=params, single_item=True)

    def get_proficiency_ratings_accounts(self, account_id):
        """
        Get proficiency ratings.

        Get account-level proficiency ratings. If not defined for this account,
        it will return proficiency ratings for the nearest super-account with ratings defined.
        Will return 404 if none found.
        
          Examples:
            curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
                -H 'Authorization: Bearer <token>'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/outcome_proficiency with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/outcome_proficiency".format(**path), data=data, params=params, single_item=True)

    def get_proficiency_ratings_courses(self, course_id):
        """
        Get proficiency ratings.

        Get account-level proficiency ratings. If not defined for this account,
        it will return proficiency ratings for the nearest super-account with ratings defined.
        Will return 404 if none found.
        
          Examples:
            curl https://<canvas>/api/v1/accounts/<account_id>/outcome_proficiency \
                -H 'Authorization: Bearer <token>'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/courses/{course_id}/outcome_proficiency with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/outcome_proficiency".format(**path), data=data, params=params, single_item=True)


class Proficiencyrating(BaseModel):
    """Proficiencyrating Model."""

    def __init__(self, description=None, points=None, mastery=None, color=None):
        """Init method for Proficiencyrating class."""
        self._description = description
        self._points = points
        self._mastery = mastery
        self._color = color

        self.logger = logging.getLogger('py3canvas.Proficiencyrating')

    @property
    def description(self):
        """The description of the rating."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def points(self):
        """A non-negative number of points for the rating."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn("Setting values on points will NOT update the remote Canvas instance.")
        self._points = value

    @property
    def mastery(self):
        """Indicates the rating where mastery is first achieved."""
        return self._mastery

    @mastery.setter
    def mastery(self, value):
        """Setter for mastery property."""
        self.logger.warn("Setting values on mastery will NOT update the remote Canvas instance.")
        self._mastery = value

    @property
    def color(self):
        """The hex color code of the rating."""
        return self._color

    @color.setter
    def color(self, value):
        """Setter for color property."""
        self.logger.warn("Setting values on color will NOT update the remote Canvas instance.")
        self._color = value


class Proficiency(BaseModel):
    """Proficiency Model."""

    def __init__(self, ratings=None):
        """Init method for Proficiency class."""
        self._ratings = ratings

        self.logger = logging.getLogger('py3canvas.Proficiency')

    @property
    def ratings(self):
        """An array of proficiency ratings. See the ProficiencyRating specification above."""
        return self._ratings

    @ratings.setter
    def ratings(self, value):
        """Setter for ratings property."""
        self.logger.warn("Setting values on ratings will NOT update the remote Canvas instance.")
        self._ratings = value

