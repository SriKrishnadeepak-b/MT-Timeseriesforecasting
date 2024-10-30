import pandas as pd

def load_data(file_path):
    data = pd.read_csv(file_path)
    data['Date'] = pd.to_datetime(data['Date'], format='%m/%Y')
    data.set_index('Date', inplace=True)
    return data

def preprocess_data(data):
    data['Enplaned_diff'] = data['Enplaned'].diff()
    return data.dropna()  # Drop NaNs introduced by differencing
