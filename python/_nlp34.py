#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp30
import re


def nlp34(sentences):
    no = []
    search_word = re.compile(r".+の.+")
    for sentence in sentences:
        for morpheme in sentence:
            is_no = search_word.match(morpheme['surface'])
            if is_no and morpheme['pos'] == "名詞":
                no.append(morpheme['surface'])
    return no

sentences = nlp30.main()
no = nlp34(sentences)
for word in no:
    print(word),
