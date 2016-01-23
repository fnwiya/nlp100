#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp30


def nlp35(sentences):
    Nseqs = []
    Nseq = []
    for sentence in sentences:
        for morpheme in sentence:
            if morpheme['pos'] == "名詞":
                Nseq.append(morpheme['surface'])
            else:
                if len(Nseq) > 1:
                    Nseqs.append(Nseq)
                Nseq = []
    return Nseqs

sentences = nlp30.main()
Nseqs = nlp35(sentences)
for Nseq in Nseqs:
    print("".join(Nseq))
