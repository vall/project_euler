#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math

def is_prime(x, cache={}):
    result = False
    x = abs(x)
    if x in cache:
        return cache[x]
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            break
    else:
        result = True
    cache[x] = result
    return result

def primes_chain_len(a, b):
    i = 0
    while is_prime(i**2 + a*i + b):
        i += 1
    return i

def main():
    a, b = 0, 0
    max_len = 0
    for i in range(-1000, 1001):
        for j in range(-1000, 1001):
            cur_len = primes_chain_len(i, j)
            if cur_len > max_len:
                a, b, max_len = i, j, cur_len
    print(a*b, max_len)

if __name__ == '__main__':
    main()
