#!/bin/bash

[ -z "$1" ] && {
  echo "\$1 is empty"
  exit 1
}

ress=(
  db_secret
  eso
  sa
)

for res in "${ress[@]}"; do
  pulumi stack init mordee-$1-dev-{res} \
    --secrets-provider gcpkms://projects/tdg-dh-truehealth-core-nonprod/locations/asia-southeast1/keyRings/pulumi-stack/cryptoKeys/default-key
  pulumi config set gcp:project tdg-dh-truehealth-core-nonprod
done
