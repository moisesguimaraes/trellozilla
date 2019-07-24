# -*- coding: utf-8 -*-

import pbr.version

from trellozilla import options

from bugzilla import Bugzilla
from oslo_config import cfg
from trello import TrelloClient

__version__ = pbr.version.VersionInfo("trellozilla").version_string()


def get_config():
    """Returns a new config object with registered trellozilla config options.

    :returns: an oslo_config.cfg.ConfigOpts object
    """
    conf = cfg.ConfigOpts()

    options.register_opts(conf)

    return conf


def trello_api(conf):
    """Returns a new Trello API object initialized with the provided configuration.

    :returns: a TrelloClient object
    """
    return TrelloClient(
        api_key=conf.trello.api_key,
        api_secret=conf.trello.api_secret,
        token=conf.trello.token,
        token_secret=conf.trello.token_secret,
    )


def bugzilla_api(conf):
    """Returns a new Bugzilla API object initialized with the provided configuration.

    :returns: a Bugzilla object
    """
    return Bugzilla(conf.bugzilla.url, api_key=conf.bugzilla.api_key)
