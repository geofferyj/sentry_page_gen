FROM python:3.7

ENV APP_ROOT /src
ENV CONFIG_ROOT /config


RUN mkdir ${CONFIG_ROOT}
COPY /team_sentry_pages/requirements.txt ${CONFIG_ROOT}/requirements.txt
RUN pip install -r ${CONFIG_ROOT}/requirements.txt

RUN mkdir ${APP_ROOT}
WORKDIR ${APP_ROOT}

ADD /team_sentry_pages/ ${APP_ROOT}
