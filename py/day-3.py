#! /usr/bin/env python3

import numpy as np

with open('../input/day3.txt') as f:
    claims = f.readlines()

# create fabric array
fabric = np.zeros((1000, 1000), dtype=np.str)
invalid_claims = np.zeros(len(claims), dtype=np.bool)


def claim_fabric(claims):
    for claim in claims:
        claim, coords = claim.split('@')
        claim = claim[1:].strip()
        start, size = coords.strip().split(':')
        x, y = [int(x) for x in start.split(',')]
        hx, hy = [int(p) for p in size.split('x')]

        something_exists = np.where(fabric[y:y+hy, x:x+hx] != '')
        fabric[y:y+hy, x:x+hx] = claim
        fabric[something_exists] = 'X'


claim_fabric(claims)

print(fabric)
# part 1
print(np.sum(fabric == 'X'))

# part 2
#print(invalid_claims)
#print(np.where(invalid_claims == True))
