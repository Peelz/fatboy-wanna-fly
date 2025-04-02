import pulumi
import pulumi_gcp as gcp
import pulumi_random as random


def create_gcp_secret_with_version(
    args: dict,
):
    secret_id = args["secret_id"]
    secret_data = args["secret_data"]

    replication = gcp.secretmanager.SecretReplicationArgs(
        auto=gcp.secretmanager.SecretReplicationAutoArgs()
    )
    secret_ver = secret_id + "-ver"
    secret = gcp.secretmanager.Secret(
        secret_id, secret_id=secret_id, replication=replication
    )
    gcp.secretmanager.SecretVersion(
        secret_ver, secret=secret.id, secret_data=secret_data
    )


def _create_secret(secret_id: str):
    passwd = random.RandomPassword(
        f"dbuser-{secret_id}",
        length=32,
        special=False,
    )
    pulumi.Output.all(secret_id=secret_id, secret_data=passwd.result).apply(
        create_gcp_secret_with_version
    )


def _create_uuid(secret_id: str):
    random_uuid = random.RandomId(f"random-uuid-of-{secret_id}", byte_length=16)

    pulumi.Output.all(secret_id=secret_id, secret_data=random_uuid.id).apply(
        create_gcp_secret_with_version
    )


def create(_, chart_values: dict):
    directus_key = chart_values["directus"]["secretRefs"]["key"]
    directus_secret = chart_values["directus"]["secretRefs"]["secret"]
    directus_admin = chart_values["directus"]["secretRefs"]["admin"]
    _create_uuid(directus_key)
    _create_uuid(directus_secret)
    _create_secret(directus_admin)
