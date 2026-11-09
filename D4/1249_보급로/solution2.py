'''
bfs/다익스트라 알고리즘
'''

import sys
sys.stdin = open("input.txt", "r")

from collections import deque
import math

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(board, n):
    que = deque()
    que.append((0, 0, 0))

    while que:
        x, y, d = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                nd = d + board[nx][ny]
                if nd < dist[nx][ny]:
                    dist[nx][ny] = nd
                    que.append((nx, ny, nd))

    return dist[n - 1][n - 1]


for test_case in range(1, T + 1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input())))

    dist = [[math.inf for _ in range(n)] for _ in range(n)]
    dist[0][0] = 0

    answer = bfs(board, n)

    print(f"#{test_case} {answer}")
