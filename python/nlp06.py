#!/usr/bin/python
# -*- coding: utf-8 -*-
def n_gram(input, n):
    output = []
    for i in range(0, len(input) - n + 1, n):
        output.append(input[i:i+n])
    return output

X = set(n_gram("paraparaparadise", 2))
Y = set(n_gram("paragraph", 2))
se = "se"
print(X.union(Y))
print(X.intersection(Y))
print(X.difference(Y))
print(se in X)
print(se in Y)
