# Module Imports
import pandas as pd
import os
import subprocess
from errors import ValidationError, UnsupportedPlatformError
from sys import platform

# Loading Wrapper Classes
from csv_parser import CsvParser
from screaming_frog_automation import ScreamingFrogAnalyser

# Setup Variables - You will need to change these depending upon your Mac!
GOOGLE_CLOUD_PROJECT_ID = ''
OUTPUTFOLDER = '/Users/jamesaphoenix/Desktop'
SERVICE_ACCOUNT_KEY_LOCATION = ''

def run(website_urls, outputfolder='',
export_tabs=False, export_reports=False, export_bulk_exports=False):

    # Automatically create the correct --headless Screaming Frog commands;
    sf = ScreamingFrogAnalyser(website_urls=website_urls,
                               outputfolder=outputfolder,
                               export_tabs=export_tabs,
                               export_reports=export_reports,
                               export_bulk_exports=export_bulk_exports)

    # Start running the web crawls
    sf.run_crawls()

    parser = CsvParser(outputfolder=outputfolder,
                   file_paths=sf._sf_folders,
                   website_urls=sf._website_urls)

    # Return the objects for running tests;
    return sf

if __name__ == '__main__':
    run(website_urls=['https://phoenixandpartners.co.uk/'],
    outputfolder=OUTPUTFOLDER,
    export_tabs='Images:Missing Alt Text',
    export_reports='Redirect & Canonical Chains',
    export_bulk_exports='All Images')
