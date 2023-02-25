FROM python:3.7-slim

RUN mkdir /hhParserBot

COPY requirements.txt /hhParserBot

RUN pip3 install -r /hhParserBot/requirements.txt --no-cache-dir

COPY . /hhParserBot

WORKDIR /hhParserBot

CMD [ "python", "./hh_parser.py" ]
