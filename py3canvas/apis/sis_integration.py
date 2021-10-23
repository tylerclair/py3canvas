"""SisIntegration API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class SisIntegrationAPI(BaseCanvasAPI):
    """SisIntegration API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SisIntegrationAPI."""
        super(SisIntegrationAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SisIntegrationAPI")

    def retrieve_assignments_enabled_for_grade_export_to_sis_accounts(
        self,
        account_id,
        course_id=None,
        ends_after=None,
        include=None,
        starts_before=None,
    ):
        """
        Retrieve assignments enabled for grade export to SIS.

        Retrieve a list of published assignments flagged as "post_to_sis".
        See the Assignments API for more details on assignments.
        Assignment group and section information are included for convenience.

        Each section includes course information for the origin course and the
        cross-listed course, if applicable. The `origin_course` is the course to
        which the section belongs or the course from which the section was
        cross-listed. Generally, the `origin_course` should be preferred when
        performing integration work. The `xlist_course` is provided for consistency
        and is only present when the section has been cross-listed.
        See Sections API and Courses Api for me details.

        The `override` is only provided if the Differentiated Assignments course
        feature is turned on and the assignment has an override for that section.
        When there is an override for the assignment the override object's
        keys/values can be merged with the top level assignment object to create a
        view of the assignment object specific to that section.
        See Assignments api for more information on assignment overrides.

        restricts to courses that start before this date (if they have a start date)
        restricts to courses that end after this date (if they have an end date)
        information to include.

          "student_overrides":: returns individual student override information
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            The ID of the account to query.
        """
        path["account_id"] = account_id

        # OPTIONAL - course_id
        """
            The ID of the course to query.
        """
        if course_id is not None:
            params["course_id"] = course_id

        # OPTIONAL - starts_before
        """
            When searching on an account,
        """
        if starts_before is not None:
            if issubclass(starts_before.__class__, str):
                starts_before = self._validate_iso8601_string(starts_before)
            elif issubclass(starts_before.__class__, date) or issubclass(
                starts_before.__class__, datetime
            ):
                starts_before = starts_before.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["starts_before"] = starts_before

        # OPTIONAL - ends_after
        """
            When searching on an account,
        """
        if ends_after is not None:
            if issubclass(ends_after.__class__, str):
                ends_after = self._validate_iso8601_string(ends_after)
            elif issubclass(ends_after.__class__, date) or issubclass(
                ends_after.__class__, datetime
            ):
                ends_after = ends_after.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["ends_after"] = ends_after

        # OPTIONAL - include
        """
            Array of additional
        """
        if include is not None:
            self._validate_enum(include, ["student_overrides"])
            params["include"] = include

        self.logger.debug(
            "GET /api/sis/accounts/{account_id}/assignments with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/sis/accounts/{account_id}/assignments".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def retrieve_assignments_enabled_for_grade_export_to_sis_courses(
        self,
        course_id,
        account_id=None,
        ends_after=None,
        include=None,
        starts_before=None,
    ):
        """
        Retrieve assignments enabled for grade export to SIS.

        Retrieve a list of published assignments flagged as "post_to_sis".
        See the Assignments API for more details on assignments.
        Assignment group and section information are included for convenience.

        Each section includes course information for the origin course and the
        cross-listed course, if applicable. The `origin_course` is the course to
        which the section belongs or the course from which the section was
        cross-listed. Generally, the `origin_course` should be preferred when
        performing integration work. The `xlist_course` is provided for consistency
        and is only present when the section has been cross-listed.
        See Sections API and Courses Api for me details.

        The `override` is only provided if the Differentiated Assignments course
        feature is turned on and the assignment has an override for that section.
        When there is an override for the assignment the override object's
        keys/values can be merged with the top level assignment object to create a
        view of the assignment object specific to that section.
        See Assignments api for more information on assignment overrides.

        restricts to courses that start before this date (if they have a start date)
        restricts to courses that end after this date (if they have an end date)
        information to include.

          "student_overrides":: returns individual student override information
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - account_id
        """
            The ID of the account to query.
        """
        if account_id is not None:
            params["account_id"] = account_id

        # REQUIRED - PATH - course_id
        """
            The ID of the course to query.
        """
        path["course_id"] = course_id

        # OPTIONAL - starts_before
        """
            When searching on an account,
        """
        if starts_before is not None:
            if issubclass(starts_before.__class__, str):
                starts_before = self._validate_iso8601_string(starts_before)
            elif issubclass(starts_before.__class__, date) or issubclass(
                starts_before.__class__, datetime
            ):
                starts_before = starts_before.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["starts_before"] = starts_before

        # OPTIONAL - ends_after
        """
            When searching on an account,
        """
        if ends_after is not None:
            if issubclass(ends_after.__class__, str):
                ends_after = self._validate_iso8601_string(ends_after)
            elif issubclass(ends_after.__class__, date) or issubclass(
                ends_after.__class__, datetime
            ):
                ends_after = ends_after.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["ends_after"] = ends_after

        # OPTIONAL - include
        """
            Array of additional
        """
        if include is not None:
            self._validate_enum(include, ["student_overrides"])
            params["include"] = include

        self.logger.debug(
            "GET /api/sis/courses/{course_id}/assignments with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/sis/courses/{course_id}/assignments".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def disable_assignments_currently_enabled_for_grade_export_to_sis(
        self, course_id, grading_period_id=None
    ):
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
        """
            The ID of the course.
        """
        path["course_id"] = course_id

        # OPTIONAL - grading_period_id
        """
            The ID of the grading period.
        """
        if grading_period_id is not None:
            data["grading_period_id"] = grading_period_id

        self.logger.debug(
            "PUT /api/sis/courses/{course_id}/disable_post_to_sis with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/sis/courses/{course_id}/disable_post_to_sis".format(**path),
            data=data,
            params=params,
            no_data=True,
        )


class Sisassignment(BaseModel):
    """Sisassignment Model.
    Assignments that have post_to_sis enabled with other objects for convenience"""

    def __init__(
        self,
        id=None,
        course_id=None,
        name=None,
        created_at=None,
        due_at=None,
        unlock_at=None,
        lock_at=None,
        points_possible=None,
        submission_types=None,
        integration_id=None,
        integration_data=None,
        include_in_final_grade=None,
        assignment_group=None,
        sections=None,
        user_overrides=None,
    ):
        """Init method for Sisassignment class."""
        self._id = id
        self._course_id = course_id
        self._name = name
        self._created_at = created_at
        self._due_at = due_at
        self._unlock_at = unlock_at
        self._lock_at = lock_at
        self._points_possible = points_possible
        self._submission_types = submission_types
        self._integration_id = integration_id
        self._integration_data = integration_data
        self._include_in_final_grade = include_in_final_grade
        self._assignment_group = assignment_group
        self._sections = sections
        self._user_overrides = user_overrides

        self.logger = logging.getLogger("py3canvas.Sisassignment")

    @property
    def id(self):
        """The unique identifier for the assignment."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def course_id(self):
        """The unique identifier for the course."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn(
            "Setting values on course_id will NOT update the remote Canvas instance."
        )
        self._course_id = value

    @property
    def name(self):
        """the name of the assignment."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def created_at(self):
        """The time at which this assignment was originally created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def due_at(self):
        """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn(
            "Setting values on due_at will NOT update the remote Canvas instance."
        )
        self._due_at = value

    @property
    def unlock_at(self):
        """(Optional) Time at which this was/will be unlocked."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn(
            "Setting values on unlock_at will NOT update the remote Canvas instance."
        )
        self._unlock_at = value

    @property
    def lock_at(self):
        """(Optional) Time at which this was/will be locked."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn(
            "Setting values on lock_at will NOT update the remote Canvas instance."
        )
        self._lock_at = value

    @property
    def points_possible(self):
        """The maximum points possible for the assignment."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn(
            "Setting values on points_possible will NOT update the remote Canvas instance."
        )
        self._points_possible = value

    @property
    def submission_types(self):
        """the types of submissions allowed for this assignment list containing one or more of the following: 'discussion_topic', 'online_quiz', 'on_paper', 'none', 'external_tool', 'online_text_entry', 'online_url', 'online_upload', 'media_recording', 'student_annotation'."""
        return self._submission_types

    @submission_types.setter
    def submission_types(self, value):
        """Setter for submission_types property."""
        self.logger.warn(
            "Setting values on submission_types will NOT update the remote Canvas instance."
        )
        self._submission_types = value

    @property
    def integration_id(self):
        """Third Party integration id for assignment."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn(
            "Setting values on integration_id will NOT update the remote Canvas instance."
        )
        self._integration_id = value

    @property
    def integration_data(self):
        """(optional, Third Party integration data for assignment)."""
        return self._integration_data

    @integration_data.setter
    def integration_data(self, value):
        """Setter for integration_data property."""
        self.logger.warn(
            "Setting values on integration_data will NOT update the remote Canvas instance."
        )
        self._integration_data = value

    @property
    def include_in_final_grade(self):
        """If false, the assignment will be omitted from the student's final grade."""
        return self._include_in_final_grade

    @include_in_final_grade.setter
    def include_in_final_grade(self, value):
        """Setter for include_in_final_grade property."""
        self.logger.warn(
            "Setting values on include_in_final_grade will NOT update the remote Canvas instance."
        )
        self._include_in_final_grade = value

    @property
    def assignment_group(self):
        """Includes attributes of a assignment_group for convenience. For more details see Assignments API."""
        return self._assignment_group

    @assignment_group.setter
    def assignment_group(self, value):
        """Setter for assignment_group property."""
        self.logger.warn(
            "Setting values on assignment_group will NOT update the remote Canvas instance."
        )
        self._assignment_group = value

    @property
    def sections(self):
        """Includes attributes of a section for convenience. For more details see Sections API."""
        return self._sections

    @sections.setter
    def sections(self, value):
        """Setter for sections property."""
        self.logger.warn(
            "Setting values on sections will NOT update the remote Canvas instance."
        )
        self._sections = value

    @property
    def user_overrides(self):
        """Includes attributes of a user assignment overrides. For more details see Assignments API."""
        return self._user_overrides

    @user_overrides.setter
    def user_overrides(self, value):
        """Setter for user_overrides property."""
        self.logger.warn(
            "Setting values on user_overrides will NOT update the remote Canvas instance."
        )
        self._user_overrides = value


