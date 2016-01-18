#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys


def morpheme_reader(mecabfile):
    sentences = []
    sentence = []
    for morpheme in mecabfile:
        if morpheme == "EOS\n":
            sentences.append(sentence)
            # shallow/deep copy
            # del sentence[:]  # 参照
            sentence = []
        else:
            surface, feature = morpheme.split("\t")
            features = feature.split(",")
            morpheme_dict = {
                'surface': surface,
                'base': features[6],
                'pos': features[0],
                'pos1': features[1],
            }
            sentence.append(morpheme_dict)

    return sentences


def main():
    with open(sys.argv[1], 'r') as mecabfile:
        sentences = morpheme_reader(mecabfile)

    return sentences


if __name__ == '__main__':
    sentences = main()
    print("[")
    for sentence in sentences:
        print(sentences)
        print("]")
