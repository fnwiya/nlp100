#!/usr/bin/python
# -*- coding: utf-8 -*-
def nlp03(text):
    pi = []
    l = text.split()
    for word in l:
        letters_num = 0
        for i in range(len(word)):
            if word[i].isalpha():
                letters_num += 1
        pi.append(letters_num)
    return pi

print(nlp03("Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."))
