import pulumi
import pulumi_gcp as gcp
import pulumi_random as random
from infra.share.password import generate_db_password


def create(gcp_project_id: str, chart_values: dict):
    databases = chart_values['databases']
    for database in databases:
        keys = database['secretStore']
        for k, v in keys.items():
            generate_db_password(v)