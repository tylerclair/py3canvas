"""SisImports API Tests for Version 1.0.

This is a testing template for the generated SisImportsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.sis_imports import SisImportsAPI
from py3canvas.apis.sis_imports import Sisimportdata
from py3canvas.apis.sis_imports import Sisimportstatistic
from py3canvas.apis.sis_imports import Sisimportstatistics
from py3canvas.apis.sis_imports import Sisimportcounts
from py3canvas.apis.sis_imports import Sisimport


class TestSisImportsAPI(unittest.TestCase):
    """Tests for the SisImportsAPI."""

    def setUp(self):
        self.client = SisImportsAPI(secrets.instance_address, secrets.access_token)

    def test_get_sis_import_list(self):
        """Integration test for the SisImportsAPI.get_sis_import_list method."""
        account_id = None  # Change me!!

        r = self.client.get_sis_import_list(
            account_id, created_before=None, created_since=None, workflow_state=None
        )

    def test_get_current_importing_sis_import(self):
        """Integration test for the SisImportsAPI.get_current_importing_sis_import method."""
        account_id = None  # Change me!!

        r = self.client.get_current_importing_sis_import(account_id)

    def test_import_sis_data(self):
        """Integration test for the SisImportsAPI.import_sis_data method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_get_sis_import_status(self):
        """Integration test for the SisImportsAPI.get_sis_import_status method."""
        account_id = None  # Change me!!
        id = None  # Change me!!

        r = self.client.get_sis_import_status(account_id, id)

    def test_restore_workflow_states_of_sis_imported_items(self):
        """Integration test for the SisImportsAPI.restore_workflow_states_of_sis_imported_items method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_abort_sis_import(self):
        """Integration test for the SisImportsAPI.abort_sis_import method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_abort_all_pending_sis_imports(self):
        """Integration test for the SisImportsAPI.abort_all_pending_sis_imports method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass
