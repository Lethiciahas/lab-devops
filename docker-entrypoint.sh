#!/bin/sh

export KUBECONFIG=$(for i in $(find /usr/bin -iname 'cluster1.yaml') ; do echo -n ":$i"; done | cut -c 2-)

##ref: https://stackoverflow.com/questions/63629990/set-kubeconfig-environment-variable-dynamically##

kubectl get nodes

spawn-fcgi -s /var/run/fcgiwrap.socket /usr/bin/fcgiwrap
chmod 777 /var/run/fcgiwrap.socket
chmod +x /usr/lib/cgi-bin/script-cgi

nginx -g "daemon off;"