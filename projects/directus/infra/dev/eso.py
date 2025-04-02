from infralib.pulumi_tdh import external_secret


def create(project_id: str, values: dict):
    # Secret Store sa
    external_secret.create_project_eso_sa(project_id, "biz-dory-eso", ["biz-dory"])

