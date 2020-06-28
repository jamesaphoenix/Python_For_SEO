from errors import ValidationError, UnsupportedPlatformError
import pandas as pd
import os

class CsvParser():
    def __init__(self, outputfolder, file_paths, website_urls):
        self._output_folder = outputfolder
        self._folders = file_paths
        self._website_urls = website_urls

        # Loading the correct files
        if len(self._folders) == 0:
            raise ValidationError('''Check: 1. The output folder, 2. Your reports/exports syntax,
                                  3. The license on your Screaming Frog account,
                                  4. Whether Screaming Frog is installed in the right location''',
                                 'file_paths = []')

        # Extracting and merging multiple CSV files
        self.merge_multiple_csv_files()

    # Helper Functions
    def _get_files(self):
        self._files = []
        for folder in self._folders:
            for file in os.listdir(folder):
                self._files.append(f"{folder}/{file}")

    def _group_multiple_csv_files(self):
        self._grouped_files = {}
        for file in self._files:
            file_name = file.split('/')[-1]
            if file_name not in self._grouped_files.keys() and file_name.endswith('.csv'):
                self._grouped_files[file_name] = [file]
            elif file_name in self._grouped_files.keys() and file_name.endswith('.csv'):
                self._grouped_files[file_name].append(file)
            else:
                continue

    def _combine_multiple_csv_files(self):
        self._csv_data_dict = {}
        for key, values in self._grouped_files.items():
            if key.endswith('.csv'):
                df = pd.DataFrame()
                for index, value in enumerate(values):
                    temp_df = pd.read_csv(value)
                    # Setting a data source + domain as an extra column:
                    temp_df['Data_Source'] = value
                    temp_df['Domain'] = self._website_urls[index]
                    df = df.append(temp_df)
            self._csv_data_dict[key] = df

    # Execution Functions
    def merge_multiple_csv_files(self):
        self._get_files()
        self._group_multiple_csv_files()
        self._combine_multiple_csv_files()
