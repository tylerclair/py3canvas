"""SisImports API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class SisImportsAPI(BaseCanvasAPI):
    """SisImports API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for SisImportsAPI."""
        super(SisImportsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.SisImportsAPI")

    def get_sis_import_list(
        self, account_id, created_before=None, created_since=None, workflow_state=None
    ):
        """
        Get SIS import list.

        Returns the list of SIS imports for an account
        
        Example:
          curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports \
            -H 'Authorization: Bearer <token>'
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - created_since
        """
            If set, only shows imports created after the specified date (use ISO8601 format)
        """
        if created_since is not None:
            if issubclass(created_since.__class__, str):
                created_since = self._validate_iso8601_string(created_since)
            elif issubclass(created_since.__class__, date) or issubclass(
                created_since.__class__, datetime
            ):
                created_since = created_since.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["created_since"] = created_since

        # OPTIONAL - created_before
        """
            If set, only shows imports created before the specified date (use ISO8601 format)
        """
        if created_before is not None:
            if issubclass(created_before.__class__, str):
                created_before = self._validate_iso8601_string(created_before)
            elif issubclass(created_before.__class__, date) or issubclass(
                created_before.__class__, datetime
            ):
                created_before = created_before.strftime("%Y-%m-%dT%H:%M:%S+00:00")
            params["created_before"] = created_before

        # OPTIONAL - workflow_state
        """
            If set, only returns imports that are in the given state.
        """
        if workflow_state is not None:
            self._validate_enum(
                workflow_state,
                [
                    "initializing",
                    "created",
                    "importing",
                    "cleanup_batch",
                    "imported",
                    "imported_with_messages",
                    "aborted",
                    "failed",
                    "failed_with_messages",
                    "restoring",
                    "partially_restored",
                    "restored",
                ],
            )
            params["workflow_state"] = workflow_state

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/sis_imports with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/sis_imports".format(**path),
            data=data,
            params=params,
            all_pages=True,
        )

    def get_current_importing_sis_import(self, account_id):
        """
        Get the current importing SIS import.

        Returns the SIS imports that are currently processing for an account. If no
        imports are running, will return an empty array.
        
        Example:
          curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/importing \
            -H 'Authorization: Bearer <token>'
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
            "GET /api/v1/accounts/{account_id}/sis_imports/importing with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/sis_imports/importing".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def import_sis_data(
        self,
        account_id,
        add_sis_stickiness=None,
        attachment=None,
        batch_mode=None,
        batch_mode_enrollment_drop_status=None,
        batch_mode_term_id=None,
        change_threshold=None,
        clear_sis_stickiness=None,
        diff_row_count_threshold=None,
        diffing_data_set_identifier=None,
        diffing_drop_status=None,
        diffing_remaster_data_set=None,
        extension=None,
        import_type=None,
        multi_term_batch_mode=None,
        override_sis_stickiness=None,
        skip_deletes=None,
        update_sis_id_if_login_claimed=None,
    ):
        """
        Import SIS data.

        Import SIS data into Canvas. Must be on a root account with SIS imports
        enabled.

        For more information on the format that's expected here, please see the
        "SIS CSV" section in the API docs.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - account_id
        """
            ID
        """
        path["account_id"] = account_id

        # OPTIONAL - import_type
        """
            Choose the data format for reading SIS data. With a standard Canvas
        install, this option can only be 'instructure_csv', and if unprovided,
        will be assumed to be so. Can be part of the query string.
        """
        if import_type is not None:
            data["import_type"] = import_type

        # OPTIONAL - attachment
        """
            There are two ways to post SIS import data - either via a
        multipart/form-data form-field-style attachment, or via a non-multipart
        raw post request.

        'attachment' is required for multipart/form-data style posts. Assumed to
        be SIS data from a file upload form field named 'attachment'.

        Examples:
          curl -F attachment=@<filename> -H "Authorization: Bearer <token>" \
              https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv

        If you decide to do a raw post, you can skip the 'attachment' argument,
        but you will then be required to provide a suitable Content-Type header.
        You are encouraged to also provide the 'extension' argument.

        Examples:
          curl -H 'Content-Type: application/octet-stream' --data-binary @<filename>.zip \
              -H "Authorization: Bearer <token>" \
              https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&extension=zip

          curl -H 'Content-Type: application/zip' --data-binary @<filename>.zip \
              -H "Authorization: Bearer <token>" \
              https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv

          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv

          curl -H 'Content-Type: text/csv' --data-binary @<filename>.csv \
              -H "Authorization: Bearer <token>" \
              https://<canvas>/api/v1/accounts/<account_id>/sis_imports.json?import_type=instructure_csv&batch_mode=1&batch_mode_term_id=15
        """
        if attachment is not None:
            data["attachment"] = attachment

        # OPTIONAL - extension
        """
            Recommended for raw post request style imports. This field will be used to
        distinguish between zip, xml, csv, and other file format extensions that
        would usually be provided with the filename in the multipart post request
        scenario. If not provided, this value will be inferred from the
        Content-Type, falling back to zip-file format if all else fails.
        """
        if extension is not None:
            data["extension"] = extension

        # OPTIONAL - batch_mode
        """
            If set, this SIS import will be run in batch mode, deleting any data
        previously imported via SIS that is not present in this latest import.
        See the SIS CSV Format page for details.
        Batch mode cannot be used with diffing.
        """
        if batch_mode is not None:
            data["batch_mode"] = batch_mode

        # OPTIONAL - batch_mode_term_id
        """
            Limit deletions to only this term. Required if batch mode is enabled.
        """
        if batch_mode_term_id is not None:
            data["batch_mode_term_id"] = batch_mode_term_id

        # OPTIONAL - multi_term_batch_mode
        """
            Runs batch mode against all terms in terms file. Requires change_threshold.
        """
        if multi_term_batch_mode is not None:
            data["multi_term_batch_mode"] = multi_term_batch_mode

        # OPTIONAL - skip_deletes
        """
            When set the import will skip any deletes. This does not account for
        objects that are deleted during the batch mode cleanup process.
        """
        if skip_deletes is not None:
            data["skip_deletes"] = skip_deletes

        # OPTIONAL - override_sis_stickiness
        """
            Many fields on records in Canvas can be marked "sticky," which means that
        when something changes in the UI apart from the SIS, that field gets
        "stuck." In this way, by default, SIS imports do not override UI changes.
        If this field is present, however, it will tell the SIS import to ignore
        "stickiness" and override all fields.
        """
        if override_sis_stickiness is not None:
            data["override_sis_stickiness"] = override_sis_stickiness

        # OPTIONAL - add_sis_stickiness
        """
            This option, if present, will process all changes as if they were UI
        changes. This means that "stickiness" will be added to changed fields.
        This option is only processed if 'override_sis_stickiness' is also provided.
        """
        if add_sis_stickiness is not None:
            data["add_sis_stickiness"] = add_sis_stickiness

        # OPTIONAL - clear_sis_stickiness
        """
            This option, if present, will clear "stickiness" from all fields touched
        by this import. Requires that 'override_sis_stickiness' is also provided.
        If 'add_sis_stickiness' is also provided, 'clear_sis_stickiness' will
        overrule the behavior of 'add_sis_stickiness'
        """
        if clear_sis_stickiness is not None:
            data["clear_sis_stickiness"] = clear_sis_stickiness

        # OPTIONAL - update_sis_id_if_login_claimed
        """
            This option, if present, will override the old (or non-existent)
        non-matching SIS ID with the new SIS ID in the upload,
        if a pseudonym is found from the login field and the SIS ID doesn't match.
        """
        if update_sis_id_if_login_claimed is not None:
            data["update_sis_id_if_login_claimed"] = update_sis_id_if_login_claimed

        # OPTIONAL - diffing_data_set_identifier
        """
            If set on a CSV import, Canvas will attempt to optimize the SIS import by
        comparing this set of CSVs to the previous set that has the same data set
        identifier, and only applying the difference between the two. See the
        SIS CSV Format documentation for more details.
        Diffing cannot be used with batch_mode
        """
        if diffing_data_set_identifier is not None:
            data["diffing_data_set_identifier"] = diffing_data_set_identifier

        # OPTIONAL - diffing_remaster_data_set
        """
            If true, and diffing_data_set_identifier is sent, this SIS import will be
        part of the data set, but diffing will not be performed. See the SIS CSV
        Format documentation for details.
        """
        if diffing_remaster_data_set is not None:
            data["diffing_remaster_data_set"] = diffing_remaster_data_set

        # OPTIONAL - diffing_drop_status
        """
            If diffing_drop_status is passed, this SIS import will use this status for
        enrollments that are not included in the sis_batch. Defaults to 'deleted'
        """
        if diffing_drop_status is not None:
            self._validate_enum(
                diffing_drop_status, ["deleted", "completed", "inactive"]
            )
            data["diffing_drop_status"] = diffing_drop_status

        # OPTIONAL - batch_mode_enrollment_drop_status
        """
            If batch_mode_enrollment_drop_status is passed, this SIS import will use
        this status for enrollments that are not included in the sis_batch. This
        will have an effect if multi_term_batch_mode is set. Defaults to 'deleted'
        This will still mark courses and sections that are not included in the
        sis_batch as deleted, and subsequently enrollments in the deleted courses
        and sections as deleted.
        """
        if batch_mode_enrollment_drop_status is not None:
            self._validate_enum(
                batch_mode_enrollment_drop_status, ["deleted", "completed", "inactive"]
            )
            data[
                "batch_mode_enrollment_drop_status"
            ] = batch_mode_enrollment_drop_status

        # OPTIONAL - change_threshold
        """
            If set with batch_mode, the batch cleanup process will not run if the
        number of items deleted is higher than the percentage set. If set to 10
        and a term has 200 enrollments, and batch would delete more than 20 of
        the enrollments the batch will abort before the enrollments are deleted.
        The change_threshold will be evaluated for course, sections, and
        enrollments independently.
        If set with diffing, diffing will not be performed if the files are
        greater than the threshold as a percent. If set to 5 and the file is more
        than 5% smaller or more than 5% larger than the file that is being
        compared to, diffing will not be performed. If the files are less than 5%,
        diffing will be performed. The way the percent is calculated is by taking
        the size of the current import and dividing it by the size of the previous
        import. The formula used is:
        |(1 - current_file_size / previous_file_size)| * 100
        See the SIS CSV Format documentation for more details.
        Required for multi_term_batch_mode.
        """
        if change_threshold is not None:
            data["change_threshold"] = change_threshold

        # OPTIONAL - diff_row_count_threshold
        """
            If set with diffing, diffing will not be performed if the number of rows
        to be run in the fully calculated diff import exceeds the threshold.
        """
        if diff_row_count_threshold is not None:
            data["diff_row_count_threshold"] = diff_row_count_threshold

        self.logger.debug(
            "POST /api/v1/accounts/{account_id}/sis_imports with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/accounts/{account_id}/sis_imports".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_sis_import_status(self, account_id, id):
        """
        Get SIS import status.

        Get the status of an already created SIS import.
        
          Examples:
            curl https://<canvas>/api/v1/accounts/<account_id>/sis_imports/<sis_import_id> \
                -H 'Authorization: Bearer <token>'
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

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/sis_imports/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/sis_imports/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def restore_workflow_states_of_sis_imported_items(
        self, account_id, id, batch_mode=None, unconclude_only=None, undelete_only=None
    ):
        """
        Restore workflow_states of SIS imported items.

        This will restore the the workflow_state for all the items that changed
        their workflow_state during the import being restored.
        This will restore states for items imported with the following importers:
        accounts.csv terms.csv courses.csv sections.csv group_categories.csv
        groups.csv users.csv admins.csv
        This also restores states for other items that changed during the import.
        An example would be if an enrollment was deleted from a sis import and the
        group_membership was also deleted as a result of the enrollment deletion,
        both items would be restored when the sis batch is restored.
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

        # OPTIONAL - batch_mode
        """
            If set, will only restore items that were deleted from batch_mode.
        """
        if batch_mode is not None:
            data["batch_mode"] = batch_mode

        # OPTIONAL - undelete_only
        """
            If set, will only restore items that were deleted. This will ignore any
        items that were created or modified.
        """
        if undelete_only is not None:
            data["undelete_only"] = undelete_only

        # OPTIONAL - unconclude_only
        """
            If set, will only restore enrollments that were concluded. This will
        ignore any items that were created or deleted.
        """
        if unconclude_only is not None:
            data["unconclude_only"] = unconclude_only

        self.logger.debug(
            "PUT /api/v1/accounts/{account_id}/sis_imports/{id}/restore_states with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/sis_imports/{id}/restore_states".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def abort_sis_import(self, account_id, id):
        """
        Abort SIS import.

        Abort a SIS import that has not completed.

        Aborting a sis batch that is running can take some time for every process to
        see the abort event. Subsequent sis batches begin to process 10 minutes
        after the abort to allow each process to clean up properly.
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

        self.logger.debug(
            "PUT /api/v1/accounts/{account_id}/sis_imports/{id}/abort with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/sis_imports/{id}/abort".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def abort_all_pending_sis_imports(self, account_id):
        """
        Abort all pending SIS imports.

        Abort already created but not processed or processing SIS imports.
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
            "PUT /api/v1/accounts/{account_id}/sis_imports/abort_all_pending with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/accounts/{account_id}/sis_imports/abort_all_pending".format(
                **path
            ),
            data=data,
            params=params,
        )


class Sisimportdata(BaseModel):
    """Sisimportdata Model."""

    def __init__(self, import_type=None, supplied_batches=None, counts=None):
        """Init method for Sisimportdata class."""
        self._import_type = import_type
        self._supplied_batches = supplied_batches
        self._counts = counts

        self.logger = logging.getLogger("py3canvas.Sisimportdata")

    @property
    def import_type(self):
        """The type of SIS import."""
        return self._import_type

    @import_type.setter
    def import_type(self, value):
        """Setter for import_type property."""
        self.logger.warn(
            "Setting values on import_type will NOT update the remote Canvas instance."
        )
        self._import_type = value

    @property
    def supplied_batches(self):
        """Which files were included in the SIS import."""
        return self._supplied_batches

    @supplied_batches.setter
    def supplied_batches(self, value):
        """Setter for supplied_batches property."""
        self.logger.warn(
            "Setting values on supplied_batches will NOT update the remote Canvas instance."
        )
        self._supplied_batches = value

    @property
    def counts(self):
        """The number of rows processed for each type of import."""
        return self._counts

    @counts.setter
    def counts(self, value):
        """Setter for counts property."""
        self.logger.warn(
            "Setting values on counts will NOT update the remote Canvas instance."
        )
        self._counts = value


class Sisimportstatistic(BaseModel):
    """Sisimportstatistic Model."""

    def __init__(
        self,
        created=None,
        concluded=None,
        deactivated=None,
        restored=None,
        deleted=None,
    ):
        """Init method for Sisimportstatistic class."""
        self._created = created
        self._concluded = concluded
        self._deactivated = deactivated
        self._restored = restored
        self._deleted = deleted

        self.logger = logging.getLogger("py3canvas.Sisimportstatistic")

    @property
    def created(self):
        """This is the number of items that were created."""
        return self._created

    @created.setter
    def created(self, value):
        """Setter for created property."""
        self.logger.warn(
            "Setting values on created will NOT update the remote Canvas instance."
        )
        self._created = value

    @property
    def concluded(self):
        """This is the number of items that marked as completed. This only applies to courses and enrollments."""
        return self._concluded

    @concluded.setter
    def concluded(self, value):
        """Setter for concluded property."""
        self.logger.warn(
            "Setting values on concluded will NOT update the remote Canvas instance."
        )
        self._concluded = value

    @property
    def deactivated(self):
        """This is the number of Enrollments that were marked as 'inactive'. This only applies to enrollments."""
        return self._deactivated

    @deactivated.setter
    def deactivated(self, value):
        """Setter for deactivated property."""
        self.logger.warn(
            "Setting values on deactivated will NOT update the remote Canvas instance."
        )
        self._deactivated = value

    @property
    def restored(self):
        """This is the number of items that were set to an active state from a completed, inactive, or deleted state."""
        return self._restored

    @restored.setter
    def restored(self, value):
        """Setter for restored property."""
        self.logger.warn(
            "Setting values on restored will NOT update the remote Canvas instance."
        )
        self._restored = value

    @property
    def deleted(self):
        """This is the number of items that were deleted."""
        return self._deleted

    @deleted.setter
    def deleted(self, value):
        """Setter for deleted property."""
        self.logger.warn(
            "Setting values on deleted will NOT update the remote Canvas instance."
        )
        self._deleted = value


class Sisimportstatistics(BaseModel):
    """Sisimportstatistics Model."""

    def __init__(
        self,
        total_state_changes=None,
        Account=None,
        EnrollmentTerm=None,
        CommunicationChannel=None,
        AbstractCourse=None,
        Course=None,
        CourseSection=None,
        Enrollment=None,
        GroupCategory=None,
        Group=None,
        GroupMembership=None,
        Pseudonym=None,
        UserObserver=None,
        AccountUser=None,
    ):
        """Init method for Sisimportstatistics class."""
        self._total_state_changes = total_state_changes
        self._Account = Account
        self._EnrollmentTerm = EnrollmentTerm
        self._CommunicationChannel = CommunicationChannel
        self._AbstractCourse = AbstractCourse
        self._Course = Course
        self._CourseSection = CourseSection
        self._Enrollment = Enrollment
        self._GroupCategory = GroupCategory
        self._Group = Group
        self._GroupMembership = GroupMembership
        self._Pseudonym = Pseudonym
        self._UserObserver = UserObserver
        self._AccountUser = AccountUser

        self.logger = logging.getLogger("py3canvas.Sisimportstatistics")

    @property
    def total_state_changes(self):
        """This is the total number of items that were changed in the sis import. There are a few caveats that can cause this number to not add up to the individual counts. There are some state changes that happen that have no impact to the object. An example would be changing a course from 'created' to 'claimed'. Both of these would be considered an active course, but would increment this counter. In this example the course would not increment the created or restored counters for course statistic."""
        return self._total_state_changes

    @total_state_changes.setter
    def total_state_changes(self, value):
        """Setter for total_state_changes property."""
        self.logger.warn(
            "Setting values on total_state_changes will NOT update the remote Canvas instance."
        )
        self._total_state_changes = value

    @property
    def Account(self):
        """This contains that statistics for accounts."""
        return self._Account

    @Account.setter
    def Account(self, value):
        """Setter for Account property."""
        self.logger.warn(
            "Setting values on Account will NOT update the remote Canvas instance."
        )
        self._Account = value

    @property
    def EnrollmentTerm(self):
        """This contains that statistics for terms."""
        return self._EnrollmentTerm

    @EnrollmentTerm.setter
    def EnrollmentTerm(self, value):
        """Setter for EnrollmentTerm property."""
        self.logger.warn(
            "Setting values on EnrollmentTerm will NOT update the remote Canvas instance."
        )
        self._EnrollmentTerm = value

    @property
    def CommunicationChannel(self):
        """This contains that statistics for communication channels. This is an indirect effect from creating or deleting a user."""
        return self._CommunicationChannel

    @CommunicationChannel.setter
    def CommunicationChannel(self, value):
        """Setter for CommunicationChannel property."""
        self.logger.warn(
            "Setting values on CommunicationChannel will NOT update the remote Canvas instance."
        )
        self._CommunicationChannel = value

    @property
    def AbstractCourse(self):
        """This contains that statistics for abstract courses."""
        return self._AbstractCourse

    @AbstractCourse.setter
    def AbstractCourse(self, value):
        """Setter for AbstractCourse property."""
        self.logger.warn(
            "Setting values on AbstractCourse will NOT update the remote Canvas instance."
        )
        self._AbstractCourse = value

    @property
    def Course(self):
        """This contains that statistics for courses."""
        return self._Course

    @Course.setter
    def Course(self, value):
        """Setter for Course property."""
        self.logger.warn(
            "Setting values on Course will NOT update the remote Canvas instance."
        )
        self._Course = value

    @property
    def CourseSection(self):
        """This contains that statistics for course sections."""
        return self._CourseSection

    @CourseSection.setter
    def CourseSection(self, value):
        """Setter for CourseSection property."""
        self.logger.warn(
            "Setting values on CourseSection will NOT update the remote Canvas instance."
        )
        self._CourseSection = value

    @property
    def Enrollment(self):
        """This contains that statistics for enrollments."""
        return self._Enrollment

    @Enrollment.setter
    def Enrollment(self, value):
        """Setter for Enrollment property."""
        self.logger.warn(
            "Setting values on Enrollment will NOT update the remote Canvas instance."
        )
        self._Enrollment = value

    @property
    def GroupCategory(self):
        """This contains that statistics for group categories."""
        return self._GroupCategory

    @GroupCategory.setter
    def GroupCategory(self, value):
        """Setter for GroupCategory property."""
        self.logger.warn(
            "Setting values on GroupCategory will NOT update the remote Canvas instance."
        )
        self._GroupCategory = value

    @property
    def Group(self):
        """This contains that statistics for groups."""
        return self._Group

    @Group.setter
    def Group(self, value):
        """Setter for Group property."""
        self.logger.warn(
            "Setting values on Group will NOT update the remote Canvas instance."
        )
        self._Group = value

    @property
    def GroupMembership(self):
        """This contains that statistics for group memberships. This can be a direct impact from the import or indirect from an enrollment being deleted."""
        return self._GroupMembership

    @GroupMembership.setter
    def GroupMembership(self, value):
        """Setter for GroupMembership property."""
        self.logger.warn(
            "Setting values on GroupMembership will NOT update the remote Canvas instance."
        )
        self._GroupMembership = value

    @property
    def Pseudonym(self):
        """This contains that statistics for pseudonyms. Pseudonyms are logins for users, and are the object that ties an enrollment to a user. This would be impacted from the user importer. ."""
        return self._Pseudonym

    @Pseudonym.setter
    def Pseudonym(self, value):
        """Setter for Pseudonym property."""
        self.logger.warn(
            "Setting values on Pseudonym will NOT update the remote Canvas instance."
        )
        self._Pseudonym = value

    @property
    def UserObserver(self):
        """This contains that statistics for user observers."""
        return self._UserObserver

    @UserObserver.setter
    def UserObserver(self, value):
        """Setter for UserObserver property."""
        self.logger.warn(
            "Setting values on UserObserver will NOT update the remote Canvas instance."
        )
        self._UserObserver = value

    @property
    def AccountUser(self):
        """This contains that statistics for account users."""
        return self._AccountUser

    @AccountUser.setter
    def AccountUser(self, value):
        """Setter for AccountUser property."""
        self.logger.warn(
            "Setting values on AccountUser will NOT update the remote Canvas instance."
        )
        self._AccountUser = value


class Sisimportcounts(BaseModel):
    """Sisimportcounts Model."""

    def __init__(
        self,
        accounts=None,
        terms=None,
        abstract_courses=None,
        courses=None,
        sections=None,
        xlists=None,
        users=None,
        enrollments=None,
        groups=None,
        group_memberships=None,
        grade_publishing_results=None,
        batch_courses_deleted=None,
        batch_sections_deleted=None,
        batch_enrollments_deleted=None,
        error_count=None,
        warning_count=None,
    ):
        """Init method for Sisimportcounts class."""
        self._accounts = accounts
        self._terms = terms
        self._abstract_courses = abstract_courses
        self._courses = courses
        self._sections = sections
        self._xlists = xlists
        self._users = users
        self._enrollments = enrollments
        self._groups = groups
        self._group_memberships = group_memberships
        self._grade_publishing_results = grade_publishing_results
        self._batch_courses_deleted = batch_courses_deleted
        self._batch_sections_deleted = batch_sections_deleted
        self._batch_enrollments_deleted = batch_enrollments_deleted
        self._error_count = error_count
        self._warning_count = warning_count

        self.logger = logging.getLogger("py3canvas.Sisimportcounts")

    @property
    def accounts(self):
        """accounts."""
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
        """terms."""
        return self._terms

    @terms.setter
    def terms(self, value):
        """Setter for terms property."""
        self.logger.warn(
            "Setting values on terms will NOT update the remote Canvas instance."
        )
        self._terms = value

    @property
    def abstract_courses(self):
        """abstract_courses."""
        return self._abstract_courses

    @abstract_courses.setter
    def abstract_courses(self, value):
        """Setter for abstract_courses property."""
        self.logger.warn(
            "Setting values on abstract_courses will NOT update the remote Canvas instance."
        )
        self._abstract_courses = value

    @property
    def courses(self):
        """courses."""
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
        """sections."""
        return self._sections

    @sections.setter
    def sections(self, value):
        """Setter for sections property."""
        self.logger.warn(
            "Setting values on sections will NOT update the remote Canvas instance."
        )
        self._sections = value

    @property
    def xlists(self):
        """xlists."""
        return self._xlists

    @xlists.setter
    def xlists(self, value):
        """Setter for xlists property."""
        self.logger.warn(
            "Setting values on xlists will NOT update the remote Canvas instance."
        )
        self._xlists = value

    @property
    def users(self):
        """users."""
        return self._users

    @users.setter
    def users(self, value):
        """Setter for users property."""
        self.logger.warn(
            "Setting values on users will NOT update the remote Canvas instance."
        )
        self._users = value

    @property
    def enrollments(self):
        """enrollments."""
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
        """groups."""
        return self._groups

    @groups.setter
    def groups(self, value):
        """Setter for groups property."""
        self.logger.warn(
            "Setting values on groups will NOT update the remote Canvas instance."
        )
        self._groups = value

    @property
    def group_memberships(self):
        """group_memberships."""
        return self._group_memberships

    @group_memberships.setter
    def group_memberships(self, value):
        """Setter for group_memberships property."""
        self.logger.warn(
            "Setting values on group_memberships will NOT update the remote Canvas instance."
        )
        self._group_memberships = value

    @property
    def grade_publishing_results(self):
        """grade_publishing_results."""
        return self._grade_publishing_results

    @grade_publishing_results.setter
    def grade_publishing_results(self, value):
        """Setter for grade_publishing_results property."""
        self.logger.warn(
            "Setting values on grade_publishing_results will NOT update the remote Canvas instance."
        )
        self._grade_publishing_results = value

    @property
    def batch_courses_deleted(self):
        """the number of courses that were removed because they were not included in the batch for batch_mode imports. Only included if courses were deleted."""
        return self._batch_courses_deleted

    @batch_courses_deleted.setter
    def batch_courses_deleted(self, value):
        """Setter for batch_courses_deleted property."""
        self.logger.warn(
            "Setting values on batch_courses_deleted will NOT update the remote Canvas instance."
        )
        self._batch_courses_deleted = value

    @property
    def batch_sections_deleted(self):
        """the number of sections that were removed because they were not included in the batch for batch_mode imports. Only included if sections were deleted."""
        return self._batch_sections_deleted

    @batch_sections_deleted.setter
    def batch_sections_deleted(self, value):
        """Setter for batch_sections_deleted property."""
        self.logger.warn(
            "Setting values on batch_sections_deleted will NOT update the remote Canvas instance."
        )
        self._batch_sections_deleted = value

    @property
    def batch_enrollments_deleted(self):
        """the number of enrollments that were removed because they were not included in the batch for batch_mode imports. Only included if enrollments were deleted."""
        return self._batch_enrollments_deleted

    @batch_enrollments_deleted.setter
    def batch_enrollments_deleted(self, value):
        """Setter for batch_enrollments_deleted property."""
        self.logger.warn(
            "Setting values on batch_enrollments_deleted will NOT update the remote Canvas instance."
        )
        self._batch_enrollments_deleted = value

    @property
    def error_count(self):
        """error_count."""
        return self._error_count

    @error_count.setter
    def error_count(self, value):
        """Setter for error_count property."""
        self.logger.warn(
            "Setting values on error_count will NOT update the remote Canvas instance."
        )
        self._error_count = value

    @property
    def warning_count(self):
        """warning_count."""
        return self._warning_count

    @warning_count.setter
    def warning_count(self, value):
        """Setter for warning_count property."""
        self.logger.warn(
            "Setting values on warning_count will NOT update the remote Canvas instance."
        )
        self._warning_count = value


class Sisimport(BaseModel):
    """Sisimport Model."""

    def __init__(
        self,
        id=None,
        created_at=None,
        ended_at=None,
        updated_at=None,
        workflow_state=None,
        data=None,
        statistics=None,
        progress=None,
        errors_attachment=None,
        user=None,
        processing_warnings=None,
        processing_errors=None,
        batch_mode=None,
        batch_mode_term_id=None,
        multi_term_batch_mode=None,
        skip_deletes=None,
        override_sis_stickiness=None,
        add_sis_stickiness=None,
        clear_sis_stickiness=None,
        diffing_data_set_identifier=None,
        diffed_against_import_id=None,
        csv_attachments=None,
    ):
        """Init method for Sisimport class."""
        self._id = id
        self._created_at = created_at
        self._ended_at = ended_at
        self._updated_at = updated_at
        self._workflow_state = workflow_state
        self._data = data
        self._statistics = statistics
        self._progress = progress
        self._errors_attachment = errors_attachment
        self._user = user
        self._processing_warnings = processing_warnings
        self._processing_errors = processing_errors
        self._batch_mode = batch_mode
        self._batch_mode_term_id = batch_mode_term_id
        self._multi_term_batch_mode = multi_term_batch_mode
        self._skip_deletes = skip_deletes
        self._override_sis_stickiness = override_sis_stickiness
        self._add_sis_stickiness = add_sis_stickiness
        self._clear_sis_stickiness = clear_sis_stickiness
        self._diffing_data_set_identifier = diffing_data_set_identifier
        self._diffed_against_import_id = diffed_against_import_id
        self._csv_attachments = csv_attachments

        self.logger = logging.getLogger("py3canvas.Sisimport")

    @property
    def id(self):
        """The unique identifier for the SIS import."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def created_at(self):
        """The date the SIS import was created."""
        return self._created_at

    @created_at.setter
    def created_at(self, value):
        """Setter for created_at property."""
        self.logger.warn(
            "Setting values on created_at will NOT update the remote Canvas instance."
        )
        self._created_at = value

    @property
    def ended_at(self):
        """The date the SIS import finished. Returns null if not finished."""
        return self._ended_at

    @ended_at.setter
    def ended_at(self, value):
        """Setter for ended_at property."""
        self.logger.warn(
            "Setting values on ended_at will NOT update the remote Canvas instance."
        )
        self._ended_at = value

    @property
    def updated_at(self):
        """The date the SIS import was last updated."""
        return self._updated_at

    @updated_at.setter
    def updated_at(self, value):
        """Setter for updated_at property."""
        self.logger.warn(
            "Setting values on updated_at will NOT update the remote Canvas instance."
        )
        self._updated_at = value

    @property
    def workflow_state(self):
        """The current state of the SIS import.
        - 'initializing': The SIS import is being created, if this gets stuck in initializing, it will not import and will continue on to next import.
        - 'created': The SIS import has been created.
        - 'importing': The SIS import is currently processing.
        - 'cleanup_batch': The SIS import is currently cleaning up courses, sections, and enrollments not included in the batch for batch_mode imports.
        - 'imported': The SIS import has completed successfully.
        - 'imported_with_messages': The SIS import completed with errors or warnings.
        - 'aborted': The SIS import was aborted.
        - 'failed_with_messages': The SIS import failed with errors.
        - 'failed': The SIS import failed.
        - 'restoring': The SIS import is restoring states of imported items.
        - 'partially_restored': The SIS import is restored some of the states of imported items. This is generally due to passing a param like undelete only.
        - 'restored': The SIS import is restored all of the states of imported items."""
        return self._workflow_state

    @workflow_state.setter
    def workflow_state(self, value):
        """Setter for workflow_state property."""
        self.logger.warn(
            "Setting values on workflow_state will NOT update the remote Canvas instance."
        )
        self._workflow_state = value

    @property
    def data(self):
        """data."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn(
            "Setting values on data will NOT update the remote Canvas instance."
        )
        self._data = value

    @property
    def statistics(self):
        """statistics."""
        return self._statistics

    @statistics.setter
    def statistics(self, value):
        """Setter for statistics property."""
        self.logger.warn(
            "Setting values on statistics will NOT update the remote Canvas instance."
        )
        self._statistics = value

    @property
    def progress(self):
        """The progress of the SIS import. The progress will reset when using batch_mode and have a different progress for the cleanup stage."""
        return self._progress

    @progress.setter
    def progress(self, value):
        """Setter for progress property."""
        self.logger.warn(
            "Setting values on progress will NOT update the remote Canvas instance."
        )
        self._progress = value

    @property
    def errors_attachment(self):
        """The errors_attachment api object of the SIS import. Only available if there are errors or warning and import has completed."""
        return self._errors_attachment

    @errors_attachment.setter
    def errors_attachment(self, value):
        """Setter for errors_attachment property."""
        self.logger.warn(
            "Setting values on errors_attachment will NOT update the remote Canvas instance."
        )
        self._errors_attachment = value

    @property
    def user(self):
        """The user that initiated the sis_batch. See the Users API for details."""
        return self._user

    @user.setter
    def user(self, value):
        """Setter for user property."""
        self.logger.warn(
            "Setting values on user will NOT update the remote Canvas instance."
        )
        self._user = value

    @property
    def processing_warnings(self):
        """Only imports that are complete will get this data. An array of CSV_file/warning_message pairs."""
        return self._processing_warnings

    @processing_warnings.setter
    def processing_warnings(self, value):
        """Setter for processing_warnings property."""
        self.logger.warn(
            "Setting values on processing_warnings will NOT update the remote Canvas instance."
        )
        self._processing_warnings = value

    @property
    def processing_errors(self):
        """An array of CSV_file/error_message pairs."""
        return self._processing_errors

    @processing_errors.setter
    def processing_errors(self, value):
        """Setter for processing_errors property."""
        self.logger.warn(
            "Setting values on processing_errors will NOT update the remote Canvas instance."
        )
        self._processing_errors = value

    @property
    def batch_mode(self):
        """Whether the import was run in batch mode."""
        return self._batch_mode

    @batch_mode.setter
    def batch_mode(self, value):
        """Setter for batch_mode property."""
        self.logger.warn(
            "Setting values on batch_mode will NOT update the remote Canvas instance."
        )
        self._batch_mode = value

    @property
    def batch_mode_term_id(self):
        """The term the batch was limited to."""
        return self._batch_mode_term_id

    @batch_mode_term_id.setter
    def batch_mode_term_id(self, value):
        """Setter for batch_mode_term_id property."""
        self.logger.warn(
            "Setting values on batch_mode_term_id will NOT update the remote Canvas instance."
        )
        self._batch_mode_term_id = value

    @property
    def multi_term_batch_mode(self):
        """Enables batch mode against all terms in term file. Requires change_threshold to be set."""
        return self._multi_term_batch_mode

    @multi_term_batch_mode.setter
    def multi_term_batch_mode(self, value):
        """Setter for multi_term_batch_mode property."""
        self.logger.warn(
            "Setting values on multi_term_batch_mode will NOT update the remote Canvas instance."
        )
        self._multi_term_batch_mode = value

    @property
    def skip_deletes(self):
        """When set the import will skip any deletes."""
        return self._skip_deletes

    @skip_deletes.setter
    def skip_deletes(self, value):
        """Setter for skip_deletes property."""
        self.logger.warn(
            "Setting values on skip_deletes will NOT update the remote Canvas instance."
        )
        self._skip_deletes = value

    @property
    def override_sis_stickiness(self):
        """Whether UI changes were overridden."""
        return self._override_sis_stickiness

    @override_sis_stickiness.setter
    def override_sis_stickiness(self, value):
        """Setter for override_sis_stickiness property."""
        self.logger.warn(
            "Setting values on override_sis_stickiness will NOT update the remote Canvas instance."
        )
        self._override_sis_stickiness = value

    @property
    def add_sis_stickiness(self):
        """Whether stickiness was added to the batch changes."""
        return self._add_sis_stickiness

    @add_sis_stickiness.setter
    def add_sis_stickiness(self, value):
        """Setter for add_sis_stickiness property."""
        self.logger.warn(
            "Setting values on add_sis_stickiness will NOT update the remote Canvas instance."
        )
        self._add_sis_stickiness = value

    @property
    def clear_sis_stickiness(self):
        """Whether stickiness was cleared."""
        return self._clear_sis_stickiness

    @clear_sis_stickiness.setter
    def clear_sis_stickiness(self, value):
        """Setter for clear_sis_stickiness property."""
        self.logger.warn(
            "Setting values on clear_sis_stickiness will NOT update the remote Canvas instance."
        )
        self._clear_sis_stickiness = value

    @property
    def diffing_data_set_identifier(self):
        """The identifier of the data set that this SIS batch diffs against."""
        return self._diffing_data_set_identifier

    @diffing_data_set_identifier.setter
    def diffing_data_set_identifier(self, value):
        """Setter for diffing_data_set_identifier property."""
        self.logger.warn(
            "Setting values on diffing_data_set_identifier will NOT update the remote Canvas instance."
        )
        self._diffing_data_set_identifier = value

    @property
    def diffed_against_import_id(self):
        """The ID of the SIS Import that this import was diffed against."""
        return self._diffed_against_import_id

    @diffed_against_import_id.setter
    def diffed_against_import_id(self, value):
        """Setter for diffed_against_import_id property."""
        self.logger.warn(
            "Setting values on diffed_against_import_id will NOT update the remote Canvas instance."
        )
        self._diffed_against_import_id = value

    @property
    def csv_attachments(self):
        """An array of CSV files for processing."""
        return self._csv_attachments

    @csv_attachments.setter
    def csv_attachments(self, value):
        """Setter for csv_attachments property."""
        self.logger.warn(
            "Setting values on csv_attachments will NOT update the remote Canvas instance."
        )
        self._csv_attachments = value
