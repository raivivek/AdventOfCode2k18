#! /usr/bin/env python3

from itertools import product


with open('../input/day2.txt') as f:
    boxids = f.readlines()


def checksum(boxids):
    twos, threes = 0, 0
    for box in boxids:
        unique_letters = set(list(box))
        counts = [box.count(x) for x in unique_letters]
        if 2 in counts:
            twos = twos + 1
        if 3 in counts:
            threes = threes + 1

    return twos*threes


def get_diff_boxids(boxids):
    for (i, j) in product(boxids, boxids):
        count = 0
        if len(i) != len(j):
            print("Error. Lengths not equal")
            break
        count = [a != b for (a, b) in zip(i, j)]
        if sum(count) == 1:
            return ''.join(
                letter for (index, letter) in enumerate(i) if not count[index]
            )

print(checksum(boxids))

print(get_diff_boxids(boxids))
