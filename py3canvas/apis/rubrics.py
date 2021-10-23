"""Rubrics API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI
from .base import BaseModel


class RubricsAPI(BaseCanvasAPI):
    """Rubrics API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for RubricsAPI."""
        super(RubricsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.RubricsAPI")

    def create_single_rubric(
        self,
        course_id,
        id=None,
        rubric_association_association_id=None,
        rubric_association_association_type=None,
        rubric_association_hide_score_total=None,
        rubric_association_id=None,
        rubric_association_purpose=None,
        rubric_association_use_for_grading=None,
        rubric_criteria=None,
        rubric_free_form_criterion_comments=None,
        rubric_title=None,
    ):
        """
        Create a single rubric.

        Returns the rubric with the given id.

        Unfortuantely this endpoint does not return a standard Rubric object,
        instead it returns a hash that looks like
          { 'rubric': Rubric, 'rubric_association': RubricAssociation }

        This may eventually be deprecated in favor of a more standardized return
        value, but that is not currently planned.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - id
        """
            The id of the rubric
        """
        if id is not None:
            data["id"] = id

        # OPTIONAL - rubric_association_id
        """
            The id of the object with which this rubric is associated
        """
        if rubric_association_id is not None:
            data["rubric_association_id"] = rubric_association_id

        # OPTIONAL - rubric[title]
        """
            The title of the rubric
        """
        if rubric_title is not None:
            data["rubric[title]"] = rubric_title

        # OPTIONAL - rubric[free_form_criterion_comments]
        """
            Whether or not you can write custom comments in the ratings field for a rubric
        """
        if rubric_free_form_criterion_comments is not None:
            data[
                "rubric[free_form_criterion_comments]"
            ] = rubric_free_form_criterion_comments

        # OPTIONAL - rubric_association[association_id]
        """
            The id of the object with which this rubric is associated
        """
        if rubric_association_association_id is not None:
            data[
                "rubric_association[association_id]"
            ] = rubric_association_association_id

        # OPTIONAL - rubric_association[association_type]
        """
            The type of object this rubric is associated with
        """
        if rubric_association_association_type is not None:
            self._validate_enum(
                rubric_association_association_type, ["Assignment", "Course", "Account"]
            )
            data[
                "rubric_association[association_type]"
            ] = rubric_association_association_type

        # OPTIONAL - rubric_association[use_for_grading]
        """
            Whether or not the associated rubric is used for grade calculation
        """
        if rubric_association_use_for_grading is not None:
            data[
                "rubric_association[use_for_grading]"
            ] = rubric_association_use_for_grading

        # OPTIONAL - rubric_association[hide_score_total]
        """
            Whether or not the score total is displayed within the rubric.
        This option is only available if the rubric is not used for grading.
        """
        if rubric_association_hide_score_total is not None:
            data[
                "rubric_association[hide_score_total]"
            ] = rubric_association_hide_score_total

        # OPTIONAL - rubric_association[purpose]
        """
            Whether or not the association is for grading (and thus linked to an assignment)
        or if it's to indicate the rubric should appear in its context
        """
        if rubric_association_purpose is not None:
            data["rubric_association[purpose]"] = rubric_association_purpose

        # OPTIONAL - rubric[criteria]
        """
            An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects
        """
        if rubric_criteria is not None:
            data["rubric[criteria]"] = rubric_criteria

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/rubrics with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/rubrics".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def update_single_rubric(
        self,
        course_id,
        id,
        rubric_association_association_id=None,
        rubric_association_association_type=None,
        rubric_association_hide_score_total=None,
        rubric_association_id=None,
        rubric_association_purpose=None,
        rubric_association_use_for_grading=None,
        rubric_criteria=None,
        rubric_free_form_criterion_comments=None,
        rubric_skip_updating_points_possible=None,
        rubric_title=None,
    ):
        """
        Update a single rubric.

        Returns the rubric with the given id.

        Unfortuantely this endpoint does not return a standard Rubric object,
        instead it returns a hash that looks like
          { 'rubric': Rubric, 'rubric_association': RubricAssociation }

        This may eventually be deprecated in favor of a more standardized return
        value, but that is not currently planned.
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
            The id of the rubric
        """
        path["id"] = id

        # OPTIONAL - rubric_association_id
        """
            The id of the object with which this rubric is associated
        """
        if rubric_association_id is not None:
            data["rubric_association_id"] = rubric_association_id

        # OPTIONAL - rubric[title]
        """
            The title of the rubric
        """
        if rubric_title is not None:
            data["rubric[title]"] = rubric_title

        # OPTIONAL - rubric[free_form_criterion_comments]
        """
            Whether or not you can write custom comments in the ratings field for a rubric
        """
        if rubric_free_form_criterion_comments is not None:
            data[
                "rubric[free_form_criterion_comments]"
            ] = rubric_free_form_criterion_comments

        # OPTIONAL - rubric[skip_updating_points_possible]
        """
            Whether or not to update the points possible
        """
        if rubric_skip_updating_points_possible is not None:
            data[
                "rubric[skip_updating_points_possible]"
            ] = rubric_skip_updating_points_possible

        # OPTIONAL - rubric_association[association_id]
        """
            The id of the object with which this rubric is associated
        """
        if rubric_association_association_id is not None:
            data[
                "rubric_association[association_id]"
            ] = rubric_association_association_id

        # OPTIONAL - rubric_association[association_type]
        """
            The type of object this rubric is associated with
        """
        if rubric_association_association_type is not None:
            self._validate_enum(
                rubric_association_association_type, ["Assignment", "Course", "Account"]
            )
            data[
                "rubric_association[association_type]"
            ] = rubric_association_association_type

        # OPTIONAL - rubric_association[use_for_grading]
        """
            Whether or not the associated rubric is used for grade calculation
        """
        if rubric_association_use_for_grading is not None:
            data[
                "rubric_association[use_for_grading]"
            ] = rubric_association_use_for_grading

        # OPTIONAL - rubric_association[hide_score_total]
        """
            Whether or not the score total is displayed within the rubric.
        This option is only available if the rubric is not used for grading.
        """
        if rubric_association_hide_score_total is not None:
            data[
                "rubric_association[hide_score_total]"
            ] = rubric_association_hide_score_total

        # OPTIONAL - rubric_association[purpose]
        """
            Whether or not the association is for grading (and thus linked to an assignment)
        or if it's to indicate the rubric should appear in its context
        """
        if rubric_association_purpose is not None:
            self._validate_enum(rubric_association_purpose, ["grading", "bookmark"])
            data["rubric_association[purpose]"] = rubric_association_purpose

        # OPTIONAL - rubric[criteria]
        """
            An indexed Hash of RubricCriteria objects where the keys are integer ids and the values are the RubricCriteria objects
        """
        if rubric_criteria is not None:
            data["rubric[criteria]"] = rubric_criteria

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/rubrics/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/rubrics/{id}".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def delete_single_rubric(self, course_id, id):
        """
        Delete a single rubric.

        Deletes a Rubric and removes all RubricAssociations.
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
            "DELETE /api/v1/courses/{course_id}/rubrics/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/courses/{course_id}/rubrics/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def list_rubrics_accounts(self, account_id):
        """
        List rubrics.

        Returns the paginated list of active rubrics for the current context.
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
            "GET /api/v1/accounts/{account_id}/rubrics with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/rubrics".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def list_rubrics_courses(self, course_id):
        """
        List rubrics.

        Returns the paginated list of active rubrics for the current context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/rubrics with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/rubrics".format(**path),
            data=data,
            params=params,
            no_data=True,
        )

    def get_single_rubric_accounts(self, account_id, id, include=None, style=None):
        """
        Get a single rubric.

        Returns the rubric with the given id.
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

        # OPTIONAL - include
        """
            Related records to include in the response.
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "assessments",
                    "graded_assessments",
                    "peer_assessments",
                    "associations",
                    "assignment_associations",
                    "course_associations",
                    "account_associations",
                ],
            )
            params["include"] = include

        # OPTIONAL - style
        """
            Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted.
        """
        if style is not None:
            self._validate_enum(style, ["full", "comments_only"])
            params["style"] = style

        self.logger.debug(
            "GET /api/v1/accounts/{account_id}/rubrics/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/accounts/{account_id}/rubrics/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def get_single_rubric_courses(self, course_id, id, include=None, style=None):
        """
        Get a single rubric.

        Returns the rubric with the given id.
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

        # OPTIONAL - include
        """
            Related records to include in the response.
        """
        if include is not None:
            self._validate_enum(
                include,
                [
                    "assessments",
                    "graded_assessments",
                    "peer_assessments",
                    "associations",
                    "assignment_associations",
                    "course_associations",
                    "account_associations",
                ],
            )
            params["include"] = include

        # OPTIONAL - style
        """
            Applicable only if assessments are being returned. If included, returns either all criteria data associated with the assessment, or just the comments. If not included, both data and comments are omitted.
        """
        if style is not None:
            self._validate_enum(style, ["full", "comments_only"])
            params["style"] = style

        self.logger.debug(
            "GET /api/v1/courses/{course_id}/rubrics/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "GET",
            "/api/v1/courses/{course_id}/rubrics/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def create_single_rubric_assessment(
        self,
        course_id,
        rubric_association_id,
        final=None,
        graded_anonymously=None,
        provisional=None,
        rubric_assessment=None,
    ):
        """
        Create a single rubric assessment.

        Returns the rubric assessment with the given id.
        The returned object also provides the information of
          :ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            The id of the course
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - rubric_association_id
        """
            The id of the object with which this rubric assessment is associated
        """
        path["rubric_association_id"] = rubric_association_id

        # OPTIONAL - provisional
        """
            (optional) Indicates whether this assessment is provisional, defaults to false.
        """
        if provisional is not None:
            data["provisional"] = provisional

        # OPTIONAL - final
        """
            (optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false.
        """
        if final is not None:
            data["final"] = final

        # OPTIONAL - graded_anonymously
        """
            (optional) Defaults to false
        """
        if graded_anonymously is not None:
            data["graded_anonymously"] = graded_anonymously

        # OPTIONAL - rubric_assessment
        """
            A Hash of data to complement the rubric assessment:
        The user id that refers to the person being assessed
          rubric_assessment[user_id]
        Assessment type. There are only three valid types:  'grading', 'peer_review', or 'provisional_grade'
          rubric_assessment[assessment_type]
        The points awarded for this row.
          rubric_assessment[criterion_id][points]
        Comments to add for this row.
          rubric_assessment[criterion_id][comments]
        For each criterion_id, change the id by the criterion number, ex: criterion_123
        If the criterion_id is not specified it defaults to false, and nothing is updated.
        """
        if rubric_assessment is not None:
            data["rubric_assessment"] = rubric_assessment

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def update_single_rubric_assessment(
        self,
        course_id,
        id,
        rubric_association_id,
        final=None,
        graded_anonymously=None,
        provisional=None,
        rubric_assessment=None,
    ):
        """
        Update a single rubric assessment.

        Returns the rubric assessment with the given id.
        The returned object also provides the information of
          :ratings, :assessor_name, :related_group_submissions_and_assessments, :artifact
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            The id of the rubric assessment
        """
        path["id"] = id

        # REQUIRED - PATH - course_id
        """
            The id of the course
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - rubric_association_id
        """
            The id of the object with which this rubric assessment is associated
        """
        path["rubric_association_id"] = rubric_association_id

        # OPTIONAL - provisional
        """
            (optional) Indicates whether this assessment is provisional, defaults to false.
        """
        if provisional is not None:
            data["provisional"] = provisional

        # OPTIONAL - final
        """
            (optional) Indicates a provisional grade will be marked as final. It only takes effect if the provisional param is passed as true. Defaults to false.
        """
        if final is not None:
            data["final"] = final

        # OPTIONAL - graded_anonymously
        """
            (optional) Defaults to false
        """
        if graded_anonymously is not None:
            data["graded_anonymously"] = graded_anonymously

        # OPTIONAL - rubric_assessment
        """
            A Hash of data to complement the rubric assessment:
        The user id that refers to the person being assessed
          rubric_assessment[user_id]
        Assessment type. There are only three valid types:  'grading', 'peer_review', or 'provisional_grade'
          rubric_assessment[assessment_type]
        The points awarded for this row.
          rubric_assessment[criterion_id][points]
        Comments to add for this row.
          rubric_assessment[criterion_id][comments]
        For each criterion_id, change the id by the criterion number, ex: criterion_123
        If the criterion_id is not specified it defaults to false, and nothing is updated.
        """
        if rubric_assessment is not None:
            data["rubric_assessment"] = rubric_assessment

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id}".format(
                **path
            ),
            data=data,
            params=params,
            no_data=True,
        )

    def delete_single_rubric_assessment(self, course_id, id, rubric_association_id):
        """
        Delete a single rubric assessment.

        Deletes a rubric assessment
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # REQUIRED - PATH - rubric_association_id
        """
            ID
        """
        path["rubric_association_id"] = rubric_association_id

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id

        self.logger.debug(
            "DELETE /api/v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/courses/{course_id}/rubric_associations/{rubric_association_id}/rubric_assessments/{id}".format(
                **path
            ),
            data=data,
            params=params,
            single_item=True,
        )

    def create_rubricassociation(
        self,
        course_id,
        rubric_association_association_id=None,
        rubric_association_association_type=None,
        rubric_association_bookmarked=None,
        rubric_association_hide_score_total=None,
        rubric_association_purpose=None,
        rubric_association_rubric_id=None,
        rubric_association_title=None,
        rubric_association_use_for_grading=None,
    ):
        """
        Create a RubricAssociation.

        Returns the rubric with the given id.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - course_id
        """
            ID
        """
        path["course_id"] = course_id

        # OPTIONAL - rubric_association[rubric_id]
        """
            The id of the Rubric
        """
        if rubric_association_rubric_id is not None:
            data["rubric_association[rubric_id]"] = rubric_association_rubric_id

        # OPTIONAL - rubric_association[association_id]
        """
            The id of the object with which this rubric is associated
        """
        if rubric_association_association_id is not None:
            data[
                "rubric_association[association_id]"
            ] = rubric_association_association_id

        # OPTIONAL - rubric_association[association_type]
        """
            The type of object this rubric is associated with
        """
        if rubric_association_association_type is not None:
            self._validate_enum(
                rubric_association_association_type, ["Assignment", "Course", "Account"]
            )
            data[
                "rubric_association[association_type]"
            ] = rubric_association_association_type

        # OPTIONAL - rubric_association[title]
        """
            The name of the object this rubric is associated with
        """
        if rubric_association_title is not None:
            data["rubric_association[title]"] = rubric_association_title

        # OPTIONAL - rubric_association[use_for_grading]
        """
            Whether or not the associated rubric is used for grade calculation
        """
        if rubric_association_use_for_grading is not None:
            data[
                "rubric_association[use_for_grading]"
            ] = rubric_association_use_for_grading

        # OPTIONAL - rubric_association[hide_score_total]
        """
            Whether or not the score total is displayed within the rubric.
        This option is only available if the rubric is not used for grading.
        """
        if rubric_association_hide_score_total is not None:
            data[
                "rubric_association[hide_score_total]"
            ] = rubric_association_hide_score_total

        # OPTIONAL - rubric_association[purpose]
        """
            Whether or not the association is for grading (and thus linked to an assignment)
        or if it's to indicate the rubric should appear in its context
        """
        if rubric_association_purpose is not None:
            self._validate_enum(rubric_association_purpose, ["grading", "bookmark"])
            data["rubric_association[purpose]"] = rubric_association_purpose

        # OPTIONAL - rubric_association[bookmarked]
        """
            Whether or not the associated rubric appears in its context
        """
        if rubric_association_bookmarked is not None:
            data["rubric_association[bookmarked]"] = rubric_association_bookmarked

        self.logger.debug(
            "POST /api/v1/courses/{course_id}/rubric_associations with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "POST",
            "/api/v1/courses/{course_id}/rubric_associations".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def update_rubricassociation(
        self,
        course_id,
        id,
        rubric_association_association_id=None,
        rubric_association_association_type=None,
        rubric_association_bookmarked=None,
        rubric_association_hide_score_total=None,
        rubric_association_purpose=None,
        rubric_association_rubric_id=None,
        rubric_association_title=None,
        rubric_association_use_for_grading=None,
    ):
        """
        Update a RubricAssociation.

        Returns the rubric with the given id.
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
            The id of the RubricAssociation to update
        """
        path["id"] = id

        # OPTIONAL - rubric_association[rubric_id]
        """
            The id of the Rubric
        """
        if rubric_association_rubric_id is not None:
            data["rubric_association[rubric_id]"] = rubric_association_rubric_id

        # OPTIONAL - rubric_association[association_id]
        """
            The id of the object with which this rubric is associated
        """
        if rubric_association_association_id is not None:
            data[
                "rubric_association[association_id]"
            ] = rubric_association_association_id

        # OPTIONAL - rubric_association[association_type]
        """
            The type of object this rubric is associated with
        """
        if rubric_association_association_type is not None:
            self._validate_enum(
                rubric_association_association_type, ["Assignment", "Course", "Account"]
            )
            data[
                "rubric_association[association_type]"
            ] = rubric_association_association_type

        # OPTIONAL - rubric_association[title]
        """
            The name of the object this rubric is associated with
        """
        if rubric_association_title is not None:
            data["rubric_association[title]"] = rubric_association_title

        # OPTIONAL - rubric_association[use_for_grading]
        """
            Whether or not the associated rubric is used for grade calculation
        """
        if rubric_association_use_for_grading is not None:
            data[
                "rubric_association[use_for_grading]"
            ] = rubric_association_use_for_grading

        # OPTIONAL - rubric_association[hide_score_total]
        """
            Whether or not the score total is displayed within the rubric.
        This option is only available if the rubric is not used for grading.
        """
        if rubric_association_hide_score_total is not None:
            data[
                "rubric_association[hide_score_total]"
            ] = rubric_association_hide_score_total

        # OPTIONAL - rubric_association[purpose]
        """
            Whether or not the association is for grading (and thus linked to an assignment)
        or if it's to indicate the rubric should appear in its context
        """
        if rubric_association_purpose is not None:
            self._validate_enum(rubric_association_purpose, ["grading", "bookmark"])
            data["rubric_association[purpose]"] = rubric_association_purpose

        # OPTIONAL - rubric_association[bookmarked]
        """
            Whether or not the associated rubric appears in its context
        """
        if rubric_association_bookmarked is not None:
            data["rubric_association[bookmarked]"] = rubric_association_bookmarked

        self.logger.debug(
            "PUT /api/v1/courses/{course_id}/rubric_associations/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "PUT",
            "/api/v1/courses/{course_id}/rubric_associations/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )

    def delete_rubricassociation(self, course_id, id):
        """
        Delete a RubricAssociation.

        Delete the RubricAssociation with the given ID
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
            "DELETE /api/v1/courses/{course_id}/rubric_associations/{id} with query params: {params} and form data: {data}".format(
                params=params, data=data, **path
            )
        )
        return self.generic_request(
            "DELETE",
            "/api/v1/courses/{course_id}/rubric_associations/{id}".format(**path),
            data=data,
            params=params,
            single_item=True,
        )


class Rubric(BaseModel):
    """Rubric Model."""

    def __init__(
        self,
        id=None,
        title=None,
        context_id=None,
        context_type=None,
        points_possible=None,
        reusable=None,
        read_only=None,
        free_form_criterion_comments=None,
        hide_score_total=None,
        data=None,
        assessments=None,
        associations=None,
    ):
        """Init method for Rubric class."""
        self._id = id
        self._title = title
        self._context_id = context_id
        self._context_type = context_type
        self._points_possible = points_possible
        self._reusable = reusable
        self._read_only = read_only
        self._free_form_criterion_comments = free_form_criterion_comments
        self._hide_score_total = hide_score_total
        self._data = data
        self._assessments = assessments
        self._associations = associations

        self.logger = logging.getLogger("py3canvas.Rubric")

    @property
    def id(self):
        """the ID of the rubric."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def title(self):
        """title of the rubric."""
        return self._title

    @title.setter
    def title(self, value):
        """Setter for title property."""
        self.logger.warn(
            "Setting values on title will NOT update the remote Canvas instance."
        )
        self._title = value

    @property
    def context_id(self):
        """the context owning the rubric."""
        return self._context_id

    @context_id.setter
    def context_id(self, value):
        """Setter for context_id property."""
        self.logger.warn(
            "Setting values on context_id will NOT update the remote Canvas instance."
        )
        self._context_id = value

    @property
    def context_type(self):
        """context_type."""
        return self._context_type

    @context_type.setter
    def context_type(self, value):
        """Setter for context_type property."""
        self.logger.warn(
            "Setting values on context_type will NOT update the remote Canvas instance."
        )
        self._context_type = value

    @property
    def points_possible(self):
        """points_possible."""
        return self._points_possible

    @points_possible.setter
    def points_possible(self, value):
        """Setter for points_possible property."""
        self.logger.warn(
            "Setting values on points_possible will NOT update the remote Canvas instance."
        )
        self._points_possible = value

    @property
    def reusable(self):
        """reusable."""
        return self._reusable

    @reusable.setter
    def reusable(self, value):
        """Setter for reusable property."""
        self.logger.warn(
            "Setting values on reusable will NOT update the remote Canvas instance."
        )
        self._reusable = value

    @property
    def read_only(self):
        """read_only."""
        return self._read_only

    @read_only.setter
    def read_only(self, value):
        """Setter for read_only property."""
        self.logger.warn(
            "Setting values on read_only will NOT update the remote Canvas instance."
        )
        self._read_only = value

    @property
    def free_form_criterion_comments(self):
        """whether or not free-form comments are used."""
        return self._free_form_criterion_comments

    @free_form_criterion_comments.setter
    def free_form_criterion_comments(self, value):
        """Setter for free_form_criterion_comments property."""
        self.logger.warn(
            "Setting values on free_form_criterion_comments will NOT update the remote Canvas instance."
        )
        self._free_form_criterion_comments = value

    @property
    def hide_score_total(self):
        """hide_score_total."""
        return self._hide_score_total

    @hide_score_total.setter
    def hide_score_total(self, value):
        """Setter for hide_score_total property."""
        self.logger.warn(
            "Setting values on hide_score_total will NOT update the remote Canvas instance."
        )
        self._hide_score_total = value

    @property
    def data(self):
        """An array with all of this Rubric's grading Criteria."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn(
            "Setting values on data will NOT update the remote Canvas instance."
        )
        self._data = value

    @property
    def assessments(self):
        """If an assessment type is included in the 'include' parameter, includes an array of rubric assessment objects for a given rubric, based on the assessment type requested. If the user does not request an assessment type this key will be absent."""
        return self._assessments

    @assessments.setter
    def assessments(self, value):
        """Setter for assessments property."""
        self.logger.warn(
            "Setting values on assessments will NOT update the remote Canvas instance."
        )
        self._assessments = value

    @property
    def associations(self):
        """If an association type is included in the 'include' parameter, includes an array of rubric association objects for a given rubric, based on the association type requested. If the user does not request an association type this key will be absent."""
        return self._associations

    @associations.setter
    def associations(self, value):
        """Setter for associations property."""
        self.logger.warn(
            "Setting values on associations will NOT update the remote Canvas instance."
        )
        self._associations = value


class Rubriccriterion(BaseModel):
    """Rubriccriterion Model."""

    def __init__(
        self,
        id=None,
        description=None,
        long_description=None,
        points=None,
        criterion_use_range=None,
        ratings=None,
    ):
        """Init method for Rubriccriterion class."""
        self._id = id
        self._description = description
        self._long_description = long_description
        self._points = points
        self._criterion_use_range = criterion_use_range
        self._ratings = ratings

        self.logger = logging.getLogger("py3canvas.Rubriccriterion")

    @property
    def id(self):
        """the ID of the criterion."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn(
            "Setting values on description will NOT update the remote Canvas instance."
        )
        self._description = value

    @property
    def long_description(self):
        """long_description."""
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        """Setter for long_description property."""
        self.logger.warn(
            "Setting values on long_description will NOT update the remote Canvas instance."
        )
        self._long_description = value

    @property
    def points(self):
        """points."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn(
            "Setting values on points will NOT update the remote Canvas instance."
        )
        self._points = value

    @property
    def criterion_use_range(self):
        """criterion_use_range."""
        return self._criterion_use_range

    @criterion_use_range.setter
    def criterion_use_range(self, value):
        """Setter for criterion_use_range property."""
        self.logger.warn(
            "Setting values on criterion_use_range will NOT update the remote Canvas instance."
        )
        self._criterion_use_range = value

    @property
    def ratings(self):
        """the possible ratings for this Criterion."""
        return self._ratings

    @ratings.setter
    def ratings(self, value):
        """Setter for ratings property."""
        self.logger.warn(
            "Setting values on ratings will NOT update the remote Canvas instance."
        )
        self._ratings = value


class Rubricrating(BaseModel):
    """Rubricrating Model."""

    def __init__(
        self,
        id=None,
        criterion_id=None,
        description=None,
        long_description=None,
        points=None,
    ):
        """Init method for Rubricrating class."""
        self._id = id
        self._criterion_id = criterion_id
        self._description = description
        self._long_description = long_description
        self._points = points

        self.logger = logging.getLogger("py3canvas.Rubricrating")

    @property
    def id(self):
        """id."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def criterion_id(self):
        """criterion_id."""
        return self._criterion_id

    @criterion_id.setter
    def criterion_id(self, value):
        """Setter for criterion_id property."""
        self.logger.warn(
            "Setting values on criterion_id will NOT update the remote Canvas instance."
        )
        self._criterion_id = value

    @property
    def description(self):
        """description."""
        return self._description

    @description.setter
    def description(self, value):
        """Setter for description property."""
        self.logger.warn(
            "Setting values on description will NOT update the remote Canvas instance."
        )
        self._description = value

    @property
    def long_description(self):
        """long_description."""
        return self._long_description

    @long_description.setter
    def long_description(self, value):
        """Setter for long_description property."""
        self.logger.warn(
            "Setting values on long_description will NOT update the remote Canvas instance."
        )
        self._long_description = value

    @property
    def points(self):
        """points."""
        return self._points

    @points.setter
    def points(self, value):
        """Setter for points property."""
        self.logger.warn(
            "Setting values on points will NOT update the remote Canvas instance."
        )
        self._points = value


class Rubricassessment(BaseModel):
    """Rubricassessment Model."""

    def __init__(
        self,
        id=None,
        rubric_id=None,
        rubric_association_id=None,
        score=None,
        artifact_type=None,
        artifact_id=None,
        artifact_attempt=None,
        assessment_type=None,
        assessor_id=None,
        data=None,
        comments=None,
    ):
        """Init method for Rubricassessment class."""
        self._id = id
        self._rubric_id = rubric_id
        self._rubric_association_id = rubric_association_id
        self._score = score
        self._artifact_type = artifact_type
        self._artifact_id = artifact_id
        self._artifact_attempt = artifact_attempt
        self._assessment_type = assessment_type
        self._assessor_id = assessor_id
        self._data = data
        self._comments = comments

        self.logger = logging.getLogger("py3canvas.Rubricassessment")

    @property
    def id(self):
        """the ID of the rubric."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def rubric_id(self):
        """the rubric the assessment belongs to."""
        return self._rubric_id

    @rubric_id.setter
    def rubric_id(self, value):
        """Setter for rubric_id property."""
        self.logger.warn(
            "Setting values on rubric_id will NOT update the remote Canvas instance."
        )
        self._rubric_id = value

    @property
    def rubric_association_id(self):
        """rubric_association_id."""
        return self._rubric_association_id

    @rubric_association_id.setter
    def rubric_association_id(self, value):
        """Setter for rubric_association_id property."""
        self.logger.warn(
            "Setting values on rubric_association_id will NOT update the remote Canvas instance."
        )
        self._rubric_association_id = value

    @property
    def score(self):
        """score."""
        return self._score

    @score.setter
    def score(self, value):
        """Setter for score property."""
        self.logger.warn(
            "Setting values on score will NOT update the remote Canvas instance."
        )
        self._score = value

    @property
    def artifact_type(self):
        """the object of the assessment."""
        return self._artifact_type

    @artifact_type.setter
    def artifact_type(self, value):
        """Setter for artifact_type property."""
        self.logger.warn(
            "Setting values on artifact_type will NOT update the remote Canvas instance."
        )
        self._artifact_type = value

    @property
    def artifact_id(self):
        """the id of the object of the assessment."""
        return self._artifact_id

    @artifact_id.setter
    def artifact_id(self, value):
        """Setter for artifact_id property."""
        self.logger.warn(
            "Setting values on artifact_id will NOT update the remote Canvas instance."
        )
        self._artifact_id = value

    @property
    def artifact_attempt(self):
        """the current number of attempts made on the object of the assessment."""
        return self._artifact_attempt

    @artifact_attempt.setter
    def artifact_attempt(self, value):
        """Setter for artifact_attempt property."""
        self.logger.warn(
            "Setting values on artifact_attempt will NOT update the remote Canvas instance."
        )
        self._artifact_attempt = value

    @property
    def assessment_type(self):
        """the type of assessment. values will be either 'grading', 'peer_review', or 'provisional_grade'."""
        return self._assessment_type

    @assessment_type.setter
    def assessment_type(self, value):
        """Setter for assessment_type property."""
        self.logger.warn(
            "Setting values on assessment_type will NOT update the remote Canvas instance."
        )
        self._assessment_type = value

    @property
    def assessor_id(self):
        """user id of the person who made the assessment."""
        return self._assessor_id

    @assessor_id.setter
    def assessor_id(self, value):
        """Setter for assessor_id property."""
        self.logger.warn(
            "Setting values on assessor_id will NOT update the remote Canvas instance."
        )
        self._assessor_id = value

    @property
    def data(self):
        """(Optional) If 'full' is included in the 'style' parameter, returned assessments will have their full details contained in their data hash. If the user does not request a style, this key will be absent."""
        return self._data

    @data.setter
    def data(self, value):
        """Setter for data property."""
        self.logger.warn(
            "Setting values on data will NOT update the remote Canvas instance."
        )
        self._data = value

    @property
    def comments(self):
        """(Optional) If 'comments_only' is included in the 'style' parameter, returned assessments will include only the comments portion of their data hash. If the user does not request a style, this key will be absent."""
        return self._comments

    @comments.setter
    def comments(self, value):
        """Setter for comments property."""
        self.logger.warn(
            "Setting values on comments will NOT update the remote Canvas instance."
        )
        self._comments = value


class Rubricassociation(BaseModel):
    """Rubricassociation Model."""

    def __init__(
        self,
        id=None,
        rubric_id=None,
        association_id=None,
        association_type=None,
        use_for_grading=None,
        summary_data=None,
        purpose=None,
        hide_score_total=None,
        hide_points=None,
        hide_outcome_results=None,
    ):
        """Init method for Rubricassociation class."""
        self._id = id
        self._rubric_id = rubric_id
        self._association_id = association_id
        self._association_type = association_type
        self._use_for_grading = use_for_grading
        self._summary_data = summary_data
        self._purpose = purpose
        self._hide_score_total = hide_score_total
        self._hide_points = hide_points
        self._hide_outcome_results = hide_outcome_results

        self.logger = logging.getLogger("py3canvas.Rubricassociation")

    @property
    def id(self):
        """the ID of the association."""
        return self._id

    @id.setter
    def id(self, value):
        """Setter for id property."""
        self.logger.warn(
            "Setting values on id will NOT update the remote Canvas instance."
        )
        self._id = value

    @property
    def rubric_id(self):
        """the ID of the rubric."""
        return self._rubric_id

    @rubric_id.setter
    def rubric_id(self, value):
        """Setter for rubric_id property."""
        self.logger.warn(
            "Setting values on rubric_id will NOT update the remote Canvas instance."
        )
        self._rubric_id = value

    @property
    def association_id(self):
        """the ID of the object this association links to."""
        return self._association_id

    @association_id.setter
    def association_id(self, value):
        """Setter for association_id property."""
        self.logger.warn(
            "Setting values on association_id will NOT update the remote Canvas instance."
        )
        self._association_id = value

    @property
    def association_type(self):
        """the type of object this association links to."""
        return self._association_type

    @association_type.setter
    def association_type(self, value):
        """Setter for association_type property."""
        self.logger.warn(
            "Setting values on association_type will NOT update the remote Canvas instance."
        )
        self._association_type = value

    @property
    def use_for_grading(self):
        """Whether or not the associated rubric is used for grade calculation."""
        return self._use_for_grading

    @use_for_grading.setter
    def use_for_grading(self, value):
        """Setter for use_for_grading property."""
        self.logger.warn(
            "Setting values on use_for_grading will NOT update the remote Canvas instance."
        )
        self._use_for_grading = value

    @property
    def summary_data(self):
        """summary_data."""
        return self._summary_data

    @summary_data.setter
    def summary_data(self, value):
        """Setter for summary_data property."""
        self.logger.warn(
            "Setting values on summary_data will NOT update the remote Canvas instance."
        )
        self._summary_data = value

    @property
    def purpose(self):
        """Whether or not the association is for grading (and thus linked to an assignment) or if it's to indicate the rubric should appear in its context. Values will be grading or bookmark."""
        return self._purpose

    @purpose.setter
    def purpose(self, value):
        """Setter for purpose property."""
        self.logger.warn(
            "Setting values on purpose will NOT update the remote Canvas instance."
        )
        self._purpose = value

    @property
    def hide_score_total(self):
        """Whether or not the score total is displayed within the rubric. This option is only available if the rubric is not used for grading."""
        return self._hide_score_total

    @hide_score_total.setter
    def hide_score_total(self, value):
        """Setter for hide_score_total property."""
        self.logger.warn(
            "Setting values on hide_score_total will NOT update the remote Canvas instance."
        )
        self._hide_score_total = value

    @property
    def hide_points(self):
        """hide_points."""
        return self._hide_points

    @hide_points.setter
    def hide_points(self, value):
        """Setter for hide_points property."""
        self.logger.warn(
            "Setting values on hide_points will NOT update the remote Canvas instance."
        )
        self._hide_points = value

    @property
    def hide_outcome_results(self):
        """hide_outcome_results."""
        return self._hide_outcome_results

    @hide_outcome_results.setter
    def hide_outcome_results(self, value):
        """Setter for hide_outcome_results property."""
        self.logger.warn(
            "Setting values on hide_outcome_results will NOT update the remote Canvas instance."
        )
        self._hide_outcome_results = value
