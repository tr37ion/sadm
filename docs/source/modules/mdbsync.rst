
mdbsync
=======
mdbsync is in charge of sending updates to the clients who suscribed to the state changes of mdb.

Client
------
The client is a ``prologin.synchronisation.Client`` instance using the mac as a backlog update key.

Server
------

The server is a ``prologin.synchronisation.Server`` subclass instance configured to use the mac as the backlog update key, as well as pulling the initial backlog from mdb.

When the server is ran as a standalone program, is listens on port 8000 by default, using the port specified as the first argument otherwise.


The server reads its configuration in ``$CFG_DIR/mdbsync-(pub|sub).yml`` for the publication and suscription keys.

The two configuration files only have a config line, ``shared_secret,``, which is a string defining the secret the client has to provide in order to publish or poll events.

.. note::
   Please read :ref:`the detailled background documentation page <synchronisation>`
