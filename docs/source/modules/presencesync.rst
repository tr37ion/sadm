Presencesync
============

Presencesync is a server running on the gate, which tracks the connection status of the users.

It's internally maintaining a list of the currently logged-in users, and periodically removing the ones not having sent a signal for a fixed amount of time.

The server can handle the following requests:
- ``/poll``: a poll url to receive database updates
- ``/get_list``: retrieves the list of the currently logged-in users
- ``/login``: Check is an user is allowed to login on a host
- ``/heartbeat``: Post informations about an user in order to keep its database entry alive
- ``/remove_expired``: Clean all the database entries that haven't been refreshed by a heatbeat for a while

Server
------

This server has to implement his own ``PubSubQueue``, called ``TimeoutedPubSubQueue``, deriving from ``prologin.synchronisation.BasePubSubQueue`` in order to achieve its mean, as the default queue doesn't handle information expiration.

Here the backlog is mapping the user login to an expiration timestamp and an hostname.  
It also has a reverse backlog mapping the hostname to the user login. The reverse backlog is a defaultdict, so that hostnames with no users logged in match to None.

It also has a login_failed counter, which can be incremented because of several machines sharing the same hostname, not being registered in mdb, or even everything being broken.
