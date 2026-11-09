'''
1 ≤ B, W ≤ 100,
-1000 ≤ X, Y, Z ≤ 1000

블랙 공 == 하얀 공

블랙 공 < 하얀 공 or 블랙 공 > 하얀 공
|블랙공-하얀공| * Z

'''

import sys
sys.stdin = open("1_sample_input.txt", "r")

T = int(input())


for test_case in range(1, T+1):
    B, W, X, Y, Z = map(int, input().split())

    change = min(B, W)

    results = []
    for i in range(change+1):
        total = (B-i) * X + (W-i) * Y + 2 * i * Z
        results.append(total)

    print(max(results))

