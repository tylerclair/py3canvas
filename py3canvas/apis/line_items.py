"""LineItems API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class LineItemsAPI(BaseCanvasAPI):
    """LineItems API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for LineItemsAPI."""
        super(LineItemsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.LineItemsAPI")

    def create_line_item(self, course_id, label, scoreMaximum, https://canvas.instructure.com/lti/submission_type=None, resourceId=None, resourceLinkId=None, tag=None):
        """
        Create a Line Item.

        Create a new Line Item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - scoreMaximum
        """
            The maximum score for the line item. Scores created for the Line Item may exceed this value.
        """
        data["scoreMaximum"] = scoreMaximum


        # REQUIRED - label
        """
            The label for the Line Item. If no resourceLinkId is specified this value will also be used
        as the name of the placeholder assignment.
        """
        data["label"] = label


        # OPTIONAL - resourceId
        """
            A Tool Provider specified id for the Line Item. Multiple line items may
        share the same resourceId within a given context.
        """
        if resourceId is not None:
            data["resourceId"] = resourceId


        # OPTIONAL - tag
        """
            A value used to qualify a line Item beyond its ids. Line Items may be queried
        by this value in the List endpoint. Multiple line items can share the same tag
        within a given context.
        """
        if tag is not None:
            data["tag"] = tag


        # OPTIONAL - resourceLinkId
        """
            The resource link id the Line Item should be attached to. This value should
        match the LTI id of the Canvas assignment associated with the tool.
        """
        if resourceLinkId is not None:
            data["resourceLinkId"] = resourceLinkId


        # OPTIONAL - https://canvas.instructure.com/lti/submission_type
        """
            (EXTENSION) - Optional block to set Assignment Submission Type when creating a new assignment is created.
        type - 'none' or 'external_tool'::
        external_tool_url - Submission URL only used when type: 'external_tool'::
        """
        if https://canvas.instructure.com/lti/submission_type is not None:
            data["https://canvas.instructure.com/lti/submission_type"] = https://canvas.instructure.com/lti/submission_type


        self.logger.debug("POST /api/lti/courses/{course_id}/line_items with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/lti/courses/{course_id}/line_items".format(**path), data=data, params=params, single_item=True)

    def update_line_item(self, course_id, id, label=None, resourceId=None, scoreMaximum=None, tag=None):
        """
        Update a Line Item.

        Update new Line Item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - scoreMaximum
        """
            The maximum score for the line item. Scores created for the Line Item may exceed this value.
        """
        if scoreMaximum is not None:
            data["scoreMaximum"] = scoreMaximum


        # OPTIONAL - label
        """
            The label for the Line Item. If no resourceLinkId is specified this value will also be used
        as the name of the placeholder assignment.
        """
        if label is not None:
            data["label"] = label


        # OPTIONAL - resourceId
        """
            A Tool Provider specified id for the Line Item. Multiple line items may
        share the same resourceId within a given context.
        """
        if resourceId is not None:
            data["resourceId"] = resourceId


        # OPTIONAL - tag
        """
            A value used to qualify a line Item beyond its ids. Line Items may be queried
        by this value in the List endpoint. Multiple line items can share the same tag
        within a given context.
        """
        if tag is not None:
            data["tag"] = tag


        self.logger.debug("PUT /api/lti/courses/{course_id}/line_items/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/lti/courses/{course_id}/line_items/{id}".format(**path), data=data, params=params, single_item=True)

    def show_line_item(self, course_id, id):
        """
        Show a Line Item.

        Show existing Line Item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/lti/courses/{course_id}/line_items/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/courses/{course_id}/line_items/{id}".format(**path), data=data, params=params, single_item=True)

    def list_line_items(self, course_id, limit=None, resource_id=None, resource_link_id=None, tag=None):
        """
        List line Items.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # OPTIONAL - tag
        """
            If specified only Line Items with this tag will be included.
        """
        if tag is not None:
            params["tag"] = tag


        # OPTIONAL - resource_id
        """
            If specified only Line Items with this resource_id will be included.
        """
        if resource_id is not None:
            params["resource_id"] = resource_id


        # OPTIONAL - resource_link_id
        """
            If specified only Line Items attached to the specified resource_link_id will be included.
        """
        if resource_link_id is not None:
            params["resource_link_id"] = resource_link_id


        # OPTIONAL - limit
        """
            May be used to limit the number of Line Items returned in a page
        """
        if limit is not None:
            params["limit"] = limit


        self.logger.debug("GET /api/lti/courses/{course_id}/line_items with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/courses/{course_id}/line_items".format(**path), data=data, params=params, single_item=True)

    def delete_line_item(self, course_id, id):
        """
        Delete a Line Item.

        Delete an existing Line Item
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/lti/courses/{course_id}/line_items/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/lti/courses/{course_id}/line_items/{id}".format(**path), data=data, params=params, single_item=True)


