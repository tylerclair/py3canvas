"""Submissions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class SubmissionsAPI(BaseCanvasAPI):
    """Submissions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SubmissionsAPI."""
        super(SubmissionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SubmissionsAPI")

    def submit_assignment_courses(self, assignment_id, course_id, submission_submission_type, comment_text_comment=None, submission_annotatable_attachment_id=None, submission_body=None, submission_file_ids=None, submission_media_comment_id=None, submission_media_comment_type=None, submission_submitted_at=None, submission_url=None, submission_user_id=None):
        """
        Submit an assignment.

        Make a submission for an assignment. You must be enrolled as a student in
        the course/section to do this.
        
        All online turn-in submission types are supported in this API. However,
        there are a few things that are not yet supported:
        
        * Files can be submitted based on a file ID of a user or group file or through the {api:SubmissionsApiController#create_file file upload API}. However, there is no API yet for listing the user and group files.
        * Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
        * Integration with Google Docs is not yet supported.
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


        # OPTIONAL - comment[text_comment]
        """
            Include a textual comment with the submission.
        """
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment


        # REQUIRED - submission[submission_type]
        """
            The type of submission being made. The assignment submission_types must
        include this submission type as an allowed option, or the submission will be rejected with a 400 error.

        The submission_type given determines which of the following parameters is
        used. For instance, to submit a URL, submission [submission_type] must be
        set to "online_url", otherwise the submission [url] parameter will be
        ignored.
        """
        self._validate_enum(submission_submission_type, ["online_text_entry", "online_url", "online_upload", "media_recording", "basic_lti_launch", "student_annotation"])
        data["submission[submission_type]"] = submission_submission_type


        # OPTIONAL - submission[body]
        """
            Submit the assignment as an HTML document snippet. Note this HTML snippet
        will be sanitized using the same ruleset as a submission made from the
        Canvas web UI. The sanitized HTML will be returned in the response as the
        submission body. Requires a submission_type of "online_text_entry".
        """
        if submission_body is not None:
            data["submission[body]"] = submission_body


        # OPTIONAL - submission[url]
        """
            Submit the assignment as a URL. The URL scheme must be "http" or "https",
        no "ftp" or other URL schemes are allowed. If no scheme is given (e.g.
        "www.example.com") then "http" will be assumed. Requires a submission_type
        of "online_url" or "basic_lti_launch".
        """
        if submission_url is not None:
            data["submission[url]"] = submission_url


        # OPTIONAL - submission[file_ids]
        """
            Submit the assignment as a set of one or more previously uploaded files
        residing in the submitting user's files section (or the group's files
        section, for group assignments).

        To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.

        Requires a submission_type of "online_upload".
        """
        if submission_file_ids is not None:
            data["submission[file_ids]"] = submission_file_ids


        # OPTIONAL - submission[media_comment_id]
        """
            The media comment id to submit. Media comment ids can be submitted via
        this API, however, note that there is not yet an API to generate or list
        existing media comments, so this functionality is currently of limited use.

        Requires a submission_type of "media_recording".
        """
        if submission_media_comment_id is not None:
            data["submission[media_comment_id]"] = submission_media_comment_id


        # OPTIONAL - submission[media_comment_type]
        """
            The type of media comment being submitted.
        """
        if submission_media_comment_type is not None:
            self._validate_enum(submission_media_comment_type, ["audio", "video"])
            data["submission[media_comment_type]"] = submission_media_comment_type


        # OPTIONAL - submission[user_id]
        """
            Submit on behalf of the given user. Requires grading permission.
        """
        if submission_user_id is not None:
            data["submission[user_id]"] = submission_user_id


        # OPTIONAL - submission[annotatable_attachment_id]
        """
            The Attachment ID of the document being annotated. This should match
        the annotatable_attachment_id on the assignment.

        Requires a submission_type of "student_annotation".
        """
        if submission_annotatable_attachment_id is not None:
            data["submission[annotatable_attachment_id]"] = submission_annotatable_attachment_id


        # OPTIONAL - submission[submitted_at]
        """
            Choose the time the submission is listed as submitted at.  Requires grading permission.
        """
        if submission_submitted_at is not None:
            if issubclass(submission_submitted_at.__class__, str):
                submission_submitted_at = self._validate_iso8601_string(submission_submitted_at)
            elif issubclass(submission_submitted_at.__class__, date) or issubclass(submission_submitted_at.__class__, datetime):
                submission_submitted_at = submission_submitted_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["submission[submitted_at]"] = submission_submitted_at


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, no_data=True)

    def submit_assignment_sections(self, assignment_id, section_id, submission_submission_type, comment_text_comment=None, submission_annotatable_attachment_id=None, submission_body=None, submission_file_ids=None, submission_media_comment_id=None, submission_media_comment_type=None, submission_submitted_at=None, submission_url=None, submission_user_id=None):
        """
        Submit an assignment.

        Make a submission for an assignment. You must be enrolled as a student in
        the course/section to do this.
        
        All online turn-in submission types are supported in this API. However,
        there are a few things that are not yet supported:
        
        * Files can be submitted based on a file ID of a user or group file or through the {api:SubmissionsApiController#create_file file upload API}. However, there is no API yet for listing the user and group files.
        * Media comments can be submitted, however, there is no API yet for creating a media comment to submit.
        * Integration with Google Docs is not yet supported.
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


        # OPTIONAL - comment[text_comment]
        """
            Include a textual comment with the submission.
        """
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment


        # REQUIRED - submission[submission_type]
        """
            The type of submission being made. The assignment submission_types must
        include this submission type as an allowed option, or the submission will be rejected with a 400 error.

        The submission_type given determines which of the following parameters is
        used. For instance, to submit a URL, submission [submission_type] must be
        set to "online_url", otherwise the submission [url] parameter will be
        ignored.
        """
        self._validate_enum(submission_submission_type, ["online_text_entry", "online_url", "online_upload", "media_recording", "basic_lti_launch", "student_annotation"])
        data["submission[submission_type]"] = submission_submission_type


        # OPTIONAL - submission[body]
        """
            Submit the assignment as an HTML document snippet. Note this HTML snippet
        will be sanitized using the same ruleset as a submission made from the
        Canvas web UI. The sanitized HTML will be returned in the response as the
        submission body. Requires a submission_type of "online_text_entry".
        """
        if submission_body is not None:
            data["submission[body]"] = submission_body


        # OPTIONAL - submission[url]
        """
            Submit the assignment as a URL. The URL scheme must be "http" or "https",
        no "ftp" or other URL schemes are allowed. If no scheme is given (e.g.
        "www.example.com") then "http" will be assumed. Requires a submission_type
        of "online_url" or "basic_lti_launch".
        """
        if submission_url is not None:
            data["submission[url]"] = submission_url


        # OPTIONAL - submission[file_ids]
        """
            Submit the assignment as a set of one or more previously uploaded files
        residing in the submitting user's files section (or the group's files
        section, for group assignments).

        To upload a new file to submit, see the submissions {api:SubmissionsApiController#create_file Upload a file API}.

        Requires a submission_type of "online_upload".
        """
        if submission_file_ids is not None:
            data["submission[file_ids]"] = submission_file_ids


        # OPTIONAL - submission[media_comment_id]
        """
            The media comment id to submit. Media comment ids can be submitted via
        this API, however, note that there is not yet an API to generate or list
        existing media comments, so this functionality is currently of limited use.

        Requires a submission_type of "media_recording".
        """
        if submission_media_comment_id is not None:
            data["submission[media_comment_id]"] = submission_media_comment_id


        # OPTIONAL - submission[media_comment_type]
        """
            The type of media comment being submitted.
        """
        if submission_media_comment_type is not None:
            self._validate_enum(submission_media_comment_type, ["audio", "video"])
            data["submission[media_comment_type]"] = submission_media_comment_type


        # OPTIONAL - submission[user_id]
        """
            Submit on behalf of the given user. Requires grading permission.
        """
        if submission_user_id is not None:
            data["submission[user_id]"] = submission_user_id


        # OPTIONAL - submission[annotatable_attachment_id]
        """
            The Attachment ID of the document being annotated. This should match
        the annotatable_attachment_id on the assignment.

        Requires a submission_type of "student_annotation".
        """
        if submission_annotatable_attachment_id is not None:
            data["submission[annotatable_attachment_id]"] = submission_annotatable_attachment_id


        # OPTIONAL - submission[submitted_at]
        """
            Choose the time the submission is listed as submitted at.  Requires grading permission.
        """
        if submission_submitted_at is not None:
            if issubclass(submission_submitted_at.__class__, str):
                submission_submitted_at = self._validate_iso8601_string(submission_submitted_at)
            elif issubclass(submission_submitted_at.__class__, date) or issubclass(submission_submitted_at.__class__, datetime):
                submission_submitted_at = submission_submitted_at.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            data["submission[submitted_at]"] = submission_submitted_at


        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, no_data=True)

    def list_assignment_submissions_courses(self, assignment_id, course_id, grouped=None, include=None):
        """
        List assignment submissions.

        A paginated list of all existing submissions for an assignment.
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
            Associations to include with the group.  "group" will add group_id and group_name.
        """
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "visibility", "course", "user", "group", "read_status"])
            params["include"] = include


        # OPTIONAL - grouped
        """
            If this argument is true, the response will be grouped by student groups.
        """
        if grouped is not None:
            params["grouped"] = grouped


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, all_pages=True)

    def list_assignment_submissions_sections(self, assignment_id, section_id, grouped=None, include=None):
        """
        List assignment submissions.

        A paginated list of all existing submissions for an assignment.
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
            Associations to include with the group.  "group" will add group_id and group_name.
        """
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "visibility", "course", "user", "group", "read_status"])
            params["include"] = include


        # OPTIONAL - grouped
        """
            If this argument is true, the response will be grouped by student groups.
        """
        if grouped is not None:
            params["grouped"] = grouped


        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions".format(**path), data=data, params=params, all_pages=True)

    def list_submissions_for_multiple_assignments_courses(self, course_id, assignment_ids=None, enrollment_state=None, graded_since=None, grading_period_id=None, grouped=None, include=None, order=None, order_direction=None, post_to_sis=None, state_based_on_date=None, student_ids=None, submitted_since=None, workflow_state=None):
        """
        List submissions for multiple assignments.

        A paginated list of all existing submissions for a given set of students and assignments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - student_ids
        """
            List of student ids to return submissions for. If this argument is
        omitted, return submissions for the calling user. Students may only list
        their own submissions. Observers may only list those of associated
        students. The special id "all" will return submissions for all students
        in the course/section as appropriate.
        """
        if student_ids is not None:
            params["student_ids"] = student_ids


        # OPTIONAL - assignment_ids
        """
            List of assignments to return submissions for. If none are given,
        submissions for all assignments are returned.
        """
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids


        # OPTIONAL - grouped
        """
            If this argument is present, the response will be grouped by student,
        rather than a flat array of submissions.
        """
        if grouped is not None:
            params["grouped"] = grouped


        # OPTIONAL - post_to_sis
        """
            If this argument is set to true, the response will only include
        submissions for assignments that have the post_to_sis flag set to true and
        user enrollments that were added through sis.
        """
        if post_to_sis is not None:
            params["post_to_sis"] = post_to_sis


        # OPTIONAL - submitted_since
        """
            If this argument is set, the response will only include submissions that
        were submitted after the specified date_time. This will exclude
        submissions that do not have a submitted_at which will exclude unsubmitted
        submissions.
        The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if submitted_since is not None:
            if issubclass(submitted_since.__class__, str):
                submitted_since = self._validate_iso8601_string(submitted_since)
            elif issubclass(submitted_since.__class__, date) or issubclass(submitted_since.__class__, datetime):
                submitted_since = submitted_since.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["submitted_since"] = submitted_since


        # OPTIONAL - graded_since
        """
            If this argument is set, the response will only include submissions that
        were graded after the specified date_time. This will exclude
        submissions that have not been graded.
        The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if graded_since is not None:
            if issubclass(graded_since.__class__, str):
                graded_since = self._validate_iso8601_string(graded_since)
            elif issubclass(graded_since.__class__, date) or issubclass(graded_since.__class__, datetime):
                graded_since = graded_since.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["graded_since"] = graded_since


        # OPTIONAL - grading_period_id
        """
            The id of the grading period in which submissions are being requested
        (Requires grading periods to exist on the account)
        """
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id


        # OPTIONAL - workflow_state
        """
            The current status of the submission
        """
        if workflow_state is not None:
            self._validate_enum(workflow_state, ["submitted", "unsubmitted", "graded", "pending_review"])
            params["workflow_state"] = workflow_state


        # OPTIONAL - enrollment_state
        """
            The current state of the enrollments. If omitted will include all
        enrollments that are not deleted.
        """
        if enrollment_state is not None:
            self._validate_enum(enrollment_state, ["active", "concluded"])
            params["enrollment_state"] = enrollment_state


        # OPTIONAL - state_based_on_date
        """
            If omitted it is set to true. When set to false it will ignore the effective
        state of the student enrollments and use the workflow_state for the
        enrollments. The argument is ignored unless enrollment_state argument is
        also passed.
        """
        if state_based_on_date is not None:
            params["state_based_on_date"] = state_based_on_date


        # OPTIONAL - order
        """
            The order submissions will be returned in.  Defaults to "id".  Doesn't
        affect results for "grouped" mode.
        """
        if order is not None:
            self._validate_enum(order, ["id", "graded_at"])
            params["order"] = order


        # OPTIONAL - order_direction
        """
            Determines whether ordered results are returned in ascending or descending
        order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode.
        """
        if order_direction is not None:
            self._validate_enum(order_direction, ["ascending", "descending"])
            params["order_direction"] = order_direction


        # OPTIONAL - include
        """
            Associations to include with the group. `total_scores` requires the
        `grouped` argument.
        """
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "total_scores", "visibility", "course", "user"])
            params["include"] = include


        self.logger.debug("GET /api/v1/courses/{course_id}/students/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/students/submissions".format(**path), data=data, params=params, no_data=True)

    def list_submissions_for_multiple_assignments_sections(self, section_id, assignment_ids=None, enrollment_state=None, graded_since=None, grading_period_id=None, grouped=None, include=None, order=None, order_direction=None, post_to_sis=None, state_based_on_date=None, student_ids=None, submitted_since=None, workflow_state=None):
        """
        List submissions for multiple assignments.

        A paginated list of all existing submissions for a given set of students and assignments.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """
            ID
        """
        path["section_id"] = section_id


        # OPTIONAL - student_ids
        """
            List of student ids to return submissions for. If this argument is
        omitted, return submissions for the calling user. Students may only list
        their own submissions. Observers may only list those of associated
        students. The special id "all" will return submissions for all students
        in the course/section as appropriate.
        """
        if student_ids is not None:
            params["student_ids"] = student_ids


        # OPTIONAL - assignment_ids
        """
            List of assignments to return submissions for. If none are given,
        submissions for all assignments are returned.
        """
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids


        # OPTIONAL - grouped
        """
            If this argument is present, the response will be grouped by student,
        rather than a flat array of submissions.
        """
        if grouped is not None:
            params["grouped"] = grouped


        # OPTIONAL - post_to_sis
        """
            If this argument is set to true, the response will only include
        submissions for assignments that have the post_to_sis flag set to true and
        user enrollments that were added through sis.
        """
        if post_to_sis is not None:
            params["post_to_sis"] = post_to_sis


        # OPTIONAL - submitted_since
        """
            If this argument is set, the response will only include submissions that
        were submitted after the specified date_time. This will exclude
        submissions that do not have a submitted_at which will exclude unsubmitted
        submissions.
        The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if submitted_since is not None:
            if issubclass(submitted_since.__class__, str):
                submitted_since = self._validate_iso8601_string(submitted_since)
            elif issubclass(submitted_since.__class__, date) or issubclass(submitted_since.__class__, datetime):
                submitted_since = submitted_since.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["submitted_since"] = submitted_since


        # OPTIONAL - graded_since
        """
            If this argument is set, the response will only include submissions that
        were graded after the specified date_time. This will exclude
        submissions that have not been graded.
        The value must be formatted as ISO 8601 YYYY-MM-DDTHH:MM:SSZ.
        """
        if graded_since is not None:
            if issubclass(graded_since.__class__, str):
                graded_since = self._validate_iso8601_string(graded_since)
            elif issubclass(graded_since.__class__, date) or issubclass(graded_since.__class__, datetime):
                graded_since = graded_since.strftime('%Y-%m-%dT%H:%M:%S+00:00')
            params["graded_since"] = graded_since


        # OPTIONAL - grading_period_id
        """
            The id of the grading period in which submissions are being requested
        (Requires grading periods to exist on the account)
        """
        if grading_period_id is not None:
            params["grading_period_id"] = grading_period_id


        # OPTIONAL - workflow_state
        """
            The current status of the submission
        """
        if workflow_state is not None:
            self._validate_enum(workflow_state, ["submitted", "unsubmitted", "graded", "pending_review"])
            params["workflow_state"] = workflow_state


        # OPTIONAL - enrollment_state
        """
            The current state of the enrollments. If omitted will include all
        enrollments that are not deleted.
        """
        if enrollment_state is not None:
            self._validate_enum(enrollment_state, ["active", "concluded"])
            params["enrollment_state"] = enrollment_state


        # OPTIONAL - state_based_on_date
        """
            If omitted it is set to true. When set to false it will ignore the effective
        state of the student enrollments and use the workflow_state for the
        enrollments. The argument is ignored unless enrollment_state argument is
        also passed.
        """
        if state_based_on_date is not None:
            params["state_based_on_date"] = state_based_on_date


        # OPTIONAL - order
        """
            The order submissions will be returned in.  Defaults to "id".  Doesn't
        affect results for "grouped" mode.
        """
        if order is not None:
            self._validate_enum(order, ["id", "graded_at"])
            params["order"] = order


        # OPTIONAL - order_direction
        """
            Determines whether ordered results are returned in ascending or descending
        order.  Defaults to "ascending".  Doesn't affect results for "grouped" mode.
        """
        if order_direction is not None:
            self._validate_enum(order_direction, ["ascending", "descending"])
            params["order_direction"] = order_direction


        # OPTIONAL - include
        """
            Associations to include with the group. `total_scores` requires the
        `grouped` argument.
        """
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "assignment", "total_scores", "visibility", "course", "user"])
            params["include"] = include


        self.logger.debug("GET /api/v1/sections/{section_id}/students/submissions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/students/submissions".format(**path), data=data, params=params, no_data=True)

    def get_single_submission_courses(self, assignment_id, course_id, user_id, include=None):
        """
        Get a single submission.

        Get a single submission, based on user id.
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


        # OPTIONAL - include
        """
            Associations to include with the group.
        """
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "full_rubric_assessment", "visibility", "course", "user", "read_status"])
            params["include"] = include


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def get_single_submission_sections(self, assignment_id, section_id, user_id, include=None):
        """
        Get a single submission.

        Get a single submission, based on user id.
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # OPTIONAL - include
        """
            Associations to include with the group.
        """
        if include is not None:
            self._validate_enum(include, ["submission_history", "submission_comments", "rubric_assessment", "full_rubric_assessment", "visibility", "course", "user", "read_status"])
            params["include"] = include


        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def upload_file_courses(self, assignment_id, course_id, user_id):
        """
        Upload a file.

        Upload a file to a submission.
        
        This API endpoint is the first step in uploading a file to a submission as a student.
        See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        
        The final step of the file upload workflow will return the attachment data,
        including the new file id. The caller can then POST to submit the
        +online_upload+ assignment with these file ids.
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


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/files".format(**path), data=data, params=params, no_data=True)

    def upload_file_sections(self, assignment_id, section_id, user_id):
        """
        Upload a file.

        Upload a file to a submission.
        
        This API endpoint is the first step in uploading a file to a submission as a student.
        See the {file:file_uploads.html File Upload Documentation} for details on the file upload workflow.
        
        The final step of the file upload workflow will return the attachment data,
        including the new file id. The caller can then POST to submit the
        +online_upload+ assignment with these file ids.
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/files".format(**path), data=data, params=params, no_data=True)

    def grade_or_comment_on_submission_courses(self, assignment_id, course_id, user_id, comment_file_ids=None, comment_group_comment=None, comment_media_comment_id=None, comment_media_comment_type=None, comment_text_comment=None, include_visibility=None, rubric_assessment=None, submission_excuse=None, submission_late_policy_status=None, submission_posted_grade=None, submission_seconds_late_override=None):
        """
        Grade or comment on a submission.

        Comment on and/or update the grading for a student's assignment submission.
        If any submission or rubric_assessment arguments are provided, the user
        must have permission to manage grades in the appropriate context (course or
        section).
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


        # OPTIONAL - comment[text_comment]
        """
            Add a textual comment to the submission.
        """
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment


        # OPTIONAL - comment[group_comment]
        """
            Whether or not this comment should be sent to the entire group (defaults
        to false). Ignored if this is not a group assignment or if no text_comment
        is provided.
        """
        if comment_group_comment is not None:
            data["comment[group_comment]"] = comment_group_comment


        # OPTIONAL - comment[media_comment_id]
        """
            Add an audio/video comment to the submission. Media comments can be added
        via this API, however, note that there is not yet an API to generate or
        list existing media comments, so this functionality is currently of
        limited use.
        """
        if comment_media_comment_id is not None:
            data["comment[media_comment_id]"] = comment_media_comment_id


        # OPTIONAL - comment[media_comment_type]
        """
            The type of media comment being added.
        """
        if comment_media_comment_type is not None:
            self._validate_enum(comment_media_comment_type, ["audio", "video"])
            data["comment[media_comment_type]"] = comment_media_comment_type


        # OPTIONAL - comment[file_ids]
        """
            Attach files to this comment that were previously uploaded using the
        Submission Comment API's files action
        """
        if comment_file_ids is not None:
            data["comment[file_ids]"] = comment_file_ids


        # OPTIONAL - include[visibility]
        """
            Whether this assignment is visible to the owner of the submission
        """
        if include_visibility is not None:
            data["include[visibility]"] = include_visibility


        # OPTIONAL - submission[posted_grade]
        """
            Assign a score to the submission, updating both the "score" and "grade"
        fields on the submission record. This parameter can be passed in a few
        different formats:

        points:: A floating point or integral value, such as "13.5". The grade
          will be interpreted directly as the score of the assignment.
          Values above assignment.points_possible are allowed, for awarding
          extra credit.
        percentage:: A floating point value appended with a percent sign, such as
           "40%". The grade will be interpreted as a percentage score on the
           assignment, where 100% == assignment.points_possible. Values above 100%
           are allowed, for awarding extra credit.
        letter grade:: A letter grade, following the assignment's defined letter
           grading scheme. For example, "A-". The resulting score will be the high
           end of the defined range for the letter grade. For instance, if "B" is
           defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
           letter grade will be rejected if the assignment does not have a defined
           letter grading scheme. For more fine-grained control of scores, pass in
           points or percentage rather than the letter grade.
        "pass/complete/fail/incomplete":: A string value of "pass" or "complete"
           will give a score of 100%. "fail" or "incomplete" will give a score of
           0.

        Note that assignments with grading_type of "pass_fail" can only be
        assigned a score of 0 or assignment.points_possible, nothing inbetween. If
        a posted_grade in the "points" or "percentage" format is sent, the grade
        will only be accepted if the grade equals one of those two values.
        """
        if submission_posted_grade is not None:
            data["submission[posted_grade]"] = submission_posted_grade


        # OPTIONAL - submission[excuse]
        """
            Sets the "excused" status of an assignment.
        """
        if submission_excuse is not None:
            data["submission[excuse]"] = submission_excuse


        # OPTIONAL - submission[late_policy_status]
        """
            Sets the late policy status to either "late", "missing", "none", or null.
        """
        if submission_late_policy_status is not None:
            data["submission[late_policy_status]"] = submission_late_policy_status


        # OPTIONAL - submission[seconds_late_override]
        """
            Sets the seconds late if late policy status is "late"
        """
        if submission_seconds_late_override is not None:
            data["submission[seconds_late_override]"] = submission_seconds_late_override


        # OPTIONAL - rubric_assessment
        """
            Assign a rubric assessment to this assignment submission. The
        sub-parameters here depend on the rubric for the assignment. The general
        format is, for each row in the rubric:

        The points awarded for this row.
          rubric_assessment[criterion_id][points]

        The rating id for the row.
          rubric_assessment[criterion_id][rating_id]

        Comments to add for this row.
          rubric_assessment[criterion_id][comments]

        For example, if the assignment rubric is (in JSON format):
          !!!javascript
          [
            {
              'id': 'crit1',
              'points': 10,
              'description': 'Criterion 1',
              'ratings':
              [
                { 'id': 'rat1', 'description': 'Good', 'points': 10 },
                { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
              ]
            },
            {
              'id': 'crit2',
              'points': 5,
              'description': 'Criterion 2',
              'ratings':
              [
                { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
                { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
                { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
              ]
            }
          ]

        Then a possible set of values for rubric_assessment would be:
            rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done.
        """
        if rubric_assessment is not None:
            data["rubric_assessment"] = rubric_assessment


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def grade_or_comment_on_submission_sections(self, assignment_id, section_id, user_id, comment_file_ids=None, comment_group_comment=None, comment_media_comment_id=None, comment_media_comment_type=None, comment_text_comment=None, include_visibility=None, rubric_assessment=None, submission_excuse=None, submission_late_policy_status=None, submission_posted_grade=None, submission_seconds_late_override=None):
        """
        Grade or comment on a submission.

        Comment on and/or update the grading for a student's assignment submission.
        If any submission or rubric_assessment arguments are provided, the user
        must have permission to manage grades in the appropriate context (course or
        section).
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # OPTIONAL - comment[text_comment]
        """
            Add a textual comment to the submission.
        """
        if comment_text_comment is not None:
            data["comment[text_comment]"] = comment_text_comment


        # OPTIONAL - comment[group_comment]
        """
            Whether or not this comment should be sent to the entire group (defaults
        to false). Ignored if this is not a group assignment or if no text_comment
        is provided.
        """
        if comment_group_comment is not None:
            data["comment[group_comment]"] = comment_group_comment


        # OPTIONAL - comment[media_comment_id]
        """
            Add an audio/video comment to the submission. Media comments can be added
        via this API, however, note that there is not yet an API to generate or
        list existing media comments, so this functionality is currently of
        limited use.
        """
        if comment_media_comment_id is not None:
            data["comment[media_comment_id]"] = comment_media_comment_id


        # OPTIONAL - comment[media_comment_type]
        """
            The type of media comment being added.
        """
        if comment_media_comment_type is not None:
            self._validate_enum(comment_media_comment_type, ["audio", "video"])
            data["comment[media_comment_type]"] = comment_media_comment_type


        # OPTIONAL - comment[file_ids]
        """
            Attach files to this comment that were previously uploaded using the
        Submission Comment API's files action
        """
        if comment_file_ids is not None:
            data["comment[file_ids]"] = comment_file_ids


        # OPTIONAL - include[visibility]
        """
            Whether this assignment is visible to the owner of the submission
        """
        if include_visibility is not None:
            data["include[visibility]"] = include_visibility


        # OPTIONAL - submission[posted_grade]
        """
            Assign a score to the submission, updating both the "score" and "grade"
        fields on the submission record. This parameter can be passed in a few
        different formats:

        points:: A floating point or integral value, such as "13.5". The grade
          will be interpreted directly as the score of the assignment.
          Values above assignment.points_possible are allowed, for awarding
          extra credit.
        percentage:: A floating point value appended with a percent sign, such as
           "40%". The grade will be interpreted as a percentage score on the
           assignment, where 100% == assignment.points_possible. Values above 100%
           are allowed, for awarding extra credit.
        letter grade:: A letter grade, following the assignment's defined letter
           grading scheme. For example, "A-". The resulting score will be the high
           end of the defined range for the letter grade. For instance, if "B" is
           defined as 86% to 84%, a letter grade of "B" will be worth 86%. The
           letter grade will be rejected if the assignment does not have a defined
           letter grading scheme. For more fine-grained control of scores, pass in
           points or percentage rather than the letter grade.
        "pass/complete/fail/incomplete":: A string value of "pass" or "complete"
           will give a score of 100%. "fail" or "incomplete" will give a score of
           0.

        Note that assignments with grading_type of "pass_fail" can only be
        assigned a score of 0 or assignment.points_possible, nothing inbetween. If
        a posted_grade in the "points" or "percentage" format is sent, the grade
        will only be accepted if the grade equals one of those two values.
        """
        if submission_posted_grade is not None:
            data["submission[posted_grade]"] = submission_posted_grade


        # OPTIONAL - submission[excuse]
        """
            Sets the "excused" status of an assignment.
        """
        if submission_excuse is not None:
            data["submission[excuse]"] = submission_excuse


        # OPTIONAL - submission[late_policy_status]
        """
            Sets the late policy status to either "late", "missing", "none", or null.
        """
        if submission_late_policy_status is not None:
            data["submission[late_policy_status]"] = submission_late_policy_status


        # OPTIONAL - submission[seconds_late_override]
        """
            Sets the seconds late if late policy status is "late"
        """
        if submission_seconds_late_override is not None:
            data["submission[seconds_late_override]"] = submission_seconds_late_override


        # OPTIONAL - rubric_assessment
        """
            Assign a rubric assessment to this assignment submission. The
        sub-parameters here depend on the rubric for the assignment. The general
        format is, for each row in the rubric:

        The points awarded for this row.
          rubric_assessment[criterion_id][points]

        The rating id for the row.
          rubric_assessment[criterion_id][rating_id]

        Comments to add for this row.
          rubric_assessment[criterion_id][comments]

        For example, if the assignment rubric is (in JSON format):
          !!!javascript
          [
            {
              'id': 'crit1',
              'points': 10,
              'description': 'Criterion 1',
              'ratings':
              [
                { 'id': 'rat1', 'description': 'Good', 'points': 10 },
                { 'id': 'rat2', 'description': 'Poor', 'points': 3 }
              ]
            },
            {
              'id': 'crit2',
              'points': 5,
              'description': 'Criterion 2',
              'ratings':
              [
                { 'id': 'rat1', 'description': 'Exemplary', 'points': 5 },
                { 'id': 'rat2', 'description': 'Complete', 'points': 5 },
                { 'id': 'rat3', 'description': 'Incomplete', 'points': 0 }
              ]
            }
          ]

        Then a possible set of values for rubric_assessment would be:
            rubric_assessment[crit1][points]=3&rubric_assessment[crit1][rating_id]=rat1&rubric_assessment[crit2][points]=5&rubric_assessment[crit2][rating_id]=rat2&rubric_assessment[crit2][comments]=Well%20Done.
        """
        if rubric_assessment is not None:
            data["rubric_assessment"] = rubric_assessment


        self.logger.debug("PUT /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}".format(**path), data=data, params=params, no_data=True)

    def list_gradeable_students(self, assignment_id, course_id):
        """
        List gradeable students.

        A paginated list of students eligible to submit the assignment. The caller must have permission to view grades.
        
        If anonymous grading is enabled for the current assignment and the allow_new_anonymous_id parameter is passed,
        the returned data will not include any values identifying the student, but will instead include an
        assignment-specific anonymous ID for each student.
        
        Section-limited instructors will only see students in their own sections.
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


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/gradeable_students".format(**path), data=data, params=params, all_pages=True)

    def list_multiple_assignments_gradeable_students(self, course_id, assignment_ids=None):
        """
        List multiple assignments gradeable students.

        A paginated list of students eligible to submit a list of assignments. The caller must have
        permission to view grades for the requested course.
        
        Section-limited instructors will only see students in their own sections.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - assignment_ids
        """
            Assignments being requested
        """
        if assignment_ids is not None:
            params["assignment_ids"] = assignment_ids


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/gradeable_students with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/gradeable_students".format(**path), data=data, params=params, no_data=True)

    def grade_or_comment_on_multiple_submissions_courses_submissions(self, course_id, grade_data_<assignment_id>_<student_id>=None, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """
            See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade


        # OPTIONAL - grade_data[<student_id>][excuse]
        """
            See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse


        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """
            See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment


        # OPTIONAL - grade_data[<student_id>][text_comment]
        """
            no description
        """
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment


        # OPTIONAL - grade_data[<student_id>][group_comment]
        """
            no description
        """
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment


        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id


        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type


        # OPTIONAL - grade_data[<student_id>][file_ids]
        """
            See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids


        # OPTIONAL - grade_data[<assignment_id>][<student_id>]
        """
            Specifies which assignment to grade.  This argument is not necessary when
        using the assignment-specific endpoints.
        """
        if grade_data_<assignment_id>_<student_id> is not None:
            data["grade_data[<assignment_id>][<student_id>]"] = grade_data_<assignment_id>_<student_id>


        self.logger.debug("POST /api/v1/courses/{course_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def grade_or_comment_on_multiple_submissions_courses_assignments(self, assignment_id, course_id, grade_data_<assignment_id>_<student_id>=None, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
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


        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """
            See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade


        # OPTIONAL - grade_data[<student_id>][excuse]
        """
            See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse


        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """
            See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment


        # OPTIONAL - grade_data[<student_id>][text_comment]
        """
            no description
        """
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment


        # OPTIONAL - grade_data[<student_id>][group_comment]
        """
            no description
        """
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment


        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id


        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type


        # OPTIONAL - grade_data[<student_id>][file_ids]
        """
            See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids


        # OPTIONAL - grade_data[<assignment_id>][<student_id>]
        """
            Specifies which assignment to grade.  This argument is not necessary when
        using the assignment-specific endpoints.
        """
        if grade_data_<assignment_id>_<student_id> is not None:
            data["grade_data[<assignment_id>][<student_id>]"] = grade_data_<assignment_id>_<student_id>


        self.logger.debug("POST /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def grade_or_comment_on_multiple_submissions_sections_submissions(self, section_id, grade_data_<assignment_id>_<student_id>=None, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - section_id
        """
            ID
        """
        path["section_id"] = section_id


        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """
            See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade


        # OPTIONAL - grade_data[<student_id>][excuse]
        """
            See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse


        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """
            See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment


        # OPTIONAL - grade_data[<student_id>][text_comment]
        """
            no description
        """
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment


        # OPTIONAL - grade_data[<student_id>][group_comment]
        """
            no description
        """
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment


        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id


        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type


        # OPTIONAL - grade_data[<student_id>][file_ids]
        """
            See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids


        # OPTIONAL - grade_data[<assignment_id>][<student_id>]
        """
            Specifies which assignment to grade.  This argument is not necessary when
        using the assignment-specific endpoints.
        """
        if grade_data_<assignment_id>_<student_id> is not None:
            data["grade_data[<assignment_id>][<student_id>]"] = grade_data_<assignment_id>_<student_id>


        self.logger.debug("POST /api/v1/sections/{section_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def grade_or_comment_on_multiple_submissions_sections_assignments(self, assignment_id, section_id, grade_data_<assignment_id>_<student_id>=None, grade_data_<student_id>_excuse=None, grade_data_<student_id>_file_ids=None, grade_data_<student_id>_group_comment=None, grade_data_<student_id>_media_comment_id=None, grade_data_<student_id>_media_comment_type=None, grade_data_<student_id>_posted_grade=None, grade_data_<student_id>_rubric_assessment=None, grade_data_<student_id>_text_comment=None):
        """
        Grade or comment on multiple submissions.

        Update the grading and comments on multiple student's assignment
        submissions in an asynchronous job.
        
        The user must have permission to manage grades in the appropriate context
        (course or section).
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


        # OPTIONAL - grade_data[<student_id>][posted_grade]
        """
            See documentation for the posted_grade argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_posted_grade is not None:
            data["grade_data[<student_id>][posted_grade]"] = grade_data_<student_id>_posted_grade


        # OPTIONAL - grade_data[<student_id>][excuse]
        """
            See documentation for the excuse argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_excuse is not None:
            data["grade_data[<student_id>][excuse]"] = grade_data_<student_id>_excuse


        # OPTIONAL - grade_data[<student_id>][rubric_assessment]
        """
            See documentation for the rubric_assessment argument in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_rubric_assessment is not None:
            data["grade_data[<student_id>][rubric_assessment]"] = grade_data_<student_id>_rubric_assessment


        # OPTIONAL - grade_data[<student_id>][text_comment]
        """
            no description
        """
        if grade_data_<student_id>_text_comment is not None:
            data["grade_data[<student_id>][text_comment]"] = grade_data_<student_id>_text_comment


        # OPTIONAL - grade_data[<student_id>][group_comment]
        """
            no description
        """
        if grade_data_<student_id>_group_comment is not None:
            data["grade_data[<student_id>][group_comment]"] = grade_data_<student_id>_group_comment


        # OPTIONAL - grade_data[<student_id>][media_comment_id]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_id is not None:
            data["grade_data[<student_id>][media_comment_id]"] = grade_data_<student_id>_media_comment_id


        # OPTIONAL - grade_data[<student_id>][media_comment_type]
        """
            no description
        """
        if grade_data_<student_id>_media_comment_type is not None:
            self._validate_enum(grade_data_<student_id>_media_comment_type, ["audio", "video"])
            data["grade_data[<student_id>][media_comment_type]"] = grade_data_<student_id>_media_comment_type


        # OPTIONAL - grade_data[<student_id>][file_ids]
        """
            See documentation for the comment[] arguments in the
        {api:SubmissionsApiController#update Submissions Update} documentation
        """
        if grade_data_<student_id>_file_ids is not None:
            data["grade_data[<student_id>][file_ids]"] = grade_data_<student_id>_file_ids


        # OPTIONAL - grade_data[<assignment_id>][<student_id>]
        """
            Specifies which assignment to grade.  This argument is not necessary when
        using the assignment-specific endpoints.
        """
        if grade_data_<assignment_id>_<student_id> is not None:
            data["grade_data[<assignment_id>][<student_id>]"] = grade_data_<assignment_id>_<student_id>


        self.logger.debug("POST /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/update_grades".format(**path), data=data, params=params, single_item=True)

    def mark_submission_as_read_courses(self, assignment_id, course_id, user_id):
        """
        Mark submission as read.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
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


        self.logger.debug("PUT /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_submission_as_read_sections(self, assignment_id, section_id, user_id):
        """
        Mark submission as read.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("PUT /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_submission_as_unread_courses(self, assignment_id, course_id, user_id):
        """
        Mark submission as unread.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
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


        self.logger.debug("DELETE /api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def mark_submission_as_unread_sections(self, assignment_id, section_id, user_id):
        """
        Mark submission as unread.

        No request fields are necessary.
        
        On success, the response will be 204 No Content with an empty body.
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


        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("DELETE /api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submissions/{user_id}/read".format(**path), data=data, params=params, no_data=True)

    def submission_summary_courses(self, assignment_id, course_id, grouped=None):
        """
        Submission Summary.

        Returns the number of submissions for the given assignment based on gradeable students
        that fall into three categories: graded, ungraded, not submitted.
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


        # OPTIONAL - grouped
        """
            If this argument is true, the response will take into account student groups.
        """
        if grouped is not None:
            params["grouped"] = grouped


        self.logger.debug("GET /api/v1/courses/{course_id}/assignments/{assignment_id}/submission_summary with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/assignments/{assignment_id}/submission_summary".format(**path), data=data, params=params, no_data=True)

    def submission_summary_sections(self, assignment_id, section_id, grouped=None):
        """
        Submission Summary.

        Returns the number of submissions for the given assignment based on gradeable students
        that fall into three categories: graded, ungraded, not submitted.
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


        # OPTIONAL - grouped
        """
            If this argument is true, the response will take into account student groups.
        """
        if grouped is not None:
            params["grouped"] = grouped


        self.logger.debug("GET /api/v1/sections/{section_id}/assignments/{assignment_id}/submission_summary with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/sections/{section_id}/assignments/{assignment_id}/submission_summary".format(**path), data=data, params=params, no_data=True)


class Mediacomment(BaseModel):
    """Mediacomment Model."""

    def __init__(self, content_type=None, display_name=None, media_id=None, media_type=None, url=None):
        """Init method for Mediacomment class."""
        self._content_type = content_type
        self._display_name = display_name
        self._media_id = media_id
        self._media_type = media_type
        self._url = url

        self.logger = logging.getLogger('py3canvas.Mediacomment')

    @property
    def content_type(self):
        """content_type."""
        return self._content_type

    @content_type.setter
    def content_type(self, value):
        """Setter for content_type property."""
        self.logger.warn("Setting values on content_type will NOT update the remote Canvas instance.")
        self._content_type = value

    @property
    def display_name(self):
        """display_name."""
        return self._display_name

    @display_name.setter
    def display_name(self, value):
        """Setter for display_name property."""
        self.logger.warn("Setting values on display_name will NOT update the remote Canvas instance.")
        self._display_name = value

    @property
    def media_id(self):
        """media_id."""
        return self._media_id

    @media_id.setter
    def media_id(self, value):
        """Setter for media_id property."""
        self.logger.warn("Setting values on media_id will NOT update the remote Canvas instance.")
        self._media_id = value

    @property
    def media_type(self):
        """media_type."""
        return self._media_type

    @media_type.setter
    def media_type(self, value):
        """Setter for media_type property."""
        self.logger.warn("Setting values on media_type will NOT update the remote Canvas instance.")
        self._media_type = value

    @property
    def url(self):
        """url."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value


class Submissioncomment(BaseModel):
    """Submissioncomment Model."""

    def __init__(self, id=None, author_id=None, author_name=None, author=None, comment=None, created_at=None, edited_at=None, media_comment=None):
        """Init method for Submissioncomment class."""
        self._id = id
        self._author_id = author_id
        self._author_name = author_name
        self._author = author
        self._comment = comment
        self._created_at = created_at
        self._edited_at = edited_at
        self._media_comment = media_comment

        self.logger = logging.getLogger('py3canvas.Submissioncomment')

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def author_id(self):
        """author_id."""
        return self._author_id

    @author_id.setter
    def author_id(self, value):
        """Setter for author_id property."""
        self.logger.warn("Setting values on author_id will NOT update the remote Canvas instance.")
        self._author_id = value

    @property
    def author_name(self):
        """author_name."""
        return self._author_name

    @author_name.setter
    def author_name(self, value):
        """Setter for author_name property."""
        self.logger.warn("Setting values on author_name will NOT update the remote Canvas instance.")
        self._author_name = value

    @property
    def author(self):
        """Abbreviated user object UserDisplay (see users API)."""
        return self._author

    @author.setter
    def author(self, value):
        """Setter for author property."""
        self.logger.warn("Setting values on author will NOT update the remote Canvas instance.")
        self._author = value

    @property
    def comment(self):
        """comment."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Setter for comment property."""
        self.logger.warn("Setting values on comment will NOT update the remote Canvas instance.")
        self._comment = value

    @property
    def created_at(self):
        """created_at."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def edited_at(self):
        """edited_at."""
        return self._edited_at

    @edited_at.setter
    def edited_at(self, value):
        """Setter for edited_at property."""
        self.logger.warn("Setting values on edited_at will NOT update the remote Canvas instance.")
        self._edited_at = value

    @property
    def media_comment(self):
        """media_comment."""
        return self._media_comment

    @media_comment.setter
    def media_comment(self, value):
        """Setter for media_comment property."""
        self.logger.warn("Setting values on media_comment will NOT update the remote Canvas instance.")
        self._media_comment = value


class Submission(BaseModel):
    """Submission Model."""

    def __init__(self, assignment_id=None, assignment=None, course=None, attempt=None, body=None, grade=None, grade_matches_current_submission=None, html_url=None, preview_url=None, score=None, submission_comments=None, submission_type=None, submitted_at=None, url=None, user_id=None, grader_id=None, graded_at=None, user=None, late=None, assignment_visible=None, excused=None, missing=None, late_policy_status=None, points_deducted=None, seconds_late=None, workflow_state=None, extra_attempts=None, anonymous_id=None, posted_at=None, read_status=None):
        """Init method for Submission class."""
        self._assignment_id = assignment_id
        self._assignment = assignment
        self._course = course
        self._attempt = attempt
        self._body = body
        self._grade = grade
        self._grade_matches_current_submission = grade_matches_current_submission
        self._html_url = html_url
        self._preview_url = preview_url
        self._score = score
        self._submission_comments = submission_comments
        self._submission_type = submission_type
        self._submitted_at = submitted_at
        self._url = url
        self._user_id = user_id
        self._grader_id = grader_id
        self._graded_at = graded_at
        self._user = user
        self._late = late
        self._assignment_visible = assignment_visible
        self._excused = excused
        self._missing = missing
        self._late_policy_status = late_policy_status
        self._points_deducted = points_deducted
        self._seconds_late = seconds_late
        self._workflow_state = workflow_state
        self._extra_attempts = extra_attempts
        self._anonymous_id = anonymous_id
        self._posted_at = posted_at
        self._read_status = read_status

        self.logger = logging.getLogger('py3canvas.Submission')

    @property
    def assignment_id(self):
        """The submission's assignment id."""
        return self._assignment_id

    @assignment_id.setter
    def assignment_id(self, value):
        """Setter for assignment_id property."""
        self.logger.warn("Setting values on assignment_id will NOT update the remote Canvas instance.")
        self._assignment_id = value

    @property
    def assignment(self):
        """The submission's assignment (see the assignments API) (optional)."""
        return self._assignment

    @assignment.setter
    def assignment(self, value):
        """Setter for assignment property."""
        self.logger.warn("Setting values on assignment will NOT update the remote Canvas instance.")
        self._assignment = value

    @property
    def course(self):
        """The submission's course (see the course API) (optional)."""
        return self._course

    @course.setter
    def course(self, value):
        """Setter for course property."""
        self.logger.warn("Setting values on course will NOT update the remote Canvas instance.")
        self._course = value

    @property
    def attempt(self):
        """This is the submission attempt number."""
        return self._attempt

    @attempt.setter
    def attempt(self, value):
        """Setter for attempt property."""
        self.logger.warn("Setting values on attempt will NOT update the remote Canvas instance.")
        self._attempt = value

    @property
    def body(self):
        """The content of the submission, if it was submitted directly in a text field."""
        return self._body

    @body.setter
    def body(self, value):
        """Setter for body property."""
        self.logger.warn("Setting values on body will NOT update the remote Canvas instance.")
        self._body = value

    @property
    def grade(self):
        """The grade for the submission, translated into the assignment grading scheme (so a letter grade, for example)."""
        return self._grade

    @grade.setter
    def grade(self, value):
        """Setter for grade property."""
        self.logger.warn("Setting values on grade will NOT update the remote Canvas instance.")
        self._grade = value

    @property
    def grade_matches_current_submission(self):
        """A boolean flag which is false if the student has re-submitted since the submission was last graded."""
        return self._grade_matches_current_submission

    @grade_matches_current_submission.setter
    def grade_matches_current_submission(self, value):
        """Setter for grade_matches_current_submission property."""
        self.logger.warn("Setting values on grade_matches_current_submission will NOT update the remote Canvas instance.")
        self._grade_matches_current_submission = value

    @property
    def html_url(self):
        """URL to the submission. This will require the user to log in."""
        return self._html_url

    @html_url.setter
    def html_url(self, value):
        """Setter for html_url property."""
        self.logger.warn("Setting values on html_url will NOT update the remote Canvas instance.")
        self._html_url = value

    @property
    def preview_url(self):
        """URL to the submission preview. This will require the user to log in."""
        return self._preview_url

    @preview_url.setter
    def preview_url(self, value):
        """Setter for preview_url property."""
        self.logger.warn("Setting values on preview_url will NOT update the remote Canvas instance.")
        self._preview_url = value

    @property
    def score(self):
        """The raw score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn("Setting values on score will NOT update the remote Canvas instance.")
        self._score = value

    @property
    def submission_comments(self):
        """Associated comments for a submission (optional)."""
        return self._submission_comments

    @submission_comments.setter
    def submission_comments(self, value):
        """Setter for submission_comments property."""
        self.logger.warn("Setting values on submission_comments will NOT update the remote Canvas instance.")
        self._submission_comments = value

    @property
    def submission_type(self):
        """The types of submission ex: ('online_text_entry'|'online_url'|'online_upload'|'media_recording'|'student_annotation')."""
        return self._submission_type

    @submission_type.setter
    def submission_type(self, value):
        """Setter for submission_type property."""
        self.logger.warn("Setting values on submission_type will NOT update the remote Canvas instance.")
        self._submission_type = value

    @property
    def submitted_at(self):
        """The timestamp when the assignment was submitted."""
        return self._submitted_at

    @submitted_at.setter
    def submitted_at(self, value):
        """Setter for submitted_at property."""
        self.logger.warn("Setting values on submitted_at will NOT update the remote Canvas instance.")
        self._submitted_at = value

    @property
    def url(self):
        """The URL of the submission (for 'online_url' submissions)."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def user_id(self):
        """The id of the user who created the submission."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def grader_id(self):
        """The id of the user who graded the submission. This will be null for submissions that haven't been graded yet. It will be a positive number if a real user has graded the submission and a negative number if the submission was graded by a process (e.g. Quiz autograder and autograding LTI tools).  Specifically autograded quizzes set grader_id to the negative of the quiz id.  Submissions autograded by LTI tools set grader_id to the negative of the tool id."""
        return self._grader_id

    @grader_id.setter
    def grader_id(self, value):
        """Setter for grader_id property."""
        self.logger.warn("Setting values on grader_id will NOT update the remote Canvas instance.")
        self._grader_id = value

    @property
    def graded_at(self):
        """graded_at."""
        return self._graded_at

    @graded_at.setter
    def graded_at(self, value):
        """Setter for graded_at property."""
        self.logger.warn("Setting values on graded_at will NOT update the remote Canvas instance.")
        self._graded_at = value

    @property
    def user(self):
        """The submissions user (see user API) (optional)."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn("Setting values on user will NOT update the remote Canvas instance.")
        self._user = value

    @property
    def late(self):
        """Whether the submission was made after the applicable due date."""
        return self._late

    @late.setter
    def late(self, value):
        """Setter for late property."""
        self.logger.warn("Setting values on late will NOT update the remote Canvas instance.")
        self._late = value

    @property
    def assignment_visible(self):
        """Whether the assignment is visible to the user who submitted the assignment. Submissions where `assignment_visible` is false no longer count towards the student's grade and the assignment can no longer be accessed by the student. `assignment_visible` becomes false for submissions that do not have a grade and whose assignment is no longer assigned to the student's section."""
        return self._assignment_visible

    @assignment_visible.setter
    def assignment_visible(self, value):
        """Setter for assignment_visible property."""
        self.logger.warn("Setting values on assignment_visible will NOT update the remote Canvas instance.")
        self._assignment_visible = value

    @property
    def excused(self):
        """Whether the assignment is excused.  Excused assignments have no impact on a user's grade."""
        return self._excused

    @excused.setter
    def excused(self, value):
        """Setter for excused property."""
        self.logger.warn("Setting values on excused will NOT update the remote Canvas instance.")
        self._excused = value

    @property
    def missing(self):
        """Whether the assignment is missing."""
        return self._missing

    @missing.setter
    def missing(self, value):
        """Setter for missing property."""
        self.logger.warn("Setting values on missing will NOT update the remote Canvas instance.")
        self._missing = value

    @property
    def late_policy_status(self):
        """The status of the submission in relation to the late policy. Can be late, missing, none, or null."""
        return self._late_policy_status

    @late_policy_status.setter
    def late_policy_status(self, value):
        """Setter for late_policy_status property."""
        self.logger.warn("Setting values on late_policy_status will NOT update the remote Canvas instance.")
        self._late_policy_status = value

    @property
    def points_deducted(self):
        """The amount of points automatically deducted from the score by the missing/late policy for a late or missing assignment."""
        return self._points_deducted

    @points_deducted.setter
    def points_deducted(self, value):
        """Setter for points_deducted property."""
        self.logger.warn("Setting values on points_deducted will NOT update the remote Canvas instance.")
        self._points_deducted = value

    @property
    def seconds_late(self):
        """The amount of time, in seconds, that an submission is late by."""
        return self._seconds_late

    @seconds_late.setter
    def seconds_late(self, value):
        """Setter for seconds_late property."""
        self.logger.warn("Setting values on seconds_late will NOT update the remote Canvas instance.")
        self._seconds_late = value

    @property
    def workflow_state(self):
        """The current state of the submission."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def extra_attempts(self):
        """Extra submission attempts allowed for the given user and assignment."""
        return self._extra_attempts

    @extra_attempts.setter
    def extra_attempts(self, value):
        """Setter for extra_attempts property."""
        self.logger.warn("Setting values on extra_attempts will NOT update the remote Canvas instance.")
        self._extra_attempts = value

    @property
    def anonymous_id(self):
        """A unique short ID identifying this submission without reference to the owning user. Only included if the caller has administrator access for the current account."""
        return self._anonymous_id

    @anonymous_id.setter
    def anonymous_id(self, value):
        """Setter for anonymous_id property."""
        self.logger.warn("Setting values on anonymous_id will NOT update the remote Canvas instance.")
        self._anonymous_id = value

    @property
    def posted_at(self):
        """The date this submission was posted to the student, or nil if it has not been posted."""
        return self._posted_at

    @posted_at.setter
    def posted_at(self, value):
        """Setter for posted_at property."""
        self.logger.warn("Setting values on posted_at will NOT update the remote Canvas instance.")
        self._posted_at = value

    @property
    def read_status(self):
        """The read status of this submission for the given user (optional). Including read_status will mark submission(s) as read."""
        return self._read_status

    @read_status.setter
    def read_status(self, value):
        """Setter for read_status property."""
        self.logger.warn("Setting values on read_status will NOT update the remote Canvas instance.")
        self._read_status = value

