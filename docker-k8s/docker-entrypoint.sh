#!/bin/sh
spawn-fcgi -s /var/run/fcgiwrap.socket /usr/bin/fcgiwrap
chmod 777 /var/run/fcgiwrap.socket
chmod +x /usr/lib/cgi-bin/script-cgi

nginx -g "daemon off;"