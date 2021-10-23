"""NamesAndRole API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class NamesAndRoleAPI(BaseCanvasAPI):
    """NamesAndRole API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for NamesAndRoleAPI."""
        super(NamesAndRoleAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.NamesAndRoleAPI")

    def list_course_memberships(self, course_id, limit=None, rlid=None, role=None):
        """
        List Course Memberships.

        Return active NamesAndRoleMemberships in the given course.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - rlid
        """
            If specified only NamesAndRoleMemberships with access to the LTI link references by this `rlid` will be included.
        Also causes the member array to be included for each returned NamesAndRoleMembership.
        If the `role` parameter is also present, it will be 'and-ed' together with this parameter
        """
        if rlid is not None:
            params["rlid"] = rlid


        # OPTIONAL - role
        """
            If specified only NamesAndRoleMemberships having this role in the given Course will be included.
        Value must be a fully-qualified LTI/LIS role URN.
        If the `rlid` parameter is also present, it will be 'and-ed' together with this parameter
        """
        if role is not None:
            params["role"] = role


        # OPTIONAL - limit
        """
            May be used to limit the number of NamesAndRoleMemberships returned in a page. Defaults to 50.
        """
        if limit is not None:
            params["limit"] = limit


        self.logger.debug("GET /api/lti/courses/{course_id}/names_and_roles with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/courses/{course_id}/names_and_roles".format(**path), data=data, params=params, single_item=True)

    def list_group_memberships(self, group_id, `rlid`=None, limit=None, role=None):
        """
        List Group Memberships.

        Return active NamesAndRoleMemberships in the given group.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # OPTIONAL - `rlid`
        """
            If specified only NamesAndRoleMemberships with access to the LTI link references by this `rlid` will be included.
        Also causes the member array to be included for each returned NamesAndRoleMembership.
        If the role parameter is also present, it will be 'and-ed' together with this parameter
        """
        if `rlid` is not None:
            params["`rlid`"] = `rlid`


        # OPTIONAL - role
        """
            If specified only NamesAndRoleMemberships having this role in the given Group will be included.
        Value must be a fully-qualified LTI/LIS role URN. Further, only
        http://purl.imsglobal.org/vocab/lis/v2/membership#Member and
        http://purl.imsglobal.org/vocab/lis/v2/membership#Manager are supported.
        If the `rlid` parameter is also present, it will be 'and-ed' together with this parameter
        """
        if role is not None:
            params["role"] = role


        # OPTIONAL - limit
        """
            May be used to limit the number of NamesAndRoleMemberships returned in a page. Defaults to 50.
        """
        if limit is not None:
            params["limit"] = limit


        self.logger.debug("GET /api/lti/groups/{group_id}/names_and_roles with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/groups/{group_id}/names_and_roles".format(**path), data=data, params=params, single_item=True)


class Namesandrolecontext(BaseModel):
    """Namesandrolecontext Model.
    An abbreviated representation of an LTI Context"""

    def __init__(self, id=None, label=None, title=None):
        """Init method for Namesandrolecontext class."""
        self._id = id
        self._label = label
        self._title = title

        self.logger = logging.getLogger('py3canvas.Namesandrolecontext')

    @property
    def id(self):
        """LTI Context unique identifier."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def label(self):
        """LTI Context short name or code."""
        return self._label

    @label.setter
    def label(self, value):
        """Setter for label property."""
        self.logger.warn("Setting values on label will NOT update the remote Canvas instance.")
        self._label = value

    @property
    def title(self):
        """LTI Context full name."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn("Setting values on title will NOT update the remote Canvas instance.")
        self._title = value


class Namesandrolemessage(BaseModel):
    """Namesandrolemessage Model.
    Additional attributes which would appear in the LTI launch message were this member to click the specified resource link (`rlid` query parameter)"""

    def __init__(self, https://purl.imsglobal.org/spec/lti/claim/message_type=None, locale=None, https://www.instructure.com/canvas_user_id=None, https://www.instructure.com/canvas_user_login_id=None, https://purl.imsglobal.org/spec/lti/claim/custom=None):
        """Init method for Namesandrolemessage class."""
        self._https://purl.imsglobal.org/spec/lti/claim/message_type = https://purl.imsglobal.org/spec/lti/claim/message_type
        self._locale = locale
        self._https://www.instructure.com/canvas_user_id = https://www.instructure.com/canvas_user_id
        self._https://www.instructure.com/canvas_user_login_id = https://www.instructure.com/canvas_user_login_id
        self._https://purl.imsglobal.org/spec/lti/claim/custom = https://purl.imsglobal.org/spec/lti/claim/custom

        self.logger = logging.getLogger('py3canvas.Namesandrolemessage')

    @property
    def https://purl.imsglobal.org/spec/lti/claim/message_type(self):
        """The type of LTI message being described. Always set to 'LtiResourceLinkRequest'."""
        return self._https://purl.imsglobal.org/spec/lti/claim/message_type

    @https://purl.imsglobal.org/spec/lti/claim/message_type.setter
    def https://purl.imsglobal.org/spec/lti/claim/message_type(self, value):
        """Setter for https://purl.imsglobal.org/spec/lti/claim/message_type property."""
        self.logger.warn("Setting values on https://purl.imsglobal.org/spec/lti/claim/message_type will NOT update the remote Canvas instance.")
        self._https://purl.imsglobal.org/spec/lti/claim/message_type = value

    @property
    def locale(self):
        """The member's preferred locale."""
        return self._locale

    @locale.setter
    def locale(self, value):
        """Setter for locale property."""
        self.logger.warn("Setting values on locale will NOT update the remote Canvas instance.")
        self._locale = value

    @property
    def https://www.instructure.com/canvas_user_id(self):
        """The member's API ID."""
        return self._https://www.instructure.com/canvas_user_id

    @https://www.instructure.com/canvas_user_id.setter
    def https://www.instructure.com/canvas_user_id(self, value):
        """Setter for https://www.instructure.com/canvas_user_id property."""
        self.logger.warn("Setting values on https://www.instructure.com/canvas_user_id will NOT update the remote Canvas instance.")
        self._https://www.instructure.com/canvas_user_id = value

    @property
    def https://www.instructure.com/canvas_user_login_id(self):
        """The member's primary login username."""
        return self._https://www.instructure.com/canvas_user_login_id

    @https://www.instructure.com/canvas_user_login_id.setter
    def https://www.instructure.com/canvas_user_login_id(self, value):
        """Setter for https://www.instructure.com/canvas_user_login_id property."""
        self.logger.warn("Setting values on https://www.instructure.com/canvas_user_login_id will NOT update the remote Canvas instance.")
        self._https://www.instructure.com/canvas_user_login_id = value

    @property
    def https://purl.imsglobal.org/spec/lti/claim/custom(self):
        """Expanded LTI custom parameters that pertain to the member (as opposed to the Context)."""
        return self._https://purl.imsglobal.org/spec/lti/claim/custom

    @https://purl.imsglobal.org/spec/lti/claim/custom.setter
    def https://purl.imsglobal.org/spec/lti/claim/custom(self, value):
        """Setter for https://purl.imsglobal.org/spec/lti/claim/custom property."""
        self.logger.warn("Setting values on https://purl.imsglobal.org/spec/lti/claim/custom will NOT update the remote Canvas instance.")
        self._https://purl.imsglobal.org/spec/lti/claim/custom = value


