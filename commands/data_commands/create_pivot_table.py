import pandas as pd

def create_pivot_table(dataframe, index, columns, values, aggfunc='mean'):
    return pd.pivot_table(dataframe, index=index, columns=columns, values=values, aggfunc=aggfunc)
