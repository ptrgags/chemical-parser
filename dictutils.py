def add_dicts(dict1, dict2):
    '''
    Merge two dicts of string -> int, adding values
    when keys are the same

    dict1 -- the first dict
    dict2 -- the secod dict
    '''
    totals = {}
    for key in dict1:
        totals.setdefault(key, 0)
        totals[key] += dict1[key]
    for key in dict2:
        totals.setdefault(key, 0)
        totals[key] += dict2[key]
    return totals

def scale_dict(d, scalar):
    '''
    Multiply every value in a string -> int dict
    by a constant scalar

    d -- a dictionary of string -> int
    scalar -- scalar multiplier
    '''
    return {k: scalar * v for k, v in d.items()}
