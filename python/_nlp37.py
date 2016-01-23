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
cnt = 0
for word, count in words.most_common():
    print(word)
    for i in range(int(count)):
        print('|'),
    cnt += 1
    if cnt == 9:
        break
