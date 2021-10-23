"""MediaObjects API Tests for Version 1.0.

This is a testing template for the generated MediaObjectsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.media_objects import MediaObjectsAPI
from py3canvas.apis.media_objects import Mediatrack
from py3canvas.apis.media_objects import Mediaobject


class TestMediaObjectsAPI(unittest.TestCase):
    """Tests for the MediaObjectsAPI."""

    def setUp(self):
        self.client = MediaObjectsAPI(secrets.instance_address, secrets.access_token)

    def test_list_media_tracks_for_media_object(self):
        """Integration test for the MediaObjectsAPI.list_media_tracks_for_media_object method."""
        media_object_id = None  # Change me!!

        r = self.client.list_media_tracks_for_media_object(media_object_id, include=None)

    def test_update_media_tracks(self):
        """Integration test for the MediaObjectsAPI.update_media_tracks method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_list_media_objects_media_objects(self):
        """Integration test for the MediaObjectsAPI.list_media_objects_media_objects method."""

        r = self.client.list_media_objects_media_objects(exclude=None, order=None, sort=None)

    def test_list_media_objects_courses(self):
        """Integration test for the MediaObjectsAPI.list_media_objects_courses method."""
        course_id = None  # Change me!!

        r = self.client.list_media_objects_courses(course_id, exclude=None, order=None, sort=None)

    def test_list_media_objects_groups(self):
        """Integration test for the MediaObjectsAPI.list_media_objects_groups method."""
        group_id = None  # Change me!!

        r = self.client.list_media_objects_groups(group_id, exclude=None, order=None, sort=None)

    def test_update_media_object(self):
        """Integration test for the MediaObjectsAPI.update_media_object method."""
        # This method utilises the PUT request method and will make changes to the Canvas instance. This needs consideration.
        pass

