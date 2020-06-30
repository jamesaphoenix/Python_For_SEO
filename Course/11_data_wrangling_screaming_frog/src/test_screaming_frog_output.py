# Module Imports
import pandas as pd
import os
import shutil
import subprocess
from errors import ValidationError, UnsupportedPlatformError
from sys import platform
import pytest

# Loading Wrapper Classes
from csv_parser import CsvParser
from screaming_frog_automation import ScreamingFrogAnalyser
from main import run

OUTPUTFOLDER = '/Users/jamesaphoenix/Desktop'
INCORRECTOUTPUTFOLDER = 'iurhgeuihge/Desktop'

### Helper Functions For Removing Folders After Completing The Task:
def delete_folders(folders):
    for folder in folders:
        shutil.rmtree(folder)

# 1. A test for the correct outputfolder (with exports)
def test_correct_outputfolder_with_exports():
    sf_worker = run(website_urls=['https://phoenixandpartners.co.uk/'],
    outputfolder=OUTPUTFOLDER,
    export_tabs='Images:Missing Alt Text',
    export_reports='Redirect & Canonical Chains',
    export_bulk_exports='All Images')

    # Testing to see whether there are more than 1 folder that was created:
    assert len(sf_worker._sf_folders) > 0

    # Removing the created folders:
    delete_folders(sf_worker._sf_folders)

# 2. A test for the incorrect output folder (with exports)
def test_incorrect_outputfolder_with_exports():
    with pytest.raises(ValidationError):
        sf_worker = run(website_urls=['https://phoenixandpartners.co.uk/'],
        outputfolder=INCORRECTOUTPUTFOLDER,
        export_tabs='Images:Missing Alt Text',
        export_reports='Redirect & Canonical Chains',
        export_bulk_exports='All Images')

# 3. A test for correct_output folders but no reports
def test_correct_output_folder_no_reports():
    sf_worker = run(website_urls=['https://phoenixandpartners.co.uk/'],
    outputfolder=OUTPUTFOLDER,
    export_tabs=False,
    export_reports=False,
    export_bulk_exports=False)

    # Testing to see whether there are more than 1 folder that was created:
    assert len(sf_worker._sf_folders) > 0

    # Removing the created folders:
    delete_folders(sf_worker._sf_folders)

# 4. A test for correctoutput folders but the wrong reports
def test_correct_output_folder_broken_reports():
    with pytest.raises(ValidationError):
        sf_worker = run(website_urls=['https://phoenixandpartners.co.uk/'],
        outputfolder=OUTPUTFOLDER,
        export_tabs='123721893',
        export_reports='123182',
        export_bulk_exports='456456')


## 5. A test for crawling multiple URLs;
def test_multiple_crawls_correct_output_folder():
        website_urls = ['https://phoenixandpartners.co.uk/',
        'sempioneer.com']

        sf_worker = run(website_urls=website_urls,
        outputfolder=OUTPUTFOLDER,
        export_tabs=False,
        export_reports=False,
        export_bulk_exports=False)

        # Testing to see whether there are more than 1 folder that was created:
        assert len(sf_worker._sf_folders) == len(website_urls)

        # Removing the created folders:
        delete_folders(sf_worker._sf_folders)
