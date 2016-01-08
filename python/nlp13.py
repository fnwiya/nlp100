#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1]) as f1:
    col1 = f1.readlines()
with open(sys.argv[2]) as f2:
    col2 = f2.readlines()

lines = zip(col1, col2)

with open('col12.txt', 'w') as write_file:
    for i in range(len(lines)):
        write_file.write('\t'.join(lines[i]))
