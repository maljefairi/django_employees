#!/bin/bash

echo "Hi there!"

# Database migrations
python /app/manage.py migrate

# Collect static files
python /app/manage.py collectstatic --noinput

# Start Gunicorn server with Unicorn worker class
gunicorn project.asgi:application --bind 0.0.0.0:8000 --workers 12 --timeout 0 -k uvicorn.workers.UvicornWorker
