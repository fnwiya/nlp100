#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp23(filename):
    search_word = re.compile(r"=(=+) (.+) =\1")
    ret = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            section = search_word.match(line)
            if section:
                ret.append((section.group(2), len(section.group(1))))
    return ret

for l in nlp23(sys.argv[1]):
    for n in l:
        print(n),
