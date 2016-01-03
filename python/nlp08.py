#!/usr/bin/python
# -*- coding: utf-8 -*-
def cipher(text):
    output = ""
    for ch in text:
        if ch.islower():
            output += chr(219-ord(ch))
        else:
            output += ch
    return output

txt = "They promised us flying cars and all we got was 140 characters"

txt = cipher(txt)
print(txt)
txt = cipher(txt)
print(txt)
