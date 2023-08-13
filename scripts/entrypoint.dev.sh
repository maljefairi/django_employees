#!/bin/bash

echo "Database is ready, running migrations..."
# Run migrations
python /app/manage.py migrate

echo "Migrations done, loading initial data..."
# Load initial superadmin password
python /app/manage.py createtestuser

echo "Initial data loaded, collecting static files..."
# Collect static files
python /app/manage.py collectstatic --noinput

echo "Static files collected, running dev server..."
# Run dev server
python /app/manage.py runserver 0.0.0.0:8000
