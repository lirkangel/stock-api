def get_path(d, key_path, default_val=None):
    paths = key_path.split('.')
    try:
        for k in paths:
            if isinstance(d, list) and to_int(k, -1) >= 0:
                d = d[to_int(k)]
            else:
                d = d[k]

        return d
    except KeyError:
        return default_val
    except TypeError:
        return default_val


def to_int(s, _default=0):
    try:
        return int(s)
    except Exception:
        return _default


def singleton(a_class):
    def on_call(*args, **kwargs):
        if on_call.instance is None:
            on_call.instance = a_class(*args, **kwargs)
        return on_call.instance

    on_call.instance = None
    return on_call
