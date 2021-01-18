import bugzilla


def get_api_client(conf):
    """
    Returns a new Bugzilla API client with the provided configuration.

    :returns: a Bugzilla API client object
    """
    return bugzilla.Bugzilla(conf.bugzilla.url, api_key=conf.bugzilla.api_key)
