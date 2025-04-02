#!/bin/sh

result=$(
  run-pgsql-cmd.sh \
    "$POSTGRES_DB" \
    "$POSTGRES_USER" \
    "$POSTGRES_USER_PASS" \
    "SELECT 1 FROM pg_database WHERE datname='$DB_NAME'" | grep 1
)

if [ -z "$result" ]; then IS_EXIST=0; else IS_EXIST=1; fi

if [ "$IS_EXIST" -ne 1 ]; then
  run-pgsql-cmd-as-postgres.sh "CREATE DATABASE $DB_NAME WITH OWNER $DB_DIRECTUS_USER ENCODING=UTF8"
else
  echo "Database \"$DB_NAME\" already exists."
fi

