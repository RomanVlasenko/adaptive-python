# Base compression algorithm
from itertools import groupby


def count(iterable):
    l = len(list(iterable))
    return str(l) if l > 1 else ""


def functional_with_l_comprehension(string):
    return "".join(([count(g) + k for k, g in groupby(list(string))]))


def functional(string):
    out_str = ''
    for k, g in groupby(list(string)):
        grp_size = len(list(g))
        if grp_size > 1:
            out_str += str(grp_size)
        out_str += k

    return out_str


def imperative(string):
    counter = 1
    curr_char = ''
    out_str = ''

    for ch in list(string):
        if curr_char == ch:
            counter += 1
        else:
            if counter > 1:
                out_str += str(counter)

            out_str += str(curr_char)
            curr_char = ch

            counter = 1

    if counter > 1:
        out_str += str(counter)
    out_str += curr_char

    return out_str


input_str = input()
print(functional_with_l_comprehension(input_str))
print(functional(input_str))
print(imperative(input_str))
