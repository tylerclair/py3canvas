"""SharedBrandConfigs API Tests for Version 1.0.

This is a testing template for the generated SharedBrandConfigsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.shared_brand_configs import SharedBrandConfigsAPI
from py3canvas.apis.shared_brand_configs import Sharedbrandconfig


class TestSharedBrandConfigsAPI(unittest.TestCase):
    """Tests for the SharedBrandConfigsAPI."""

    def setUp(self):
        self.client = SharedBrandConfigsAPI(secrets.instance_address, secrets.access_token)

    def test_share_brandconfig_theme(self):
        """Integration test for the SharedBrandConfigsAPI.share_brandconfig_theme method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_update_shared_theme(self):
        """Integration test for the SharedBrandConfigsAPI.update_shared_theme method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_un_share_brandconfig_theme(self):
        """Integration test for the SharedBrandConfigsAPI.un_share_brandconfig_theme method."""
        id = None  # Change me!!

        r = self.client.un_share_brandconfig_theme(id)

