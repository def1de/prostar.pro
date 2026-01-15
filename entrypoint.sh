#!/usr/bin/env sh
set -e

echo "⏳ Waiting for PostgreSQL..."
until PGPASSWORD=$POSTGRES_PASSWORD psql -h postgres -U $POSTGRES_USER -d $POSTGRES_DB -c '\q' 2>/dev/null; do
  echo "  PostgreSQL is unavailable - sleeping"
  sleep 2
done
echo "✓ PostgreSQL is ready"

echo "🗄️  Initializing database..."
flask init-db || echo "✓ Database already initialized"

echo "🚀 Starting application with Gunicorn..."
exec gunicorn --bind 0.0.0.0:5000 --workers 4 --timeout 120 app:app