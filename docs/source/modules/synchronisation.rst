Synchronisation servers
=======================

The syncronisation servers are generic implementation of servers that want to sent updates to a list of suscribers.

You could find their implementation at ``prologin.synchronisation``.

At each update, they call a suscriber callback for each single client.

Structure
---------

The server holds a dictionnary of elements receiving updates.
See the function ``prologin.synchronisation.apply_updates``, which deserves that purpose.

Client are receiving updates via a long polling protocol:
they start making an http request for having an update, wait until the server has some to provide, and make a request again once it received one.


For each newly connected client making a request on ``/poll``, a ``PollHandler`` is created, which registers the client and unregisters it once the connection closed.

Similarly, an ``UpdateHandler`` is created at each new json update received on ``/update``, which serves the update to all the suscribers using ``apply_updates``.

Base server classes
-------------------

``BasePubSubQueue`` is base abstract class defining the base structure everything works on:
- It has a set of suscribers and a method getting a backlog
- each new suscriber connecting receives a backlog and is added to the suscribers set
- It has a method to post an update to all the suscribers

``DefaultPubsubQueue`` is an actual implementation over to previous, meant to work with a unique field. Is just holds a backlog, applies each new update to it, and serves the update to all connected clients.

``Server`` is connecting all those elements alltogether, making Poll and UpdateHandler actually listen on some urls, as well as initializing the initial publication backlog.

It's a subclass of ``prologin.web.TornadoApp``, please refer to this module's documentation to know more about it.

It raises an exception by default when trying to pull the initial backlog, and goes into an infinite loop flooding the logs, so you have to subclass it and override the ``get_initial_backlog`` method.
  
Base client class
-----------------

The client is a subclass of ``prologin.webapi.Client``, which provides a bare ``send_request`` wrapper, able of making both get and post requests.

The client is working on a suscription url it's trading data with.
It can both ``send_update(s)`` and ``poll_updates``.


Clients have to use a shared secret to send update as well as for receiving some.

When polling responses, they consider each line of the response as a new update, decode it as utf-8 encoded update json, update an initial empty state with each line of the update while calling back with the state and metadatas for each update line.
