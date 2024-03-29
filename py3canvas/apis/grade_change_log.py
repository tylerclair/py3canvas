"""GradeChangeLog API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class GradeChangeLogAPI(BaseCanvasAPI):
    """GradeChangeLog API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for GradeChangeLogAPI."""
        super(GradeChangeLogAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.GradeChangeLogAPI")

    def query_by_assignment(self, assignment_id, end_time=None, start_time=None):
        """
        Query by assignment.

        List grade change events for a given assignment.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id

        # OPTIONAL - start_time
        """
            The beginning of the time range from which you want events.
        """
        if start_time is not None:
            if issubclass(start_time.__class__, str):
                start_time = self._validate_iso8601_string(start_time)
            elif issubclass(start_time.__class__, date) or issubclass(
                start_time.__class__, datetime
            ):
                start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """
            The end of the time range from which you want events.
        """
        if end_time is not None:
            if issubclass(end_time.__class__, str):
                end_time = self._validate_iso8601_string(end_time)
            elif issubclass(end_time.__class__, date) or issubclass(
                end_time.__class__, datetime
            ):
                end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_time"] = end_time

        self.logger.debug(
            "GET /api/v1/audit/grade_change/assignments/{assignment_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/audit/grade_change/assignments/{assignment_id}".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def query_by_course(self, course_id, end_time=None, start_time=None):
        """
        Query by course.

        List grade change events for a given course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - start_time
        """
            The beginning of the time range from which you want events.
        """
        if start_time is not None:
            if issubclass(start_time.__class__, str):
                start_time = self._validate_iso8601_string(start_time)
            elif issubclass(start_time.__class__, date) or issubclass(
                start_time.__class__, datetime
            ):
                start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """
            The end of the time range from which you want events.
        """
        if end_time is not None:
            if issubclass(end_time.__class__, str):
                end_time = self._validate_iso8601_string(end_time)
            elif issubclass(end_time.__class__, date) or issubclass(
                end_time.__class__, datetime
            ):
                end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_time"] = end_time

        self.logger.debug(
            "GET /api/v1/audit/grade_change/courses/{course_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/audit/grade_change/courses/{course_id}".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def query_by_student(self, student_id, end_time=None, start_time=None):
        """
        Query by student.

        List grade change events for a given student.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - student_id
        """
            ID
        """
        path["student_id"] = student_id

        # OPTIONAL - start_time
        """
            The beginning of the time range from which you want events.
        """
        if start_time is not None:
            if issubclass(start_time.__class__, str):
                start_time = self._validate_iso8601_string(start_time)
            elif issubclass(start_time.__class__, date) or issubclass(
                start_time.__class__, datetime
            ):
                start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """
            The end of the time range from which you want events.
        """
        if end_time is not None:
            if issubclass(end_time.__class__, str):
                end_time = self._validate_iso8601_string(end_time)
            elif issubclass(end_time.__class__, date) or issubclass(
                end_time.__class__, datetime
            ):
                end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_time"] = end_time

        self.logger.debug(
            "GET /api/v1/audit/grade_change/students/{student_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/audit/grade_change/students/{student_id}".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def query_by_grader(self, grader_id, end_time=None, start_time=None):
        """
        Query by grader.

        List grade change events for a given grader.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - grader_id
        """
            ID
        """
        path["grader_id"] = grader_id

        # OPTIONAL - start_time
        """
            The beginning of the time range from which you want events.
        """
        if start_time is not None:
            if issubclass(start_time.__class__, str):
                start_time = self._validate_iso8601_string(start_time)
            elif issubclass(start_time.__class__, date) or issubclass(
                start_time.__class__, datetime
            ):
                start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """
            The end of the time range from which you want events.
        """
        if end_time is not None:
            if issubclass(end_time.__class__, str):
                end_time = self._validate_iso8601_string(end_time)
            elif issubclass(end_time.__class__, date) or issubclass(
                end_time.__class__, datetime
            ):
                end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_time"] = end_time

        self.logger.debug(
            "GET /api/v1/audit/grade_change/graders/{grader_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/audit/grade_change/graders/{grader_id}".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def advanced_query(
        self,
        assignment_id=None,
        course_id=None,
        end_time=None,
        grader_id=None,
        start_time=None,
        student_id=None,
    ):
        """
        Advanced query.

        List grade change events satisfying all given parameters. Teachers may query for events in courses they teach.
        Queries without +course_id+ require account administrator rights.

        At least one of +course_id+, +assignment_id+, +student_id+, or +grader_id+ must be specified.
        """
        path = {}
        data = {}
        params = {}

        # OPTIONAL - course_id
        """
            Restrict query to events in the specified course.
        """
        if course_id is not None:
            params["course_id"] = course_id

        # OPTIONAL - assignment_id
        """
            Restrict query to the given assignment. If "override" is given, query the course final grade override instead.
        """
        if assignment_id is not None:
            params["assignment_id"] = assignment_id

        # OPTIONAL - student_id
        """
            User id of a student to search grading events for.
        """
        if student_id is not None:
            params["student_id"] = student_id

        # OPTIONAL - grader_id
        """
            User id of a grader to search grading events for.
        """
        if grader_id is not None:
            params["grader_id"] = grader_id

        # OPTIONAL - start_time
        """
            The beginning of the time range from which you want events.
        """
        if start_time is not None:
            if issubclass(start_time.__class__, str):
                start_time = self._validate_iso8601_string(start_time)
            elif issubclass(start_time.__class__, date) or issubclass(
                start_time.__class__, datetime
            ):
                start_time = start_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["start_time"] = start_time

        # OPTIONAL - end_time
        """
            The end of the time range from which you want events.
        """
        if end_time is not None:
            if issubclass(end_time.__class__, str):
                end_time = self._validate_iso8601_string(end_time)
            elif issubclass(end_time.__class__, date) or issubclass(
                end_time.__class__, datetime
            ):
                end_time = end_time.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["end_time"] = end_time

        self.logger.debug(
            "GET /api/v1/audit/grade_change with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/audit/grade_change".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )


class Gradechangeeventlinks(BaseModel):
    """Gradechangeeventlinks Model."""

    def __init__(
        self, assignment=None, course=None, student=None, grader=None, page_view=None
    ):
        """Init method for Gradechangeeventlinks class."""
        self._assignment = assignment
        self._course = course
        self._student = student
        self._grader = grader
        self._page_view = page_view

        self.logger = logging.getLogger("py3canvas.Gradechangeeventlinks")

    @property
    def assignment(self):
        """ID of the assignment associated with the event."""
        return self._assignment

    @assignment.setter
    def assignment(self, value):
        """Setter for assignment property."""
        self.logger.warn(
            "Setting values on assignment will NOT update the remote Canvas instance."
        )
        self._assignment = value

    @property
    def course(self):
        """ID of the course associated with the event. will match the context_id in the associated assignment if the context type for the assignment is a course."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter for course property."""
        self.logger.warn(
            "Setting values on course will NOT update the remote Canvas instance."
        )
        self._course = value

    @property
    def student(self):
        """ID of the student associated with the event. will match the user_id in the associated submission."""
        return self._student

    @student.setter
    def student(self, value):
        """Setter for student property."""
        self.logger.warn(
            "Setting values on student will NOT update the remote Canvas instance."
        )
        self._student = value

    @property
    def grader(self):
        """ID of the grader associated with the event. will match the grader_id in the associated submission."""
        return self._grader

    @grader.setter
    def grader(self, value):
        """Setter for grader property."""
        self.logger.warn(
            "Setting values on grader will NOT update the remote Canvas instance."
        )
        self._grader = value

    @property
    def page_view(self):
        """ID of the page view during the event if it exists."""
        return self._page_view

    @page_view.setter
    def page_view(self, value):
        """Setter for page_view property."""
        self.logger.warn(
            "Setting values on page_view will NOT update the remote Canvas instance."
        )
        self._page_view = value


class Gradechangeevent(BaseModel):
    """Gradechangeevent Model."""

    def __init__(
        self,
        id=None,
        created_at=None,
        event_type=None,
        excused_after=None,
        excused_before=None,
        grade_after=None,
        grade_before=None,
        graded_anonymously=None,
        version_number=None,
        request_id=None,
        links=None,
    ):
        """Init method for Gradechangeevent class."""
        self._id = id
        self._created_at = created_at
        self._event_type = event_type
        self._excused_after = excused_after
        self._excused_before = excused_before
        self._grade_after = grade_after
        self._grade_before = grade_before
        self._graded_anonymously = graded_anonymously
        self._version_number = version_number
        self._request_id = request_id
        self._links = links

        self.logger = logging.getLogger("py3canvas.Gradechangeevent")

    @property
    def id(self):
        """ID of the event."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def created_at(self):
        """timestamp of the event."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def event_type(self):
        """GradeChange event type."""
        return self._event_type

    @event_type.setter
    def event_type(self, value):
        """Setter for event_type property."""
        self.logger.warn(
            "Setting values on event_type will NOT update the remote Canvas instance."
        )
        self._event_type = value

    @property
    def excused_after(self):
        """Boolean indicating whether the submission was excused after the change."""
        return self._excused_after

    @excused_after.setter
    def excused_after(self, value):
        """Setter for excused_after property."""
        self.logger.warn(
            "Setting values on excused_after will NOT update the remote Canvas instance."
        )
        self._excused_after = value

    @property
    def excused_before(self):
        """Boolean indicating whether the submission was excused before the change."""
        return self._excused_before

    @excused_before.setter
    def excused_before(self, value):
        """Setter for excused_before property."""
        self.logger.warn(
            "Setting values on excused_before will NOT update the remote Canvas instance."
        )
        self._excused_before = value

    @property
    def grade_after(self):
        """The grade after the change."""
        return self._grade_after

    @grade_after.setter
    def grade_after(self, value):
        """Setter for grade_after property."""
        self.logger.warn(
            "Setting values on grade_after will NOT update the remote Canvas instance."
        )
        self._grade_after = value

    @property
    def grade_before(self):
        """The grade before the change."""
        return self._grade_before

    @grade_before.setter
    def grade_before(self, value):
        """Setter for grade_before property."""
        self.logger.warn(
            "Setting values on grade_before will NOT update the remote Canvas instance."
        )
        self._grade_before = value

    @property
    def graded_anonymously(self):
        """Boolean indicating whether the student name was visible when the grade was given. Could be null if the grade change record was created before this feature existed."""
        return self._graded_anonymously

    @graded_anonymously.setter
    def graded_anonymously(self, value):
        """Setter for graded_anonymously property."""
        self.logger.warn(
            "Setting values on graded_anonymously will NOT update the remote Canvas instance."
        )
        self._graded_anonymously = value

    @property
    def version_number(self):
        """Version Number of the grade change submission."""
        return self._version_number

    @version_number.setter
    def version_number(self, value):
        """Setter for version_number property."""
        self.logger.warn(
            "Setting values on version_number will NOT update the remote Canvas instance."
        )
        self._version_number = value

    @property
    def request_id(self):
        """The unique request id of the request during the grade change."""
        return self._request_id

    @request_id.setter
    def request_id(self, value):
        """Setter for request_id property."""
        self.logger.warn(
            "Setting values on request_id will NOT update the remote Canvas instance."
        )
        self._request_id = value

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
