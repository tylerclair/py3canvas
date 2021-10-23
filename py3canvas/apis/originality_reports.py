"""OriginalityReports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class OriginalityReportsAPI(BaseCanvasAPI):
    """OriginalityReports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for OriginalityReportsAPI."""
        super(OriginalityReportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.OriginalityReportsAPI")

    def create_originality_report(self, assignment_id, originality_report_originality_score, submission_id, originality_report_attempt=None, originality_report_error_message=None, originality_report_file_id=None, originality_report_originality_report_file_id=None, originality_report_originality_report_url=None, originality_report_tool_setting_resource_type_code=None, originality_report_tool_setting_resource_url=None, originality_report_workflow_state=None):
        """
        Create an Originality Report.

        Create a new OriginalityReport for the specified file
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # OPTIONAL - originality_report[file_id]
        """
            The id of the file being given an originality score. Required
        if creating a report associated with a file.
        """
        if originality_report_file_id is not None:
            data["originality_report[file_id]"] = originality_report_file_id


        # REQUIRED - originality_report[originality_score]
        """
            A number between 0 and 100 representing the measure of the
        specified file's originality.
        """
        data["originality_report[originality_score]"] = originality_report_originality_score


        # OPTIONAL - originality_report[originality_report_url]
        """
            The URL where the originality report for the specified
        file may be found.
        """
        if originality_report_originality_report_url is not None:
            data["originality_report[originality_report_url]"] = originality_report_originality_report_url


        # OPTIONAL - originality_report[originality_report_file_id]
        """
            The ID of the file within Canvas that contains the originality
        report for the submitted file provided in the request URL.
        """
        if originality_report_originality_report_file_id is not None:
            data["originality_report[originality_report_file_id]"] = originality_report_originality_report_file_id


        # OPTIONAL - originality_report[tool_setting][resource_type_code]
        """
            The resource type code of the resource handler Canvas should use for the
        LTI launch for viewing originality reports. If set Canvas will launch
        to the message with type 'basic-lti-launch-request' in the specified
        resource handler rather than using the originality_report_url.
        """
        if originality_report_tool_setting_resource_type_code is not None:
            data["originality_report[tool_setting][resource_type_code]"] = originality_report_tool_setting_resource_type_code


        # OPTIONAL - originality_report[tool_setting][resource_url]
        """
            The URL Canvas should launch to when showing an LTI originality report.
        Note that this value is inferred from the specified resource handler's
        message "path" value (See `resource_type_code`) unless
        it is specified. If this parameter is used a `resource_type_code`
        must also be specified.
        """
        if originality_report_tool_setting_resource_url is not None:
            data["originality_report[tool_setting][resource_url]"] = originality_report_tool_setting_resource_url


        # OPTIONAL - originality_report[workflow_state]
        """
            May be set to "pending", "error", or "scored". If an originality score
        is provided a workflow state of "scored" will be inferred.
        """
        if originality_report_workflow_state is not None:
            data["originality_report[workflow_state]"] = originality_report_workflow_state


        # OPTIONAL - originality_report[error_message]
        """
            A message describing the error. If set, the "workflow_state"
        will be set to "error."
        """
        if originality_report_error_message is not None:
            data["originality_report[error_message]"] = originality_report_error_message


        # OPTIONAL - originality_report[attempt]
        """
            If no `file_id` is given, and no file is required for the assignment
        (that is, the assignment allows an online text entry), this parameter
        may be given to clarify which attempt number the report is for (in the
        case of resubmissions). If this field is omitted and no `file_id` is
        given, the report will be created (or updated, if it exists) for the
        first submission attempt with no associated file.
        """
        if originality_report_attempt is not None:
            data["originality_report[attempt]"] = originality_report_attempt


        self.logger.debug("POST /api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report".format(**path), data=data, params=params, single_item=True)

    def edit_originality_report_submissions(self, assignment_id, id, submission_id, originality_report_error_message=None, originality_report_originality_report_file_id=None, originality_report_originality_report_url=None, originality_report_originality_score=None, originality_report_tool_setting_resource_type_code=None, originality_report_tool_setting_resource_url=None, originality_report_workflow_state=None):
        """
        Edit an Originality Report.

        Modify an existing originality report. An alternative to this endpoint is
        to POST the same parameters listed below to the CREATE endpoint.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - originality_report[originality_score]
        """
            A number between 0 and 100 representing the measure of the
        specified file's originality.
        """
        if originality_report_originality_score is not None:
            data["originality_report[originality_score]"] = originality_report_originality_score


        # OPTIONAL - originality_report[originality_report_url]
        """
            The URL where the originality report for the specified
        file may be found.
        """
        if originality_report_originality_report_url is not None:
            data["originality_report[originality_report_url]"] = originality_report_originality_report_url


        # OPTIONAL - originality_report[originality_report_file_id]
        """
            The ID of the file within Canvas that contains the originality
        report for the submitted file provided in the request URL.
        """
        if originality_report_originality_report_file_id is not None:
            data["originality_report[originality_report_file_id]"] = originality_report_originality_report_file_id


        # OPTIONAL - originality_report[tool_setting][resource_type_code]
        """
            The resource type code of the resource handler Canvas should use for the
        LTI launch for viewing originality reports. If set Canvas will launch
        to the message with type 'basic-lti-launch-request' in the specified
        resource handler rather than using the originality_report_url.
        """
        if originality_report_tool_setting_resource_type_code is not None:
            data["originality_report[tool_setting][resource_type_code]"] = originality_report_tool_setting_resource_type_code


        # OPTIONAL - originality_report[tool_setting][resource_url]
        """
            The URL Canvas should launch to when showing an LTI originality report.
        Note that this value is inferred from the specified resource handler's
        message "path" value (See `resource_type_code`) unless
        it is specified. If this parameter is used a `resource_type_code`
        must also be specified.
        """
        if originality_report_tool_setting_resource_url is not None:
            data["originality_report[tool_setting][resource_url]"] = originality_report_tool_setting_resource_url


        # OPTIONAL - originality_report[workflow_state]
        """
            May be set to "pending", "error", or "scored". If an originality score
        is provided a workflow state of "scored" will be inferred.
        """
        if originality_report_workflow_state is not None:
            data["originality_report[workflow_state]"] = originality_report_workflow_state


        # OPTIONAL - originality_report[error_message]
        """
            A message describing the error. If set, the "workflow_state"
        will be set to "error."
        """
        if originality_report_error_message is not None:
            data["originality_report[error_message]"] = originality_report_error_message


        self.logger.debug("PUT /api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id}".format(**path), data=data, params=params, single_item=True)

    def edit_originality_report_files(self, assignment_id, file_id, originality_report_error_message=None, originality_report_originality_report_file_id=None, originality_report_originality_report_url=None, originality_report_originality_score=None, originality_report_tool_setting_resource_type_code=None, originality_report_tool_setting_resource_url=None, originality_report_workflow_state=None):
        """
        Edit an Originality Report.

        Modify an existing originality report. An alternative to this endpoint is
        to POST the same parameters listed below to the CREATE endpoint.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - file_id
        """
            ID
        """
        path["file_id"] = file_id


        # OPTIONAL - originality_report[originality_score]
        """
            A number between 0 and 100 representing the measure of the
        specified file's originality.
        """
        if originality_report_originality_score is not None:
            data["originality_report[originality_score]"] = originality_report_originality_score


        # OPTIONAL - originality_report[originality_report_url]
        """
            The URL where the originality report for the specified
        file may be found.
        """
        if originality_report_originality_report_url is not None:
            data["originality_report[originality_report_url]"] = originality_report_originality_report_url


        # OPTIONAL - originality_report[originality_report_file_id]
        """
            The ID of the file within Canvas that contains the originality
        report for the submitted file provided in the request URL.
        """
        if originality_report_originality_report_file_id is not None:
            data["originality_report[originality_report_file_id]"] = originality_report_originality_report_file_id


        # OPTIONAL - originality_report[tool_setting][resource_type_code]
        """
            The resource type code of the resource handler Canvas should use for the
        LTI launch for viewing originality reports. If set Canvas will launch
        to the message with type 'basic-lti-launch-request' in the specified
        resource handler rather than using the originality_report_url.
        """
        if originality_report_tool_setting_resource_type_code is not None:
            data["originality_report[tool_setting][resource_type_code]"] = originality_report_tool_setting_resource_type_code


        # OPTIONAL - originality_report[tool_setting][resource_url]
        """
            The URL Canvas should launch to when showing an LTI originality report.
        Note that this value is inferred from the specified resource handler's
        message "path" value (See `resource_type_code`) unless
        it is specified. If this parameter is used a `resource_type_code`
        must also be specified.
        """
        if originality_report_tool_setting_resource_url is not None:
            data["originality_report[tool_setting][resource_url]"] = originality_report_tool_setting_resource_url


        # OPTIONAL - originality_report[workflow_state]
        """
            May be set to "pending", "error", or "scored". If an originality score
        is provided a workflow state of "scored" will be inferred.
        """
        if originality_report_workflow_state is not None:
            data["originality_report[workflow_state]"] = originality_report_workflow_state


        # OPTIONAL - originality_report[error_message]
        """
            A message describing the error. If set, the "workflow_state"
        will be set to "error."
        """
        if originality_report_error_message is not None:
            data["originality_report[error_message]"] = originality_report_error_message


        self.logger.debug("PUT /api/lti/assignments/{assignment_id}/files/{file_id}/originality_report with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/lti/assignments/{assignment_id}/files/{file_id}/originality_report".format(**path), data=data, params=params, single_item=True)

    def show_originality_report_submissions(self, assignment_id, id, submission_id):
        """
        Show an Originality Report.

        Get a single originality report
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - submission_id
        """
            ID
        """
        path["submission_id"] = submission_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/assignments/{assignment_id}/submissions/{submission_id}/originality_report/{id}".format(**path), data=data, params=params, single_item=True)

    def show_originality_report_files(self, assignment_id, file_id):
        """
        Show an Originality Report.

        Get a single originality report
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - assignment_id
        """
            ID
        """
        path["assignment_id"] = assignment_id


        # REQUIRED - PATH - file_id
        """
            ID
        """
        path["file_id"] = file_id


        self.logger.debug("GET /api/lti/assignments/{assignment_id}/files/{file_id}/originality_report with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/assignments/{assignment_id}/files/{file_id}/originality_report".format(**path), data=data, params=params, single_item=True)


