#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

with open(sys.argv[1]) as f:
    content = f.read()

content.replace("\t", " ")

print(content)
