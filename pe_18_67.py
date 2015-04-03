#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import math
import sys

def traverse_triang(tri):
    for i in range(1, len(tri)):
        for j in range(len(tri[i])):
            start_id = max(0, j-1) 
            end_id =  min(j, len(tri[i-1])) + 1
            max_parent = max(tri[i-1][start_id : end_id])
            tri[i][j] += max_parent
    print(max(tri[-1]))

def main():
    tri = []
    for line in sys.stdin:
        arr = map(int, line.strip().split())
        tri.append(arr)
    for i in tri:
        print(i)
    traverse_triang(tri)

if __name__ == '__main__':
    main()
