#!/usr/bin/python
# -*- coding: utf-8 -*-


def nlp02(text1, text2):
    output = ""
    for i in range(len(text1)):
        output += text1[i]
        output += text2[i]
    return output

print(nlp02(u"パトカー", u"タクシー"))
