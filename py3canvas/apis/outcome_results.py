"""OutcomeResults API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class OutcomeResultsAPI(BaseCanvasAPI):
    """OutcomeResults API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for OutcomeResultsAPI."""
        super(OutcomeResultsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.OutcomeResultsAPI")

    def get_outcome_results(
        self,
        course_id,
        include=None,
        include_hidden=None,
        outcome_ids=None,
        user_ids=None,
    ):
        """
        Get outcome results.

        Gets the outcome results for users and outcomes in the specified context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - user_ids
        """
            If specified, only the users whose ids are given will be included in the
        results. SIS ids can be used, prefixed by "sis_user_id:".
        It is an error to specify an id for a user who is not a student in
        the context.
        """
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - outcome_ids
        """
            If specified, only the outcomes whose ids are given will be included in the
        results. it is an error to specify an id for an outcome which is not linked
        to the context.
        """
        if outcome_ids is not None:
            params["outcome_ids"] = outcome_ids

        # OPTIONAL - include
        """
            [String, "alignments"|"outcomes"|"outcomes.alignments"|"outcome_groups"|"outcome_links"|"outcome_paths"|"users"]
        Specify additional collections to be side loaded with the result.
        "alignments" includes only the alignments referenced by the returned
        results.
        "outcomes.alignments" includes all alignments referenced by outcomes in the
        context.
        """
        if include is not None:
            params["include"] = include

        # OPTIONAL - include_hidden
        """
            If true, results that are hidden from the learning mastery gradebook and student rollup
        scores will be included
        """
        if include_hidden is not None:
            params["include_hidden"] = include_hidden

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/outcome_results with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/outcome_results".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_outcome_result_rollups(
        self,
        course_id,
        aggregate=None,
        aggregate_stat=None,
        exclude=None,
        include=None,
        outcome_ids=None,
        sort_by=None,
        sort_order=None,
        sort_outcome_id=None,
        user_ids=None,
    ):
        """
        Get outcome result rollups.

        Gets the outcome rollups for the users and outcomes in the specified
        context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - aggregate
        """
            If specified, instead of returning one rollup for each user, all the user
        rollups will be combined into one rollup for the course that will contain
        the average (or median, see below) rollup score for each outcome.
        """
        if aggregate is not None:
            self._validate_enum(aggregate, ["course"])
            params["aggregate"] = aggregate

        # OPTIONAL - aggregate_stat
        """
            If aggregate rollups requested, then this value determines what
        statistic is used for the aggregate. Defaults to "mean" if this value
        is not specified.
        """
        if aggregate_stat is not None:
            self._validate_enum(aggregate_stat, ["mean", "median"])
            params["aggregate_stat"] = aggregate_stat

        # OPTIONAL - user_ids
        """
            If specified, only the users whose ids are given will be included in the
        results or used in an aggregate result. it is an error to specify an id
        for a user who is not a student in the context
        """
        if user_ids is not None:
            params["user_ids"] = user_ids

        # OPTIONAL - outcome_ids
        """
            If specified, only the outcomes whose ids are given will be included in the
        results. it is an error to specify an id for an outcome which is not linked
        to the context.
        """
        if outcome_ids is not None:
            params["outcome_ids"] = outcome_ids

        # OPTIONAL - include
        """
            [String, "courses"|"outcomes"|"outcomes.alignments"|"outcome_groups"|"outcome_links"|"outcome_paths"|"users"]
        Specify additional collections to be side loaded with the result.
        """
        if include is not None:
            params["include"] = include

        # OPTIONAL - exclude
        """
            Specify additional values to exclude. "missing_user_rollups" excludes
        rollups for users without results.
        """
        if exclude is not None:
            self._validate_enum(exclude, ["missing_user_rollups"])
            params["exclude"] = exclude

        # OPTIONAL - sort_by
        """
            If specified, sorts outcome result rollups. "student" sorting will sort
        by a user's sortable name. "outcome" sorting will sort by the given outcome's
        rollup score. The latter requires specifying the "sort_outcome_id" parameter.
        By default, the sort order is ascending.
        """
        if sort_by is not None:
            self._validate_enum(sort_by, ["student", "outcome"])
            params["sort_by"] = sort_by

        # OPTIONAL - sort_outcome_id
        """
            If outcome sorting requested, then this determines which outcome to use
        for rollup score sorting.
        """
        if sort_outcome_id is not None:
            params["sort_outcome_id"] = sort_outcome_id

        # OPTIONAL - sort_order
        """
            If sorting requested, then this allows changing the default sort order of
        ascending to descending.
        """
        if sort_order is not None:
            self._validate_enum(sort_order, ["asc", "desc"])
            params["sort_order"] = sort_order

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/outcome_rollups with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/outcome_rollups".format(**path),
            data=data,
            params=params,
            no_data=True,
        )


class Outcomeresult(BaseModel):
    """Outcomeresult Model.
    A student's result for an outcome"""

    def __init__(
        self,
        id=None,
        score=None,
        submitted_or_assessed_at=None,
        links=None,
        percent=None,
    ):
        """Init method for Outcomeresult class."""
        self._id = id
        self._score = score
        self._submitted_or_assessed_at = submitted_or_assessed_at
        self._links = links
        self._percent = percent

        self.logger = logging.getLogger("py3canvas.Outcomeresult")

    @property
    def id(self):
        """A unique identifier for this result."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def score(self):
        """The student's score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn(
            "Setting values on score will NOT update the remote Canvas instance."
        )
        self._score = value

    @property
    def submitted_or_assessed_at(self):
        """The datetime the resulting OutcomeResult was submitted at, or absent that, when it was assessed."""
        return self._submitted_or_assessed_at

    @submitted_or_assessed_at.setter
    def submitted_or_assessed_at(self, value):
        """Setter for submitted_or_assessed_at property."""
        self.logger.warn(
            "Setting values on submitted_or_assessed_at will NOT update the remote Canvas instance."
        )
        self._submitted_or_assessed_at = value

    @property
    def links(self):
        """Unique identifiers of objects associated with this result."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn(
            "Setting values on links will NOT update the remote Canvas instance."
        )
        self._links = value

    @property
    def percent(self):
        """score's percent of maximum points possible for outcome, scaled to reflect any custom mastery levels that differ from the learning outcome."""
        return self._percent

    @percent.setter
    def percent(self, value):
        """Setter for percent property."""
        self.logger.warn(
            "Setting values on percent will NOT update the remote Canvas instance."
        )
        self._percent = value


