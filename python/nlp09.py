#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


def typoglycemia(text):
    words = text.split()
    if len(words) <= 4:
        return text
    else:
        start_word = words[0]
        end_word = words[-1]
        mid = list(words[1:-2])
        random.shuffle(mid)
        ret = start_word + " " + " ".join(mid) + " " + end_word
        return ret

print(typoglycemia("I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."))
