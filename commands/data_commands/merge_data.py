import pandas as pd

def merge_data(df1, df2, key, how='inner'):
    return pd.merge(df1, df2, on=key, how=how)
