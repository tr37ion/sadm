Presence local services
=======================

There's a web server running on all the machines in order to provide presence informations.
It can handle two types of requests:
- ``/send_heartbeat``: used to notify the presencesync server about the machine's status. A thread is running and periodically requesting the server to this url in order to check its status and send a heartbeat to presencesync if someone is logged in.
- ``/login``: requests a login to presencesync using the appropriate username and hostname. 

In order to centralize the user status, we do have a pam module handling session openning and closing.

When it's called, the user's password has already been checked, as /etc/shadow is synchronized between all the machines. This module is here for tracking and additionnal checks.

It does the following:
- for session opennings, it checks the user it's logging in from a tty, nor screen, it requests a home migration to the nearest server, starts a network block device client, mounts the home of the user if it's not done already, and return back to pam.
- for session closings, it kills all the processes from the user, unmounts the home and stops the network block device client.
  
  
TODO:
ask for precisions about the role of presenced and presencesync, make a flowchart of the login process
