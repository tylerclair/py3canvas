"""WebhooksSubscriptions API Version 1.0.

This API client was generated using a template. Make sure this code is valid before using it.
"""
import logging
from datetime import date, datetime
from .base import BaseCanvasAPI



class WebhooksSubscriptionsAPI(BaseCanvasAPI):
    """WebhooksSubscriptions API Version 1.0."""

    def __init__(self, *args, **kwargs):
        """Init method for WebhooksSubscriptionsAPI."""
        super(WebhooksSubscriptionsAPI, self).__init__(*args, **kwargs)
        self.logger = logging.getLogger("py3canvas.WebhooksSubscriptionsAPI")

    def create_webhook_subscription(self, submission_ContextId, subscription_ContextType, subscription_EventTypes, subscription_Format, subscription_TransportMetadata, subscription_TransportType):
        """
        Create a Webhook Subscription.

        Creates a webook subscription for the specified event type and
        context.
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - submission[ContextId]
        """
            The id of the context for the subscription.
        """
        data["submission[ContextId]"] = submission_ContextId


        # REQUIRED - subscription[ContextType]
        """
            The type of context for the subscription. Must be 'assignment',
        'account', or 'course'.
        """
        data["subscription[ContextType]"] = subscription_ContextType


        # REQUIRED - subscription[EventTypes]
        """
            Array of strings representing the event types for
        the subscription.
        """
        data["subscription[EventTypes]"] = subscription_EventTypes


        # REQUIRED - subscription[Format]
        """
            Format to deliver the live events. Must be 'live-event' or 'caliper'.
        """
        data["subscription[Format]"] = subscription_Format


        # REQUIRED - subscription[TransportMetadata]
        """
            An object with a single key: 'Url'. Example: { "Url": "sqs.example" }
        """
        data["subscription[TransportMetadata]"] = subscription_TransportMetadata


        # REQUIRED - subscription[TransportType]
        """
            Must be either 'sqs' or 'https'.
        """
        data["subscription[TransportType]"] = subscription_TransportType


        self.logger.debug("POST /api/lti/subscriptions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("POST", "/api/lti/subscriptions".format(**path), data=data, params=params, single_item=True)

    def delete_webhook_subscription(self, id):
        """
        Delete a Webhook Subscription.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("DELETE /api/lti/subscriptions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("DELETE", "/api/lti/subscriptions/{id}".format(**path), data=data, params=params, no_data=True)

    def show_single_webhook_subscription(self, id):
        """
        Show a single Webhook Subscription.

        
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("GET /api/lti/subscriptions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/subscriptions/{id}".format(**path), data=data, params=params, no_data=True)

    def update_webhook_subscription(self, id):
        """
        Update a Webhook Subscription.

        This endpoint uses the same parameters as the create endpoint
        """
        path = {}
        data = {}
        params = {}

        # REQUIRED - PATH - id
        """
            ID
        """
        path["id"] = id


        self.logger.debug("PUT /api/lti/subscriptions/{id} with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("PUT", "/api/lti/subscriptions/{id}".format(**path), data=data, params=params, no_data=True)

    def list_all_webhook_subscription_for_tool_proxy(self):
        """
        List all Webhook Subscription for a tool proxy.

        This endpoint returns a paginated list with a default limit of 100 items per result set.
        You can retrieve the next result set by setting a 'StartKey' header in your next request
        with the value of the 'EndKey' header in the response.
        
        Example use of a 'StartKey' header object:
          { "Id":"71d6dfba-0547-477d-b41d-db8cb528c6d1","DeveloperKey":"10000000000001" }
        """
        path = {}
        data = {}
        params = {}

        self.logger.debug("GET /api/lti/subscriptions with query params: {params} and form data: {data}".format(params=params, data=data, **path))
        return self.generic_request("GET", "/api/lti/subscriptions".format(**path), data=data, params=params, no_data=True)

