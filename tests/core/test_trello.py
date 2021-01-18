import unittest
from unittest import mock

from trellozilla.core import trello


class TestTrello(unittest.TestCase):
    """Tests for `trellozilla.core.trello`."""

    def test_get_client_api(self):
        with mock.patch("trello.TrelloClient") as trello_client_mock:
            conf_mock = mock.Mock()

            trello.get_api_client(conf_mock)

            trello_client_mock.assert_called_once_with(
                api_key=conf_mock.trello.api_key,
                api_secret=conf_mock.trello.api_secret,
                token=conf_mock.trello.token,
                token_secret=conf_mock.trello.token_secret,
            )
