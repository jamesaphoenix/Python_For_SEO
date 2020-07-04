#!/home/jamesphoenix/1_google_ads_optimisation/env/bin python3
import io
import pandas as pd
from google.cloud import bigquery

def push_data_to_bigquery(client, df, dataset_id, table_id, date_column_name):
    table_schema = []
    for name, dtype in zip(df.columns, df.dtypes):
        if name == date_column_name:
            table_schema.append('DATETIME')
        elif dtype.name == 'object':
            table_schema.append('STRING')
        else:
            table_schema.append(str(dtype).upper())

    # Assigning the references
    dataset_id = dataset_id
    table_id = table_id
    dataset_ref = client.dataset(dataset_id)
    table_ref = dataset_ref.table(table_id)

    # Extracting the column names
    bq_column_names = list(df.columns)

    # Converting the date column
    df[date_column_name] = pd.to_datetime(df[date_column_name])
    df[date_column_name] = df[date_column_name].dt.strftime("%Y-%m-%dT%H:%M:%S")

    # Customise the Jobconfig setup
    job_config = bigquery.LoadJobConfig()
    job_config.source_format = bigquery.SourceFormat.NEWLINE_DELIMITED_JSON
    schema_results = []

    # Dynamically creating the SQL Schema From Two Lists (Column Names)
    for name, schema in zip(bq_column_names, table_schema):
        schema_results.append(bigquery.SchemaField(name, schema, mode='NULLABLE'))

    job_config.schema = schema_results

    # Running the Job iside of a StringIO stream:
    with io.StringIO(df.to_json(orient="records",lines=True)) as source_file:
        job = client.load_table_from_file(source_file, table_ref, job_config=job_config)
    job.result()
