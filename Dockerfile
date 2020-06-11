FROM python:3.7-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add postgresql-dev bash
 
RUN mkdir /config
ADD /config/requirements.txt /config/
RUN pip install -r /config/requirements.txt
RUN mkdir /src
WORKDIR /src
