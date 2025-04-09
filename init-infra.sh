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

  pulumi stack init workshop-directus-dev-${res} \
    --secrets-provider gcpkms://projects/tdg-dh-truehealth-core-nonprod/locations/asia-southeast1/keyRings/pulumi-stack/cryptoKeys/default-key
  pulumi config set gcp:project tdg-dh-truehealth-core-nonprod
done
