#!/usr/bin/env sh
set -e

# Ensure Flask can find the app
export FLASK_APP=app

# Initialize DB
flask init-db || true

# Start the server
exec gunicorn --bind 0.0.0.0:5000 app:app