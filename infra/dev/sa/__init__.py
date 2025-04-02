from infra.share import eso_sa


def create(gcp_project_id: str, chart_values: dict):
    eso_sa.create_iam_eso_sa(gcp_project_id, chart_values)
