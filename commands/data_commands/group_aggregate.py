def group_and_aggregate(dataframe, group_by_column, agg_func):
    return dataframe.groupby(group_by_column).agg(agg_func)
