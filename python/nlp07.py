#!/usr/bin/python
# -*- coding: utf-8 -*-
def nlp07(x, y, z):
    return unicode(x) + u'時の' + unicode(y) + u'は' + unicode(z)

x = 12
y = u'気温'
z = 22.4
print(nlp07(x, y, z))
