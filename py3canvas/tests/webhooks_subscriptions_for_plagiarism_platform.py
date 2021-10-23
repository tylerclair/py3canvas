"""WebhooksSubscriptionsForPlagiarismPlatform API Tests for Version 1.0.

This is a testing template for the generated WebhooksSubscriptionsForPlagiarismPlatformAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.webhooks_subscriptions_for_plagiarism_platform import WebhooksSubscriptionsForPlagiarismPlatformAPI


class TestWebhooksSubscriptionsForPlagiarismPlatformAPI(unittest.TestCase):
    """Tests for the WebhooksSubscriptionsForPlagiarismPlatformAPI."""

    def setUp(self):
        self.client = WebhooksSubscriptionsForPlagiarismPlatformAPI(secrets.instance_address, secrets.access_token)

    def test_create_webhook_subscription(self):
        """Integration test for the WebhooksSubscriptionsForPlagiarismPlatformAPI.create_webhook_subscription method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_webhook_subscription(self):
        """Integration test for the WebhooksSubscriptionsForPlagiarismPlatformAPI.delete_webhook_subscription method."""
        id = None  # Change me!!

        r = self.client.delete_webhook_subscription(id)

    def test_show_single_webhook_subscription(self):
        """Integration test for the WebhooksSubscriptionsForPlagiarismPlatformAPI.show_single_webhook_subscription method."""
        id = None  # Change me!!

        r = self.client.show_single_webhook_subscription(id)

    def test_update_webhook_subscription(self):
        """Integration test for the WebhooksSubscriptionsForPlagiarismPlatformAPI.update_webhook_subscription method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_all_webhook_subscription_for_tool_proxy(self):
        """Integration test for the WebhooksSubscriptionsForPlagiarismPlatformAPI.list_all_webhook_subscription_for_tool_proxy method."""

        r = self.client.list_all_webhook_subscription_for_tool_proxy()

