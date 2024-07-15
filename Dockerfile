FROM python:3.6-alpine

RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.6/main" >> /etc/apk/repositories 
RUN echo "http://dl-cdn.alpinelinux.org/alpine/v3.6/community" >> /etc/apk/repositories
RUN apk add mongodb mongodb-tools
RUN apk add openrc --no-cache
RUN apk add --no-cache --upgrade bash

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8080

COPY commands.sh /scripts/commands.sh
RUN chmod +x /scripts/commands.sh

ENTRYPOINT ["bash"]
CMD ["/scripts/commands.sh"]
