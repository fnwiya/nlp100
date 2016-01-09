#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def get_uniq_string(filename):
    first_row_strings = []
    with open(filename) as f:
        lines = f.readlines()
    for line in lines:
        first_row_strings.append(line.split()[0])
    return set(first_row_strings)

for string in get_uniq_string(sys.argv[1]):
    print(string)
