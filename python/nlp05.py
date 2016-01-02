#!/usr/bin/python
# -*- coding: utf-8 -*-
def n_gram(input, n):
    output = []
    for i in range(0, len(input) - n + 1, n):
        output.append(input[i:i+n])
    return output

print(n_gram("I am an NLPer".split(), 2))
print(n_gram("I am an NLPer", 2))
