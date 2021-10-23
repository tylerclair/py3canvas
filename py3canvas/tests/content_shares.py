"""ContentShares API Tests for Version 1.0.

This is a testing template for the generated ContentSharesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.content_shares import ContentSharesAPI
from py3canvas.apis.content_shares import Contentshare


class TestContentSharesAPI(unittest.TestCase):
    """Tests for the ContentSharesAPI."""

    def setUp(self):
        self.client = ContentSharesAPI(secrets.instance_address, secrets.access_token)

    def test_create_content_share(self):
        """Integration test for the ContentSharesAPI.create_content_share method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_content_shares_sent(self):
        """Integration test for the ContentSharesAPI.list_content_shares_sent method."""
        user_id = None  # Change me!!

        r = self.client.list_content_shares_sent(user_id)

    def test_list_content_shares_received(self):
        """Integration test for the ContentSharesAPI.list_content_shares_received method."""
        user_id = None  # Change me!!

        r = self.client.list_content_shares_received(user_id)

    def test_get_unread_shares_count(self):
        """Integration test for the ContentSharesAPI.get_unread_shares_count method."""
        user_id = None  # Change me!!

        r = self.client.get_unread_shares_count(user_id)

    def test_get_content_share(self):
        """Integration test for the ContentSharesAPI.get_content_share method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_content_share(id, user_id)

    def test_remove_content_share(self):
        """Integration test for the ContentSharesAPI.remove_content_share method."""
        user_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.remove_content_share(id, user_id)

    def test_add_users_to_content_share(self):
        """Integration test for the ContentSharesAPI.add_users_to_content_share method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_content_share(self):
        """Integration test for the ContentSharesAPI.update_content_share method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

