import unittest
from unittest import mock

from trellozilla.jobs import generate_trello_oauth_token


class TestGenerateTrelloOAuthToken(unittest.TestCase):
    """Tests for `trellozilla.jobs.generate_trello_oauth_token`."""

    def test_generate_trello_oauth_token(self):
        with mock.patch(
            "trellozilla.jobs.generate_trello_oauth_token."
            "create_oauth_token",
        ) as create_oauth_token_mock, mock.patch(
            "trellozilla.jobs.generate_trello_oauth_token."
            "GenerateTrelloOAuthToken.conf"
        ) as conf_mock:
            generate_trello_oauth_token.main()

            create_oauth_token_mock.assert_called_once_with(
                name="TrelloZilla",
                key=conf_mock.trello.api_key,
                secret=conf_mock.trello.api_secret,
                expiration=conf_mock.expiration,
            )
