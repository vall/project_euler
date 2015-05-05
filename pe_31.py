#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
from collections import defaultdict

def coin_rec(n):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]
    cache = {}
    return coin_rec_fun(n, coins, 0, cache)

def coin_rec_fun(n, coins, coin_id, cache):
    if not coins:
        return 0
    if (n, coin_id) in cache:
        return cache[(n, coin_id)]
    res = 0
    for c in range(coin_id, len(coins)):
        v = n - coins[c]
        if v == 0:
            res += 1
        elif v > 0: 
            res += coin_rec_fun(v, coins, c, cache)
    cache[(n, coin_id)] = res
    return res

def main():
    print(coin_rec(200))

if __name__ == '__main__':
    main()
