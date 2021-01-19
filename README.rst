TrelloZilla
===========

.. image:: https://img.shields.io/pypi/v/trellozilla.svg
        :target: https://pypi.python.org/pypi/trellozilla

.. image:: https://api.travis-ci.com/moisesguimaraes/trellozilla.svg?branch=master
        :target: https://travis-ci.com/moisesguimaraes/trellozilla

.. image:: https://readthedocs.org/projects/trellozilla/badge/?version=latest
        :target: https://trellozilla.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

TrelloZilla is a small set of boilerplate code to
automate jobs in/between both Bugzilla and Trello.

TrelloZilla is Free Software and released under the
`Apache Software License 2.0 <https://www.apache.org/licenses/LICENSE-2.0>`_.

The complete TrelloZilla documentation can be found at
`readthedocs.io <https://trellozilla.readthedocs.io>`_.

Features
--------

* TrelloZilla is configurable via oslo.config so you can safely provide
  your Trello and Bugzilla credentials, and as well be able to customize
  your automated jobs.

* The ``generate_trello_oauth_token`` job can be used to generate the Trello
  credentials required by TrelloZilla.

* TrelloZilla can create Trello API client objects based on provided credentials.

* TrelloZilla can create Bugzilla API client objects based on provided credentials.
