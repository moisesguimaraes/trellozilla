import unittest
from unittest import mock

import trellozilla


class TestTrelloZilla(unittest.TestCase):
    """Tests for `trellozilla`."""

    def test_config_is_called_with_trellozilla(self):
        with mock.patch(
            "trellozilla.config.get_config"
        ) as get_conf_mock, mock.patch("trellozilla.logging"), mock.patch(
            "trellozilla.bugzilla.get_api_client"
        ) as get_bugzilla_api_mock, mock.patch(
            "trellozilla.trello.get_api_client"
        ) as get_trello_api_mock:
            conf_mock = get_conf_mock.return_value
            trello_mock = get_trello_api_mock.return_value
            bugzilla_mock = get_bugzilla_api_mock.return_value

            bugzilla_mock.logged_in = True
            job = trellozilla.TrelloZilla()
            job.run()

            conf_mock.assert_called_with(project="trellozilla")
            trello_mock.list_boards.assert_called_once()

            bugzilla_mock.logged_in = False
            job.run()

    def test_register_opts_call(self):
        with mock.patch("trellozilla.config.get_config") as get_conf_mock:
            job = trellozilla.TrelloZilla()
            job.register_opts([(mock.sentinel.GROUP, mock.sentinel.OPTS)])

            conf_mock = get_conf_mock.return_value

            conf_mock.register_opts.assert_called_once_with(
                mock.sentinel.OPTS,
                mock.sentinel.GROUP,
            )

    def test_register_cli_opts_call(self):
        with mock.patch("trellozilla.config.get_config") as get_conf_mock:
            job = trellozilla.TrelloZilla()
            job.register_cli_opts([(mock.sentinel.GROUP, mock.sentinel.OPTS)])

            conf_mock = get_conf_mock.return_value

            conf_mock.register_cli_opts.assert_called_once_with(
                mock.sentinel.OPTS,
                mock.sentinel.GROUP,
            )

    def test_fetch_bzs_call(self):
        with mock.patch("trellozilla.config.get_config"), mock.patch(
            "trellozilla.logging"
        ), mock.patch(
            "trellozilla.bugzilla.get_api_client"
        ) as get_bugzilla_api_mock:
            job = trellozilla.TrelloZilla()
            job.fetch_bzs(mock.sentinel.URL)

            bugzilla_mock = get_bugzilla_api_mock.return_value

            bugzilla_mock.url_to_query.assert_called_once_with(
                mock.sentinel.URL,
            )
            bugzilla_mock.query.assert_called_with(
                bugzilla_mock.url_to_query.return_value,
            )
