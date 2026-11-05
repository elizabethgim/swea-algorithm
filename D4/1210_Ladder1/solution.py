import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = 10
N = 100

def track(sx, sy, board):
    que = deque()
    que.append((sx, sy))

    visited = [[False for _ in range(N)] for _ in range(N)]
    visited[sx][sy] = True

    while que:
        x, y = que.popleft()

        if 0 <= y+1 < N and board[x][y+1] == 1 and not visited[x][y+1]:
            que.append((x, y+1))
            visited[x][y+1] = True

        elif 0 <= y-1 < N and board[x][y-1] == 1 and not visited[x][y-1]:
            que.append((x, y-1))
            visited[x][y - 1] = True

        elif 0 <= x-1 < N and board[x-1][y] == 1 and not visited[x-1][y]:
            que.append((x-1, y))
            visited[x - 1][y] = True

    # for v in visited:
    #     print(v)

    for i in range(N):
        if visited[0][i]:
            return i

    return -1

for test_case in range(1, T+1):
    tc = int(input())
    board = []

    for i in range(N):
        board.append(list(map(int, input().split())))

    answer = 0
    for i in range(N):
        for j in range(N):
            if board[i][j] == 2:
                answer = track(i, j, board)
                break


    print(f"#{tc} {answer}")