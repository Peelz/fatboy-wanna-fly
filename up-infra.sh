#!/bin/bash

[ -z "$1" ] && {
  echo "prefix \$1 is empty"
  exit 1
}
ress=(
  sa
  directus_secret
  db_secret
  eso
)

for res in "${ress[@]}"; do
  pulumi up -r -s workshop-directus-dev-${res} 
done
