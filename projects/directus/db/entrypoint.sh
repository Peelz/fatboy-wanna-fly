#!/bin/ash
# source ./check_env_vars.sh
# ret_val=$?
# if [ "$ret_val" -ne 0 ]; then
#   exit 1
# fi
#
basedir=$(dirname $0)

./sql/create-users.sql.sh
./sql/create-db.sh
./sql/grant.sql.sh

# run-pgsql-script.sh $DB_NAME $DB_DIRECTUS_USER $DB_ADMIN_USER_PASS "$dirname/sql/create-schema.sql"
