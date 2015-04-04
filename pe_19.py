#!/usr/bin/env pypy
# -*- coding: utf-8 -*-

from __future__ import print_function

def month_len(year, monht):
    month_len_table = {
        0: 31,
        1: year_len(year) - 337,
        2: 31,
        3: 30,
        4: 31,
        5: 30,
        6: 31,
        7: 31,
        8: 30,
        9: 31,
        10: 30,
        11: 31
    }
    return month_len_table[monht]

def year_len(year):
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return 366
    return 365

def main():
    res = 0
    d = year_len(1900)
    year = 1901
    month = 0
    while year <= 2000:
        if d % 7 == 6:
            res += 1
        d += month_len(year, month)
        month += 1
        if month > 11:
            year += 1
            month = 0
    print(res)

if __name__ == '__main__':
    main()
