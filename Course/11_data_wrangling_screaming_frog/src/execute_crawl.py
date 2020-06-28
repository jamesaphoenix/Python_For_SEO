# Module Imports
import pandas as pd
import os
import subprocess
from errors import ValidationError, UnsupportedPlatformError
from sys import platform

# Loading Wrapper Classes
from csv_parser import CsvParser
from screaming_frog_automation import ScreamingFrogAnalyser

GOOGLE_CLOUD_PROJECT_ID = ''
OUTPUTFOLDER = ''
SERVICE_ACCOUNT_KEY_LOCATION = ''

def run(website_urls=website_urls, outputfolder=OUTPUTFOLDER,
export_tabs=export_tabs, export_bulk_exports=export_bulk_exports):
    sf = ScreamingFrogAnalyser(website_urls=website_urls,
                               outputfolder=OUTPUTFOLDER,
                               export_tabs=export_tabs,
                               export_bulk_exports=export_bulk_exports)

    sf.run_crawls()

    parser = CsvParser(outputfolder=outputfolder,
                   file_paths=sf._sf_folders,
                   website_urls=sf._website_urls)
