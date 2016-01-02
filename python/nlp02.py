#!/usr/bin/python
# -*- coding: utf-8 -*-


def nlp02(text1, text2):
    output = ""
    for i in range(min(len(text1), len(text2))):
        output += text1[i]
        output += text2[i]
    return output

print(nlp02(u"パトカー", u"タクシー"))
