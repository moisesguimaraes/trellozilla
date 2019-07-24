Usage
=====

TreloZilla requires you to provide some configuration values in order to
give you back both Trello and Bugzilla API objects.  The sample configuration
file is well documented and self-explanatory about how you can produce the
right values in it.

Generating a configuration file
-------------------------------

To generate a sample configuration file:

.. code-block:: console

    $ oslo-config-generator --namespace trellozilla.config > trellozilla.conf

To learn more about where to put your configuration file, check the 
`oslo.config documentation`_.

The Trello configuration
------------------------

The Trello configuration is composed of four values:

* api_key
* api_secret
* token
* token_secret

The first two ones you can find at https://trello.com/app-key.

Once you have setup your configuration file with your Trello api_key and api_secret
you can use the following command to generate the token and token_secret:

.. code-block:: console

    $ generate_trello_oauth_token

The Bugzilla configuration
--------------------------

The Bugzilla configuration is composed of two values:

* url
* api_key

The buggzila api_key can be generated at:

    *your_bugzilla_url*/userprefs.cgi?tab=apikey

Getting the API objects
-----------------------

To use TrelloZilla in a project:

.. code-block:: python

    import trellozilla

    conf = trellozilla.get_config()

    conf()  # or `conf(project="my_project")` to help oslo.config finding your config file.

    trello = trellozilla.trello_api(conf)
    bugzilla = trellozilla.bugzilla_api(conf)

For following usage of both Trello and Bugzilla API objects, please refeer to
py-trello_ and python-bugzilla_ projects.

.. _py-trello: https://github.com/sarumont/py-trello
.. _python-bugzilla: https://github.com/python-bugzilla/python-bugzilla
.. _`oslo.config documentation`: https://docs.openstack.org/oslo.config/latest/configuration/options.html#default
