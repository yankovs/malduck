from six import add_metaclass, integer_types, string_types, binary_type, PY3

if PY3:
    from builtins import int as long
else:
    from __builtin__ import long


def is_integer(v):
    return isinstance(v, integer_types)


def is_string(v):
    return isinstance(v, string_types)


def is_binary(v):
    return isinstance(v, binary_type)
