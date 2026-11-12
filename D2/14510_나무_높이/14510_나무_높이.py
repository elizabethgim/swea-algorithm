'''
https://ghs4593.tistory.com/12

1, 2, 1, 2, 1, 2, ...
남은 일 수: 4
1 2 3 4
o o o
x o x o
'''

import sys
sys.stdin = open("Sample_input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_tree_height = max(trees)

    diff = [0 for _ in range(N)]
    for i in range(N):
        diff[i] = max_tree_height - trees[i]

    water = [[0, 0] for _ in range(N)] # one, two
    one, two = 0, 0

    for i in range(N):
        two += diff[i] // 2
        one += diff[i] % 2

    if two > one:
        while two - one > 1:
            two -= 1
            one += 2

    if one > two:
        answer = one * 2 - 1
    else:
        answer = two * 2

    print(f"#{test_case} {answer}")
