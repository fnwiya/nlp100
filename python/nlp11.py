#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys


def separate_by_tab(filename):
    with open(filename) as f:
        content = f.read()
    content.replace("\t", " ")
    print(content)

separate_by_tab(sys.argv[1])
