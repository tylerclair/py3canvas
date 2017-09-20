"""LatePolicy API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class LatePolicyAPI(BaseCanvasAPI):
    """LatePolicy API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for LatePolicyAPI."""
        super(LatePolicyAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.LatePolicyAPI")

    def get_late_policy(self, id):
        """
        Get a late policy.

        Returns the late policy for a course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        self.logger.debug("GET /api/v1/courses/{id}/late_policy with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{id}/late_policy".format(**path), data=data, params=params, no_data=True)

    def create_late_policy(self, id, late_policy_late_submission_deduction=None, late_policy_late_submission_deduction_enabled=None, late_policy_late_submission_interval=None, late_policy_late_submission_minimum_percent=None, late_policy_late_submission_minimum_percent_enabled=None, late_policy_missing_submission_deduction=None, late_policy_missing_submission_deduction_enabled=None):
        """
        Create a late policy.

        Create a late policy. If the course already has a late policy, a
        bad_request is returned since there can only be one late policy
        per course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - late_policy[missing_submission_deduction_enabled]
        """Whether to enable the missing submission deduction late policy."""
        if late_policy_missing_submission_deduction_enabled is not None:
            data["late_policy[missing_submission_deduction_enabled]"] = late_policy_missing_submission_deduction_enabled

        # OPTIONAL - late_policy[missing_submission_deduction]
        """How many percentage points to deduct from a missing submission."""
        if late_policy_missing_submission_deduction is not None:
            data["late_policy[missing_submission_deduction]"] = late_policy_missing_submission_deduction

        # OPTIONAL - late_policy[late_submission_deduction_enabled]
        """Whether to enable the late submission deduction late policy."""
        if late_policy_late_submission_deduction_enabled is not None:
            data["late_policy[late_submission_deduction_enabled]"] = late_policy_late_submission_deduction_enabled

        # OPTIONAL - late_policy[late_submission_deduction]
        """How many percentage points to deduct per the late submission interval."""
        if late_policy_late_submission_deduction is not None:
            data["late_policy[late_submission_deduction]"] = late_policy_late_submission_deduction

        # OPTIONAL - late_policy[late_submission_interval]
        """The interval for late policies."""
        if late_policy_late_submission_interval is not None:
            data["late_policy[late_submission_interval]"] = late_policy_late_submission_interval

        # OPTIONAL - late_policy[late_submission_minimum_percent_enabled]
        """Whether to enable the late submission minimum percent for a late policy."""
        if late_policy_late_submission_minimum_percent_enabled is not None:
            data["late_policy[late_submission_minimum_percent_enabled]"] = late_policy_late_submission_minimum_percent_enabled

        # OPTIONAL - late_policy[late_submission_minimum_percent]
        """The minimum grade a submissions can have in percentage points."""
        if late_policy_late_submission_minimum_percent is not None:
            data["late_policy[late_submission_minimum_percent]"] = late_policy_late_submission_minimum_percent

        self.logger.debug("POST /api/v1/courses/{id}/late_policy with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{id}/late_policy".format(**path), data=data, params=params, no_data=True)

    def patch_late_policy(self, id, late_policy_late_submission_deduction=None, late_policy_late_submission_deduction_enabled=None, late_policy_late_submission_interval=None, late_policy_late_submission_minimum_percent=None, late_policy_late_submission_minimum_percent_enabled=None, late_policy_missing_submission_deduction=None, late_policy_missing_submission_deduction_enabled=None):
        """
        Patch a late policy.

        Patch a late policy. No body is returned upon success.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """ID"""
        path["id"] = id

        # OPTIONAL - late_policy[missing_submission_deduction_enabled]
        """Whether to enable the missing submission deduction late policy."""
        if late_policy_missing_submission_deduction_enabled is not None:
            data["late_policy[missing_submission_deduction_enabled]"] = late_policy_missing_submission_deduction_enabled

        # OPTIONAL - late_policy[missing_submission_deduction]
        """How many percentage points to deduct from a missing submission."""
        if late_policy_missing_submission_deduction is not None:
            data["late_policy[missing_submission_deduction]"] = late_policy_missing_submission_deduction

        # OPTIONAL - late_policy[late_submission_deduction_enabled]
        """Whether to enable the late submission deduction late policy."""
        if late_policy_late_submission_deduction_enabled is not None:
            data["late_policy[late_submission_deduction_enabled]"] = late_policy_late_submission_deduction_enabled

        # OPTIONAL - late_policy[late_submission_deduction]
        """How many percentage points to deduct per the late submission interval."""
        if late_policy_late_submission_deduction is not None:
            data["late_policy[late_submission_deduction]"] = late_policy_late_submission_deduction

        # OPTIONAL - late_policy[late_submission_interval]
        """The interval for late policies."""
        if late_policy_late_submission_interval is not None:
            data["late_policy[late_submission_interval]"] = late_policy_late_submission_interval

        # OPTIONAL - late_policy[late_submission_minimum_percent_enabled]
        """Whether to enable the late submission minimum percent for a late policy."""
        if late_policy_late_submission_minimum_percent_enabled is not None:
            data["late_policy[late_submission_minimum_percent_enabled]"] = late_policy_late_submission_minimum_percent_enabled

        # OPTIONAL - late_policy[late_submission_minimum_percent]
        """The minimum grade a submissions can have in percentage points."""
        if late_policy_late_submission_minimum_percent is not None:
            data["late_policy[late_submission_minimum_percent]"] = late_policy_late_submission_minimum_percent

        self.logger.debug("PATCH /api/v1/courses/{id}/late_policy with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PATCH", "/api/v1/courses/{id}/late_policy".format(**path), data=data, params=params, no_data=True)


