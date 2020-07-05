import yaml

class ConfigurationError(Exception):
    def __init__(self, message, errors):
        super().__init__(message)
        self.errors = errors

def config_setup_check(config_options:list):
    results = []
    for item in config_options:
        if item == '':
            results.append(item)
    if results:
        raise ConfigurationError('There was an error with your configuration', '''Double check that either your GOOGLE_CLOUD_PROJECT_ID or
        SERVICE_ACCOUNT_KEY_LOCATION are not empty strings.''')
    print("Passed all data upload validation checks!")
    return "Passed all validation checks!"

def dataframe_checker(obj):
    truth_values = []
    """This function will return a boolean True for if there
    is a pandas dataframe that is not empty and has rows greater than 0 and False for anything else."""
    for key, value in obj._csv_data_dict.items():
        df = obj._csv_data_dict[key]
        if type(df).__name__ == 'DataFrame' and df.shape[0] > 0:
            truth_values.append(True)
        else:
            truth_values.append(False)
    return truth_values

def dataframe_row_checker(obj):
    new_dict = {}
    """This function will return any non-empty dataframes."""
    for key, value in obj._csv_data_dict.items():
        df = obj._csv_data_dict[key]
        if type(df).__name__ == 'DataFrame' and df.shape[0] > 0:
            new_dict[key] = value
    return new_dict

class YamlParser(object):
    def __init__(self):
        self._parse_setup_file()
        self._check_bigquery_inputs()
    def _parse_setup_file(self):
        with open('setup.yaml') as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
    def _check_bigquery_inputs(self):
        """ Checking to see whether all of the bigquery inputs are numbers."""
        good_values = [item for item in self.data['bigquery_table_id_mappings'].values() if item]
        if len(good_values) == len(self.data['bigquery_table_id_mappings'].values()):
            self._bigquery_inputs_validated = True
        else:
            self._bigquery_inputs_validated = False
