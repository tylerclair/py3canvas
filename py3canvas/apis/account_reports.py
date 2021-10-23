"""AccountReports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class AccountReportsAPI(BaseCanvasAPI):
    """AccountReports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for AccountReportsAPI."""
        super(AccountReportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.AccountReportsAPI")

    def list_available_reports(self, account_id):
        """
        List Available Reports.

        Returns a paginated list of reports for the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/reports with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/reports".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def start_report(
        self,
        account_id,
        report,
        parameters=None,
        parameters_course_id=None,
        parameters_users=None,
    ):
        """
        Start a Report.

        Generates a report instance for the account. Note that "report" in the
        request must match one of the available report names. To fetch a list of
        available report names and parameters for each report (including whether or
        not those parameters are required), see
        {api:AccountReportsController#available_reports List Available Reports}.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - report
        """
            ID
        """
        path["report"] = report

        # OPTIONAL - parameters
        """
            The parameters will vary for each report. To fetch a list
        of available parameters for each report, see {api:AccountReportsController#available_reports List Available Reports}.
        A few example parameters have been provided below. Note that the example
        parameters provided below may not be valid for every report.
        """
        if parameters is not None:
            data["parameters"] = parameters

        # OPTIONAL - parameters[course_id]
        """
            The id of the course to report on.
        Note: this parameter has been listed to serve as an example and may not be
        valid for every report.
        """
        if parameters_course_id is not None:
            data["parameters[course_id]"] = parameters_course_id

        # OPTIONAL - parameters[users]
        """
            If true, user data will be included. If
        false, user data will be omitted. Note: this parameter has been listed to
        serve as an example and may not be valid for every report.
        """
        if parameters_users is not None:
            data["parameters[users]"] = parameters_users

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/reports/{report} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/reports/{report}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def index_of_reports(self, account_id, report):
        """
        Index of Reports.

        Shows all reports that have been run for the account of a specific type.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - report
        """
            ID
        """
        path["report"] = report

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/reports/{report} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/reports/{report}".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def status_of_report(self, account_id, id, report):
        """
        Status of a Report.

        Returns the status of a report.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - report
        """
            ID
        """
        path["report"] = report

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/reports/{report}/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/reports/{report}/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_report(self, account_id, id, report):
        """
        Delete a Report.

        Deletes a generated report instance.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # REQUIRED - PATH - report
        """
            ID
        """
        path["report"] = report

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "DELETE /api/v1/accounts/{account_id}/reports/{report}/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/accounts/{account_id}/reports/{report}/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Report(BaseModel):
    """Report Model."""

    def __init__(
        self,
        id=None,
        report=None,
        file_url=None,
        attachment=None,
        status=None,
        created_at=None,
        started_at=None,
        ended_at=None,
        parameters=None,
        progress=None,
        current_line=None,
    ):
        """Init method for Report class."""
        self._id = id
        self._report = report
        self._file_url = file_url
        self._attachment = attachment
        self._status = status
        self._created_at = created_at
        self._started_at = started_at
        self._ended_at = ended_at
        self._parameters = parameters
        self._progress = progress
        self._current_line = current_line

        self.logger = logging.getLogger("py3canvas.Report")

    @property
    def id(self):
        """The unique identifier for the report."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def report(self):
        """The type of report."""
        return self._report

    @report.setter
    def report(self, value):
        """Setter for report property."""
        self.logger.warn(
            "Setting values on report will NOT update the remote Canvas instance."
        )
        self._report = value

    @property
    def file_url(self):
        """The url to the report download."""
        return self._file_url

    @file_url.setter
    def file_url(self, value):
        """Setter for file_url property."""
        self.logger.warn(
            "Setting values on file_url will NOT update the remote Canvas instance."
        )
        self._file_url = value

    @property
    def attachment(self):
        """The attachment api object of the report. Only available after the report has completed."""
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        """Setter for attachment property."""
        self.logger.warn(
            "Setting values on attachment will NOT update the remote Canvas instance."
        )
        self._attachment = value

    @property
    def status(self):
        """The status of the report."""
        return self._status

    @status.setter
    def status(self, value):
        """Setter for status property."""
        self.logger.warn(
            "Setting values on status will NOT update the remote Canvas instance."
        )
        self._status = value

    @property
    def created_at(self):
        """The date and time the report was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def started_at(self):
        """The date and time the report started processing."""
        return self._started_at

    @started_at.setter
    def started_at(self, value):
        """Setter for started_at property."""
        self.logger.warn(
            "Setting values on started_at will NOT update the remote Canvas instance."
        )
        self._started_at = value

    @property
    def ended_at(self):
        """The date and time the report finished processing."""
        return self._ended_at

    @ended_at.setter
    def ended_at(self, value):
        """Setter for ended_at property."""
        self.logger.warn(
            "Setting values on ended_at will NOT update the remote Canvas instance."
        )
        self._ended_at = value

    @property
    def parameters(self):
        """The report parameters."""
        return self._parameters

    @parameters.setter
    def parameters(self, value):
        """Setter for parameters property."""
        self.logger.warn(
            "Setting values on parameters will NOT update the remote Canvas instance."
        )
        self._parameters = value

    @property
    def progress(self):
        """The progress of the report."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn(
            "Setting values on progress will NOT update the remote Canvas instance."
        )
        self._progress = value

    @property
    def current_line(self):
        """This is the current line count being written to the report. It updates every 1000 records."""
        return self._current_line

    @current_line.setter
    def current_line(self, value):
        """Setter for current_line property."""
        self.logger.warn(
            "Setting values on current_line will NOT update the remote Canvas instance."
        )
        self._current_line = value


class Reportparameters(BaseModel):
    """Reportparameters Model.
    The parameters returned will vary for each report."""

    def __init__(
        self,
        enrollment_term_id=None,
        include_deleted=None,
        course_id=None,
        order=None,
        users=None,
        accounts=None,
        terms=None,
        courses=None,
        sections=None,
        enrollments=None,
        groups=None,
        xlist=None,
        sis_terms_csv=None,
        sis_accounts_csv=None,
        include_enrollment_state=None,
        enrollment_state=None,
        start_at=None,
        end_at=None,
    ):
        """Init method for Reportparameters class."""
        self._enrollment_term_id = enrollment_term_id
        self._include_deleted = include_deleted
        self._course_id = course_id
        self._order = order
        self._users = users
        self._accounts = accounts
        self._terms = terms
        self._courses = courses
        self._sections = sections
        self._enrollments = enrollments
        self._groups = groups
        self._xlist = xlist
        self._sis_terms_csv = sis_terms_csv
        self._sis_accounts_csv = sis_accounts_csv
        self._include_enrollment_state = include_enrollment_state
        self._enrollment_state = enrollment_state
        self._start_at = start_at
        self._end_at = end_at

        self.logger = logging.getLogger("py3canvas.Reportparameters")

    @property
    def enrollment_term_id(self):
        """The canvas id of the term to get grades from."""
        return self._enrollment_term_id

    @enrollment_term_id.setter
    def enrollment_term_id(self, value):
        """Setter for enrollment_term_id property."""
        self.logger.warn(
            "Setting values on enrollment_term_id will NOT update the remote Canvas instance."
        )
        self._enrollment_term_id = value

    @property
    def include_deleted(self):
        """If true, deleted objects will be included. If false, deleted objects will be omitted."""
        return self._include_deleted

    @include_deleted.setter
    def include_deleted(self, value):
        """Setter for include_deleted property."""
        self.logger.warn(
            "Setting values on include_deleted will NOT update the remote Canvas instance."
        )
        self._include_deleted = value

    @property
    def course_id(self):
        """The id of the course to report on."""
        return self._course_id

    @course_id.setter
    def course_id(self, value):
        """Setter for course_id property."""
        self.logger.warn(
            "Setting values on course_id will NOT update the remote Canvas instance."
        )
        self._course_id = value

    @property
    def order(self):
        """The sort order for the csv, Options: 'users', 'courses', 'outcomes'."""
        return self._order

    @order.setter
    def order(self, value):
        """Setter for order property."""
        self.logger.warn(
            "Setting values on order will NOT update the remote Canvas instance."
        )
        self._order = value

    @property
    def users(self):
        """If true, user data will be included. If false, user data will be omitted."""
        return self._users

    @users.setter
    def users(self, value):
        """Setter for users property."""
        self.logger.warn(
            "Setting values on users will NOT update the remote Canvas instance."
        )
        self._users = value

    @property
    def accounts(self):
        """If true, account data will be included. If false, account data will be omitted."""
        return self._accounts

    @accounts.setter
    def accounts(self, value):
        """Setter for accounts property."""
        self.logger.warn(
            "Setting values on accounts will NOT update the remote Canvas instance."
        )
        self._accounts = value

    @property
    def terms(self):
        """If true, term data will be included. If false, term data will be omitted."""
        return self._terms

    @terms.setter
    def terms(self, value):
        """Setter for terms property."""
        self.logger.warn(
            "Setting values on terms will NOT update the remote Canvas instance."
        )
        self._terms = value

    @property
    def courses(self):
        """If true, course data will be included. If false, course data will be omitted."""
        return self._courses

    @courses.setter
    def courses(self, value):
        """Setter for courses property."""
        self.logger.warn(
            "Setting values on courses will NOT update the remote Canvas instance."
        )
        self._courses = value

    @property
    def sections(self):
        """If true, section data will be included. If false, section data will be omitted."""
        return self._sections

    @sections.setter
    def sections(self, value):
        """Setter for sections property."""
        self.logger.warn(
            "Setting values on sections will NOT update the remote Canvas instance."
        )
        self._sections = value

    @property
    def enrollments(self):
        """If true, enrollment data will be included. If false, enrollment data will be omitted."""
        return self._enrollments

    @enrollments.setter
    def enrollments(self, value):
        """Setter for enrollments property."""
        self.logger.warn(
            "Setting values on enrollments will NOT update the remote Canvas instance."
        )
        self._enrollments = value

    @property
    def groups(self):
        """If true, group data will be included. If false, group data will be omitted."""
        return self._groups

    @groups.setter
    def groups(self, value):
        """Setter for groups property."""
        self.logger.warn(
            "Setting values on groups will NOT update the remote Canvas instance."
        )
        self._groups = value

    @property
    def xlist(self):
        """If true, data for crosslisted courses will be included. If false, data for crosslisted courses will be omitted."""
        return self._xlist

    @xlist.setter
    def xlist(self, value):
        """Setter for xlist property."""
        self.logger.warn(
            "Setting values on xlist will NOT update the remote Canvas instance."
        )
        self._xlist = value

    @property
    def sis_terms_csv(self):
        """sis_terms_csv."""
        return self._sis_terms_csv

    @sis_terms_csv.setter
    def sis_terms_csv(self, value):
        """Setter for sis_terms_csv property."""
        self.logger.warn(
            "Setting values on sis_terms_csv will NOT update the remote Canvas instance."
        )
        self._sis_terms_csv = value

    @property
    def sis_accounts_csv(self):
        """sis_accounts_csv."""
        return self._sis_accounts_csv

    @sis_accounts_csv.setter
    def sis_accounts_csv(self, value):
        """Setter for sis_accounts_csv property."""
        self.logger.warn(
            "Setting values on sis_accounts_csv will NOT update the remote Canvas instance."
        )
        self._sis_accounts_csv = value

    @property
    def include_enrollment_state(self):
        """If true, enrollment state will be included. If false, enrollment state will be omitted. Defaults to false."""
        return self._include_enrollment_state

    @include_enrollment_state.setter
    def include_enrollment_state(self, value):
        """Setter for include_enrollment_state property."""
        self.logger.warn(
            "Setting values on include_enrollment_state will NOT update the remote Canvas instance."
        )
        self._include_enrollment_state = value

    @property
    def enrollment_state(self):
        """Include enrollment state. Defaults to 'all' Options: ['active'| 'invited'| 'creation_pending'| 'deleted'| 'rejected'| 'completed'| 'inactive'| 'all']."""
        return self._enrollment_state

    @enrollment_state.setter
    def enrollment_state(self, value):
        """Setter for enrollment_state property."""
        self.logger.warn(
            "Setting values on enrollment_state will NOT update the remote Canvas instance."
        )
        self._enrollment_state = value

    @property
    def start_at(self):
        """The beginning date for submissions. Max time range is 2 weeks."""
        return self._start_at

    @start_at.setter
    def start_at(self, value):
        """Setter for start_at property."""
        self.logger.warn(
            "Setting values on start_at will NOT update the remote Canvas instance."
        )
        self._start_at = value

    @property
    def end_at(self):
        """The end date for submissions. Max time range is 2 weeks."""
        return self._end_at

    @end_at.setter
    def end_at(self, value):
        """Setter for end_at property."""
        self.logger.warn(
            "Setting values on end_at will NOT update the remote Canvas instance."
        )
        self._end_at = value
