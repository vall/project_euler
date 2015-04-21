#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math
def fix_str(x):
    v = str(x)
    if len(v) < 4:
        v = ' '*(4-len(v)) + v
    return v

def diag_sum(arr):
    res = 0
    l = len(arr)
    for i in range(l):
        res += arr[i][i]
        res += arr[l-i-1][i]
    return res - 1

def main():
    short_solution()
    long_solution()

def long_solution():
    delt = {
        0: (-1, 0), #left
        1: (0, 1),  #down
        2: (1, 0),  #right
        3: (0, -1)  #up
    }
    size = 1001  
    arr = [[0]*size for _ in range(size)]
    x = size - 1 if size % 2 else 0
    y = 0 if size % 2 else size - 1  
    val = size ** 2
    d = 0 if size % 2 else 2 
    while val > 0:
        arr[y][x] = val
        nx = x + delt[d][0]
        ny = y + delt[d][1]
        if nx >= size or nx < 0 or ny >= size or ny < 0 or arr[ny][nx] != 0:
            d = (d+1) % 4
            nx = x + delt[d][0]
            ny = y + delt[d][1]
        x = nx
        y = ny
        val -= 1
    print(diag_sum(arr))

def short_solution():
    val = 1
    delt = 2
    res = 1
    for _ in range(500):
        res += val*4
        res += 10*delt
        val += 4*delt
        delt += 2
    print(res)

if __name__ == '__main__':
    main()
