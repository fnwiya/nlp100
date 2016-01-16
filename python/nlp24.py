#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import re


def nlp24(filename):
    media_file_pattarn = re.compile(r"[ファイル|file|File]:([\w\-_\s.,\d]+\.[a-zA-Z\d]+).*\|")
    ret = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            media_file = media_file_pattarn.search(line)
            if media_file:
                ret.append(media_file.group(1))
    return ret


for l in nlp24(sys.argv[1]):
    print(l)
