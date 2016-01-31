#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys

class Morph():
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def print_all(self):
        return self.surface + "\t" + self.base + ", " + self.pos + ", " + self.pos1


def morpheme_reader(cabochafile):
    sentences = []
    sentence = []
    for line in cabochafile:
        if line == "EOS\n":
            sentences.append(sentence)
            sentence = []
        elif line[0] == "*":
            continue
        else:
            surface, feature = line.split("\t")
            features = feature.split(",")
            morph = Morph(surface, features[6], features[0], features[1])
            sentence.append(morph)
    return sentences


def main():
    with open(sys.argv[1], "r") as cabochafile:
        sentences = morpheme_reader(cabochafile)
    return sentences

if __name__ == '__main__':
    sentences = main()
    print("Here is morphs of third sentence of givien text.")
    print("---")
    for morph in sentences[2]:
        print(morph.print_all)
