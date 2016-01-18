#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp30

def nlp31(sentences):
    verbs = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == "動詞":
                verbs.append(morpheme['surface'])
    return verbs

sentences = nlp30.main()
verbs = nlp31(sentences)
for verb in verbs:
    print(verb),
