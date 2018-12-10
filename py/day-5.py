#! /usr/bin/env python3

with open('../input/day5.txt') as f:
    string = f.read().strip()

#string = "vVNQqnuUtBbTlLeEaALwTWuUJjuhCcHqQUZvztT"
string = "vVNQqnuUtBbTlLeEaALwTWuUJjuhCcHqQUZvztTpfOoFPqQWGxCWwchHgFLEcCeqBmM"
string = "vVNCcnqQqnuUtBbTlLeEaALwTWuUJjuhCcHqQUZvztTpfOoFPqQWGxCWwchHgFLEeqBmMbluYyRrxXPyLlYpUfmRrMwlGgotTOvNWwKnNknVABfFbVDdvaRtQUuqJjtTRrrNUdDunhDyCcYxXdHLjxPVFfvpXJYTibBIWwUUctTCuuvRRrrVWEejuUJwDEeOZzodLlNoCLWwGglcuUVOKfQVoyYOnsmMSqQNvWjNCctTnxhHbBXUycCtTlLYuoOauUrnNifFIyXfcZzKkCkKluYyUMfFmFfL"

def matchPolar(f, s):
    Ul = f.isupper() and s.islower()
    lU = f.islower() and s.isupper()
    polar = Ul or lU
    fu, fs = f.lower(), s.lower()

    return polar and (fu == fs)

def scanString(string):
    remove_idx = [0 for x in string]


    i = 0
    while i < len(string) - 1:
        counter = 0
        cur, nxt = string[i], string[i+1]

        while matchPolar(cur, nxt):
            counter = counter + 1
            #print(cur, nxt, counter)

            if remove_idx[i - counter + 1] == 1:
                counter = counter + 1
                continue

            remove_idx[i - counter + 1] = 1
            remove_idx[i + counter] = 1

            if (i - counter < 0) or (i + counter + 1 >= len(string)):
                break
            cur = string[i - counter]
            nxt = string[i + counter + 1]


        i = i + counter + 1

    print(''.join([x for i, x in enumerate(string) if remove_idx[i] == 0]))


def scanString2(string):
    match = True
    while match:
        i = 0
        match = False
        while i < len(string) - 1:
            if matchPolar(string[i], string[i+1]):
                match = True
                string.remove(string[i])
                string.remove(string[i+1])
            i = i + 1

scanString(list(string))