class Outcomerollupscorelinks(BaseModel):
    """Outcomerollupscorelinks Model."""

    def __init__(self, outcome=None):
        """Init method for Outcomerollupscorelinks class."""
        self._outcome = outcome

        self.logger = logging.getLogger("py3canvas.Outcomerollupscorelinks")

    @property
    def outcome(self):
        """The id of the related outcome."""
        return self._outcome

    @outcome.setter
    def outcome(self, value):
        """Setter for outcome property."""
        self.logger.warn(
            "Setting values on outcome will NOT update the remote Canvas instance."
        )
        self._outcome = value


class Outcomerollupscore(BaseModel):
    """Outcomerollupscore Model."""

    def __init__(self, score=None, count=None, links=None):
        """Init method for Outcomerollupscore class."""
        self._score = score
        self._count = count
        self._links = links

        self.logger = logging.getLogger("py3canvas.Outcomerollupscore")

    @property
    def score(self):
        """The rollup score for the outcome, based on the student alignment scores related to the outcome. This could be null if the student has no related scores."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn(
            "Setting values on score will NOT update the remote Canvas instance."
        )
        self._score = value

    @property
    def count(self):
        """The number of alignment scores included in this rollup."""
        return self._count

    @count.setter
    def count(self, value):
        """Setter for count property."""
        self.logger.warn(
            "Setting values on count will NOT update the remote Canvas instance."
        )
        self._count = value

    @property
    def links(self):
        """links."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn(
            "Setting values on links will NOT update the remote Canvas instance."
        )
        self._links = value


