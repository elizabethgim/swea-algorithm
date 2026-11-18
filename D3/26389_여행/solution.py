'''
N - S
E - W

(0, 0)
NWSE
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    answer = "No"
    A = input().strip()

    n, w, s, e = 0, 0, 0, 0

    for a in A:
        if a == "N":
            n += 1
        elif a == "S":
            s += 1
        elif a == "W":
            w += 1
        else:  # E
            e += 1

    print(n, s, w, e)
    if n == s and w == e:
        answer = "Yes"
    else:
        ns = "No"
        we = "No"

        if n > 0 and s > 0:
            ns = "Yes"
        elif n == 0 and s == 0:
            ns = "Yes"
        elif (n == 0 and s > 0) or (n > 0 and s == 0):
            ns = "No"

        if w > 0 and e > 0:
            we = "Yes"
        elif w == 0 and e == 0:
            we = "Yes"
        elif (w == 0 and e > 0) or (w > 0 and e == 0):
            we = "No"

        if ns == "Yes" and we == "Yes":
            answer = "Yes"

    print(answer)

