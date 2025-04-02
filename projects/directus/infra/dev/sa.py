import pulumi_gcp as gcp
from infralib.pulumi_tdh.secret import service_account_key

def create(pid: str, values: dict):
    # create, get new service account
    sa_name = values['serviceAccount']['directus']

    sa = gcp.serviceaccount.Account(
        f"sa-{sa_name}",
        account_id=sa_name,
        display_name="My Account SA",
    )

    # create key, or get exist from resource name
    key = gcp.serviceaccount.Key(
        "resource-key-name",
        service_account_id=sa.name,
        public_key_type="TYPE_X509_PEM_FILE"
    )

    # use this function in 'apply'
    key.private_key.apply(
        lambda v: service_account_key(f"workshop-cred-json-{sa_name}", f'{v}')
    )

    
