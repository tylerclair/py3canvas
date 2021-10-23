"""ContentMigrations API Tests for Version 1.0.

This is a testing template for the generated ContentMigrationsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.content_migrations import ContentMigrationsAPI
from py3canvas.apis.content_migrations import Migrationissue
from py3canvas.apis.content_migrations import Contentmigration
from py3canvas.apis.content_migrations import Migrator


class TestContentMigrationsAPI(unittest.TestCase):
    """Tests for the ContentMigrationsAPI."""

    def setUp(self):
        self.client = ContentMigrationsAPI(secrets.instance_address, secrets.access_token)

    def test_list_migration_issues_accounts(self):
        """Integration test for the ContentMigrationsAPI.list_migration_issues_accounts method."""
        account_id = None  # Change me!!
        content_migration_id = None  # Change me!!

        r = self.client.list_migration_issues_accounts(account_id, content_migration_id)

    def test_list_migration_issues_courses(self):
        """Integration test for the ContentMigrationsAPI.list_migration_issues_courses method."""
        course_id = None  # Change me!!
        content_migration_id = None  # Change me!!

        r = self.client.list_migration_issues_courses(content_migration_id, course_id)

    def test_list_migration_issues_groups(self):
        """Integration test for the ContentMigrationsAPI.list_migration_issues_groups method."""
        group_id = None  # Change me!!
        content_migration_id = None  # Change me!!

        r = self.client.list_migration_issues_groups(content_migration_id, group_id)

    def test_list_migration_issues_users(self):
        """Integration test for the ContentMigrationsAPI.list_migration_issues_users method."""
        user_id = None  # Change me!!
        content_migration_id = None  # Change me!!

        r = self.client.list_migration_issues_users(content_migration_id, user_id)

    def test_get_migration_issue_accounts(self):
        """Integration test for the ContentMigrationsAPI.get_migration_issue_accounts method."""
        account_id = None  # Change me!!
        content_migration_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_migration_issue_accounts(account_id, content_migration_id, id)

    def test_get_migration_issue_courses(self):
        """Integration test for the ContentMigrationsAPI.get_migration_issue_courses method."""
        course_id = None  # Change me!!
        content_migration_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_migration_issue_courses(content_migration_id, course_id, id)

    def test_get_migration_issue_groups(self):
        """Integration test for the ContentMigrationsAPI.get_migration_issue_groups method."""
        group_id = None  # Change me!!
        content_migration_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_migration_issue_groups(content_migration_id, group_id, id)

    def test_get_migration_issue_users(self):
        """Integration test for the ContentMigrationsAPI.get_migration_issue_users method."""
        user_id = None  # Change me!!
        content_migration_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_migration_issue_users(content_migration_id, id, user_id)

    def test_update_migration_issue_accounts(self):
        """Integration test for the ContentMigrationsAPI.update_migration_issue_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_migration_issue_courses(self):
        """Integration test for the ContentMigrationsAPI.update_migration_issue_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_migration_issue_groups(self):
        """Integration test for the ContentMigrationsAPI.update_migration_issue_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_migration_issue_users(self):
        """Integration test for the ContentMigrationsAPI.update_migration_issue_users method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_content_migrations_accounts(self):
        """Integration test for the ContentMigrationsAPI.list_content_migrations_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_content_migrations_accounts(account_id)

    def test_list_content_migrations_courses(self):
        """Integration test for the ContentMigrationsAPI.list_content_migrations_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_content_migrations_courses(course_id)

    def test_list_content_migrations_groups(self):
        """Integration test for the ContentMigrationsAPI.list_content_migrations_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_content_migrations_groups(group_id)

    def test_list_content_migrations_users(self):
        """Integration test for the ContentMigrationsAPI.list_content_migrations_users method."""
        user_id = None  # Change me!!

        r = self.client.list_content_migrations_users(user_id)

    def test_get_content_migration_accounts(self):
        """Integration test for the ContentMigrationsAPI.get_content_migration_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_content_migration_accounts(account_id, id)

    def test_get_content_migration_courses(self):
        """Integration test for the ContentMigrationsAPI.get_content_migration_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_content_migration_courses(course_id, id)

    def test_get_content_migration_groups(self):
        """Integration test for the ContentMigrationsAPI.get_content_migration_groups method."""
        group_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_content_migration_groups(group_id, id)

    def test_get_content_migration_users(self):
        """Integration test for the ContentMigrationsAPI.get_content_migration_users method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_content_migration_users(id, user_id)

    def test_create_content_migration_accounts(self):
        """Integration test for the ContentMigrationsAPI.create_content_migration_accounts method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_content_migration_courses(self):
        """Integration test for the ContentMigrationsAPI.create_content_migration_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_content_migration_groups(self):
        """Integration test for the ContentMigrationsAPI.create_content_migration_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_content_migration_users(self):
        """Integration test for the ContentMigrationsAPI.create_content_migration_users method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_content_migration_accounts(self):
        """Integration test for the ContentMigrationsAPI.update_content_migration_accounts method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_content_migration_courses(self):
        """Integration test for the ContentMigrationsAPI.update_content_migration_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_content_migration_groups(self):
        """Integration test for the ContentMigrationsAPI.update_content_migration_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_content_migration_users(self):
        """Integration test for the ContentMigrationsAPI.update_content_migration_users method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_migration_systems_accounts(self):
        """Integration test for the ContentMigrationsAPI.list_migration_systems_accounts method."""
        account_id = None  # Change me!!

        r = self.client.list_migration_systems_accounts(account_id)

    def test_list_migration_systems_courses(self):
        """Integration test for the ContentMigrationsAPI.list_migration_systems_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_migration_systems_courses(course_id)

    def test_list_migration_systems_groups(self):
        """Integration test for the ContentMigrationsAPI.list_migration_systems_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_migration_systems_groups(group_id)

    def test_list_migration_systems_users(self):
        """Integration test for the ContentMigrationsAPI.list_migration_systems_users method."""
        user_id = None  # Change me!!

        r = self.client.list_migration_systems_users(user_id)

    def test_list_items_for_selective_import_accounts(self):
        """Integration test for the ContentMigrationsAPI.list_items_for_selective_import_accounts method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_items_for_selective_import_accounts(account_id, id, type=None)

    def test_list_items_for_selective_import_courses(self):
        """Integration test for the ContentMigrationsAPI.list_items_for_selective_import_courses method."""
        course_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_items_for_selective_import_courses(course_id, id, type=None)

    def test_list_items_for_selective_import_groups(self):
        """Integration test for the ContentMigrationsAPI.list_items_for_selective_import_groups method."""
        group_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_items_for_selective_import_groups(group_id, id, type=None)

    def test_list_items_for_selective_import_users(self):
        """Integration test for the ContentMigrationsAPI.list_items_for_selective_import_users method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.list_items_for_selective_import_users(id, user_id, type=None)

