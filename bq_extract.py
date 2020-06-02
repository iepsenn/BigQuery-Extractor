import os
from google.cloud import bigquery
import yaml

if "GOOGLE_APPLICATION_CREDENTIALS" not in os.environ:
    # default
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'bq_credentials.json'

client = bigquery.Client()

query_config = bigquery.QueryJobConfig(
    use_legacy_sql=False,
    location="southamerica-east1"
)


def get_bq_data(table: str, dataset: str, project: str):

    dataset_ref = client.dataset(dataset, project=project)
    dataset = client.get_dataset(dataset_ref)

    table_ref = dataset_ref.table(table)
    table = client.get_table(table_ref)

    return client.list_rows(table).to_dataframe()


with open('config.yaml', 'r') as config_file:
    params = yaml.load(config_file)


for param in params['tables_params']:
    table = param[0]
    dataset = param[1]
    project = param[2]
    data_path = param[3]

    if not os.path.exists(data_path):
        os.makedirs(data_path)

    output_filename = '{}{}_{}.csv'.format(data_path, dataset, table)

    dataframe = get_bq_data(table, dataset, project)

    dataframe.to_csv(output_filename, index=False)
