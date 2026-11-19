'''
높이가 B 이상인 탑 중에서 가장 작은 탑

'''
import sys
sys.stdin = open("input.txt", "r")

import math
T = int(input())

def dfs(start, total):
    global answer

    # print(total)
    if total >= B:
        answer = min(total, answer)
        return

    for i in range(start, N):
        total += H[i]
        dfs(i+1, total)
        total -= H[i]


for tc in range(1, T+1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    visited = [False for _ in range(N)]

    answer = math.inf
    for i in range(N):
        dfs(i, 0)

    answer = abs(answer-B)
    print(f"#{tc} {answer}")
