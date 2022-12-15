FROM python:3.10-alpine3.16

WORKDIR /work

COPY ./requirements.txt /work/
RUN pip install -r requirements.txt

COPY ./ris_4 /work/ris_4