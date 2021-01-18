import unittest
from unittest import mock

from trellozilla.core import config


class TestConfig(unittest.TestCase):
    """Tests for `trellozilla.core.config`."""

    def test_list_opts(self):
        opts = config.list_opts()

        self.assertEqual(len(opts), 2)
        self.assertEqual(opts[0][0], "bugzilla")
        self.assertEqual(opts[1][0], "trello")

    def test_if_register_opts_uses_list_opts(self):
        with mock.patch("trellozilla.core.config.list_opts") as list_opts_mock:
            conf_mock = mock.Mock()
            list_opts_mock.return_value = [
                (mock.sentinel.GROUP, mock.sentinel.OPTS)
            ]
            config.register_opts(conf_mock)

            list_opts_mock.assert_called_once_with()
            conf_mock.register_opts.assert_called_with(
                mock.sentinel.OPTS,
                mock.sentinel.GROUP,
            )

    def test_if_options_are_registered_during_get_config(self):
        with mock.patch(
            "trellozilla.core.config.register_opts"
        ) as register_opts_mock:
            conf = config.get_config()

            register_opts_mock.assert_called_with(conf)
