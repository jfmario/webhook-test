
FROM python:3-alpine

COPY ./src/ /app/src/
COPY ./README.md /app/README.md
COPY ./requirements.txt /app/requirements.txt
COPY setup.py /app/setup.py

WORKDIR /app

RUN python3 -m pip install .

ENTRYPOINT python3 -m webhook_test