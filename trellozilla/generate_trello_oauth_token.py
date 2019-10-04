from oslo_config import cfg
from trello.util import create_oauth_token
from trellozilla import TrelloZilla


class GenerateTrelloOAuthToken(TrelloZilla):
    def __init__(self):
        super().__init__()

        expiration = cfg.StrOpt(
            "expiration",
            help="the new token's expiration, defaults to '30days'",
            default="30days",
        )

        self.register_cli_opts([(None, [expiration])])

    def run(self):
        create_oauth_token(
            name="TrelloZilla",
            key=self.conf.trello.api_key,
            secret=self.conf.trello.api_secret,
            expiration=self.conf.expiration,
        )


def main():
    GenerateTrelloOAuthToken().run()
