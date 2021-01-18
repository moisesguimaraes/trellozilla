from trello import TrelloClient


def get_api_client(conf):
    """
    Returns a new Trello API client object with the provided configuration.

    :returns: a TrelloClient object
    """
    return TrelloClient(
        api_key=conf.trello.api_key,
        api_secret=conf.trello.api_secret,
        token=conf.trello.token,
        token_secret=conf.trello.token_secret,
    )
