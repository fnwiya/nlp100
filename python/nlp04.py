#!/usr/bin/python
# -*- coding: utf-8 -*-
def nlp04(text):
    output = {}
    elements_list = text.split()
    for i in range(len(elements_list)):
        n = i + 1
        if n in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
            output[elements_list[i][0]] = n
        else:
            output[elements_list[i][0:2]] = n
    return output

print(nlp04("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."))
