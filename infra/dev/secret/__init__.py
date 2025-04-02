from . import database_secret


def create(gcp_project_id: str, chart_values: dict):
    service_account = None
    database_secret.create(gcp_project_id, chart_values)