class Lineitem(BaseModel):
    """Lineitem Model."""

    def __init__(self, id=None, scoreMaximum=None, label=None, tag=None, resourceId=None, resourceLinkId=None, https://canvas.instructure.com/lti/submission_type=None):
        """Init method for Lineitem class."""
        self._id = id
        self._scoreMaximum = scoreMaximum
        self._label = label
        self._tag = tag
        self._resourceId = resourceId
        self._resourceLinkId = resourceLinkId
        self._https://canvas.instructure.com/lti/submission_type = https://canvas.instructure.com/lti/submission_type

        self.logger = logging.getLogger('py3canvas.Lineitem')

    @property
    def id(self):
        """The fully qualified URL for showing, updating, and deleting the Line Item."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def scoreMaximum(self):
        """The maximum score of the Line Item."""
        return self._scoreMaximum

    @scoreMaximum.setter
    def scoreMaximum(self, value):
        """Setter for scoreMaximum property."""
        self.logger.warn("Setting values on scoreMaximum will NOT update the remote Canvas instance.")
        self._scoreMaximum = value

    @property
    def label(self):
        """The label of the Line Item."""
        return self._label

    @label.setter
    def label(self, value):
        """Setter for label property."""
        self.logger.warn("Setting values on label will NOT update the remote Canvas instance.")
        self._label = value

    @property
    def tag(self):
        """Tag used to qualify a line Item beyond its ids."""
        return self._tag

    @tag.setter
    def tag(self, value):
        """Setter for tag property."""
        self.logger.warn("Setting values on tag will NOT update the remote Canvas instance.")
        self._tag = value

    @property
    def resourceId(self):
        """A Tool Provider specified id for the Line Item. Multiple line items can share the same resourceId within a given context."""
        return self._resourceId

    @resourceId.setter
    def resourceId(self, value):
        """Setter for resourceId property."""
        self.logger.warn("Setting values on resourceId will NOT update the remote Canvas instance.")
        self._resourceId = value

    @property
    def resourceLinkId(self):
        """The resource link id the Line Item is attached to."""
        return self._resourceLinkId

    @resourceLinkId.setter
    def resourceLinkId(self, value):
        """Setter for resourceLinkId property."""
        self.logger.warn("Setting values on resourceLinkId will NOT update the remote Canvas instance.")
        self._resourceLinkId = value

    @property
    def https://canvas.instructure.com/lti/submission_type(self):
        """The extension that defines the submission_type of the line_item. Only returns if set through the line_item create endpoint."""
        return self._https://canvas.instructure.com/lti/submission_type

    @https://canvas.instructure.com/lti/submission_type.setter
    def https://canvas.instructure.com/lti/submission_type(self, value):
        """Setter for https://canvas.instructure.com/lti/submission_type property."""
        self.logger.warn("Setting values on https://canvas.instructure.com/lti/submission_type will NOT update the remote Canvas instance.")
        self._https://canvas.instructure.com/lti/submission_type = value

