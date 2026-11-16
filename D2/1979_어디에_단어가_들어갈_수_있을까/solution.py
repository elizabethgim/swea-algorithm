'''
흰 색 부분은 1
검은 색 부분은 0
'''

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())


def bfs(i, j):
    que = deque()
    que.append((i, j, 1))

    while que:
        x, y, d = que.popleft()

        for k in range(2):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and board[nx][ny] == 0:
                    visited[nx][ny] = True
                    que.append((nx, ny, d+1))


for tc in range(1, T+1):
    N, K = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    count = 0
    dx = [0, 1]
    dy = [1, 0]
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                bfs(i, j)


    # for i in range(N):
    #     row_total = 0
    #     col_total = 0
    #     for j in range(N):
    #         if board[i][j] == 0:
    #             row_total += 1
    #         elif board[i][j] == 1:
    #             if row_total >= K:
    #                 count += 1
    #             row_total = 0
    #         if board[j][i] == 0:
    #             col_total += 1
    #         elif board[j][i] == 1:
    #             if col_total >= K:
    #                 count += 1
    #             col_total = 0

    print(f"#{tc} {count}")
