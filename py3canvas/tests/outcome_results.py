"""OutcomeResults API Tests for Version 1.0.

This is a testing template for the generated OutcomeResultsAPI Class.
"""
import unittest
import requests
import secrets
from py3canvas.apis.outcome_results import OutcomeResultsAPI
from py3canvas.apis.outcome_results import Outcomeresult
from py3canvas.apis.outcome_results import Outcomerollupscorelinks
from py3canvas.apis.outcome_results import Outcomerollupscore
from py3canvas.apis.outcome_results import Outcomerolluplinks
from py3canvas.apis.outcome_results import Outcomerollup
from py3canvas.apis.outcome_results import Outcomealignment
from py3canvas.apis.outcome_results import Outcomepath
from py3canvas.apis.outcome_results import Outcomepathpart


class TestOutcomeResultsAPI(unittest.TestCase):
    """Tests for the OutcomeResultsAPI."""

    def setUp(self):
        self.client = OutcomeResultsAPI(secrets.instance_address, secrets.access_token)

    def test_get_outcome_results(self):
        """Integration test for the OutcomeResultsAPI.get_outcome_results method."""
        course_id = None  # Change me!!

        r = self.client.get_outcome_results(
            course_id,
            include=None,
            include_hidden=None,
            outcome_ids=None,
            user_ids=None,
        )

    def test_get_outcome_result_rollups(self):
        """Integration test for the OutcomeResultsAPI.get_outcome_result_rollups method."""
        course_id = None  # Change me!!

        r = self.client.get_outcome_result_rollups(
            course_id,
            aggregate=None,
            aggregate_stat=None,
            exclude=None,
            include=None,
            outcome_ids=None,
            sort_by=None,
            sort_order=None,
            sort_outcome_id=None,
            user_ids=None,
        )
