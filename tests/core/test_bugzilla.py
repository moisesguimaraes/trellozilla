import unittest
from unittest import mock

from trellozilla.core import bugzilla


class TestBugzilla(unittest.TestCase):
    """Tests for `trellozilla.core.bugzilla`."""

    def test_get_client_api(self):
        with mock.patch("bugzilla.Bugzilla") as trello_client_mock:
            conf_mock = mock.Mock()

            bugzilla.get_api_client(conf_mock)

            trello_client_mock.assert_called_once_with(
                conf_mock.bugzilla.url,
                api_key=conf_mock.bugzilla.api_key,
            )
