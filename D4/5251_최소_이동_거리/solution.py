'''
 1<=T<=50,
 1<=N, s, e<=1000,
 1<=w<=10,
 1<=E<=1000000
'''

import sys
sys.stdin = open("sample_input.txt", "r")

import math
from collections import deque

T = int(input())


for tc in range(1, T+1):
    n, e = map(int, input().split())

    dist = [[0 for _ in range(n+1)] for _ in range(n+1)]
    answer = [math.inf] * (n+1)

    for i in range(e):
        start, end, width = map(int, input().split())
        dist[start][end] = width

    print(dist)

    que = deque()
    que.append((0, 0))

    while que:
        node, d = que.popleft()

        for next_node in range(n+1):
            if dist[node][next_node] != 0:
                cost = d+dist[node][next_node]
                print(next_node, cost)

                if cost < answer[next_node]:
                    answer[next_node] = cost
                    que.append((next_node, cost))
    print(answer)

    print(f"#{tc} {answer[n]}")
