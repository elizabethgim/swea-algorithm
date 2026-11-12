'''
주변 8방향에 지뢰가 없어야지만 큐에 넣기
지뢰가 있지만 클릭할 수 있을 때
'''

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def bfs(si, sj, board):
    que = deque()
    que.append((si, sj))

    while que:
        x, y = que.popleft()
        # print(x, y)

        for k in range(8):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                if board[nx][ny] == ".":
                    # que.append((nx, ny))
                    # visited[nx][ny] = True
                    visited[nx][ny] = True

                    # check
                    flag = True
                    for m in range(8):
                        mx = nx + dx[m]
                        my = ny + dy[m]

                        if 0 <= mx < N and 0 <= my < N and board[mx][my] == '*':
                            flag = False

                    if flag:
                        que.append((nx, ny))

    return visited


for tc in range(1, T+1):
    N = int(input())

    board = []
    bomb = [[0 for _ in range(N)] for _ in range(N)]

    for _ in range(N):
        board.append([x for x in input()])

    answer = 0
    visited = [[False for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if board[i][j] == "*":
                bomb[i][j] = -1
                visited[i][j] = True

                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if 0 <= ni < N and 0 <= nj < N:
                        if bomb[ni][nj] != -1:
                            bomb[ni][nj] += 1

    # for i in range(N):
    #     print(bomb[i])
    # print()

    for i in range(N):
        for j in range(N):
            if bomb[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                bfs(i, j, board)
                answer += 1

    # for i in range(N):
    #     print(visited[i])
    # print()

    for i in range(N):
        for j in range(N):
            if not visited[i][j] and bomb[i][j] > 0:
                answer += 1

    print(f"#{tc} {answer}")


    # for i in range(N):
    #     for j in range(N):
    #         if board[i][j] == "." and not visited[i][j]:
    #             visited[i][j] = True
    #             visited = bfs(i, j, answer, board)
    #             answer += 1
    #
    #             for _ in range(N):
    #                 print(visited[_])
    #             print()
    #
    # print(f"#{tc} {answer}")
    # cnt = 1
    # for i in range(N):
    #     for j in range(N):
    #         if board[i][j] == ".":
    #             bomb = bfs(i, j, cnt, bomb)
    #             cnt += 1

    # print(f"#{tc} {cnt-1}")
