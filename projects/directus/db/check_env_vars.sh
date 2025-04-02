#!/bin/ash

if [ -z "${POSTGRES_DB}" ];
then
  export POSTGRES_DB="postgres"
fi

if [ -z "${POSTGRES_USER}" ];
then
  export POSTGRES_USER="postgres"
fi

if [ -z "${POSTGRES_USER_PASS}" ];
then
  echo "POSTGRES_USER_PASS env variable is not set."
  exit 1
fi

if [ -z "${DB_NAME}" ];
then
  echo "DB_NAME env variable is not set."
  exit 1
fi

if [ -z "${DB_ADMIN_USER}" ];
then
  echo "DB_ADMIN_USER env variable is not set."
  exit 1
fi

if [ -z "${DB_ADMIN_USER_PASS}" ];
then
  echo "DB_ADMIN_USER_PASS env variable is not set."
  exit 1
fi

if [ -z "${DB_DIRECTUS_USER}" ];
then
  echo "DB_DIRECTUS_USER env variable is not set."
  exit 1
fi

if [ -z "${DB_DIRECTUS_USER_PASS}" ];
then
  echo "DB_DIRECTUS_USER_PASS env variable is not set."
  exit 1
fi
