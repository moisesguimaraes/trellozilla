from oslo_config import cfg
from oslo_log import log as logging

extra_log_level_defaults = [
    "bugzilla=WARN",
    "oauthlib=WARN",
    "requests_oauthlib=WARN",
]
logging.set_defaults(
    default_log_levels=logging.get_default_log_levels()
    + extra_log_level_defaults
)

_bugzilla_opts = [
    cfg.URIOpt("url", help="Your Bugzilla url", required=True, secret=True),
    cfg.StrOpt(
        "api_key",
        help="Your Bugzilla API key available at: "
        "[$bugzilla_url]/userprefs.cgi?tab=apikey",
        required=True,
        secret=True,
    ),
]

_trello_opts = [
    cfg.StrOpt(
        "api_key",
        help="Your Trello API key available at: https://trello.com/app-key",
        required=True,
        secret=True,
    ),
    cfg.StrOpt(
        "api_secret",
        help="Your OAuth Secret available at: https://trello.com/app-key",
        required=True,
        secret=True,
    ),
    cfg.StrOpt(
        "token",
        help="Your 3-legged OAuth Token generated with "
        "the generate_trello_oauth_token cli tool.",
        secret=True,
    ),
    cfg.StrOpt(
        "token_secret",
        help="Your 3-legged OAuth Token Secret generated with "
        "the generate_trello_oauth_token cli tool.",
        secret=True,
    ),
]


def list_opts():
    """Returns a list of config options available in the library.

    The returned list includes all oslo.config options which may be registered
    at runtime by the library.

    Each element of the list is a tuple. The first element is the name of the
    group under which the list of elements in the second element will be
    registered. A group name of None corresponds to the [DEFAULT] group in
    config files.

    The purpose of this is to allow tools like the Oslo sample config file
    generator to discover the options exposed to users by this library.

    :returns: a list of (group_name, opts) tuples
    """
    return [("bugzilla", _bugzilla_opts), ("trello", _trello_opts)]


def register_opts(conf):
    """Registers trellozilla config options to a config object.

    :param conf: an oslo_config.cfg.ConfigOpts object
    """
    logging.register_options(conf)

    for group, opts in list_opts():
        conf.register_opts(opts, group)


def get_config():
    """
    Returns a new config object with registered trellozilla config options.

    :returns: an oslo_config.cfg.ConfigOpts object
    """
    conf = cfg.ConfigOpts()

    register_opts(conf)

    return conf
