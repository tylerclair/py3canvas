"""Score API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ScoreAPI(BaseCanvasAPI):
    """Score API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ScoreAPI."""
        super(ScoreAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ScoreAPI")

    def create_score(self, activityProgress, course_id, gradingProgress, line_item_id, timestamp, userId, comment=None, https://canvas.instructure.com/lti/submission=None, scoreGiven=None, scoreMaximum=None):
        """
        Create a Score.

        Create a new Result from the score params. If this is for the first created line_item for a
        resourceLinkId, or it is a line item that is not attached to a resourceLinkId, then a submission
        record will be created for the associated assignment when gradingProgress is set to
        FullyGraded or PendingManual.
        
        The submission score will also be updated when a score object is sent with either of those
        two values for gradingProgress. If a score object is sent with either of FullyGraded or
        PendingManual as the value for gradingProgress and scoreGiven is missing, the assignment
        will not be graded. This also supposes the line_item meets the condition to create a submission.
        
        A submission comment with an unknown author will be created when the comment value is included.
        This also supposes the line_item meets the condition to create a submission.
        
        NOTE: Upcoming Feature
        It will soon be possible to submit a file along with this score, which will attach the file to the
        submission that is created. Files should be formatted as Content Items, with the correct syntax
        below.
        
        Returns a url pointing to the Result. If any files were submitted, also returns the Content Items
        which were sent in the request, each with a url pointing to the Progress of the file upload.
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


        # REQUIRED - userId
        """
            The lti_user_id or the Canvas user_id.
        Returns a 422 if user not found in Canvas or is not a student.
        """
        data["userId"] = userId


        # REQUIRED - activityProgress
        """
            Indicate to Canvas the status of the user towards the activity's completion.
        Must be one of Initialized, Started, InProgress, Submitted, Completed.
        """
        data["activityProgress"] = activityProgress


        # REQUIRED - gradingProgress
        """
            Indicate to Canvas the status of the grading process.
        A value of PendingManual will require intervention by a grader.
        Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored.
        FullyGraded values will require no action.
        Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded.
        """
        data["gradingProgress"] = gradingProgress


        # REQUIRED - timestamp
        """
            Date and time when the score was modified in the tool. Should use subsecond precision.
        Returns a 400 if the timestamp is earlier than the updated_at time of the Result.
        """
        data["timestamp"] = timestamp


        # OPTIONAL - scoreGiven
        """
            The Current score received in the tool for this line item and user,
        scaled to the scoreMaximum
        """
        if scoreGiven is not None:
            data["scoreGiven"] = scoreGiven


        # OPTIONAL - scoreMaximum
        """
            Maximum possible score for this result; it must be present if scoreGiven is present.
        Returns 412 if not present when scoreGiven is present.
        """
        if scoreMaximum is not None:
            data["scoreMaximum"] = scoreMaximum


        # OPTIONAL - comment
        """
            Comment visible to the student about this score.
        """
        if comment is not None:
            data["comment"] = comment


        # OPTIONAL - https://canvas.instructure.com/lti/submission
        """
            (EXTENSION) Optional submission type and data.
        new_submission [Boolean] flag to indicate that this is a new submission. Defaults to true unless submission_type is none.
        submission_type [String] permissible values are: none, basic_lti_launch, online_text_entry, external_tool, online_upload, or online_url. Defaults to external_tool. Ignored if content_items are provided.
        submission_data [String] submission data (URL or body text)
        submitted_at [String] Date and time that the submission was originally created. Should use subsecond precision. This should match the data and time that the original submission happened in Canvas.
        content_items [Array] Files that should be included with the submission. Each item should contain `type: file`, a url pointing to the file, a title, and a progress url that Canvas can report to. If present, submission_type will be online_upload.
        """
        if https://canvas.instructure.com/lti/submission is not None:
            data["https://canvas.instructure.com/lti/submission"] = https://canvas.instructure.com/lti/submission


        self.logger.debug("POST /api/lti/courses/{course_id}/line_items/{line_item_id}/scores with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/lti/courses/{course_id}/line_items/{line_item_id}/scores".format(**path), data=data, params=params, all_pages=True)


class Score(BaseModel):
    """Score Model."""

    def __init__(self, userId=None, scoreGiven=None, scoreMaximum=None, comment=None, timestamp=None, activityProgress=None, gradingProgress=None):
        """Init method for Score class."""
        self._userId = userId
        self._scoreGiven = scoreGiven
        self._scoreMaximum = scoreMaximum
        self._comment = comment
        self._timestamp = timestamp
        self._activityProgress = activityProgress
        self._gradingProgress = gradingProgress

        self.logger = logging.getLogger('py3canvas.Score')

    @property
    def userId(self):
        """The lti_user_id or the Canvas user_id."""
        return self._userId

    @userId.setter
    def userId(self, value):
        """Setter for userId property."""
        self.logger.warn("Setting values on userId will NOT update the remote Canvas instance.")
        self._userId = value

    @property
    def scoreGiven(self):
        """The Current score received in the tool for this line item and user, scaled to the scoreMaximum."""
        return self._scoreGiven

    @scoreGiven.setter
    def scoreGiven(self, value):
        """Setter for scoreGiven property."""
        self.logger.warn("Setting values on scoreGiven will NOT update the remote Canvas instance.")
        self._scoreGiven = value

    @property
    def scoreMaximum(self):
        """Maximum possible score for this result; it must be present if scoreGiven is present."""
        return self._scoreMaximum

    @scoreMaximum.setter
    def scoreMaximum(self, value):
        """Setter for scoreMaximum property."""
        self.logger.warn("Setting values on scoreMaximum will NOT update the remote Canvas instance.")
        self._scoreMaximum = value

    @property
    def comment(self):
        """Comment visible to the student about this score."""
        return self._comment

    @comment.setter
    def comment(self, value):
        """Setter for comment property."""
        self.logger.warn("Setting values on comment will NOT update the remote Canvas instance.")
        self._comment = value

    @property
    def timestamp(self):
        """Date and time when the score was modified in the tool. Should use subsecond precision."""
        return self._timestamp

    @timestamp.setter
    def timestamp(self, value):
        """Setter for timestamp property."""
        self.logger.warn("Setting values on timestamp will NOT update the remote Canvas instance.")
        self._timestamp = value

    @property
    def activityProgress(self):
        """Indicate to Canvas the status of the user towards the activity's completion. Must be one of Initialized, Started, InProgress, Submitted, Completed."""
        return self._activityProgress

    @activityProgress.setter
    def activityProgress(self, value):
        """Setter for activityProgress property."""
        self.logger.warn("Setting values on activityProgress will NOT update the remote Canvas instance.")
        self._activityProgress = value

    @property
    def gradingProgress(self):
        """Indicate to Canvas the status of the grading process. A value of PendingManual will require intervention by a grader. Values of NotReady, Failed, and Pending will cause the scoreGiven to be ignored. FullyGraded values will require no action. Possible values are NotReady, Failed, Pending, PendingManual, FullyGraded."""
        return self._gradingProgress

    @gradingProgress.setter
    def gradingProgress(self, value):
        """Setter for gradingProgress property."""
        self.logger.warn("Setting values on gradingProgress will NOT update the remote Canvas instance.")
        self._gradingProgress = value

