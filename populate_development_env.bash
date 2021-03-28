#!/bin/bash

# echo "Flushing Django database..."
# docker-compose exec django python manage.py flush --no-input

echo "Migrating Django changes..."
docker-compose exec django python manage.py migrate --no-input

echo "Populating Django database..."
docker-compose exec django python manage.py loaddata lovelace_django_dumpdata.json

echo "Collecting static files..."
python manage.py collectstatic --no-input
