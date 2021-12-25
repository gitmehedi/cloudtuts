FROM python:3.7

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
    && rm -rf /var/lib/apt/lists/*

ENV DJANGO_SUPERUSER_PASSWORD=code200!
ENV DJANGO_SUPERUSER_EMAIL=admin@gmail.com
ENV DJANGO_SUPERUSER_USERNAME=admin

WORKDIR /usr/src/app
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000
RUN chmod +x entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]