from trellozilla import options

from oslo_config import cfg
from trello.util import create_oauth_token


def generate_trello_oauth_token():
    """Creates a new OAuth token for Trello.
    """
    conf = options.get_config()

    conf.register_cli_opt(
        cfg.StrOpt(
            "expiration",
            help="the new token's expiration, defaults to '30days'",
            default="30days",
        )
    )

    conf(project="trellozilla")

    create_oauth_token(key=conf.trello.api_key, secret=conf.trello.api_secret)
