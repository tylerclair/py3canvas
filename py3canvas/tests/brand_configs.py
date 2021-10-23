"""BrandConfigs API Tests for Version 1.0.

This is a testing template for the generated BrandConfigsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.brand_configs import BrandConfigsAPI


class TestBrandConfigsAPI(unittest.TestCase):
    """Tests for the BrandConfigsAPI."""

    def setUp(self):
        self.client = BrandConfigsAPI(secrets.instance_address, secrets.access_token)

    def test_get_brand_config_variables_that_should_be_used_for_this_domain(self):
        """Integration test for the BrandConfigsAPI.get_brand_config_variables_that_should_be_used_for_this_domain method."""

        r = self.client.get_brand_config_variables_that_should_be_used_for_this_domain()

