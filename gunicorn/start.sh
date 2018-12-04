#!/bin/sh

# Django migrate
python manage.py makemigrations -v 3 | python manage.py migrate -v 3

# Gunicorn execution
gunicorn -c gunicorn-config.py facebook_django_mock.wsgi