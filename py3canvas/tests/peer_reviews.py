"""PeerReviews API Tests for Version 1.0.

This is a testing template for the generated PeerReviewsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.peer_reviews import PeerReviewsAPI
from py3canvas.apis.peer_reviews import Peerreview


class TestPeerReviewsAPI(unittest.TestCase):
    """Tests for the PeerReviewsAPI."""

    def setUp(self):
        self.client = PeerReviewsAPI(secrets.instance_address, secrets.access_token)

    def test_get_all_peer_reviews_courses_peer_reviews(self):
        """Integration test for the PeerReviewsAPI.get_all_peer_reviews_courses_peer_reviews method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.get_all_peer_reviews_courses_peer_reviews(
            assignment_id, course_id, include=None
        )

    def test_get_all_peer_reviews_sections_peer_reviews(self):
        """Integration test for the PeerReviewsAPI.get_all_peer_reviews_sections_peer_reviews method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!

        r = self.client.get_all_peer_reviews_sections_peer_reviews(
            assignment_id, section_id, include=None
        )

    def test_get_all_peer_reviews_courses_submissions(self):
        """Integration test for the PeerReviewsAPI.get_all_peer_reviews_courses_submissions method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!

        r = self.client.get_all_peer_reviews_courses_submissions(
            assignment_id, course_id, submission_id, include=None
        )

    def test_get_all_peer_reviews_sections_submissions(self):
        """Integration test for the PeerReviewsAPI.get_all_peer_reviews_sections_submissions method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!

        r = self.client.get_all_peer_reviews_sections_submissions(
            assignment_id, section_id, submission_id, include=None
        )

    def test_create_peer_review_courses(self):
        """Integration test for the PeerReviewsAPI.create_peer_review_courses method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_create_peer_review_sections(self):
        """Integration test for the PeerReviewsAPI.create_peer_review_sections method."""
        # This method utilises the POST request method and will make changes to the Canvas instance. This needs consideration.
        pass

    def test_delete_peer_review_courses(self):
        """Integration test for the PeerReviewsAPI.delete_peer_review_courses method."""
        course_id = None  # Change me!!
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.delete_peer_review_courses(
            assignment_id, course_id, submission_id, user_id
        )

    def test_delete_peer_review_sections(self):
        """Integration test for the PeerReviewsAPI.delete_peer_review_sections method."""
        section_id = None  # Change me!!
        assignment_id = None  # Change me!!
        submission_id = None  # Change me!!
        user_id = None  # Change me!!

        r = self.client.delete_peer_review_sections(
            assignment_id, section_id, submission_id, user_id
        )
