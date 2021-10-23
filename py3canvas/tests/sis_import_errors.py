"""SisImportErrors API Tests for Version 1.0.

This is a testing template for the generated SisImportErrorsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.sis_import_errors import SisImportErrorsAPI
from py3canvas.apis.sis_import_errors import Sisimporterror


class TestSisImportErrorsAPI(unittest.TestCase):
    """Tests for the SisImportErrorsAPI."""

    def setUp(self):
        self.client = SisImportErrorsAPI(secrets.instance_address, secrets.access_token)

    def test_get_sis_import_error_list_sis_imports(self):
        """Integration test for the SisImportErrorsAPI.get_sis_import_error_list_sis_imports method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_sis_import_error_list_sis_imports(account_id, id, failure=None)

    def test_get_sis_import_error_list_sis_import_errors(self):
        """Integration test for the SisImportErrorsAPI.get_sis_import_error_list_sis_import_errors method."""
        account_id = None  # Change me!!

        r = self.client.get_sis_import_error_list_sis_import_errors(account_id, failure=None)

