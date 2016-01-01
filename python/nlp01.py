# -*- coding: utf-8 -*-
def nlp01(text):
    output = ""
    for i in range(0, len(text), 2):
        output += text[i]
    return output

print(nlp01(u"パタトクカシーー"))
