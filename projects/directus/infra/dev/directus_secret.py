import pulumi_gcp as gcp
import pulumi_random as random

def _create_secret(secret_id: str):
    passwd = random.RandomPassword(
        f"dbuser-{secret_id}",
        length=32,
        special=False,
    )


    replication = gcp.secretmanager.SecretReplicationArgs(auto=gcp.secretmanager.SecretReplicationAutoArgs())

    secret_ver = secret_id + "-ver"
    secret = gcp.secretmanager.Secret(
        secret_id,
        secret_id=secret_id,
        replication=replication
    )

    gcp.secretmanager.SecretVersion(
        secret_ver,
        secret=secret.id,
        secret_data=f"{passwd}"
    )

def _create_uuid(secret_id: str):
    random_uuid = random.RandomId(f"random-uuid-of-{secret_id}", byte_length=16)
    replication = gcp.secretmanager.SecretReplicationArgs(auto=gcp.secretmanager.SecretReplicationAutoArgs())

    secret_ver = secret_id + "-ver"
    secret = gcp.secretmanager.Secret(
        secret_id,
        secret_id=secret_id,
        replication=replication
    )

    gcp.secretmanager.SecretVersion(
        secret_ver,
        secret=secret.id,
        secret_data=f"{random_uuid}"
    )

def create(_, chart_values: dict):
    directus_key = chart_values["directus"]["secretRefs"]["key"]
    directus_secret = chart_values["directus"]["secretRefs"]["secret"]
    directus_admin = chart_values["directus"]["secretRefs"]["admin"]
    _create_uuid(directus_key)
    _create_uuid(directus_secret)
    _create_secret(directus_admin)

