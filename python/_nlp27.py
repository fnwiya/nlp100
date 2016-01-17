#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp27(filename):
    link_pattarn = re.compile(r"")
    ret = {}
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            link = link_pattarn.search(line)
            if link:
                ret[link.group()] = link.group()
    return ret

for o in nlp27(sys.argv[1]):
    print(o)
