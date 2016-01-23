#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp30
from collections import Counter


def nlp36(sentences):
    words = []
    for sentence in sentences:
        for morpheme in sentence:
            words.append(morpheme['surface'])
    return Counter(words)

sentences = nlp30.main()
words = nlp36(sentences)
for word in words:
    print(word)

