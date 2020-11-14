# Google Cloud Credentials + BQ Client Initialisation
credentials = service_account.Credentials.from_service_account_file('service_account.json')
client = bigquery.Client(credentials=credentials, project='pushgroup-adinvestor')

class BigQueryAutomation():
    def __init__(self, client, project_id, dataset_id,
    available_data_dict):
        self.client = client
        self.project_id = project_id
        self.dataset_id = dataset_id
        self.available_data_dict = available_data_dict

    # Helper Functions
    def extract_schema_data(self, df, date_column_name):
        table_schema = []
        for name, dtype in zip(df.columns, df.dtypes):
            if name == date_column_name:
                table_schema.append('DATETIME')
            elif dtype.name == 'object':
                table_schema.append('STRING')
            else:
                table_schema.append(str(dtype).upper())
        return table_schema

    # Automatically create the required schema
    def _create_schema_dictionary(self):
        self.master_schema_data = []
        for key, value in self.available_data_dict.items():

            schema_dict = {}
            schema_dict['name'] = key

            # Extracting the column names:
            bq_column_names = list(value.columns)
            # Converting the date column:
            value['Date'] = pd.to_datetime(value['Date'])
            value['Date'] = value['Date'].dt.strftime("%Y-%m-%dT%H:%M:%S")

            # Dynamically creating the SQL Schema From Two Lists (Column Names)
            table_schema = self.extract_schema_data(value, 'Date')
            schema_results = []
            for name, schema in zip(bq_column_names, table_schema):
                schema_results.append(bigquery.SchemaField(name, schema, mode='NULLABLE'))

            schema_dict['data'] = value
            schema_dict['schema'] = schema_results

            # Save it to the schema data list
            self.master_schema_data.append(schema_dict)

    # Create BigQuery Tables
    def _create_single_bg_table(self):
        pass

    # Push The Data To BigQuery If The BigQuery table is there it is an dataframe that is not empty
    def automate_bg_reports(self):
        pass
