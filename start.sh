#!/bin/bash

gunicorn -c gunicorn-config.py facebook_django_mock.wsgi