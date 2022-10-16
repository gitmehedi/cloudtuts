FROM nginx:latest
MAINTAINER gitmehedi

RUN set -x; apt-get -y update && apt-get install -y curl vim

COPY html/* /usr/share/nginx/html/
COPY ./default.conf /etc/nginx/conf.d/default.conf
VOLUME [ "//usr/share/nginx/html" ]

CMD ["nginx","-g","daemon off;"]
