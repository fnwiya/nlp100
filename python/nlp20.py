#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import json
import gzip
import re
import codecs


def nlp20(filename, search_word):
    search_word = re.compile(search_word)
    with gzip.open(filename, 'r') as f:
        with codecs.open('jawiki-england.txt', 'w', 'utf-8') as o:
            for line in f:
                obj = json.loads(line)
                if re.search(search_word, obj['title']) or re.search(search_word, obj['text']):
                    o.write(obj['text']+"\n"+"\n")

nlp20(sys.argv[1], u"イギリス")
