#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from collections import defaultdict


def sort_by_nth_col_count(filename, n):
    prefectures = defaultdict(int)
    with open(filename) as f:
        line = f.readline()
        while line:
            prefectures[line.split()[n-1]] += 1
            line = f.readline()
    for k, v in sorted(prefectures.items(), key=lambda x: x[1], reverse=True):
        print(k)

sort_by_nth_col_count(sys.argv[1], 1)
