import functools
import pbr.version

from trellozilla import options

from bugzilla import Bugzilla
from oslo_config import cfg
from oslo_log import log as logging
from trello import TrelloClient

__version__ = pbr.version.VersionInfo("trellozilla").version_string()

LOG = logging.getLogger(__name__)

extra_log_level_defaults = [
    "bugzilla=WARN",
    "oauthlib=WARN",
    "requests_oauthlib=WARN",
]
logging.set_defaults(
    default_log_levels=logging.get_default_log_levels()
    + extra_log_level_defaults
)


def get_config():
    """
    Returns a new config object with registered trellozilla config options.

    :returns: an oslo_config.cfg.ConfigOpts object
    """
    conf = cfg.ConfigOpts()

    register_opts(conf)

    return conf


def register_opts(conf):
    """Registers trellozilla config options to a config object.

    :param conf: an oslo_config.cfg.ConfigOpts object
    """
    logging.register_options(conf)

    for group, opts in options.list_opts():
        conf.register_opts(opts, group)


def trello_api(conf):
    """
    Returns a new Trello API object with the provided configuration.

    :returns: a TrelloClient object
    """
    return TrelloClient(
        api_key=conf.trello.api_key,
        api_secret=conf.trello.api_secret,
        token=conf.trello.token,
        token_secret=conf.trello.token_secret,
    )


def bugzilla_api(conf):
    """
    Returns a new Bugzilla API object with the provided configuration.

    :returns: a Bugzilla object
    """
    return Bugzilla(conf.bugzilla.url, api_key=conf.bugzilla.api_key)


class TrelloZilla:
    def __init__(self):
        self._conf = cfg.ConfigOpts()

        logging.register_options(self._conf)
        self.register_opts(options.list_opts())

    def register_opts(self, list_opts):
        for group, opts in list_opts:
            self._conf.register_opts(opts, group)

    def register_cli_opts(self, list_opts):
        for group, opts in list_opts:
            self._conf.register_cli_opts(opts, group)

    @property
    @functools.lru_cache()
    def conf(self):
        self._conf(project="trellozilla")
        logging.setup(self._conf, "trellozilla")

        return self._conf

    @property
    @functools.lru_cache()
    def trello(self):
        return trello_api(self.conf)

    @property
    @functools.lru_cache()
    def bugzilla(self):
        return bugzilla_api(self.conf)

    def fetch_bzs(self, bugzilla_query_url):
        return self.bugzilla.query(
            self.bugzilla.url_to_query(bugzilla_query_url)
        )

    def run(self):
        try:
            self.trello.list_boards()
            LOG.info("trellozilla successfully connects to trello.")
        except Exception:
            LOG.exception("trellozilla failed to connected to trello.")

        try:
            if self.bugzilla.logged_in:
                LOG.info("trellozilla successfully connects to bugzilla.")
            else:
                LOG.info(
                    "trellozilla successfully connects to bugzilla, "
                    "but the user is not logged in."
                )
        except Exception:
            LOG.exception("trellozilla failed to connected to bugzilla.")


def main():
    TrelloZilla().run()
