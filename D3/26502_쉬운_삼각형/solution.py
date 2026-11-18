'''
x값과 먼 값
그에 해당하는 y값의 좌표를 곱해서
max 값 갱신
'''

import sys

sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    dots = []

    for _ in range(N):
        x, y = map(int, input().split())
        dots.append((x, y))

    dots.sort(key=lambda x: (x[0], x[1]))

    area = 0

    for dot in dots:
        diff_x = 0
        diff_y = 0
        for dot2 in dots:
            if dot[0] == dot2[0]:
                diff_y = max(diff_y, abs(dot[1] - dot2[1]))

            if dot[1] == dot2[1]:
                diff_x = max(diff_x, abs(dot[0] - dot2[0]))

        area = max(area, diff_x * diff_y)

    print(area)
