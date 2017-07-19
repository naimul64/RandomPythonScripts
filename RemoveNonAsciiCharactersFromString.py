#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def removeNonAscii(string):
    nonascii = bytearray(range(0x80, 0x100))
    return string.translate(None, nonascii)


print removeNonAscii("ROKSANA Ã¢â‚¬Å¾")
print removeNonAscii("abc ডড cde রর efg")