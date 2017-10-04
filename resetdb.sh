#!/bin/bash

rm -rf db.sqlite3
rm -rf garderie/migrations/00* garderie/migrations/__pycache__/00*
python manage.py makemigrations
python manage.py migrate
./manage.py loaddata garderie/fixtures/fixture.json
./manage.py loaddata testoli/fixtures/fixture.json
