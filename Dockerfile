FROM python:3.11-alpine

LABEL "author"="KARMA123321"

WORKDIR ./usr/api_tests

RUN apk update && apk upgrade && apk add bash

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

CMD pytest -s -v tests/* --alluredir=allure