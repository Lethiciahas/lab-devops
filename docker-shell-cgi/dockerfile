FROM nginx:stable-alpine
COPY docker-entrypoint.sh /
COPY cluster1.yaml /usr/bin/
COPY default.conf /etc/nginx/conf.d/
COPY fcgiwrap.conf /etc/nginx/
COPY script-cgi /usr/lib/cgi-bin/
RUN apk update && apk add spawn-fcgi fcgiwrap
RUN chmod +x docker-entrypoint.sh
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" && install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]