FROM python:3.7-slim

RUN mkdir /hh_parser_bot

COPY requirements.txt /hh_parser_bot

RUN pip3 install -r /hh_parser_bot/requirements.txt --no-cache-dir

COPY . /hh_parser_bot

WORKDIR /hh_parser_bot

CMD [ "python", "./hh_parser.py" ]
