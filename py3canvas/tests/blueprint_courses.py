"""BlueprintCourses API Tests for Version 1.0.

This is a testing template for the generated BlueprintCoursesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.blueprint_courses import BlueprintCoursesAPI
from py3canvas.apis.blueprint_courses import Blueprinttemplate
from py3canvas.apis.blueprint_courses import Blueprintmigration
from py3canvas.apis.blueprint_courses import Blueprintrestriction
from py3canvas.apis.blueprint_courses import Changerecord
from py3canvas.apis.blueprint_courses import Exceptionrecord
from py3canvas.apis.blueprint_courses import Blueprintsubscription


class TestBlueprintCoursesAPI(unittest.TestCase):
    """Tests for the BlueprintCoursesAPI."""

    def setUp(self):
        self.client = BlueprintCoursesAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_get_blueprint_information(self):
        """Integration test for the BlueprintCoursesAPI.get_blueprint_information method."""
        course_id = None  # Change me!!
        template_id = None  # Change me!!

        r = self.client.get_blueprint_information(course_id, template_id)

    def test_get_associated_course_information(self):
        """Integration test for the BlueprintCoursesAPI.get_associated_course_information method."""
        course_id = None  # Change me!!
        template_id = None  # Change me!!

        r = self.client.get_associated_course_information(course_id, template_id)

    def test_update_associated_courses(self):
        """Integration test for the BlueprintCoursesAPI.update_associated_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_begin_migration_to_push_to_associated_courses(self):
        """Integration test for the BlueprintCoursesAPI.begin_migration_to_push_to_associated_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_set_or_remove_restrictions_on_blueprint_course_object(self):
        """Integration test for the BlueprintCoursesAPI.set_or_remove_restrictions_on_blueprint_course_object method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_unsynced_changes(self):
        """Integration test for the BlueprintCoursesAPI.get_unsynced_changes method."""
        course_id = None  # Change me!!
        template_id = None  # Change me!!

        r = self.client.get_unsynced_changes(course_id, template_id)

    def test_list_blueprint_migrations(self):
        """Integration test for the BlueprintCoursesAPI.list_blueprint_migrations method."""
        course_id = None  # Change me!!
        template_id = None  # Change me!!

        r = self.client.list_blueprint_migrations(course_id, template_id)

    def test_show_blueprint_migration(self):
        """Integration test for the BlueprintCoursesAPI.show_blueprint_migration method."""
        course_id = None  # Change me!!
        template_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_blueprint_migration(course_id, id, template_id)

    def test_get_migration_details(self):
        """Integration test for the BlueprintCoursesAPI.get_migration_details method."""
        course_id = None  # Change me!!
        template_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_migration_details(course_id, id, template_id)

    def test_list_blueprint_subscriptions(self):
        """Integration test for the BlueprintCoursesAPI.list_blueprint_subscriptions method."""
        course_id = None  # Change me!!

        r = self.client.list_blueprint_subscriptions(course_id)

    def test_list_blueprint_imports(self):
        """Integration test for the BlueprintCoursesAPI.list_blueprint_imports method."""
        course_id = None  # Change me!!
        subscription_id = None  # Change me!!

        r = self.client.list_blueprint_imports(course_id, subscription_id)

    def test_show_blueprint_import(self):
        """Integration test for the BlueprintCoursesAPI.show_blueprint_import method."""
        course_id = None  # Change me!!
        subscription_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.show_blueprint_import(course_id, id, subscription_id)

    def test_get_import_details(self):
        """Integration test for the BlueprintCoursesAPI.get_import_details method."""
        course_id = None  # Change me!!
        subscription_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_import_details(course_id, id, subscription_id)