class Assignmentgroupattributes(BaseModel):
    """Assignmentgroupattributes Model.
    Some of the attributes of an Assignment Group. See Assignments API for more details"""

    def __init__(
        self,
        id=None,
        name=None,
        group_weight=None,
        sis_source_id=None,
        integration_data=None,
    ):
        """Init method for Assignmentgroupattributes class."""
        self._id = id
        self._name = name
        self._group_weight = group_weight
        self._sis_source_id = sis_source_id
        self._integration_data = integration_data

        self.logger = logging.getLogger("py3canvas.Assignmentgroupattributes")

    @property
    def id(self):
        """the id of the Assignment Group."""
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
        """the name of the Assignment Group."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def group_weight(self):
        """the weight of the Assignment Group."""
        return self._group_weight

    @group_weight.setter
    def group_weight(self, value):
        """Setter for group_weight property."""
        self.logger.warn(
            "Setting values on group_weight will NOT update the remote Canvas instance."
        )
        self._group_weight = value

    @property
    def sis_source_id(self):
        """the sis source id of the Assignment Group."""
        return self._sis_source_id

    @sis_source_id.setter
    def sis_source_id(self, value):
        """Setter for sis_source_id property."""
        self.logger.warn(
            "Setting values on sis_source_id will NOT update the remote Canvas instance."
        )
        self._sis_source_id = value

    @property
    def integration_data(self):
        """the integration data of the Assignment Group."""
        return self._integration_data

    @integration_data.setter
    def integration_data(self, value):
        """Setter for integration_data property."""
        self.logger.warn(
            "Setting values on integration_data will NOT update the remote Canvas instance."
        )
        self._integration_data = value


class Sectionattributes(BaseModel):
    """Sectionattributes Model.
    Some of the attributes of a section. For more details see Sections API."""

    def __init__(
        self,
        id=None,
        name=None,
        sis_id=None,
        integration_id=None,
        origin_course=None,
        xlist_course=None,
        override=None,
    ):
        """Init method for Sectionattributes class."""
        self._id = id
        self._name = name
        self._sis_id = sis_id
        self._integration_id = integration_id
        self._origin_course = origin_course
        self._xlist_course = xlist_course
        self._override = override

        self.logger = logging.getLogger("py3canvas.Sectionattributes")

    @property
    def id(self):
        """The unique identifier for the section."""
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
        """The name of the section."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def sis_id(self):
        """The sis id of the section."""
        return self._sis_id

    @sis_id.setter
    def sis_id(self, value):
        """Setter for sis_id property."""
        self.logger.warn(
            "Setting values on sis_id will NOT update the remote Canvas instance."
        )
        self._sis_id = value

    @property
    def integration_id(self):
        """Optional: The integration ID of the section."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn(
            "Setting values on integration_id will NOT update the remote Canvas instance."
        )
        self._integration_id = value

    @property
    def origin_course(self):
        """The course to which the section belongs or the course from which the section was cross-listed."""
        return self._origin_course

    @origin_course.setter
    def origin_course(self, value):
        """Setter for origin_course property."""
        self.logger.warn(
            "Setting values on origin_course will NOT update the remote Canvas instance."
        )
        self._origin_course = value

    @property
    def xlist_course(self):
        """Optional: Attributes of the xlist course. Only present when the section has been cross-listed. See Courses API for more details."""
        return self._xlist_course

    @xlist_course.setter
    def xlist_course(self, value):
        """Setter for xlist_course property."""
        self.logger.warn(
            "Setting values on xlist_course will NOT update the remote Canvas instance."
        )
        self._xlist_course = value

    @property
    def override(self):
        """Optional: Attributes of the assignment override that apply to the section. See Assignment API for more details."""
        return self._override

    @override.setter
    def override(self, value):
        """Setter for override property."""
        self.logger.warn(
            "Setting values on override will NOT update the remote Canvas instance."
        )
        self._override = value


class Courseattributes(BaseModel):
    """Courseattributes Model.
    Attributes of a course object.  See Courses API for more details"""

    def __init__(self, id=None, name=None, sis_id=None, integration_id=None):
        """Init method for Courseattributes class."""
        self._id = id
        self._name = name
        self._sis_id = sis_id
        self._integration_id = integration_id

        self.logger = logging.getLogger("py3canvas.Courseattributes")

    @property
    def id(self):
        """The unique Canvas identifier for the origin course."""
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
        """The name of the origin course."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn(
            "Setting values on name will NOT update the remote Canvas instance."
        )
        self._name = value

    @property
    def sis_id(self):
        """The sis id of the origin_course."""
        return self._sis_id

    @sis_id.setter
    def sis_id(self, value):
        """Setter for sis_id property."""
        self.logger.warn(
            "Setting values on sis_id will NOT update the remote Canvas instance."
        )
        self._sis_id = value

    @property
    def integration_id(self):
        """The integration ID of the origin_course."""
        return self._integration_id

    @integration_id.setter
    def integration_id(self, value):
        """Setter for integration_id property."""
        self.logger.warn(
            "Setting values on integration_id will NOT update the remote Canvas instance."
        )
        self._integration_id = value


