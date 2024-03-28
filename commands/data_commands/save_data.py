def save_data(dataframe, file_path, file_type='csv'):
    if file_type == 'csv':
        dataframe.to_csv(file_path, index=False)
    elif file_type == 'excel':
        dataframe.to_excel(file_path, index=False)
    else:
        raise ValueError("Unsupported file type provided")
 