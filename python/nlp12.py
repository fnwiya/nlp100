#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def write_one_col(col_num, write_filename):
    with open(sys.argv[1]) as f:
        col = []
        lines = f.readlines()
        for line in lines:
            col.append(line.split()[col_num] + '\n')
        with open(write_filename, 'w') as f:
            f.writelines(col)

write_one_col(0, "col1.txt")
write_one_col(1, "col2.txt")
