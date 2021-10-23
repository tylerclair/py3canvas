"""AuthenticationProviders API Tests for Version 1.0.

This is a testing template for the generated AuthenticationProvidersAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.authentication_providers import AuthenticationProvidersAPI
from py3canvas.apis.authentication_providers import Authenticationprovider
from py3canvas.apis.authentication_providers import Ssosettings
from py3canvas.apis.authentication_providers import Federatedattributesconfig
from py3canvas.apis.authentication_providers import Federatedattributeconfig


class TestAuthenticationProvidersAPI(unittest.TestCase):
    """Tests for the AuthenticationProvidersAPI."""

    def setUp(self):
        self.client = AuthenticationProvidersAPI(
            secrets.instance_address, secrets.access_token
        )

    def test_list_authentication_providers(self):
        """Integration test for the AuthenticationProvidersAPI.list_authentication_providers method."""
        account_id = None  # Change me!!

        r = self.client.list_authentication_providers(account_id)

    def test_add_authentication_provider(self):
        """Integration test for the AuthenticationProvidersAPI.add_authentication_provider method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_authentication_provider(self):
        """Integration test for the AuthenticationProvidersAPI.update_authentication_provider method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_authentication_provider(self):
        """Integration test for the AuthenticationProvidersAPI.get_authentication_provider method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_authentication_provider(account_id, id)

    def test_delete_authentication_provider(self):
        """Integration test for the AuthenticationProvidersAPI.delete_authentication_provider method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.delete_authentication_provider(account_id, id)

    def test_show_account_auth_settings(self):
        """Integration test for the AuthenticationProvidersAPI.show_account_auth_settings method."""
        account_id = None  # Change me!!

        r = self.client.show_account_auth_settings(account_id)

    def test_update_account_auth_settings(self):
        """Integration test for the AuthenticationProvidersAPI.update_account_auth_settings method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass
