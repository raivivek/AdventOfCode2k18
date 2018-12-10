#! /usr/bin/env python3

with open('../input/day1.txt', 'r') as f:
    freqs = [int(x.strip()) for x in f.readlines()]

# part 1
print(sum(freqs))

# part 2

seen = {0: 1}
run = 0

found = False

while not found:
    for num in freqs:
        run = run + num
        if seen.get(run, False):
            found = True
            break
        else:
            seen[run] = 1

print(run)
