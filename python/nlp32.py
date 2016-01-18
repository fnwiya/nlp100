#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp30

def nlp32(sentences):
    verbs = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == "動詞":
                verbs.append(morpheme['base'])
    return verbs

sentences = nlp30.main()
verbs = nlp32(sentences)
for verb in verbs:
    print(verb),
