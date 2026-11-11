import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = 10

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def bfs(board):
    que = deque()
    que.append((1, 1))

    visited = [[False for _ in range(16)] for _ in range(16)]
    visited[1][1] = True

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if not visited[nx][ny]:
                    if board[nx][ny] == 0 or board[nx][ny] == 3:
                        que.append((nx, ny))
                        visited[nx][ny] = True

    if visited[13][13]:
        return 1

    return 0


for tc in range(1, 11):
    n = int(input())

    board = []
    for _ in range(16):
        board.append(list(int(s) for s in input()))

    answer = bfs(board)
    print(f"#{n} {answer}")
