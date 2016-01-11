#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp22(filename):
    search_word = re.compile("\[\[Category:(.+)\]\]")
    ret = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            category_name = search_word.match(line)
            if category_name:
                ret.append(category_name.group(1))
    return ret

for l in nlp22(sys.argv[1]):
    print(l),
