#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp21(filename):
    search_word = re.compile(r"\[\[Category:.+\]\]")
    ret = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if search_word.search(line):
                ret.append(line)
    return ret

for l in nlp21(sys.argv[1]):
    print(l),
