#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def split_file(filename, number_of_parts):
    with open(filename) as f:
        lines = f.readlines()

    if len(lines) % number_of_parts != 0:
        raise Exception("Undividable by N=%d" % number_of_parts)
    else:
        number_of_lines = len(lines) / number_of_parts

    for i in range(number_of_parts):
        with open("split%s.txt" % str(i), "w") as w:
            w.writelines(lines[number_of_lines * i: number_of_lines * (i + 1)])

split_file(sys.argv[1], int(sys.argv[2]))
