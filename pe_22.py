#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function
import itertools

def main():
    for idx, perm in enumerate(itertools.permutations('0123456789')):
        if idx == 999999:
            print(''.join(perm))
            break

if __name__ == '__main__':
    main()
