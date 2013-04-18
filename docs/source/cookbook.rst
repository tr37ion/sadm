Cookbook
========

All the things you might need to do as an organizer or a root are documented
here.

User related operations
-----------------------

Most of the operations are made very simple with the use of ``udb``. If you are
an organizer, you can access ``udb`` in read only mode. If you are a root, you
obviously have write access too.

``udb`` displays the information (including passwords) of every contestant to
organizers. Organizers can't see the information of other organizers or roots.

All services should be using ``udb`` for authentication. Synchronization might
take up to 5 minutes (usually only one minute) if anything is changed.

Giving back his password to a contestant
    First of all, make sure to ask the contestant for his badge, which he
    should always have on him. Use the name from the badge to look up the user
    in the ``udb``. The password should be visible there.

Adding an organizer
    **Root only**. Go to ``udb`` and add a user with type ``orga``.

Machine registration
--------------------

``mdb`` contains the information of all machines on the contest LANs. If a
machine is not in ``mdb``, it is considered an alien and won't be able to
access the network.

All of these operations are **root only**. Organizers can't access the ``mdb``
administration interface.

Adding a user machine to the network
    In the ``mdb`` configuration, authorize self registration by adding a
    VolatileSetting ``allow_self_registration`` to true. Netboot the user
    machine - it should ask for registration details. After the details have
    been entered, the machine should reboot to the user environment. Disable
    ``allow_self_registration`` when you're done.

Adding a machine we don't manage to the user network
    Some organizers may want to use their laptop. Ask them for their MAC
    address and the hostname they want. Then, go to ``mdb`` and manually take
    an IP from the user IP pool by incrementing the last allocation integer.
    Finally, insert a ``mdb`` machine record with machine type ``orga`` using
    the IP address you manually allocated (if you set the last allocation to
    100, you should assign the IP .100). Wait a minute for the DHCP
    configuration to be synced, and connect the laptop to the network.