import gc
import json

import pulumi
import pulumi_gcp as gcp
import pulumi_random as random


def create_db_secret(pid: str, values: dict, db_key: str):
    # psql
    _create_db_password(
        values["database"][db_key]["users"]["directus"]["gcpSecretRef"],
        values["database"][db_key]["users"]["directus"]["userName"],
        "DB_DIRECTUS_USER",
        "DB_DIRECTUS_USER_PASS",
        with_pass_only=True,
    )


def _create_db_password(
    secret_id: str,
    username: str,
    user_env_var: str,
    passwd_env_var: str,
    version=1,
    with_pass_only=False,
):
    password = random.RandomPassword(
        f"dbuser-{secret_id}_{version}",
        length=32,
        special=False,
    )
    replication = gcp.secretmanager.SecretReplicationArgs(
        auto=gcp.secretmanager.SecretReplicationAutoArgs()
    )
    secret = gcp.secretmanager.Secret(
        f"sm-{secret_id}", secret_id=f"{secret_id}", replication=replication
    )

    pulumi.Output.all(
        secret=secret,
        secret_id=secret_id,
        username=username,
        password=password.result,
        user_env_var=user_env_var,
        passwd_env_var=passwd_env_var,
    ).apply(_create_secret_version)

    if with_pass_only:
        password_only_secret_id = f"{secret_id}-password-only"
        secret_password_only = gcp.secretmanager.Secret(
            f"sm-{password_only_secret_id}",
            secret_id=f"{secret_id}-password-only",
            replication=replication,
        )
        return gcp.secretmanager.SecretVersion(
            f"smver-{password_only_secret_id}",
            secret=secret_password_only.id,
            secret_data=password.result,
        )


def _create_secret_version(args):
    secret_id = args["secret_id"]
    secret = args["secret"]
    username = args["username"]
    secret_data = {
        f"{args['user_env_var']}": username,
        f"{args['passwd_env_var']}": args["password"],
    }
    return gcp.secretmanager.SecretVersion(
        f"smver-{secret_id}",
        secret=secret.id,
        secret_data=json.dumps(secret_data),
    )
