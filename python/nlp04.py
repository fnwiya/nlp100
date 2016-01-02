#!/usr/bin/python
# -*- coding: utf-8 -*-
def nlp04(text):
    output = {}
    elements_list = text.split()
    for i in range(len(elements_list)):
        if i == 0 or i == 4 or i == 5 or i == 6 or i == 7 or i == 8 or i == 14 or i == 15 or i == 18:
            output[elements_list[i][0]] = i
        else:
            output[elements_list[i][0:2]] = i
    return output

print(nlp04("Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."))
