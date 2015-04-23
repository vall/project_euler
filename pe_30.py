#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import itertools

def consists_of(n, digits):
    return sorted(n) == map(str, digits)

def sum_of_fifths_pow_str(digits):
    res = str(sum(map(lambda x:x**5, digits)))
    res = (6-len(res))*'0' + res
    return res

def main():
    result = 0
    digits = range(10)*6
    for d in itertools.combinations_with_replacement(range(10), r=6):
        val = sum_of_fifths(d)
        if consists_of(val, d):
            print(d, val)
            result += int(val)
    print(result-1)

if __name__ == '__main__':
    main()
