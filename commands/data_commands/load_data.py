import pandas as pd

def load_data(file_path, file_type='csv'):
    if file_type == 'csv':
        return pd.read_csv(file_path)
    elif file_type == 'excel':
        return pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file type provided")
