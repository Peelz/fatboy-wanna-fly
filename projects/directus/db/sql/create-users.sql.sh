#!/bin/ash

SQL_OUT_FILE=$(pwd)/sql/create-users.sql

cat <<EOF > "$SQL_OUT_FILE"
  DO \$\$
  BEGIN
    CREATE ROLE ${DB_DIRECTUS_USER} WITH LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE PASSWORD '$DB_DIRECTUS_USER_PASS';
  EXCEPTION
      WHEN duplicate_object THEN
        RAISE NOTICE '%, moving to next statement', SQLERRM USING ERRCODE = SQLSTATE;
  END;
  \$\$;


EOF

run-pgsql-script-as-postgres.sh "$SQL_OUT_FILE"
rm "$SQL_OUT_FILE"
