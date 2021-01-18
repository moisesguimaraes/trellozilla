import functools
import pbr.version

from oslo_log import log as logging

from trellozilla.core import bugzilla
from trellozilla.core import config
from trellozilla.core import trello


__version__ = pbr.version.VersionInfo("trellozilla").version_string()

LOG = logging.getLogger(__name__)


class TrelloZilla:
    def __init__(self):
        self._conf = config.get_config()

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
        return trello.get_api_client(self.conf)

    @property
    @functools.lru_cache()
    def bugzilla(self):
        return bugzilla.get_api_client(self.conf)

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
