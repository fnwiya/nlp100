#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp25(filename):
    base_info_pattarn = re.compile(r"")
    ret = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            base_info = base_info_pattarn.search(line)
            if base_info:
                ret[base_info.group()] = base_info.group()
    return ret

for o in nlp25(sys.argv[1]):
    print(o)
