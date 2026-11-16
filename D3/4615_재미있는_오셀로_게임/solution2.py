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


def put(r, c, k):
    op = 3 - k
    board[r][c] = k

    for d in range(8):
        nr = r + dx[d]
        nc = c + dy[d]
        cnt = 0

        while 0 <= nr < N and 0 <= nc < N and board[nr][nc] == op:
            cnt += 1
            nr += dx[d]
            nc += dy[d]

        if cnt and 0 <= nr < N and 0 <= nc < N and board[nr][nc] == k:
            for s in range(1, cnt+1):
                board[r+dx[d]*s][c+dy[d]*s] = k


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
            put(i, j, k)

    count = [0, 0]
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                count[0] += 1
            elif board[i][j] == 2:
                count[1] += 1

    print(f"#{tc} {count[0]} {count[1]}")
