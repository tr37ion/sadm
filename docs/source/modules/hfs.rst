Presence local services
=======================

There's a web server running on all the rhfs machines.
It can handle two types of requests, which are both POSTs:
- ``/get_hfs``: 
- ``/migrate_user``: send an user to another server.

When it's called, the user's password has already been checked, as /etc/shadow is synchronized between all the machines. This module is here for tracking and additionnal checks.

It does the following:
- for session opennings, it checks the user it's logging in from a tty, nor screen, it requests a home migration to the nearest server, starts a network block device client, mounts the home of the user if it's not done already, and return back to pam.
- for session closings, it kills all the processes from the user, unmounts the home and stops the network block device client.
