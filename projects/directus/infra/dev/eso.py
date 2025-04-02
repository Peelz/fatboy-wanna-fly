from infralib.pulumi_tdh import external_secret


def create(project_id: str, values: dict):
    # Secret Store sa
    namespace = values['namespace']
    account_name = values['serviceAccount']['secretStore']
    external_secret.create_project_eso_sa(
        project_id,
        account_name,
        [namespace]
    )
