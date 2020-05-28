def create_params(**kwargs) -> dict:
    # need to check start and end date if present
    if 'start_date' in kwargs or 'end_date' in kwargs:
        # either none or both need to be defined
        if (not kwargs.get('start_date') and kwargs.get('end_date')) or \
                (kwargs.get('start_date') and not kwargs.get('end_date')):
            raise ValueError('If start or end date is passed both start and end date need to be specified.')
    return {k: v for k, v in kwargs.items() if v is not None}


def list_to_dataframe(list_to_transform, output_format):
    """
    Transform a list of dicts into a pandas DataFrame if wanted.

    :param list_to_transform: the list with dicts to transform
    :param output_format: Return a dictionary or pandas.DataFrame.
                          Possible values: 'dict' or 'json' -> dictionary
                                           'DataFrame', 'pd.DataFrame', or 'pandas.DataFrame' -> pandas.DataFrame

    :return: List of dicts or pandas DataFrame with content of given dict.
    """
    if output_format in ['dict', 'json', 'list']:
        return list_to_transform
    elif output_format in ['DataFrame', 'pd.DataFrame', 'pandas.DataFrame']:
        import pandas as pd
        return pd.DataFrame.from_dict(list_to_transform)
    else:
        raise ValueError('Output format {format} is not supported'.format(format=output_format))
