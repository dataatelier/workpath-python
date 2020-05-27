def create_params(**kwargs) -> dict:
    # need to check start and end date if present
    if 'start_date' in kwargs or 'end_date' in kwargs:
        # either none or both need to be defined
        if (not kwargs.get('start_date') and kwargs.get('end_date')) or \
                (kwargs.get('start_date') and not kwargs.get('end_date')):
            raise ValueError('If start or end date is passed both start and end date need to be specified.')
    return {k: v for k, v in kwargs.items() if v is not None}
