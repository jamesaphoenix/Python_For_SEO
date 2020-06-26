# Google Cloud Credentials + BQ Client Initialisation
credentials = service_account.Credentials.from_service_account_file('service_account.json')
client = bigquery.Client(credentials=credentials, project='pushgroup-adinvestor')

class BigQueryAutomation():
    def __init__(self, project_id):
        pass
        # Use super().innit() to get all of the def __init variables from GoogleAuthentication

    # Helper Functions
    # Automatically create the required schema
    def _create_schema_creation(self):
        pass
    # Create BigQuery Tables
    def _create_bg_table(self):
        pass

    def _push_single_bg_table(self):
        pass

    # Push The Data To BigQuery If The BigQuery table is there it is an dataframe that is not empty
    def automate_bg_reports(self):
        pass
