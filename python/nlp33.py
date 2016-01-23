#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp30


def nlp33(sentences):
    sahen = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos1'] == "サ変接続":
                sahen.append(morpheme['surface'])
    return sahen

sentences = nlp30.main()
sahen = nlp33(sentences)
for word in sahen:
    print(word),