class Toolsetting(BaseModel):
    """Toolsetting Model."""

    def __init__(self, resource_type_code=None, resource_url=None):
        """Init method for Toolsetting class."""
        self._resource_type_code = resource_type_code
        self._resource_url = resource_url

        self.logger = logging.getLogger('py3canvas.Toolsetting')

    @property
    def resource_type_code(self):
        """the resource type code of the resource handler to use to display originality reports."""
        return self._resource_type_code

    @resource_type_code.setter
    def resource_type_code(self, value):
        """Setter for resource_type_code property."""
        self.logger.warn("Setting values on resource_type_code will NOT update the remote Canvas instance.")
        self._resource_type_code = value

    @property
    def resource_url(self):
        """a URL that may be used to override the launch URL inferred by the specified resource_type_code. If used a 'resource_type_code' must also be specified."""
        return self._resource_url

    @resource_url.setter
    def resource_url(self, value):
        """Setter for resource_url property."""
        self.logger.warn("Setting values on resource_url will NOT update the remote Canvas instance.")
        self._resource_url = value


class Originalityreport(BaseModel):
    """Originalityreport Model."""

    def __init__(self, id=None, file_id=None, originality_score=None, originality_report_file_id=None, originality_report_url=None, tool_setting=None, error_report=None, submission_time=None, root_account_id=None):
        """Init method for Originalityreport class."""
        self._id = id
        self._file_id = file_id
        self._originality_score = originality_score
        self._originality_report_file_id = originality_report_file_id
        self._originality_report_url = originality_report_url
        self._tool_setting = tool_setting
        self._error_report = error_report
        self._submission_time = submission_time
        self._root_account_id = root_account_id

        self.logger = logging.getLogger('py3canvas.Originalityreport')

    @property
    def id(self):
        """The id of the OriginalityReport."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def file_id(self):
        """The id of the file receiving the originality score."""
        return self._file_id

    @file_id.setter
    def file_id(self, value):
        """Setter for file_id property."""
        self.logger.warn("Setting values on file_id will NOT update the remote Canvas instance.")
        self._file_id = value

    @property
    def originality_score(self):
        """A number between 0 and 100 representing the originality score."""
        return self._originality_score

    @originality_score.setter
    def originality_score(self, value):
        """Setter for originality_score property."""
        self.logger.warn("Setting values on originality_score will NOT update the remote Canvas instance.")
        self._originality_score = value

    @property
    def originality_report_file_id(self):
        """The ID of the file within Canvas containing the originality report document (if provided)."""
        return self._originality_report_file_id

    @originality_report_file_id.setter
    def originality_report_file_id(self, value):
        """Setter for originality_report_file_id property."""
        self.logger.warn("Setting values on originality_report_file_id will NOT update the remote Canvas instance.")
        self._originality_report_file_id = value

    @property
    def originality_report_url(self):
        """A non-LTI launch URL where the originality score of the file may be found."""
        return self._originality_report_url

    @originality_report_url.setter
    def originality_report_url(self, value):
        """Setter for originality_report_url property."""
        self.logger.warn("Setting values on originality_report_url will NOT update the remote Canvas instance.")
        self._originality_report_url = value

    @property
    def tool_setting(self):
        """A ToolSetting object containing optional 'resource_type_code' and 'resource_url'."""
        return self._tool_setting

    @tool_setting.setter
    def tool_setting(self, value):
        """Setter for tool_setting property."""
        self.logger.warn("Setting values on tool_setting will NOT update the remote Canvas instance.")
        self._tool_setting = value

    @property
    def error_report(self):
        """A message describing the error. If set, the workflow_state will become 'error.'."""
        return self._error_report

    @error_report.setter
    def error_report(self, value):
        """Setter for error_report property."""
        self.logger.warn("Setting values on error_report will NOT update the remote Canvas instance.")
        self._error_report = value

    @property
    def submission_time(self):
        """The submitted_at date time of the submission."""
        return self._submission_time

    @submission_time.setter
    def submission_time(self, value):
        """Setter for submission_time property."""
        self.logger.warn("Setting values on submission_time will NOT update the remote Canvas instance.")
        self._submission_time = value

    @property
    def root_account_id(self):
        """The id of the root Account associated with the OriginalityReport."""
        return self._root_account_id

    @root_account_id.setter
    def root_account_id(self, value):
        """Setter for root_account_id property."""
        self.logger.warn("Setting values on root_account_id will NOT update the remote Canvas instance.")
        self._root_account_id = value

