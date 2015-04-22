#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import itertools

def main():
    res = len(set([a**b for a,b in itertools.product(range(2,101), repeat=2)]))
    print(res)

if __name__ == '__main__':
    main()
