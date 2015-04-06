#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math

def get_divisors(x):
    res = [1]
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            res.append(i)
            res.append(x/i)
    return res

def main():
    res = 0
    for i in range(10000):
        d = sum(get_divisors(i))
        d2 = sum(get_divisors(d))
        if d2 == i and i != d:
            res += i
    print(res)

if __name__ == '__main__':
    main()
