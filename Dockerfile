ARG DEBIAN_VERSION=bookworm
ARG PYTHON_VERSION=3.9
ARG APP_FOLDER=/var/www/link_shortener

FROM python:${PYTHON_VERSION}-slim-${DEBIAN_VERSION} as generic-base

ARG APP_FOLDER

WORKDIR ${APP_FOLDER}

COPY . ${APP_FOLDER}

RUN : "---------- install generic build container deps ----------" \
    && set -x \
    && apt-get update \
    && apt-get install -y --no-install-recommends \
        curl \
        build-essential \
        unzip \
        python3-dev \
    && pip install -r requirements.txt


RUN : "---------- running django preperations ----------" \
    && set -x \
    && python manage.py makemigrations \
    && python manage.py migrate \
    && python manage.py collectstatic --noinput

EXPOSE 8123

ENTRYPOINT ["python", "manage.py", "runserver", "0.0.0.0:8123"]