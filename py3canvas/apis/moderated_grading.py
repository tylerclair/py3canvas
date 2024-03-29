"""ModeratedGrading API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ModeratedGradingAPI(BaseCanvasAPI):
    """ModeratedGrading API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ModeratedGradingAPI."""
        super(ModeratedGradingAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ModeratedGradingAPI")

    def list_students_selected_for_moderation(self, assignment_id, course_id):
        """
        List students selected for moderation.

        Returns a paginated list of students selected for moderation
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

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students".format(
                **path
            ),
            data=data,
            params=params,
            all_pages=True,
        )

    def select_students_for_moderation(
        self, assignment_id, course_id, student_ids=None
    ):
        """
        Select students for moderation.

        Returns an array of users that were selected for moderation
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

        # OPTIONAL - student_ids
        """
            user ids for students to select for moderation
        """
        if student_ids is not None:
            data["student_ids"] = student_ids

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/moderated_students".format(
                **path
            ),
            data=data,
            params=params,
            all_pages=True,
        )

    def bulk_select_provisional_grades(self, assignment_id, course_id):
        """
        Bulk select provisional grades.

        Choose which provisional grades will be received by associated students for an assignment.
        The caller must be the final grader for the assignment or an admin with :select_final_grade rights.
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

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/bulk_select with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/bulk_select".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def show_provisional_grade_status_for_student(
        self, assignment_id, course_id, student_id=None
    ):
        """
        Show provisional grade status for a student.

        Tell whether the student's submission needs one or more provisional grades.
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

        # OPTIONAL - student_id
        """
            The id of the student to show the status for
        """
        if student_id is not None:
            params["student_id"] = student_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/status".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def select_provisional_grade(self, assignment_id, course_id, provisional_grade_id):
        """
        Select provisional grade.

        Choose which provisional grade the student should receive for a submission.
        The caller must be the final grader for the assignment or an admin with :select_final_grade rights.
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

        # REQUIRED - PATH - provisional_grade_id
        """
            ID
        """
        path["provisional_grade_id"] = provisional_grade_id

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/{provisional_grade_id}/select".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def publish_provisional_grades_for_assignment(self, assignment_id, course_id):
        """
        Publish provisional grades for an assignment.

        Publish the selected provisional grade for all submissions to an assignment.
        Use the "Select provisional grade" endpoint to choose which provisional grade to publish
        for a particular submission.

        Students not in the moderation set will have their one and only provisional grade published.

        WARNING: This is irreversible. This will overwrite existing grades in the gradebook.
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

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/provisional_grades/publish".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def show_provisional_grade_status_for_student(
        self, assignment_id, course_id, anonymous_id=None
    ):
        """
        Show provisional grade status for a student.

        Determine whether or not the student's submission needs one or more provisional grades.
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

        # OPTIONAL - anonymous_id
        """
            The id of the student to show the status for
        """
        if anonymous_id is not None:
            params["anonymous_id"] = anonymous_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/assignments/{assignment_id}/anonymous_provisional_grades/status with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/assignments/{assignment_id}/anonymous_provisional_grades/status".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )


class Provisionalgrade(BaseModel):
    """Provisionalgrade Model."""

    def __init__(
        self,
        provisional_grade_id=None,
        score=None,
        grade=None,
        grade_matches_current_submission=None,
        graded_at=None,
        final=None,
        speedgrader_url=None,
    ):
        """Init method for Provisionalgrade class."""
        self._provisional_grade_id = provisional_grade_id
        self._score = score
        self._grade = grade
        self._grade_matches_current_submission = grade_matches_current_submission
        self._graded_at = graded_at
        self._final = final
        self._speedgrader_url = speedgrader_url

        self.logger = logging.getLogger("py3canvas.Provisionalgrade")

    @property
    def provisional_grade_id(self):
        """The identifier for the provisional grade."""
        return self._provisional_grade_id

    @provisional_grade_id.setter
    def provisional_grade_id(self, value):
        """Setter for provisional_grade_id property."""
        self.logger.warn(
            "Setting values on provisional_grade_id will NOT update the remote Canvas instance."
        )
        self._provisional_grade_id = value

    @property
    def score(self):
        """The numeric score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn(
            "Setting values on score will NOT update the remote Canvas instance."
        )
        self._score = value

    @property
    def grade(self):
        """The grade."""
        return self._grade

    @grade.setter
    def grade(self, value):
        """Setter for grade property."""
        self.logger.warn(
            "Setting values on grade will NOT update the remote Canvas instance."
        )
        self._grade = value

    @property
    def grade_matches_current_submission(self):
        """Whether the grade was applied to the most current submission (false if the student resubmitted after grading)."""
        return self._grade_matches_current_submission

    @grade_matches_current_submission.setter
    def grade_matches_current_submission(self, value):
        """Setter for grade_matches_current_submission property."""
        self.logger.warn(
            "Setting values on grade_matches_current_submission will NOT update the remote Canvas instance."
        )
        self._grade_matches_current_submission = value

    @property
    def graded_at(self):
        """When the grade was given."""
        return self._graded_at

    @graded_at.setter
    def graded_at(self, value):
        """Setter for graded_at property."""
        self.logger.warn(
            "Setting values on graded_at will NOT update the remote Canvas instance."
        )
        self._graded_at = value

    @property
    def final(self):
        """Whether this is the 'final' provisional grade created by the moderator."""
        return self._final

    @final.setter
    def final(self, value):
        """Setter for final property."""
        self.logger.warn(
            "Setting values on final will NOT update the remote Canvas instance."
        )
        self._final = value

    @property
    def speedgrader_url(self):
        """A link to view this provisional grade in SpeedGrader™."""
        return self._speedgrader_url

    @speedgrader_url.setter
    def speedgrader_url(self, value):
        """Setter for speedgrader_url property."""
        self.logger.warn(
            "Setting values on speedgrader_url will NOT update the remote Canvas instance."
        )
        self._speedgrader_url = value
