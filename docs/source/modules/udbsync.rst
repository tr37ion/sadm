mdbsync
=======
udbsync is in charge of sending updates to the clients who suscribed to the state changes of udb.

Client
------
The client is a ``prologin.synchronisation.Client`` instance using the login as the backlog update key.

Server
------
The server has two url handlers inherited from its mother class, see it's documentation for further reading.

The server is a ``prologin.synchronisation.Server`` subclass instance configured to use the login as the backlog update key, as well as pulling the initial backlog from mdb.

When the server is ran as a standalone program, is listens on port 8000 by default, using the port specified as the first argument otherwise.

The server reads its configuration in ``$CFG_DIR/udbsync-(pub|sub).yml`` for the publication and suscription shared secrets.

The two configuration files only have a config line, ``shared_secret,``, which is a string defining the secret the client has to provide in order to publish or poll events.

.. note::
   Please read :ref:`the detailled background page <synchronisation>`
