#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp26(filename):
    emphasis_pattarn = re.compile(r"")
    ret = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            emphasis = emphasis_pattarn.search(line)
            if emphasis:
                ret[emphasis.group()] = emphasis.group()
    return ret

for o in nlp26(sys.argv[1]):
    print(o)
