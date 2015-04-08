#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math
import sys

def name_score(name):
    res = 0
    for ltr in name:
        if ltr.isalpha():
            v = ord(ltr.lower()) - ord('a') + 1
            res += v
    return res

def main():
    names = sys.stdin.readline().strip().split(',')
    names = sorted(names)
    res = 0
    for idx, name in enumerate(names):
        res += (idx + 1) * name_score(name)
    print(res)

if __name__ == '__main__':
    main()
