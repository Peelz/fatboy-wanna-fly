# fatboy-wanna-fly

## Pre install

- helm
- python
- argocd

## pull chart install helm

```sh
helm repo add directus https://digitalist-se.github.io/directus-helm-chart/
helm pull --untar directus/directus 
```

## Update repository url

```sh
git remote set-url origin {your-repo}
# ex git remote set-url oirigin git@bitbucket.org:truedmp/tdh-infra-database.git
```

## Pulumi

Stack initial

```sh
  pulumi stack init ${tenant}-directus-dev-${resource} \
    --secrets-provider gcpkms://projects/tdg-dh-truehealth-core-nonprod/locations/asia-southeast1/keyRings/pulumi-stack/cryptoKeys/default-key
  pulumi config set gcp:project tdg-dh-truehealth-core-nonprod

```

Update Infra stacks 
```sh
pulumi up -r -s ${tenant}-directus-dev-${resource} 

```
