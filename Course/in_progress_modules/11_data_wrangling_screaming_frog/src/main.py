# Module Imports
from errors import ValidationError, UnsupportedPlatformError
from google.cloud import bigquery
from google.oauth2 import service_account
import os
import pandas as pd
import subprocess
from sys import platform, exit

# Loading Wrapper Classes
from csv_parser import CsvParser
from screaming_frog_automation import ScreamingFrogAnalyser

# Utility Functions
from utils import config_setup_check, dataframe_checker, dataframe_row_checker, YamlParser
config = YamlParser()

# Setup Variables - You will need to change these depending upon your Mac + Google Cloud Platform Setup!
OUTPUTFOLDER = config.data['environment-variables']['OUTPUTFOLDER']
SERVICE_ACCOUNT_KEY_LOCATION = config.data['environment-variables']['SERVICE_ACCOUNT_KEY_LOCATION']
GOOGLE_CLOUD_PROJECT_ID = config.data['environment-variables']['GOOGLE_CLOUD_PROJECT_ID']
GOOGLE_CLOUD_BIGQUERY_DATASET_ID = config.data['environment-variables']['GOOGLE_CLOUD_BIGQUERY_DATASET_ID']
BIGQUERY_TABLE_ID_MAPPINGS = config.data['bigquery_table_id_mappings']

def sf_run(website_urls, outputfolder='',
export_tabs=False, export_reports=False,
export_bulk_exports=False, push_data_to_biquery=False,
create_bigquery_table=False, bigquery_table_mapping=BIGQUERY_TABLE_ID_MAPPINGS):

    if OUTPUTFOLDER == '':
        raise ValidationError('Your OUTPUTFOLDER cannot be empty', 'Please update your outputfolder to a valid value.')

    # Automatically create the correct --headless Screaming Frog commands;
    sf = ScreamingFrogAnalyser(website_urls=website_urls,
                               outputfolder=outputfolder,
                               export_tabs=export_tabs,
                               export_reports=export_reports,
                               export_bulk_exports=export_bulk_exports)

    # 1. Start running + saving the web crawls
    sf.run_crawls()

    parser = CsvParser(outputfolder=outputfolder,
                   file_paths=sf._sf_folders,
                   website_urls=sf._website_urls)

    # 2.1 Data checking: Making sure that there is data & at least one of the dataframes contains rows:
    if not any(dataframe_checker(parser)):
        print('''Finished crawling and saved the output to your desired folder/folders. It's impossible to save to BigQuery because you have no .csv data.
        Re-run the script with export_tabs, export_reports, or export_bulk_exports if you would like to upload to BigQuery!
        Existing the program.
        ''')
        # exit() <-- Disabling this whilst running tests.
        return sf

    # 2.1 Data checking - For valid credentials (Google Cloud Project ID + Service Account Key):
    if push_data_to_biquery == True:
        config_setup_check([GOOGLE_CLOUD_PROJECT_ID, SERVICE_ACCOUNT_KEY_LOCATION])
        # Google Cloud Credentials + BQ Client Initialisation
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_KEY_LOCATION)
        client = bigquery.Client(credentials=credentials, project=GOOGLE_CLOUD_PROJECT_ID)

    # 2.1 Data checking - Compile a list of dataframes that have both rows and columns:
    available_data = dataframe_row_checker(parser)

    # 3.1 Storing The Queryable Data:
    if create_bigquery_table == True:
        # Automatically generate the BigQuery tables with timestamped names + push the relevant data:
        print("Some function here that will automatically generate Xn BigQuery tables.")
        pass
    else:
        # Automatically use the BigQuery Table Mapping
        print("Some function here that will map the name of the BigQuery table_id against the csv_name.")
        if config._bigquery_inputs_validated == False:
            raise ValidationError("You need to use a custom dictionary to map your concatenated .csv data against BigQuery table ids.", '''
            Please update the setup.yaml file with the relevant bigquery_tab_id mappings.''')

        # Match the dictionary mapping against the available_data dictionary and only contain the Bigquery table_id's where there is data.
        # Error checking that the length of the dictionary keys are the same length as the available_data dict keys.
        pass

    # Return the objects for running tests;
    return sf

if __name__ == '__main__':
    sf_run(website_urls=['https://phoenixandpartners.co.uk/'],
    outputfolder=OUTPUTFOLDER,
    export_tabs='Images:Missing Alt Text',
    export_reports='Redirect & Canonical Chains',
    export_bulk_exports='All Images')
