#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def sort_by_nth_col(filename, n):
    with open(filename) as f:
        lines = f.readlines()
    sorted_lines = sorted(lines, key=lambda x: x.split()[n-1])
    sorted_lines.reverse()
    return sorted_lines

for line in sort_by_nth_col(sys.argv[1], 3):
    print(line),
