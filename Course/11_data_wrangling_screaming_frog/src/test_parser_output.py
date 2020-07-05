from errors import ValidationError, UnsupportedPlatformError
from csv_parser import CsvParser
import pandas as pd
import os

# Setting Some Variables From The Mock-Test Data Folder:
outputfolder = '/Users/jamesaphoenix/Desktop/Imran_And_James/Python_For_SEO/Course/11_data_wrangling_screaming_frog/src/test_data'

# Single File Paths:
csv_single_file_path = [outputfolder + '/' +  '2020.07.04.19.48.59']
seo_spider_single_file_path = [outputfolder + '/' + '2020-no-csv-exports-1']

# Multiple File Paths:
csv_multiple_file_paths = ['2020.07.04.19.48.59', '2020.07.04.19.49.38']; csv_multiple_file_paths = [outputfolder + '/' + item for item in csv_multiple_file_paths]
seo_spider_multiple_file_paths = ['2020-no-csv-exports-1', '2020-no-csv-exports-2'];
seo_spider_multiple_file_paths = [outputfolder + '/' + item for item in seo_spider_multiple_file_paths]

website_urls = ['https://phoenixandpartners.co.uk/', 'https://phoenixandpartners.co.uk/']

# Helper Functions:
def check_data_frame(obj):
    # 1. Check that the csv_data dict exists;
    assert len(obj._csv_data_dict.keys()) > 0
    # 2. Check that every csv_data_dict is a pandas dataframe and that it isn't empty:
    for key, value in obj._csv_data_dict.items():
        df = obj._csv_data_dict[key]
        assert type(df).__name__ == 'DataFrame'

# Tests:
def test_parser_single_files_no_csvs():
    parser = CsvParser(outputfolder=outputfolder,
                      file_paths=seo_spider_single_file_path,
                      website_urls=website_urls[0])
    assert len(parser._csv_data_dict.keys()) == 0

def test_parser_multiple_files_no_csvs():
    parser = CsvParser(outputfolder=outputfolder,
                      file_paths=seo_spider_multiple_file_paths,
                      website_urls=website_urls)
    assert len(parser._csv_data_dict.keys()) == 0

def test_parser_single_files_csvs():
    parser = CsvParser(outputfolder=outputfolder,
                      file_paths=csv_single_file_path,
                      website_urls=website_urls[0])
    # Multiple tests here:
    check_data_frame(parser)

def test_parser_multiple_files_csvs():
    parser = CsvParser(outputfolder=outputfolder,
                      file_paths=csv_multiple_file_paths ,
                      website_urls=website_urls)
    # Multiple tests here:
    check_data_frame(parser)
