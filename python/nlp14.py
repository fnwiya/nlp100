#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

def head(filename, show_lines):
    with open(filename) as f:
        lines = f.readlines()
    for i in range(show_lines):
        print(lines[i]),

head(sys.argv[1], int(sys.argv[2]))
