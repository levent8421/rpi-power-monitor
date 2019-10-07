def __raise_exception(ex, msg):
    raise ex(msg)


def no_none(param, ex, msg):
    if param:
        if isinstance(param, str):
            if param.isspace():
                __raise_exception(ex, msg)
        elif len(param) <= 0:
            __raise_exception(ex, msg)
    else:
        __raise_exception(ex, msg)
