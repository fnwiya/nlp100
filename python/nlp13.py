#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def combine_2files(file1, file2, output_filename):
    with open(file1) as f1:
        col1 = f1.readlines()
    with open(file2) as f2:
        col2 = f2.readlines()
    lines = zip(col1, col2)
    with open(output_filename, 'w') as write_file:
        for i in range(len(lines)):
            write_file.write('\t'.join(lines[i]))

combine_2files(sys.argv[1], sys.argv[2], 'col12.txt')
