"""CustomGradebookColumns API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class CustomGradebookColumnsAPI(BaseCanvasAPI):
    """CustomGradebookColumns API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for CustomGradebookColumnsAPI."""
        super(CustomGradebookColumnsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.CustomGradebookColumnsAPI")

    def list_custom_gradebook_columns(self, course_id, include_hidden=None):
        """
        List custom gradebook columns.

        A paginated list of all custom gradebook columns for a course
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - include_hidden
        """
            Include hidden parameters (defaults to false)
        """
        if include_hidden is not None:
            params["include_hidden"] = include_hidden

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/custom_gradebook_columns with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/custom_gradebook_columns".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def create_custom_gradebook_column(
        self,
        column_title,
        course_id,
        column_hidden=None,
        column_position=None,
        column_read_only=None,
        column_teacher_notes=None,
    ):
        """
        Create a custom gradebook column.

        Create a custom gradebook column
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - column[title]
        """
            no description
        """
        data["column[title]"] = column_title

        # OPTIONAL - column[position]
        """
            The position of the column relative to other custom columns
        """
        if column_position is not None:
            data["column[position]"] = column_position

        # OPTIONAL - column[hidden]
        """
            Hidden columns are not displayed in the gradebook
        """
        if column_hidden is not None:
            data["column[hidden]"] = column_hidden

        # OPTIONAL - column[teacher_notes]
        """
            Set this if the column is created by a teacher.  The gradebook only
        supports one teacher_notes column.
        """
        if column_teacher_notes is not None:
            data["column[teacher_notes]"] = column_teacher_notes

        # OPTIONAL - column[read_only]
        """
            Set this to prevent the column from being editable in the gradebook ui
        """
        if column_read_only is not None:
            data["column[read_only]"] = column_read_only

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/custom_gradebook_columns with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/custom_gradebook_columns".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_custom_gradebook_column(self, course_id, id):
        """
        Update a custom gradebook column.

        Accepts the same parameters as custom gradebook column creation
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

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/custom_gradebook_columns/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_custom_gradebook_column(self, course_id, id):
        """
        Delete a custom gradebook column.

        Permanently deletes a custom column and its associated data
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

        self.logger.debug(
            "DELETE /api/v1/courses/{course_id}/custom_gradebook_columns/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def reorder_custom_columns(self, course_id, order):
        """
        Reorder custom columns.

        Puts the given columns in the specified order

        <b>200 OK</b> is returned if successful
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - order
        """
            no description
        """
        data["order"] = order

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/custom_gradebook_columns/reorder with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/custom_gradebook_columns/reorder".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def list_entries_for_column(self, course_id, id, include_hidden=None):
        """
        List entries for a column.

        This does not list entries for students without associated data.
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

        # OPTIONAL - include_hidden
        """
            If true, hidden columns will be included in the
        result. If false or absent, only visible columns
        will be returned.
        """
        if include_hidden is not None:
            params["include_hidden"] = include_hidden

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data".format(
                **path
            ),
            data=data,
            params=params,
            all_pages=True,
        )

    def update_column_data(self, column_data_content, course_id, id, user_id):
        """
        Update column data.

        Set the content of a custom column
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

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id

        # REQUIRED - column_data[content]
        """
            Column content.  Setting this to blank will delete the datum object.
        """
        data["column_data[content]"] = column_data_content

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/custom_gradebook_columns/{id}/data/{user_id}".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def bulk_update_column_data(self, column_data, course_id):
        """
        Bulk update column data.

        Set the content of custom columns

        {
          "column_data": [
            {
              "column_id": example_column_id,
              "user_id": example_student_id,
              "content": example_content
              },
              {
              "column_id": example_column_id,
              "user_id": example_student_id,
              "content: example_content
            }
          ]
        }
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - column_data
        """
            Column content. Setting this to an empty string will delete the data object.
        """
        data["column_data"] = column_data

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/custom_gradebook_column_data with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/custom_gradebook_column_data".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Customcolumn(BaseModel):
    """Customcolumn Model."""

    def __init__(
        self,
        id=None,
        teacher_notes=None,
        title=None,
        position=None,
        hidden=None,
        read_only=None,
    ):
        """Init method for Customcolumn class."""
        self._id = id
        self._teacher_notes = teacher_notes
        self._title = title
        self._position = position
        self._hidden = hidden
        self._read_only = read_only

        self.logger = logging.getLogger("py3canvas.Customcolumn")

    @property
    def id(self):
        """The ID of the custom gradebook column."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def teacher_notes(self):
        """When true, this column's visibility will be toggled in the Gradebook when a user selects to show or hide notes."""
        return self._teacher_notes

    @teacher_notes.setter
    def teacher_notes(self, value):
        """Setter for teacher_notes property."""
        self.logger.warn(
            "Setting values on teacher_notes will NOT update the remote Canvas instance."
        )
        self._teacher_notes = value

    @property
    def title(self):
        """header text."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn(
            "Setting values on title will NOT update the remote Canvas instance."
        )
        self._title = value

    @property
    def position(self):
        """column order."""
        return self._position

    @position.setter
    def position(self, value):
        """Setter for position property."""
        self.logger.warn(
            "Setting values on position will NOT update the remote Canvas instance."
        )
        self._position = value

    @property
    def hidden(self):
        """won't be displayed if hidden is true."""
        return self._hidden

    @hidden.setter
    def hidden(self, value):
        """Setter for hidden property."""
        self.logger.warn(
            "Setting values on hidden will NOT update the remote Canvas instance."
        )
        self._hidden = value

    @property
    def read_only(self):
        """won't be editable in the gradebook UI."""
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """Setter for read_only property."""
        self.logger.warn(
            "Setting values on read_only will NOT update the remote Canvas instance."
        )
        self._read_only = value


class Columndatum(BaseModel):
    """Columndatum Model.
    ColumnDatum objects contain the entry for a column for each user."""

    def __init__(self, content=None, user_id=None):
        """Init method for Columndatum class."""
        self._content = content
        self._user_id = user_id

        self.logger = logging.getLogger("py3canvas.Columndatum")

    @property
    def content(self):
        """content."""
        return self._content

    @content.setter
    def content(self, value):
        """Setter for content property."""
        self.logger.warn(
            "Setting values on content will NOT update the remote Canvas instance."
        )
        self._content = value

    @property
    def user_id(self):
        """user_id."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn(
            "Setting values on user_id will NOT update the remote Canvas instance."
        )
        self._user_id = value
