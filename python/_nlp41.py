#!/usr/bin/env python
# -*- coding: utf-8 -*-
import nlp40


class Chunk():
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs
