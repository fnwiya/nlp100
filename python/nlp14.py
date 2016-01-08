#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

n = int(sys.argv[2])
with open(sys.argv[1]) as f:
    lines = f.readlines()

for i in range(n):
    print(lines[i]),
