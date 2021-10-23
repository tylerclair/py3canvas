"""DiscussionTopics API Tests for Version 1.0.

This is a testing template for the generated DiscussionTopicsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.discussion_topics import DiscussionTopicsAPI
from py3canvas.apis.discussion_topics import Fileattachment
from py3canvas.apis.discussion_topics import Discussiontopic


class TestDiscussionTopicsAPI(unittest.TestCase):
    """Tests for the DiscussionTopicsAPI."""

    def setUp(self):
        self.client = DiscussionTopicsAPI(secrets.instance_address, secrets.access_token)

    def test_list_discussion_topics_courses(self):
        """Integration test for the DiscussionTopicsAPI.list_discussion_topics_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_discussion_topics_courses(course_id, exclude_context_module_locked_topics=None, filter_by=None, include=None, only_announcements=None, order_by=None, scope=None, search_term=None)

    def test_list_discussion_topics_groups(self):
        """Integration test for the DiscussionTopicsAPI.list_discussion_topics_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_discussion_topics_groups(group_id, exclude_context_module_locked_topics=None, filter_by=None, include=None, only_announcements=None, order_by=None, scope=None, search_term=None)

    def test_create_new_discussion_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.create_new_discussion_topic_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_new_discussion_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.create_new_discussion_topic_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.update_topic_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.update_topic_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.delete_topic_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.delete_topic_courses(course_id, topic_id)

    def test_delete_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.delete_topic_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.delete_topic_groups(group_id, topic_id)

    def test_reorder_pinned_topics_courses(self):
        """Integration test for the DiscussionTopicsAPI.reorder_pinned_topics_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_reorder_pinned_topics_groups(self):
        """Integration test for the DiscussionTopicsAPI.reorder_pinned_topics_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_entry_courses(self):
        """Integration test for the DiscussionTopicsAPI.update_entry_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_entry_groups(self):
        """Integration test for the DiscussionTopicsAPI.update_entry_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_entry_courses(self):
        """Integration test for the DiscussionTopicsAPI.delete_entry_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_entry_courses(course_id, id, topic_id)

    def test_delete_entry_groups(self):
        """Integration test for the DiscussionTopicsAPI.delete_entry_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_entry_groups(group_id, id, topic_id)

    def test_get_single_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.get_single_topic_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.get_single_topic_courses(course_id, topic_id, include=None)

    def test_get_single_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.get_single_topic_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.get_single_topic_groups(group_id, topic_id, include=None)

    def test_get_full_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.get_full_topic_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.get_full_topic_courses(course_id, topic_id)

    def test_get_full_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.get_full_topic_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.get_full_topic_groups(group_id, topic_id)

    def test_post_entry_courses(self):
        """Integration test for the DiscussionTopicsAPI.post_entry_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_post_entry_groups(self):
        """Integration test for the DiscussionTopicsAPI.post_entry_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_duplicate_discussion_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.duplicate_discussion_topic_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_duplicate_discussion_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.duplicate_discussion_topic_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_topic_entries_courses(self):
        """Integration test for the DiscussionTopicsAPI.list_topic_entries_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.list_topic_entries_courses(course_id, topic_id)

    def test_list_topic_entries_groups(self):
        """Integration test for the DiscussionTopicsAPI.list_topic_entries_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.list_topic_entries_groups(group_id, topic_id)

    def test_post_reply_courses(self):
        """Integration test for the DiscussionTopicsAPI.post_reply_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_post_reply_groups(self):
        """Integration test for the DiscussionTopicsAPI.post_reply_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_entry_replies_courses(self):
        """Integration test for the DiscussionTopicsAPI.list_entry_replies_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!
        entry_id = None  # Change me!!

        r = self.client.list_entry_replies_courses(course_id, entry_id, topic_id)

    def test_list_entry_replies_groups(self):
        """Integration test for the DiscussionTopicsAPI.list_entry_replies_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!
        entry_id = None  # Change me!!

        r = self.client.list_entry_replies_groups(entry_id, group_id, topic_id)

    def test_list_entries_courses(self):
        """Integration test for the DiscussionTopicsAPI.list_entries_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.list_entries_courses(course_id, topic_id, ids=None)

    def test_list_entries_groups(self):
        """Integration test for the DiscussionTopicsAPI.list_entries_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.list_entries_groups(group_id, topic_id, ids=None)

    def test_mark_topic_as_read_courses(self):
        """Integration test for the DiscussionTopicsAPI.mark_topic_as_read_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_topic_as_read_groups(self):
        """Integration test for the DiscussionTopicsAPI.mark_topic_as_read_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_topic_as_unread_courses(self):
        """Integration test for the DiscussionTopicsAPI.mark_topic_as_unread_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.mark_topic_as_unread_courses(course_id, topic_id)

    def test_mark_topic_as_unread_groups(self):
        """Integration test for the DiscussionTopicsAPI.mark_topic_as_unread_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.mark_topic_as_unread_groups(group_id, topic_id)

    def test_mark_all_entries_as_read_courses(self):
        """Integration test for the DiscussionTopicsAPI.mark_all_entries_as_read_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_all_entries_as_read_groups(self):
        """Integration test for the DiscussionTopicsAPI.mark_all_entries_as_read_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_all_entries_as_unread_courses(self):
        """Integration test for the DiscussionTopicsAPI.mark_all_entries_as_unread_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.mark_all_entries_as_unread_courses(course_id, topic_id, forced_read_state=None)

    def test_mark_all_entries_as_unread_groups(self):
        """Integration test for the DiscussionTopicsAPI.mark_all_entries_as_unread_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.mark_all_entries_as_unread_groups(group_id, topic_id, forced_read_state=None)

    def test_mark_entry_as_read_courses(self):
        """Integration test for the DiscussionTopicsAPI.mark_entry_as_read_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_entry_as_read_groups(self):
        """Integration test for the DiscussionTopicsAPI.mark_entry_as_read_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_mark_entry_as_unread_courses(self):
        """Integration test for the DiscussionTopicsAPI.mark_entry_as_unread_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!
        entry_id = None  # Change me!!

        r = self.client.mark_entry_as_unread_courses(course_id, entry_id, topic_id, forced_read_state=None)

    def test_mark_entry_as_unread_groups(self):
        """Integration test for the DiscussionTopicsAPI.mark_entry_as_unread_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!
        entry_id = None  # Change me!!

        r = self.client.mark_entry_as_unread_groups(entry_id, group_id, topic_id, forced_read_state=None)

    def test_rate_entry_courses(self):
        """Integration test for the DiscussionTopicsAPI.rate_entry_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_rate_entry_groups(self):
        """Integration test for the DiscussionTopicsAPI.rate_entry_groups method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_subscribe_to_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.subscribe_to_topic_courses method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_subscribe_to_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.subscribe_to_topic_groups method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_unsubscribe_from_topic_courses(self):
        """Integration test for the DiscussionTopicsAPI.unsubscribe_from_topic_courses method."""
        course_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.unsubscribe_from_topic_courses(course_id, topic_id)

    def test_unsubscribe_from_topic_groups(self):
        """Integration test for the DiscussionTopicsAPI.unsubscribe_from_topic_groups method."""
        group_id = None  # Change me!!
        topic_id = None  # Change me!!

        r = self.client.unsubscribe_from_topic_groups(group_id, topic_id)

