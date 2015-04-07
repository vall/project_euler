#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math

def get_divisors(x):
    res = [1]
    for i in range(2, int(math.sqrt(x))+1):
        if x % i == 0:
            res.append(i)
            if x/i != i:
                res.append(x/i)
    return res

def get_abundant_numbers():
    res = set()
    for i in range(1, 28123):
        if sum(get_divisors(i)) > i:
            res.add(i)
    return res

def is_sum_of(val, numbers):
    for n in numbers:
        if n > val:
            break
        if (val - n) in numbers:
            return True
    return False

def main():
    abund = get_abundant_numbers()
    res = 0
    for i in range(28123):
        if not is_sum_of(i, abund):
            res += i
    print(res)

if __name__ == '__main__':
    main()
