#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math

def get_recurrent_cycle_len(x):
    v = 1
    seen_remainder = {}
    pos = 0
    while True:
        if v / x != 0:
            d = v/x
            v -= d*x
            if v == 0:
                return 0
            if v in seen_remainder:
                return pos - seen_remainder[v]
            seen_remainder[v] = pos
        v *= 10
        pos += 1
    return None

def main():
    max_cycle = 0
    result = 0
    for i in range(1, 1000):
        cycle_len = get_recurrent_cycle_len(i)
        if max_cycle < cycle_len:
            result = i
            max_cycle = cycle_len
    print(result, max_cycle)

if __name__ == '__main__':
    main()
