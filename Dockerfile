FROM python:3.11-alpine

LABEL "author"="KARMA123321"

WORKDIR ./usr/api_tests

COPY . .

RUN apk update && apk upgrade && apk add bash

RUN pip3 install -r requirements.txt

CMD pytest -s -v tests/*