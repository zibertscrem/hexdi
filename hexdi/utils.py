import collections


def get_module_name(obj):
    if isinstance(obj, str):
        return obj

    if callable(obj):
        return get_module_name(obj.__call__())

    if isinstance(obj, collections.Iterable):
        lst = list(obj)
        if len(lst) > 0:
            o = lst.pop(0)
            if callable(o):
                if len(lst) > 0:
                    arguments = lst[1]
                    return get_module_name(o.__call__(*arguments))


def get_submodules(mod):
    pass


def is_module(mod):
    pass


def is_package(mod):
    pass


def read_module_as_string(mod):
    pass
