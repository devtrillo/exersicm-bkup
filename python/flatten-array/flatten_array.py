def flatten(iterable):
    flattened = []
    _flatten_into(iterable, flattened)
    return flattened


def _flatten_into(iterable, flattened):
    for item in iterable:
        if item is None:
            continue
        if isinstance(item, list):
            _flatten_into(item, flattened)
        else:
            flattened.append(item)