class Namesandrolemembership(BaseModel):
    """Namesandrolemembership Model.
    A member of a LTI Context in one or more roles"""

    def __init__(self, status=None, name=None, picture=None, given_name=None, family_name=None, email=None, lis_person_sourcedid=None, user_id=None, roles=None, message=None):
        """Init method for Namesandrolemembership class."""
        self._status = status
        self._name = name
        self._picture = picture
        self._given_name = given_name
        self._family_name = family_name
        self._email = email
        self._lis_person_sourcedid = lis_person_sourcedid
        self._user_id = user_id
        self._roles = roles
        self._message = message

        self.logger = logging.getLogger('py3canvas.Namesandrolemembership')

    @property
    def status(self):
        """Membership state."""
        return self._status

    @status.setter
    def status(self, value):
        """Setter for status property."""
        self.logger.warn("Setting values on status will NOT update the remote Canvas instance.")
        self._status = value

    @property
    def name(self):
        """Member's full name. Only included if tool privacy level is `public` or `name_only`."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def picture(self):
        """URL to the member's avatar. Only included if tool privacy level is `public`."""
        return self._picture

    @picture.setter
    def picture(self, value):
        """Setter for picture property."""
        self.logger.warn("Setting values on picture will NOT update the remote Canvas instance.")
        self._picture = value

    @property
    def given_name(self):
        """Member's 'first' name. Only included if tool privacy level is `public` or `name_only`."""
        return self._given_name

    @given_name.setter
    def given_name(self, value):
        """Setter for given_name property."""
        self.logger.warn("Setting values on given_name will NOT update the remote Canvas instance.")
        self._given_name = value

    @property
    def family_name(self):
        """Member's 'last' name. Only included if tool privacy level is `public` or `name_only`."""
        return self._family_name

    @family_name.setter
    def family_name(self, value):
        """Setter for family_name property."""
        self.logger.warn("Setting values on family_name will NOT update the remote Canvas instance.")
        self._family_name = value

    @property
    def email(self):
        """Member's email address. Only included if tool privacy level is `public` or `email_only`."""
        return self._email

    @email.setter
    def email(self, value):
        """Setter for email property."""
        self.logger.warn("Setting values on email will NOT update the remote Canvas instance.")
        self._email = value

    @property
    def lis_person_sourcedid(self):
        """Member's primary SIS identifier. Only included if tool privacy level is `public` or `name_only`."""
        return self._lis_person_sourcedid

    @lis_person_sourcedid.setter
    def lis_person_sourcedid(self, value):
        """Setter for lis_person_sourcedid property."""
        self.logger.warn("Setting values on lis_person_sourcedid will NOT update the remote Canvas instance.")
        self._lis_person_sourcedid = value

    @property
    def user_id(self):
        """Member's unique LTI identifier."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def roles(self):
        """Member's roles in the current Context, expressed as LTI/LIS URNs."""
        return self._roles

    @roles.setter
    def roles(self, value):
        """Setter for roles property."""
        self.logger.warn("Setting values on roles will NOT update the remote Canvas instance.")
        self._roles = value

    @property
    def message(self):
        """Only present when the request specifies a `rlid` query parameter. Contains additional attributes which would appear in the LTI launch message were this member to click the link referenced by the `rlid` query parameter."""
        return self._message

    @message.setter
    def message(self, value):
        """Setter for message property."""
        self.logger.warn("Setting values on message will NOT update the remote Canvas instance.")
        self._message = value


class Namesandrolememberships(BaseModel):
    """Namesandrolememberships Model."""

    def __init__(self, id=None, context=None, members=None):
        """Init method for Namesandrolememberships class."""
        self._id = id
        self._context = context
        self._members = members

        self.logger = logging.getLogger('py3canvas.Namesandrolememberships')

    @property
    def id(self):
        """Invocation URL."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def context(self):
        """The LTI Context containing the memberships."""
        return self._context

    @context.setter
    def context(self, value):
        """Setter for context property."""
        self.logger.warn("Setting values on context will NOT update the remote Canvas instance.")
        self._context = value

    @property
    def members(self):
        """A list of NamesAndRoleMembership."""
        return self._members

    @members.setter
    def members(self, value):
        """Setter for members property."""
        self.logger.warn("Setting values on members will NOT update the remote Canvas instance.")
        self._members = value

