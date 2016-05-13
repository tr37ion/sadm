#!/bin/sh


set -e


echo "######## SYNCING rhfs0 ########"
rsync --delete -axPHAX /export/nfsroot_staging /export/nfsroot

systemctl restart udbsync
spleep 5

for serv in rfs{2,4,6}; do
    echo "######## SYNCING $serv ########"
    rsync --delete -axPHAX /export/nfsroot/ "$serv":/export/nfsroot
    rsync --delete -axPHAX /export/skeleton/ "$serv":/export/skeleton
done
