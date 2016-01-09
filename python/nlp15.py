#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

n = int(sys.argv[2])
with open(sys.argv[1]) as f:
    lines = f.readlines()
    l = len(lines)

for line in lines[len(lines) - n:]:
    print(line),