class Outcomerolluplinks(BaseModel):
    """Outcomerolluplinks Model."""

    def __init__(self, course=None, user=None, section=None):
        """Init method for Outcomerolluplinks class."""
        self._course = course
        self._user = user
        self._section = section

        self.logger = logging.getLogger("py3canvas.Outcomerolluplinks")

    @property
    def course(self):
        """If an aggregate result was requested, the course field will be present. Otherwise, the user and section field will be present (Optional) The id of the course that this rollup applies to."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter for course property."""
        self.logger.warn(
            "Setting values on course will NOT update the remote Canvas instance."
        )
        self._course = value

    @property
    def user(self):
        """(Optional) The id of the user that this rollup applies to."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn(
            "Setting values on user will NOT update the remote Canvas instance."
        )
        self._user = value

    @property
    def section(self):
        """(Optional) The id of the section the user is in."""
        return self._section

    @section.setter
    def section(self, value):
        """Setter for section property."""
        self.logger.warn(
            "Setting values on section will NOT update the remote Canvas instance."
        )
        self._section = value


class Outcomerollup(BaseModel):
    """Outcomerollup Model."""

    def __init__(self, scores=None, name=None, links=None):
        """Init method for Outcomerollup class."""
        self._scores = scores
        self._name = name
        self._links = links

        self.logger = logging.getLogger("py3canvas.Outcomerollup")

    @property
    def scores(self):
        """an array of OutcomeRollupScore objects."""
        return self._scores

    @scores.setter
    def scores(self, value):
        """Setter for scores property."""
        self.logger.warn(
            "Setting values on scores will NOT update the remote Canvas instance."
        )
        self._scores = value

    @property
    def name(self):
        """The name of the resource for this rollup. For example, the user name."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def links(self):
        """links."""
        return self._links

    @links.setter
    def links(self, value):
        """Setter for links property."""
        self.logger.warn(
            "Setting values on links will NOT update the remote Canvas instance."
        )
        self._links = value


class Outcomealignment(BaseModel):
    """Outcomealignment Model.
    An asset aligned with this outcome"""

    def __init__(self, id=None, name=None, html_url=None):
        """Init method for Outcomealignment class."""
        self._id = id
        self._name = name
        self._html_url = html_url

        self.logger = logging.getLogger("py3canvas.Outcomealignment")

    @property
    def id(self):
        """A unique identifier for this alignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def name(self):
        """The name of this alignment."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def html_url(self):
        """(Optional) A URL for details about this alignment."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn(
            "Setting values on html_url will NOT update the remote Canvas instance."
        )
        self._html_url = value


class Outcomepath(BaseModel):
    """Outcomepath Model.
    The full path to an outcome"""

    def __init__(self, id=None, parts=None):
        """Init method for Outcomepath class."""
        self._id = id
        self._parts = parts

        self.logger = logging.getLogger("py3canvas.Outcomepath")

    @property
    def id(self):
        """A unique identifier for this outcome."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def parts(self):
        """an array of OutcomePathPart objects."""
        return self._parts

    @parts.setter
    def parts(self, value):
        """Setter for parts property."""
        self.logger.warn(
            "Setting values on parts will NOT update the remote Canvas instance."
        )
        self._parts = value


class Outcomepathpart(BaseModel):
    """Outcomepathpart Model.
    An outcome or outcome group"""

    def __init__(self, name=None):
        """Init method for Outcomepathpart class."""
        self._name = name

        self.logger = logging.getLogger("py3canvas.Outcomepathpart")

    @property
    def name(self):
        """The title of the outcome or outcome group."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value