class Sectionassignmentoverrideattributes(BaseModel):
    """Sectionassignmentoverrideattributes Model.
    Attributes of an assignment override that apply to the section object.  See Assignments API for more details"""

    def __init__(self, override_title=None, due_at=None, unlock_at=None, lock_at=None):
        """Init method for Sectionassignmentoverrideattributes class."""
        self._override_title = override_title
        self._due_at = due_at
        self._unlock_at = unlock_at
        self._lock_at = lock_at

        self.logger = logging.getLogger("py3canvas.Sectionassignmentoverrideattributes")

    @property
    def override_title(self):
        """The title for the assignment override."""
        return self._override_title

    @override_title.setter
    def override_title(self, value):
        """Setter for override_title property."""
        self.logger.warn(
            "Setting values on override_title will NOT update the remote Canvas instance."
        )
        self._override_title = value

    @property
    def due_at(self):
        """the due date for the assignment. returns null if not present. NOTE: If this assignment has assignment overrides, this field will be the due date as it applies to the user requesting information from the API."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn(
            "Setting values on due_at will NOT update the remote Canvas instance."
        )
        self._due_at = value

    @property
    def unlock_at(self):
        """(Optional) Time at which this was/will be unlocked."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn(
            "Setting values on unlock_at will NOT update the remote Canvas instance."
        )
        self._unlock_at = value

    @property
    def lock_at(self):
        """(Optional) Time at which this was/will be locked."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn(
            "Setting values on lock_at will NOT update the remote Canvas instance."
        )
        self._lock_at = value


class Userassignmentoverrideattributes(BaseModel):
    """Userassignmentoverrideattributes Model.
    Attributes of assignment overrides that apply to users.  See Assignments API for more details"""

    def __init__(
        self,
        id=None,
        title=None,
        due_at=None,
        unlock_at=None,
        lock_at=None,
        students=None,
    ):
        """Init method for Userassignmentoverrideattributes class."""
        self._id = id
        self._title = title
        self._due_at = due_at
        self._unlock_at = unlock_at
        self._lock_at = lock_at
        self._students = students

        self.logger = logging.getLogger("py3canvas.Userassignmentoverrideattributes")

    @property
    def id(self):
        """The unique Canvas identifier for the assignment override."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def title(self):
        """The title of the assignment override."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn(
            "Setting values on title will NOT update the remote Canvas instance."
        )
        self._title = value

    @property
    def due_at(self):
        """The time at which this assignment is due."""
        return self._due_at

    @due_at.setter
    def due_at(self, value):
        """Setter for due_at property."""
        self.logger.warn(
            "Setting values on due_at will NOT update the remote Canvas instance."
        )
        self._due_at = value

    @property
    def unlock_at(self):
        """(Optional) Time at which this was/will be unlocked."""
        return self._unlock_at

    @unlock_at.setter
    def unlock_at(self, value):
        """Setter for unlock_at property."""
        self.logger.warn(
            "Setting values on unlock_at will NOT update the remote Canvas instance."
        )
        self._unlock_at = value

    @property
    def lock_at(self):
        """(Optional) Time at which this was/will be locked."""
        return self._lock_at

    @lock_at.setter
    def lock_at(self, value):
        """Setter for lock_at property."""
        self.logger.warn(
            "Setting values on lock_at will NOT update the remote Canvas instance."
        )
        self._lock_at = value

    @property
    def students(self):
        """Includes attributes of a student for convenience. For more details see Users API."""
        return self._students

    @students.setter
    def students(self, value):
        """Setter for students property."""
        self.logger.warn(
            "Setting values on students will NOT update the remote Canvas instance."
        )
        self._students = value


class Studentattributes(BaseModel):
    """Studentattributes Model.
    Attributes of student.  See Users API for more details"""

    def __init__(self, user_id=None, sis_user_id=None):
        """Init method for Studentattributes class."""
        self._user_id = user_id
        self._sis_user_id = sis_user_id

        self.logger = logging.getLogger("py3canvas.Studentattributes")

    @property
    def user_id(self):
        """The unique Canvas identifier for the user."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value

    @property
    def sis_user_id(self):
        """The SIS ID associated with the user.  This field is only included if the user came from a SIS import and has permissions to view SIS information."""
        return self._sis_user_id

    @sis_user_id.setter
    def sis_user_id(self, value):
        """Setter for sis_user_id property."""
        self.logger.warn(
            "Setting values on sis_user_id will NOT update the remote Canvas instance."
        )
        self._sis_user_id = value
