"""ErrorReports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ErrorReportsAPI(BaseCanvasAPI):
    """ErrorReports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ErrorReportsAPI."""
        super(ErrorReportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ErrorReportsAPI")

    def create_error_report(self, error_subject, error_comments=None, error_email=None, error_http_env=None, error_url=None):
        """
        Create Error Report.

        Create a new error report documenting an experienced problem
        
        Performs the same action as when a user uses the "help -> report a problem"
        dialog.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - error[subject]
        """
            The summary of the problem
        """
        data["error[subject]"] = error_subject


        # OPTIONAL - error[url]
        """
            URL from which the report was issued
        """
        if error_url is not None:
            data["error[url]"] = error_url


        # OPTIONAL - error[email]
        """
            Email address for the reporting user
        """
        if error_email is not None:
            data["error[email]"] = error_email


        # OPTIONAL - error[comments]
        """
            The long version of the story from the user one what they experienced
        """
        if error_comments is not None:
            data["error[comments]"] = error_comments


        # OPTIONAL - error[http_env]
        """
            A collection of metadata about the users' environment.  If not provided,
        canvas will collect it based on information found in the request.
        (Doesn't have to be HTTPENV info, could be anything JSON object that can be
        serialized as a hash, a mobile app might include relevant metadata for
        itself)
        """
        if error_http_env is not None:
            data["error[http_env]"] = error_http_env


        self.logger.debug("POST /api/v1/error_reports with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/error_reports".format(**path), data=data, params=params, no_data=True)


class Errorreport(BaseModel):
    """Errorreport Model.
    A collection of information around a specific notification of a problem"""

    def __init__(self, subject=None, comments=None, user_perceived_severity=None, email=None, url=None, context_asset_string=None, user_roles=None):
        """Init method for Errorreport class."""
        self._subject = subject
        self._comments = comments
        self._user_perceived_severity = user_perceived_severity
        self._email = email
        self._url = url
        self._context_asset_string = context_asset_string
        self._user_roles = user_roles

        self.logger = logging.getLogger('py3canvas.Errorreport')

    @property
    def subject(self):
        """The users problem summary, like an email subject line."""
        return self._subject

    @subject.setter
    def subject(self, value):
        """Setter for subject property."""
        self.logger.warn("Setting values on subject will NOT update the remote Canvas instance.")
        self._subject = value

    @property
    def comments(self):
        """long form documentation of what was witnessed."""
        return self._comments

    @comments.setter
    def comments(self, value):
        """Setter for comments property."""
        self.logger.warn("Setting values on comments will NOT update the remote Canvas instance.")
        self._comments = value

    @property
    def user_perceived_severity(self):
        """categorization of how bad the user thinks the problem is.  Should be one of [just_a_comment, not_urgent, workaround_possible, blocks_what_i_need_to_do, extreme_critical_emergency]."""
        return self._user_perceived_severity

    @user_perceived_severity.setter
    def user_perceived_severity(self, value):
        """Setter for user_perceived_severity property."""
        self.logger.warn("Setting values on user_perceived_severity will NOT update the remote Canvas instance.")
        self._user_perceived_severity = value

    @property
    def email(self):
        """the email address of the reporting user."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email property."""
        self.logger.warn("Setting values on email will NOT update the remote Canvas instance.")
        self._email = value

    @property
    def url(self):
        """URL of the page on which the error was reported."""
        return self._url

    @url.setter
    def url(self, value):
        """Setter for url property."""
        self.logger.warn("Setting values on url will NOT update the remote Canvas instance.")
        self._url = value

    @property
    def context_asset_string(self):
        """string describing the asset being interacted with at the time of error.  Formatted '[type]_[id]'."""
        return self._context_asset_string

    @context_asset_string.setter
    def context_asset_string(self, value):
        """Setter for context_asset_string property."""
        self.logger.warn("Setting values on context_asset_string will NOT update the remote Canvas instance.")
        self._context_asset_string = value

    @property
    def user_roles(self):
        """comma seperated list of roles the reporting user holds.  Can be one [student], or many [teacher,admin]."""
        return self._user_roles

    @user_roles.setter
    def user_roles(self, value):
        """Setter for user_roles property."""
        self.logger.warn("Setting values on user_roles will NOT update the remote Canvas instance.")
        self._user_roles = value

