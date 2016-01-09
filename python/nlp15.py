#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def tail(filename, show_lines):
    with open(filename) as f:
        lines = f.readlines()
    for line in lines[len(lines) - show_lines:]:
        print(line),

tail(sys.argv[1], int(sys.argv[2]))
