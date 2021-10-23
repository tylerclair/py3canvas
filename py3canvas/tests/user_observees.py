"""UserObservees API Tests for Version 1.0.

This is a testing template for the generated UserObserveesAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.user_observees import UserObserveesAPI
from py3canvas.apis.user_observees import Pairingcode


class TestUserObserveesAPI(unittest.TestCase):
    """Tests for the UserObserveesAPI."""

    def setUp(self):
        self.client = UserObserveesAPI(secrets.instance_address, secrets.access_token)

    def test_list_observees(self):
        """Integration test for the UserObserveesAPI.list_observees method."""
        user_id = None  # Change me!!

        r = self.client.list_observees(user_id, include=None)

    def test_list_observers(self):
        """Integration test for the UserObserveesAPI.list_observers method."""
        user_id = None  # Change me!!

        r = self.client.list_observers(user_id, include=None)

    def test_add_observee_with_credentials(self):
        """Integration test for the UserObserveesAPI.add_observee_with_credentials method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_show_observee(self):
        """Integration test for the UserObserveesAPI.show_observee method."""
        user_id = None  # Change me!!
        observee_id = None  # Change me!!

        r = self.client.show_observee(observee_id, user_id)

    def test_show_observer(self):
        """Integration test for the UserObserveesAPI.show_observer method."""
        user_id = None  # Change me!!
        observer_id = None  # Change me!!

        r = self.client.show_observer(observer_id, user_id)

    def test_add_observee(self):
        """Integration test for the UserObserveesAPI.add_observee method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_remove_observee(self):
        """Integration test for the UserObserveesAPI.remove_observee method."""
        user_id = None  # Change me!!
        observee_id = None  # Change me!!

        r = self.client.remove_observee(observee_id, user_id, root_account_id=None)

    def test_create_observer_pairing_code(self):
        """Integration test for the UserObserveesAPI.create_observer_pairing_code method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass
