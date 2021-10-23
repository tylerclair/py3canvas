"""ImmersiveReader API Tests for Version 1.0.

This is a testing template for the generated ImmersiveReaderAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.immersive_reader import ImmersiveReaderAPI


class TestImmersiveReaderAPI(unittest.TestCase):
    """Tests for the ImmersiveReaderAPI."""

    def setUp(self):
        self.client = ImmersiveReaderAPI(secrets.instance_address, secrets.access_token)
