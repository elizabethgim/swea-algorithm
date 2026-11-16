'''
 1이면 흑돌, 2이면 백돌
[0, 0, 0, 0]
[0, 2, 1, 0]
[0, 1, 2, 0]
[0, 0, 0, 0]

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]


def check(i, j, k, board):
    op = 1 if k == 2 else 2

    answer = []
    for m in range(8):
        ni = i + dx[m]
        nj = j + dy[m]

        if 0 <= ni < N and 0 <= nj < N:
            if board[ni][nj] == op:
                stack = [(ni, nj)]
                nx, ny = ni, nj

                while True:
                    nx = nx + dx[m]
                    ny = ny + dy[m]

                    if 0 <= nx < N and 0 <= ny < N:
                        if board[nx][ny] == op:
                            stack.append((nx, ny))
                        elif board[nx][ny] == k:
                            answer = answer + stack
                            break
                        elif board[nx][ny] == 0:
                            break
                    else:
                        break

    return answer


for tc in range(1, T+1):
    N, M = map(int, input().split())

    board = [[0 for _ in range(N)] for _ in range(N)]

    board[N // 2-1][N // 2-1] = 2
    board[N // 2][N // 2] = 2
    board[N // 2][N // 2-1] = 1
    board[N // 2-1][N // 2] = 1

    for i in range(M):
        j, i, k = map(int, input().split())

        i = i-1
        j = j-1

        if 0 <= i < N and 0 <= j < N and board[i][j] == 0:
            flip = check(i, j, k, board)

            if flip:
                board[i][j] = k

            while flip:
                x, y = flip.pop()
                board[x][y] = k

    count = [0, 0]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count[0] += 1
            elif board[i][j] == 2:
                count[1] += 1

            # if k == 1:
            #     count[k-1] += len(flip) + 1
            #     count[k] -= len(flip)
            # elif k == 2:
            #     count[k-1] += len(flip) + 1
            #     count[k-2] -= len(flip)
        #
        #     if flip:
        #         board[i][j] = k
        #
        #         while flip:
        #             x, y = flip.pop()
        #             board[x][y] = k
        #
        #     for ii in range(N):
        #         print(board[ii])
        #     print(f"{count[0]} {count[1]}")
        #     print()

            # ni, nj, ni2, nj2, flag = check(i, j, k, board)
            # if flag:
            #     board[i][j] = k
            #     board[ni][nj] = k
            #     if k == 2:
            #         count[k-1] += 2
            #         count[k-2] -= 1
            #     elif k == 1:
            #         count[k - 1] += 2
            #         count[k] -= 1
            #
            #     for i in range(N):
            #         print(board[i])
            #     print(f"{count[0]} {count[1]}")
            #     print()

    print(f"#{tc} {count[0]} {count[1]}")
