#!/bin/ash
source ./check_env_vars.sh
ret_val=$?
if [ "$ret_val" -ne 0 ]; then
  exit 1
fi

./sql/create-users.sql.sh
./sql/grant.sql.sh
run-pgsql-script.sh 'mordee' $DB_ADMIN_USER $DB_ADMIN_USER_PASS "$(pwd)/sql/create-schema.sql"
