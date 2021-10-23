"""ContentMigrations API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class ContentMigrationsAPI(BaseCanvasAPI):
    """ContentMigrations API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for ContentMigrationsAPI."""
        super(ContentMigrationsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.ContentMigrationsAPI")

    def list_migration_issues_accounts(self, account_id, content_migration_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def list_migration_issues_courses(self, content_migration_id, course_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def list_migration_issues_groups(self, content_migration_id, group_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def list_migration_issues_users(self, content_migration_id, user_id):
        """
        List migration issues.

        Returns paginated migration issues
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues".format(**path), data=data, params=params, all_pages=True)

    def get_migration_issue_accounts(self, account_id, content_migration_id, id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_issue_courses(self, content_migration_id, course_id, id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_issue_groups(self, content_migration_id, group_id, id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def get_migration_issue_users(self, content_migration_id, id, user_id):
        """
        Get a migration issue.

        Returns data on an individual migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_accounts(self, account_id, content_migration_id, id, workflow_state):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # REQUIRED - workflow_state
        """
            Set the workflow_state of the issue.
        """
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state


        self.logger.debug("PUT /api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_courses(self, content_migration_id, course_id, id, workflow_state):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # REQUIRED - workflow_state
        """
            Set the workflow_state of the issue.
        """
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state


        self.logger.debug("PUT /api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_groups(self, content_migration_id, group_id, id, workflow_state):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # REQUIRED - workflow_state
        """
            Set the workflow_state of the issue.
        """
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state


        self.logger.debug("PUT /api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def update_migration_issue_users(self, content_migration_id, id, user_id, workflow_state):
        """
        Update a migration issue.

        Update the workflow_state of a migration issue
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - content_migration_id
        """
            ID
        """
        path["content_migration_id"] = content_migration_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # REQUIRED - workflow_state
        """
            Set the workflow_state of the issue.
        """
        self._validate_enum(workflow_state, ["active", "resolved"])
        data["workflow_state"] = workflow_state


        self.logger.debug("PUT /api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/content_migrations/{content_migration_id}/migration_issues/{id}".format(**path), data=data, params=params, single_item=True)

    def list_content_migrations_accounts(self, account_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def list_content_migrations_courses(self, course_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def list_content_migrations_groups(self, group_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def list_content_migrations_users(self, user_id):
        """
        List content migrations.

        Returns paginated content migrations
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations".format(**path), data=data, params=params, all_pages=True)

    def get_content_migration_accounts(self, account_id, id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_content_migration_courses(self, course_id, id):
        """
        Get a content migration.

        Returns data on an individual content migration
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


        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_content_migration_groups(self, group_id, id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def get_content_migration_users(self, id, user_id):
        """
        Get a content migration.

        Returns data on an individual content migration
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_accounts(self, account_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, select=None, selective_import=None, settings_content_export_id=None, settings_file_url=None, settings_folder_id=None, settings_insert_into_module_id=None, settings_insert_into_module_position=None, settings_insert_into_module_type=None, settings_move_to_assignment_group_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - migration_type
        """
            The type of the migration. Use the
        {api:ContentMigrationsController#available_migrators Migrator} endpoint to
        see all available migrators. Default allowed values:
        canvas_cartridge_importer, common_cartridge_importer,
        course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        """
        data["migration_type"] = migration_type


        # OPTIONAL - pre_attachment[name]
        """
            Required if uploading a file. This is the first step in uploading a file
        to the content migration. See the {file:file_uploads.html File Upload
        Documentation} for details on the file upload workflow.
        """
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name


        # OPTIONAL - pre_attachment[*]
        """
            Other file upload properties, See {file:file_uploads.html File Upload
        Documentation}
        """
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*


        # OPTIONAL - settings[file_url]
        """
            A URL to download the file from. Must not require authentication.
        """
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url


        # OPTIONAL - settings[content_export_id]
        """
            The id of a ContentExport to import. This allows you to import content previously exported from Canvas
        without needing to download and re-upload it.
        """
        if settings_content_export_id is not None:
            data["settings[content_export_id]"] = settings_content_export_id


        # OPTIONAL - settings[source_course_id]
        """
            The course to copy from for a course copy migration. (required if doing
        course copy)
        """
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id


        # OPTIONAL - settings[folder_id]
        """
            The folder to unzip the .zip file into for a zip_file_import.
        """
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id


        # OPTIONAL - settings[overwrite_quizzes]
        """
            Whether to overwrite quizzes with the same identifiers between content
        packages.
        """
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes


        # OPTIONAL - settings[question_bank_id]
        """
            The existing question bank ID to import questions into if not specified in
        the content package.
        """
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id


        # OPTIONAL - settings[question_bank_name]
        """
            The question bank to import questions into if not specified in the content
        package, if both bank id and name are set, id will take precedence.
        """
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name


        # OPTIONAL - settings[insert_into_module_id]
        """
            The id of a module in the target course. This will add all imported items
        (that can be added to a module) to the given module.
        """
        if settings_insert_into_module_id is not None:
            data["settings[insert_into_module_id]"] = settings_insert_into_module_id


        # OPTIONAL - settings[insert_into_module_type]
        """
            If provided (and +insert_into_module_id+ is supplied),
        only add objects of the specified type to the module.
        """
        if settings_insert_into_module_type is not None:
            self._validate_enum(settings_insert_into_module_type, ["assignment", "discussion_topic", "file", "page", "quiz"])
            data["settings[insert_into_module_type]"] = settings_insert_into_module_type


        # OPTIONAL - settings[insert_into_module_position]
        """
            The (1-based) position to insert the imported items into the course
        (if +insert_into_module_id+ is supplied). If this parameter
        is omitted, items will be added to the end of the module.
        """
        if settings_insert_into_module_position is not None:
            data["settings[insert_into_module_position]"] = settings_insert_into_module_position


        # OPTIONAL - settings[move_to_assignment_group_id]
        """
            The id of an assignment group in the target course. If provided, all
        imported assignments will be moved to the given assignment group.
        """
        if settings_move_to_assignment_group_id is not None:
            data["settings[move_to_assignment_group_id]"] = settings_move_to_assignment_group_id


        # OPTIONAL - date_shift_options[shift_dates]
        """
            Whether to shift dates in the copied course
        """
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates


        # OPTIONAL - date_shift_options[old_start_date]
        """
            The original start date of the source content/course
        """
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date


        # OPTIONAL - date_shift_options[old_end_date]
        """
            The original end date of the source content/course
        """
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date


        # OPTIONAL - date_shift_options[new_start_date]
        """
            The new start date for the content/course
        """
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date


        # OPTIONAL - date_shift_options[new_end_date]
        """
            The new end date for the source content/course
        """
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date


        # OPTIONAL - date_shift_options[day_substitutions][X]
        """
            Move anything scheduled for day 'X' to the specified day. (0-Sunday,
        1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        """
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X


        # OPTIONAL - date_shift_options[remove_dates]
        """
            Whether to remove dates in the copied course. Cannot be used
        in conjunction with *shift_dates*.
        """
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates


        # OPTIONAL - selective_import
        """
            If set, perform a selective import instead of importing all content.
        The migration will identify the contents of the package and then stop
        in the +waiting_for_select+ workflow state. At this point, use the
        {api:ContentMigrationsController#content_list List items endpoint}
        to enumerate the contents of the package, identifying the copy
        parameters for the desired content. Then call the
        {api:ContentMigrationsController#update Update endpoint} and provide these
        copy parameters to start the import.
        """
        if selective_import is not None:
            data["selective_import"] = selective_import


        # OPTIONAL - select
        """
            For +course_copy_importer+ migrations, this parameter allows you to select
        the objects to copy without using the +selective_import+ argument and
        +waiting_for_select+ state as is required for uploaded imports (though that
        workflow is also supported for course copy migrations).
        The keys are object types like 'files', 'folders', 'pages', etc. The value
        for each key is a list of object ids. An id can be an integer or a string.
        Multiple object types can be selected in the same call.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/accounts/{account_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/accounts/{account_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_courses(self, course_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, select=None, selective_import=None, settings_content_export_id=None, settings_file_url=None, settings_folder_id=None, settings_insert_into_module_id=None, settings_insert_into_module_position=None, settings_insert_into_module_type=None, settings_move_to_assignment_group_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        # REQUIRED - migration_type
        """
            The type of the migration. Use the
        {api:ContentMigrationsController#available_migrators Migrator} endpoint to
        see all available migrators. Default allowed values:
        canvas_cartridge_importer, common_cartridge_importer,
        course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        """
        data["migration_type"] = migration_type


        # OPTIONAL - pre_attachment[name]
        """
            Required if uploading a file. This is the first step in uploading a file
        to the content migration. See the {file:file_uploads.html File Upload
        Documentation} for details on the file upload workflow.
        """
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name


        # OPTIONAL - pre_attachment[*]
        """
            Other file upload properties, See {file:file_uploads.html File Upload
        Documentation}
        """
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*


        # OPTIONAL - settings[file_url]
        """
            A URL to download the file from. Must not require authentication.
        """
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url


        # OPTIONAL - settings[content_export_id]
        """
            The id of a ContentExport to import. This allows you to import content previously exported from Canvas
        without needing to download and re-upload it.
        """
        if settings_content_export_id is not None:
            data["settings[content_export_id]"] = settings_content_export_id


        # OPTIONAL - settings[source_course_id]
        """
            The course to copy from for a course copy migration. (required if doing
        course copy)
        """
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id


        # OPTIONAL - settings[folder_id]
        """
            The folder to unzip the .zip file into for a zip_file_import.
        """
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id


        # OPTIONAL - settings[overwrite_quizzes]
        """
            Whether to overwrite quizzes with the same identifiers between content
        packages.
        """
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes


        # OPTIONAL - settings[question_bank_id]
        """
            The existing question bank ID to import questions into if not specified in
        the content package.
        """
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id


        # OPTIONAL - settings[question_bank_name]
        """
            The question bank to import questions into if not specified in the content
        package, if both bank id and name are set, id will take precedence.
        """
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name


        # OPTIONAL - settings[insert_into_module_id]
        """
            The id of a module in the target course. This will add all imported items
        (that can be added to a module) to the given module.
        """
        if settings_insert_into_module_id is not None:
            data["settings[insert_into_module_id]"] = settings_insert_into_module_id


        # OPTIONAL - settings[insert_into_module_type]
        """
            If provided (and +insert_into_module_id+ is supplied),
        only add objects of the specified type to the module.
        """
        if settings_insert_into_module_type is not None:
            self._validate_enum(settings_insert_into_module_type, ["assignment", "discussion_topic", "file", "page", "quiz"])
            data["settings[insert_into_module_type]"] = settings_insert_into_module_type


        # OPTIONAL - settings[insert_into_module_position]
        """
            The (1-based) position to insert the imported items into the course
        (if +insert_into_module_id+ is supplied). If this parameter
        is omitted, items will be added to the end of the module.
        """
        if settings_insert_into_module_position is not None:
            data["settings[insert_into_module_position]"] = settings_insert_into_module_position


        # OPTIONAL - settings[move_to_assignment_group_id]
        """
            The id of an assignment group in the target course. If provided, all
        imported assignments will be moved to the given assignment group.
        """
        if settings_move_to_assignment_group_id is not None:
            data["settings[move_to_assignment_group_id]"] = settings_move_to_assignment_group_id


        # OPTIONAL - date_shift_options[shift_dates]
        """
            Whether to shift dates in the copied course
        """
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates


        # OPTIONAL - date_shift_options[old_start_date]
        """
            The original start date of the source content/course
        """
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date


        # OPTIONAL - date_shift_options[old_end_date]
        """
            The original end date of the source content/course
        """
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date


        # OPTIONAL - date_shift_options[new_start_date]
        """
            The new start date for the content/course
        """
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date


        # OPTIONAL - date_shift_options[new_end_date]
        """
            The new end date for the source content/course
        """
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date


        # OPTIONAL - date_shift_options[day_substitutions][X]
        """
            Move anything scheduled for day 'X' to the specified day. (0-Sunday,
        1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        """
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X


        # OPTIONAL - date_shift_options[remove_dates]
        """
            Whether to remove dates in the copied course. Cannot be used
        in conjunction with *shift_dates*.
        """
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates


        # OPTIONAL - selective_import
        """
            If set, perform a selective import instead of importing all content.
        The migration will identify the contents of the package and then stop
        in the +waiting_for_select+ workflow state. At this point, use the
        {api:ContentMigrationsController#content_list List items endpoint}
        to enumerate the contents of the package, identifying the copy
        parameters for the desired content. Then call the
        {api:ContentMigrationsController#update Update endpoint} and provide these
        copy parameters to start the import.
        """
        if selective_import is not None:
            data["selective_import"] = selective_import


        # OPTIONAL - select
        """
            For +course_copy_importer+ migrations, this parameter allows you to select
        the objects to copy without using the +selective_import+ argument and
        +waiting_for_select+ state as is required for uploaded imports (though that
        workflow is also supported for course copy migrations).
        The keys are object types like 'files', 'folders', 'pages', etc. The value
        for each key is a list of object ids. An id can be an integer or a string.
        Multiple object types can be selected in the same call.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/courses/{course_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/courses/{course_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_groups(self, group_id, migration_type, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, select=None, selective_import=None, settings_content_export_id=None, settings_file_url=None, settings_folder_id=None, settings_insert_into_module_id=None, settings_insert_into_module_position=None, settings_insert_into_module_type=None, settings_move_to_assignment_group_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - migration_type
        """
            The type of the migration. Use the
        {api:ContentMigrationsController#available_migrators Migrator} endpoint to
        see all available migrators. Default allowed values:
        canvas_cartridge_importer, common_cartridge_importer,
        course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        """
        data["migration_type"] = migration_type


        # OPTIONAL - pre_attachment[name]
        """
            Required if uploading a file. This is the first step in uploading a file
        to the content migration. See the {file:file_uploads.html File Upload
        Documentation} for details on the file upload workflow.
        """
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name


        # OPTIONAL - pre_attachment[*]
        """
            Other file upload properties, See {file:file_uploads.html File Upload
        Documentation}
        """
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*


        # OPTIONAL - settings[file_url]
        """
            A URL to download the file from. Must not require authentication.
        """
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url


        # OPTIONAL - settings[content_export_id]
        """
            The id of a ContentExport to import. This allows you to import content previously exported from Canvas
        without needing to download and re-upload it.
        """
        if settings_content_export_id is not None:
            data["settings[content_export_id]"] = settings_content_export_id


        # OPTIONAL - settings[source_course_id]
        """
            The course to copy from for a course copy migration. (required if doing
        course copy)
        """
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id


        # OPTIONAL - settings[folder_id]
        """
            The folder to unzip the .zip file into for a zip_file_import.
        """
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id


        # OPTIONAL - settings[overwrite_quizzes]
        """
            Whether to overwrite quizzes with the same identifiers between content
        packages.
        """
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes


        # OPTIONAL - settings[question_bank_id]
        """
            The existing question bank ID to import questions into if not specified in
        the content package.
        """
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id


        # OPTIONAL - settings[question_bank_name]
        """
            The question bank to import questions into if not specified in the content
        package, if both bank id and name are set, id will take precedence.
        """
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name


        # OPTIONAL - settings[insert_into_module_id]
        """
            The id of a module in the target course. This will add all imported items
        (that can be added to a module) to the given module.
        """
        if settings_insert_into_module_id is not None:
            data["settings[insert_into_module_id]"] = settings_insert_into_module_id


        # OPTIONAL - settings[insert_into_module_type]
        """
            If provided (and +insert_into_module_id+ is supplied),
        only add objects of the specified type to the module.
        """
        if settings_insert_into_module_type is not None:
            self._validate_enum(settings_insert_into_module_type, ["assignment", "discussion_topic", "file", "page", "quiz"])
            data["settings[insert_into_module_type]"] = settings_insert_into_module_type


        # OPTIONAL - settings[insert_into_module_position]
        """
            The (1-based) position to insert the imported items into the course
        (if +insert_into_module_id+ is supplied). If this parameter
        is omitted, items will be added to the end of the module.
        """
        if settings_insert_into_module_position is not None:
            data["settings[insert_into_module_position]"] = settings_insert_into_module_position


        # OPTIONAL - settings[move_to_assignment_group_id]
        """
            The id of an assignment group in the target course. If provided, all
        imported assignments will be moved to the given assignment group.
        """
        if settings_move_to_assignment_group_id is not None:
            data["settings[move_to_assignment_group_id]"] = settings_move_to_assignment_group_id


        # OPTIONAL - date_shift_options[shift_dates]
        """
            Whether to shift dates in the copied course
        """
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates


        # OPTIONAL - date_shift_options[old_start_date]
        """
            The original start date of the source content/course
        """
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date


        # OPTIONAL - date_shift_options[old_end_date]
        """
            The original end date of the source content/course
        """
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date


        # OPTIONAL - date_shift_options[new_start_date]
        """
            The new start date for the content/course
        """
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date


        # OPTIONAL - date_shift_options[new_end_date]
        """
            The new end date for the source content/course
        """
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date


        # OPTIONAL - date_shift_options[day_substitutions][X]
        """
            Move anything scheduled for day 'X' to the specified day. (0-Sunday,
        1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        """
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X


        # OPTIONAL - date_shift_options[remove_dates]
        """
            Whether to remove dates in the copied course. Cannot be used
        in conjunction with *shift_dates*.
        """
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates


        # OPTIONAL - selective_import
        """
            If set, perform a selective import instead of importing all content.
        The migration will identify the contents of the package and then stop
        in the +waiting_for_select+ workflow state. At this point, use the
        {api:ContentMigrationsController#content_list List items endpoint}
        to enumerate the contents of the package, identifying the copy
        parameters for the desired content. Then call the
        {api:ContentMigrationsController#update Update endpoint} and provide these
        copy parameters to start the import.
        """
        if selective_import is not None:
            data["selective_import"] = selective_import


        # OPTIONAL - select
        """
            For +course_copy_importer+ migrations, this parameter allows you to select
        the objects to copy without using the +selective_import+ argument and
        +waiting_for_select+ state as is required for uploaded imports (though that
        workflow is also supported for course copy migrations).
        The keys are object types like 'files', 'folders', 'pages', etc. The value
        for each key is a list of object ids. An id can be an integer or a string.
        Multiple object types can be selected in the same call.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/groups/{group_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/groups/{group_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def create_content_migration_users(self, migration_type, user_id, date_shift_options_day_substitutions_X=None, date_shift_options_new_end_date=None, date_shift_options_new_start_date=None, date_shift_options_old_end_date=None, date_shift_options_old_start_date=None, date_shift_options_remove_dates=None, date_shift_options_shift_dates=None, pre_attachment_*=None, pre_attachment_name=None, select=None, selective_import=None, settings_content_export_id=None, settings_file_url=None, settings_folder_id=None, settings_insert_into_module_id=None, settings_insert_into_module_position=None, settings_insert_into_module_type=None, settings_move_to_assignment_group_id=None, settings_overwrite_quizzes=None, settings_question_bank_id=None, settings_question_bank_name=None, settings_source_course_id=None):
        """
        Create a content migration.

        Create a content migration. If the migration requires a file to be uploaded
        the actual processing of the file will start once the file upload process is completed.
        File uploading works as described in the {file:file_uploads.html File Upload Documentation}
        except that the values are set on a *pre_attachment* sub-hash.
        
        For migrations that don't require a file to be uploaded, like course copy, the
        processing will begin as soon as the migration is created.
        
        You can use the {api:ProgressController#show Progress API} to track the
        progress of the migration. The migration's progress is linked to with the
        _progress_url_ value.
        
        The two general workflows are:
        
        If no file upload is needed:
        
        1. POST to create
        2. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
        For file uploading:
        
        1. POST to create with file info in *pre_attachment*
        2. Do {file:file_uploads.html file upload processing} using the data in the *pre_attachment* data
        3. {api:ContentMigrationsController#show GET} the ContentMigration
        4. Use the {api:ProgressController#show Progress} specified in _progress_url_ to monitor progress
        
         (required if doing .zip file upload)
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - migration_type
        """
            The type of the migration. Use the
        {api:ContentMigrationsController#available_migrators Migrator} endpoint to
        see all available migrators. Default allowed values:
        canvas_cartridge_importer, common_cartridge_importer,
        course_copy_importer, zip_file_importer, qti_converter, moodle_converter
        """
        data["migration_type"] = migration_type


        # OPTIONAL - pre_attachment[name]
        """
            Required if uploading a file. This is the first step in uploading a file
        to the content migration. See the {file:file_uploads.html File Upload
        Documentation} for details on the file upload workflow.
        """
        if pre_attachment_name is not None:
            data["pre_attachment[name]"] = pre_attachment_name


        # OPTIONAL - pre_attachment[*]
        """
            Other file upload properties, See {file:file_uploads.html File Upload
        Documentation}
        """
        if pre_attachment_* is not None:
            data["pre_attachment[*]"] = pre_attachment_*


        # OPTIONAL - settings[file_url]
        """
            A URL to download the file from. Must not require authentication.
        """
        if settings_file_url is not None:
            data["settings[file_url]"] = settings_file_url


        # OPTIONAL - settings[content_export_id]
        """
            The id of a ContentExport to import. This allows you to import content previously exported from Canvas
        without needing to download and re-upload it.
        """
        if settings_content_export_id is not None:
            data["settings[content_export_id]"] = settings_content_export_id


        # OPTIONAL - settings[source_course_id]
        """
            The course to copy from for a course copy migration. (required if doing
        course copy)
        """
        if settings_source_course_id is not None:
            data["settings[source_course_id]"] = settings_source_course_id


        # OPTIONAL - settings[folder_id]
        """
            The folder to unzip the .zip file into for a zip_file_import.
        """
        if settings_folder_id is not None:
            data["settings[folder_id]"] = settings_folder_id


        # OPTIONAL - settings[overwrite_quizzes]
        """
            Whether to overwrite quizzes with the same identifiers between content
        packages.
        """
        if settings_overwrite_quizzes is not None:
            data["settings[overwrite_quizzes]"] = settings_overwrite_quizzes


        # OPTIONAL - settings[question_bank_id]
        """
            The existing question bank ID to import questions into if not specified in
        the content package.
        """
        if settings_question_bank_id is not None:
            data["settings[question_bank_id]"] = settings_question_bank_id


        # OPTIONAL - settings[question_bank_name]
        """
            The question bank to import questions into if not specified in the content
        package, if both bank id and name are set, id will take precedence.
        """
        if settings_question_bank_name is not None:
            data["settings[question_bank_name]"] = settings_question_bank_name


        # OPTIONAL - settings[insert_into_module_id]
        """
            The id of a module in the target course. This will add all imported items
        (that can be added to a module) to the given module.
        """
        if settings_insert_into_module_id is not None:
            data["settings[insert_into_module_id]"] = settings_insert_into_module_id


        # OPTIONAL - settings[insert_into_module_type]
        """
            If provided (and +insert_into_module_id+ is supplied),
        only add objects of the specified type to the module.
        """
        if settings_insert_into_module_type is not None:
            self._validate_enum(settings_insert_into_module_type, ["assignment", "discussion_topic", "file", "page", "quiz"])
            data["settings[insert_into_module_type]"] = settings_insert_into_module_type


        # OPTIONAL - settings[insert_into_module_position]
        """
            The (1-based) position to insert the imported items into the course
        (if +insert_into_module_id+ is supplied). If this parameter
        is omitted, items will be added to the end of the module.
        """
        if settings_insert_into_module_position is not None:
            data["settings[insert_into_module_position]"] = settings_insert_into_module_position


        # OPTIONAL - settings[move_to_assignment_group_id]
        """
            The id of an assignment group in the target course. If provided, all
        imported assignments will be moved to the given assignment group.
        """
        if settings_move_to_assignment_group_id is not None:
            data["settings[move_to_assignment_group_id]"] = settings_move_to_assignment_group_id


        # OPTIONAL - date_shift_options[shift_dates]
        """
            Whether to shift dates in the copied course
        """
        if date_shift_options_shift_dates is not None:
            data["date_shift_options[shift_dates]"] = date_shift_options_shift_dates


        # OPTIONAL - date_shift_options[old_start_date]
        """
            The original start date of the source content/course
        """
        if date_shift_options_old_start_date is not None:
            data["date_shift_options[old_start_date]"] = date_shift_options_old_start_date


        # OPTIONAL - date_shift_options[old_end_date]
        """
            The original end date of the source content/course
        """
        if date_shift_options_old_end_date is not None:
            data["date_shift_options[old_end_date]"] = date_shift_options_old_end_date


        # OPTIONAL - date_shift_options[new_start_date]
        """
            The new start date for the content/course
        """
        if date_shift_options_new_start_date is not None:
            data["date_shift_options[new_start_date]"] = date_shift_options_new_start_date


        # OPTIONAL - date_shift_options[new_end_date]
        """
            The new end date for the source content/course
        """
        if date_shift_options_new_end_date is not None:
            data["date_shift_options[new_end_date]"] = date_shift_options_new_end_date


        # OPTIONAL - date_shift_options[day_substitutions][X]
        """
            Move anything scheduled for day 'X' to the specified day. (0-Sunday,
        1-Monday, 2-Tuesday, 3-Wednesday, 4-Thursday, 5-Friday, 6-Saturday)
        """
        if date_shift_options_day_substitutions_X is not None:
            data["date_shift_options[day_substitutions][X]"] = date_shift_options_day_substitutions_X


        # OPTIONAL - date_shift_options[remove_dates]
        """
            Whether to remove dates in the copied course. Cannot be used
        in conjunction with *shift_dates*.
        """
        if date_shift_options_remove_dates is not None:
            data["date_shift_options[remove_dates]"] = date_shift_options_remove_dates


        # OPTIONAL - selective_import
        """
            If set, perform a selective import instead of importing all content.
        The migration will identify the contents of the package and then stop
        in the +waiting_for_select+ workflow state. At this point, use the
        {api:ContentMigrationsController#content_list List items endpoint}
        to enumerate the contents of the package, identifying the copy
        parameters for the desired content. Then call the
        {api:ContentMigrationsController#update Update endpoint} and provide these
        copy parameters to start the import.
        """
        if selective_import is not None:
            data["selective_import"] = selective_import


        # OPTIONAL - select
        """
            For +course_copy_importer+ migrations, this parameter allows you to select
        the objects to copy without using the +selective_import+ argument and
        +waiting_for_select+ state as is required for uploaded imports (though that
        workflow is also supported for course copy migrations).
        The keys are object types like 'files', 'folders', 'pages', etc. The value
        for each key is a list of object ids. An id can be an integer or a string.
        Multiple object types can be selected in the same call.
        """
        if select is not None:
            self._validate_enum(select, ["folders", "files", "attachments", "quizzes", "assignments", "announcements", "calendar_events", "discussion_topics", "modules", "module_items", "pages", "rubrics"])
            data["select"] = select


        self.logger.debug("POST /api/v1/users/{user_id}/content_migrations with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/v1/users/{user_id}/content_migrations".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_accounts(self, account_id, id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem, or when
        importing content selectively. If the first upload has a problem you can
        supply new _pre_attachment_ values to start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("PUT /api/v1/accounts/{account_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/accounts/{account_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_courses(self, course_id, id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem, or when
        importing content selectively. If the first upload has a problem you can
        supply new _pre_attachment_ values to start the process again.
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


        self.logger.debug("PUT /api/v1/courses/{course_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/courses/{course_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_groups(self, group_id, id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem, or when
        importing content selectively. If the first upload has a problem you can
        supply new _pre_attachment_ values to start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("PUT /api/v1/groups/{group_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/groups/{group_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def update_content_migration_users(self, id, user_id):
        """
        Update a content migration.

        Update a content migration. Takes same arguments as {api:ContentMigrationsController#create create} except that you
        can't change the migration type. However, changing most settings after the
        migration process has started will not do anything. Generally updating the
        content migration will be used when there is a file upload problem, or when
        importing content selectively. If the first upload has a problem you can
        supply new _pre_attachment_ values to start the process again.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("PUT /api/v1/users/{user_id}/content_migrations/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/v1/users/{user_id}/content_migrations/{id}".format(**path), data=data, params=params, single_item=True)

    def list_migration_systems_accounts(self, account_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_migration_systems_courses(self, course_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id


        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_migration_systems_groups(self, group_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_migration_systems_users(self, user_id):
        """
        List Migration Systems.

        Lists the currently available migration types. These values may change.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/migrators with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/migrators".format(**path), data=data, params=params, all_pages=True)

    def list_items_for_selective_import_accounts(self, account_id, id, type=None):
        """
        List items for selective import.

        Enumerates the content available for selective import in a tree structure. Each node provides
        a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
        to selectively copy the content associated with that tree node and its children. Each node may also
        provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
        for a subset of the resources in a given node.
        
        If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:
        
          [{
            "type": "course_settings",
            "property": "copy[all_course_settings]",
            "title": "Course Settings"
          },
          {
            "type": "context_modules",
            "property": "copy[all_context_modules]",
            "title": "Modules",
            "count": 5,
            "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
          },
          {
            "type": "assignments",
            "property": "copy[all_assignments]",
            "title": "Assignments",
            "count": 2,
            "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
          }]
        
        When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
        results in a node for each assignment group and a sub_item for each assignment, like this:
        
          [{
            "type": "assignment_groups",
            "title": "An Assignment Group",
            "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
            "sub_items": [{
                "type": "assignments",
                "title": "Assignment 1",
                "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
            }, {
                "type": "assignments",
                "title": "Assignment 2",
                "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
            }]
          }]
        
        
        To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
        {api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:
        
          copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1
        
        You can include multiple copy parameters to selectively import multiple items or groups of items.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - type
        """
            The type of content to enumerate.
        """
        if type is not None:
            self._validate_enum(type, ["context_modules", "assignments", "quizzes", "assessment_question_banks", "discussion_topics", "wiki_pages", "context_external_tools", "tool_profiles", "announcements", "calendar_events", "rubrics", "groups", "learning_outcomes", "attachments"])
            params["type"] = type


        self.logger.debug("GET /api/v1/accounts/{account_id}/content_migrations/{id}/selective_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/accounts/{account_id}/content_migrations/{id}/selective_data".format(**path), data=data, params=params)

    def list_items_for_selective_import_courses(self, course_id, id, type=None):
        """
        List items for selective import.

        Enumerates the content available for selective import in a tree structure. Each node provides
        a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
        to selectively copy the content associated with that tree node and its children. Each node may also
        provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
        for a subset of the resources in a given node.
        
        If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:
        
          [{
            "type": "course_settings",
            "property": "copy[all_course_settings]",
            "title": "Course Settings"
          },
          {
            "type": "context_modules",
            "property": "copy[all_context_modules]",
            "title": "Modules",
            "count": 5,
            "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
          },
          {
            "type": "assignments",
            "property": "copy[all_assignments]",
            "title": "Assignments",
            "count": 2,
            "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
          }]
        
        When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
        results in a node for each assignment group and a sub_item for each assignment, like this:
        
          [{
            "type": "assignment_groups",
            "title": "An Assignment Group",
            "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
            "sub_items": [{
                "type": "assignments",
                "title": "Assignment 1",
                "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
            }, {
                "type": "assignments",
                "title": "Assignment 2",
                "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
            }]
          }]
        
        
        To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
        {api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:
        
          copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1
        
        You can include multiple copy parameters to selectively import multiple items or groups of items.
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


        # OPTIONAL - type
        """
            The type of content to enumerate.
        """
        if type is not None:
            self._validate_enum(type, ["context_modules", "assignments", "quizzes", "assessment_question_banks", "discussion_topics", "wiki_pages", "context_external_tools", "tool_profiles", "announcements", "calendar_events", "rubrics", "groups", "learning_outcomes", "attachments"])
            params["type"] = type


        self.logger.debug("GET /api/v1/courses/{course_id}/content_migrations/{id}/selective_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/courses/{course_id}/content_migrations/{id}/selective_data".format(**path), data=data, params=params)

    def list_items_for_selective_import_groups(self, group_id, id, type=None):
        """
        List items for selective import.

        Enumerates the content available for selective import in a tree structure. Each node provides
        a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
        to selectively copy the content associated with that tree node and its children. Each node may also
        provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
        for a subset of the resources in a given node.
        
        If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:
        
          [{
            "type": "course_settings",
            "property": "copy[all_course_settings]",
            "title": "Course Settings"
          },
          {
            "type": "context_modules",
            "property": "copy[all_context_modules]",
            "title": "Modules",
            "count": 5,
            "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
          },
          {
            "type": "assignments",
            "property": "copy[all_assignments]",
            "title": "Assignments",
            "count": 2,
            "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
          }]
        
        When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
        results in a node for each assignment group and a sub_item for each assignment, like this:
        
          [{
            "type": "assignment_groups",
            "title": "An Assignment Group",
            "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
            "sub_items": [{
                "type": "assignments",
                "title": "Assignment 1",
                "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
            }, {
                "type": "assignments",
                "title": "Assignment 2",
                "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
            }]
          }]
        
        
        To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
        {api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:
        
          copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1
        
        You can include multiple copy parameters to selectively import multiple items or groups of items.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - group_id
        """
            ID
        """
        path["group_id"] = group_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - type
        """
            The type of content to enumerate.
        """
        if type is not None:
            self._validate_enum(type, ["context_modules", "assignments", "quizzes", "assessment_question_banks", "discussion_topics", "wiki_pages", "context_external_tools", "tool_profiles", "announcements", "calendar_events", "rubrics", "groups", "learning_outcomes", "attachments"])
            params["type"] = type


        self.logger.debug("GET /api/v1/groups/{group_id}/content_migrations/{id}/selective_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/groups/{group_id}/content_migrations/{id}/selective_data".format(**path), data=data, params=params)

    def list_items_for_selective_import_users(self, id, user_id, type=None):
        """
        List items for selective import.

        Enumerates the content available for selective import in a tree structure. Each node provides
        a +property+ copy argument that can be supplied to the {api:ContentMigrationsController#update Update endpoint}
        to selectively copy the content associated with that tree node and its children. Each node may also
        provide a +sub_items_url+ or an array of +sub_items+ which you can use to obtain copy parameters
        for a subset of the resources in a given node.
        
        If no +type+ is sent you will get a list of the top-level sections in the content. It will look something like this:
        
          [{
            "type": "course_settings",
            "property": "copy[all_course_settings]",
            "title": "Course Settings"
          },
          {
            "type": "context_modules",
            "property": "copy[all_context_modules]",
            "title": "Modules",
            "count": 5,
            "sub_items_url": "http://example.com/api/v1/courses/22/content_migrations/77/selective_data?type=context_modules"
          },
          {
            "type": "assignments",
            "property": "copy[all_assignments]",
            "title": "Assignments",
            "count": 2,
            "sub_items_url": "http://localhost:3000/api/v1/courses/22/content_migrations/77/selective_data?type=assignments"
          }]
        
        When a +type+ is provided, nodes may be further divided via +sub_items+. For example, using +type=assignments+
        results in a node for each assignment group and a sub_item for each assignment, like this:
        
          [{
            "type": "assignment_groups",
            "title": "An Assignment Group",
            "property": "copy[assignment_groups][id_i855cf145e5acc7435e1bf1c6e2126e5f]",
            "sub_items": [{
                "type": "assignments",
                "title": "Assignment 1",
                "property": "copy[assignments][id_i2102a7fa93b29226774949298626719d]"
            }, {
                "type": "assignments",
                "title": "Assignment 2",
                "property": "copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]"
            }]
          }]
        
        
        To import the items corresponding to a particular tree node, use the +property+ as a parameter to the
        {api:ContentMigrationsController#update Update endpoint} and assign a value of 1, for example:
        
          copy[assignments][id_i310cba275dc3f4aa8a3306bbbe380979]=1
        
        You can include multiple copy parameters to selectively import multiple items or groups of items.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - user_id
        """
            ID
        """
        path["user_id"] = user_id


        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        # OPTIONAL - type
        """
            The type of content to enumerate.
        """
        if type is not None:
            self._validate_enum(type, ["context_modules", "assignments", "quizzes", "assessment_question_banks", "discussion_topics", "wiki_pages", "context_external_tools", "tool_profiles", "announcements", "calendar_events", "rubrics", "groups", "learning_outcomes", "attachments"])
            params["type"] = type


        self.logger.debug("GET /api/v1/users/{user_id}/content_migrations/{id}/selective_data with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/v1/users/{user_id}/content_migrations/{id}/selective_data".format(**path), data=data, params=params)


class Migrationissue(BaseModel):
    """Migrationissue Model."""

    def __init__(self, id=None, content_migration_url=None, description=None, workflow_state=None, fix_issue_html_url=None, issue_type=None, error_report_html_url=None, error_message=None, created_at=None, updated_at=None):
        """Init method for Migrationissue class."""
        self._id = id
        self._content_migration_url = content_migration_url
        self._description = description
        self._workflow_state = workflow_state
        self._fix_issue_html_url = fix_issue_html_url
        self._issue_type = issue_type
        self._error_report_html_url = error_report_html_url
        self._error_message = error_message
        self._created_at = created_at
        self._updated_at = updated_at

        self.logger = logging.getLogger('py3canvas.Migrationissue')

    @property
    def id(self):
        """the unique identifier for the issue."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def content_migration_url(self):
        """API url to the content migration."""
        return self._content_migration_url

    @content_migration_url.setter
    def content_migration_url(self, value):
        """Setter for content_migration_url property."""
        self.logger.warn("Setting values on content_migration_url will NOT update the remote Canvas instance.")
        self._content_migration_url = value

    @property
    def description(self):
        """Description of the issue for the end-user."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn("Setting values on description will NOT update the remote Canvas instance.")
        self._description = value

    @property
    def workflow_state(self):
        """Current state of the issue: active, resolved."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def fix_issue_html_url(self):
        """HTML Url to the Canvas page to investigate the issue."""
        return self._fix_issue_html_url

    @fix_issue_html_url.setter
    def fix_issue_html_url(self, value):
        """Setter for fix_issue_html_url property."""
        self.logger.warn("Setting values on fix_issue_html_url will NOT update the remote Canvas instance.")
        self._fix_issue_html_url = value

    @property
    def issue_type(self):
        """Severity of the issue: todo, warning, error."""
        return self._issue_type

    @issue_type.setter
    def issue_type(self, value):
        """Setter for issue_type property."""
        self.logger.warn("Setting values on issue_type will NOT update the remote Canvas instance.")
        self._issue_type = value

    @property
    def error_report_html_url(self):
        """Link to a Canvas error report if present (If the requesting user has permissions)."""
        return self._error_report_html_url

    @error_report_html_url.setter
    def error_report_html_url(self, value):
        """Setter for error_report_html_url property."""
        self.logger.warn("Setting values on error_report_html_url will NOT update the remote Canvas instance.")
        self._error_report_html_url = value

    @property
    def error_message(self):
        """Site administrator error message (If the requesting user has permissions)."""
        return self._error_message

    @error_message.setter
    def error_message(self, value):
        """Setter for error_message property."""
        self.logger.warn("Setting values on error_message will NOT update the remote Canvas instance.")
        self._error_message = value

    @property
    def created_at(self):
        """timestamp."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn("Setting values on created_at will NOT update the remote Canvas instance.")
        self._created_at = value

    @property
    def updated_at(self):
        """timestamp."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn("Setting values on updated_at will NOT update the remote Canvas instance.")
        self._updated_at = value


class Contentmigration(BaseModel):
    """Contentmigration Model."""

    def __init__(self, id=None, migration_type=None, migration_type_title=None, migration_issues_url=None, attachment=None, progress_url=None, user_id=None, workflow_state=None, started_at=None, finished_at=None, pre_attachment=None):
        """Init method for Contentmigration class."""
        self._id = id
        self._migration_type = migration_type
        self._migration_type_title = migration_type_title
        self._migration_issues_url = migration_issues_url
        self._attachment = attachment
        self._progress_url = progress_url
        self._user_id = user_id
        self._workflow_state = workflow_state
        self._started_at = started_at
        self._finished_at = finished_at
        self._pre_attachment = pre_attachment

        self.logger = logging.getLogger('py3canvas.Contentmigration')

    @property
    def id(self):
        """the unique identifier for the migration."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn("Setting values on id will NOT update the remote Canvas instance.")
        self._id = value

    @property
    def migration_type(self):
        """the type of content migration."""
        return self._migration_type

    @migration_type.setter
    def migration_type(self, value):
        """Setter for migration_type property."""
        self.logger.warn("Setting values on migration_type will NOT update the remote Canvas instance.")
        self._migration_type = value

    @property
    def migration_type_title(self):
        """the name of the content migration type."""
        return self._migration_type_title

    @migration_type_title.setter
    def migration_type_title(self, value):
        """Setter for migration_type_title property."""
        self.logger.warn("Setting values on migration_type_title will NOT update the remote Canvas instance.")
        self._migration_type_title = value

    @property
    def migration_issues_url(self):
        """API url to the content migration's issues."""
        return self._migration_issues_url

    @migration_issues_url.setter
    def migration_issues_url(self, value):
        """Setter for migration_issues_url property."""
        self.logger.warn("Setting values on migration_issues_url will NOT update the remote Canvas instance.")
        self._migration_issues_url = value

    @property
    def attachment(self):
        """attachment api object for the uploaded file may not be present for all migrations."""
        return self._attachment

    @attachment.setter
    def attachment(self, value):
        """Setter for attachment property."""
        self.logger.warn("Setting values on attachment will NOT update the remote Canvas instance.")
        self._attachment = value

    @property
    def progress_url(self):
        """The api endpoint for polling the current progress."""
        return self._progress_url

    @progress_url.setter
    def progress_url(self, value):
        """Setter for progress_url property."""
        self.logger.warn("Setting values on progress_url will NOT update the remote Canvas instance.")
        self._progress_url = value

    @property
    def user_id(self):
        """The user who started the migration."""
        return self._user_id

    @user_id.setter
    def user_id(self, value):
        """Setter for user_id property."""
        self.logger.warn("Setting values on user_id will NOT update the remote Canvas instance.")
        self._user_id = value

    @property
    def workflow_state(self):
        """Current state of the content migration: pre_processing, pre_processed, running, waiting_for_select, completed, failed."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn("Setting values on workflow_state will NOT update the remote Canvas instance.")
        self._workflow_state = value

    @property
    def started_at(self):
        """timestamp."""
        return self._started_at

    @started_at.setter
    def started_at(self, value):
        """Setter for started_at property."""
        self.logger.warn("Setting values on started_at will NOT update the remote Canvas instance.")
        self._started_at = value

    @property
    def finished_at(self):
        """timestamp."""
        return self._finished_at

    @finished_at.setter
    def finished_at(self, value):
        """Setter for finished_at property."""
        self.logger.warn("Setting values on finished_at will NOT update the remote Canvas instance.")
        self._finished_at = value

    @property
    def pre_attachment(self):
        """file uploading data, see {file:file_uploads.html File Upload Documentation} for file upload workflow This works a little differently in that all the file data is in the pre_attachment hash if there is no upload_url then there was an attachment pre-processing error, the error message will be in the message key This data will only be here after a create or update call."""
        return self._pre_attachment

    @pre_attachment.setter
    def pre_attachment(self, value):
        """Setter for pre_attachment property."""
        self.logger.warn("Setting values on pre_attachment will NOT update the remote Canvas instance.")
        self._pre_attachment = value


class Migrator(BaseModel):
    """Migrator Model."""

    def __init__(self, type=None, requires_file_upload=None, name=None, required_settings=None):
        """Init method for Migrator class."""
        self._type = type
        self._requires_file_upload = requires_file_upload
        self._name = name
        self._required_settings = required_settings

        self.logger = logging.getLogger('py3canvas.Migrator')

    @property
    def type(self):
        """The value to pass to the create endpoint."""
        return self._type

    @type.setter
    def type(self, value):
        """Setter for type property."""
        self.logger.warn("Setting values on type will NOT update the remote Canvas instance.")
        self._type = value

    @property
    def requires_file_upload(self):
        """Whether this endpoint requires a file upload."""
        return self._requires_file_upload

    @requires_file_upload.setter
    def requires_file_upload(self, value):
        """Setter for requires_file_upload property."""
        self.logger.warn("Setting values on requires_file_upload will NOT update the remote Canvas instance.")
        self._requires_file_upload = value

    @property
    def name(self):
        """Description of the package type expected."""
        return self._name

    @name.setter
    def name(self, value):
        """Setter for name property."""
        self.logger.warn("Setting values on name will NOT update the remote Canvas instance.")
        self._name = value

    @property
    def required_settings(self):
        """A list of fields this system requires."""
        return self._required_settings

    @required_settings.setter
    def required_settings(self, value):
        """Setter for required_settings property."""
        self.logger.warn("Setting values on required_settings will NOT update the remote Canvas instance.")
        self._required_settings = value

