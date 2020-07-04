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
