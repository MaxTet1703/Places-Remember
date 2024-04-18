FROM python:3.11

COPY ./app/ /backend/app/
COPY ./core/ /backend/core/
COPY ./manage.py /backend/
COPY ./config.cfg /backend/
COPY ./requirements.txt /backend/

WORKDIR /backend/ 

ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install --no-cache-dir -r requirements.txt 