class Latepolicy(BaseModel):
    """Latepolicy Model."""

    def __init__(self, course_id, late_submission_deduction=0, late_submission_minimum_percent=0, late_submission_interval="day", created_at=None, late_submission_deduction_enabled=False, missing_submission_deduction_enabled=False, updated_at=None, late_submission_minimum_percent_enabled=False, missing_submission_deduction=0):
        """Init method for Latepolicy class."""
        self._late_submission_deduction = late_submission_deduction
        self._late_submission_minimum_percent = late_submission_minimum_percent
        self._late_submission_interval = late_submission_interval
        self._created_at = created_at
        self._late_submission_deduction_enabled = late_submission_deduction_enabled
        self._missing_submission_deduction_enabled = missing_submission_deduction_enabled
        self._updated_at = updated_at
        self._course_id = course_id
        self._late_submission_minimum_percent_enabled = late_submission_minimum_percent_enabled
        self._missing_submission_deduction = missing_submission_deduction
        self._id = id

        self.logger = logging.getLogger('py3canvas.Latepolicy')

    @property
    def late_submission_deduction(self):
        """amount of percentage points to deduct per late_submission_interval."""
        return self._late_submission_deduction

    @late_submission_deduction.setter
    def late_submission_deduction(self, value):
        """Setter for late_submission_deduction property."""
        self.logger.warn("Setting values on late_submission_deduction will NOT update the remote Canvas instance.")
        self._late_submission_deduction = value

    @property
    def late_submission_minimum_percent(self):
        """the minimum score a submission can receive in percentage points."""
        return self._late_submission_minimum_percent

    @late_submission_minimum_percent.setter
    def late_submission_minimum_percent(self, value):
        """Setter for late_submission_minimum_percent property."""
        self.logger.warn("Setting values on late_submission_minimum_percent will NOT update the remote Canvas instance.")
        self._late_submission_minimum_percent = value

    @property
    def late_submission_interval(self):
        """time interval for late submission deduction."""
        return self._late_submission_interval

    @late_submission_interval.setter
    def late_submission_interval(self, value):
        """Setter for late_submission_interval property."""
        self.logger.warn("Setting values on late_submission_interval will NOT update the remote Canvas instance.")
        self._late_submission_interval = value

    @property
    def created_at(self):
        """the time at which this late policy was originally created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def late_submission_deduction_enabled(self):
        """whether to enable late submission deductions."""
        return self._late_submission_deduction_enabled

    @late_submission_deduction_enabled.setter
    def late_submission_deduction_enabled(self, value):
        """Setter for late_submission_deduction_enabled property."""
        self.logger.warn("Setting values on late_submission_deduction_enabled will NOT update the remote Canvas instance.")
        self._late_submission_deduction_enabled = value

    @property
    def missing_submission_deduction_enabled(self):
        """whether to enable missing submission deductions."""
        return self._missing_submission_deduction_enabled

    @missing_submission_deduction_enabled.setter
    def missing_submission_deduction_enabled(self, value):
        """Setter for missing_submission_deduction_enabled property."""
        self.logger.warn("Setting values on missing_submission_deduction_enabled will NOT update the remote Canvas instance.")
        self._missing_submission_deduction_enabled = value

    @property
    def updated_at(self):
        """the time at which this late policy was last modified in any way."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value

    @property
    def course_id(self):
        """the unique identifier for the course."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn("Setting values on course_id will NOT update the remote Canvas instance.")
        self._course_id = value

    @property
    def late_submission_minimum_percent_enabled(self):
        """whether to enable late submission minimum percent."""
        return self._late_submission_minimum_percent_enabled

    @late_submission_minimum_percent_enabled.setter
    def late_submission_minimum_percent_enabled(self, value):
        """Setter for late_submission_minimum_percent_enabled property."""
        self.logger.warn("Setting values on late_submission_minimum_percent_enabled will NOT update the remote Canvas instance.")
        self._late_submission_minimum_percent_enabled = value

    @property
    def missing_submission_deduction(self):
        """amount of percentage points to deduct."""
        return self._missing_submission_deduction

    @missing_submission_deduction.setter
    def missing_submission_deduction(self, value):
        """Setter for missing_submission_deduction property."""
        self.logger.warn("Setting values on missing_submission_deduction will NOT update the remote Canvas instance.")
        self._missing_submission_deduction = value

    @property
    def id(self):
        """the unique identifier for the late policy."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

