FROM nginx:stable-alpine
COPY docker-entrypoint.sh /
COPY cluster1.yaml /usr/bin/
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/
COPY script-cgi /usr/lib/cgi-bin/
RUN apk update && apk add spawn-fcgi fcgiwrap
RUN chmod +x docker-entrypoint.sh

ENTRYPOINT ["sh", "/docker-entrypoint.sh"]