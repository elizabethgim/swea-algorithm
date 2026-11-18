'''
1
1 2
1 2 3
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    a, b, c = map(int, input().split())

    # total = a * (a+1) // 2
    # total *= b * (b+1) // 2
    # total *= c * (c+1) // 2
    #
    # print(total % 998244353)

    temp = 0
    for i in range(1, a + 1):
        temp += i

    total = temp
    temp = 0
    for j in range(1, b + 1):
        temp += j
    total *= temp

    temp = 0
    for k in range(1, c + 1):
        temp += k

    total *= temp

    print(total % 998244353)

