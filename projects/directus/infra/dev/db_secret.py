from ..share.db_secret import create_db_secret

def create(gcp_project: str, values: dict):
    create_db_secret(gcp_project, values, "postgres")

