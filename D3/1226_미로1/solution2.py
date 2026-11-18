import sys
sys.stdin = open("input.txt", "r")

T = 10

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(board):
    stack = []
    stack.append((1, 1))

    visited = [[False for _ in range(16)] for _ in range(16)]

    while stack:
        x, y = stack.pop()

        if visited[x][y]:
            continue

        visited[x][y] = True

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if not visited[nx][ny]:
                    if board[nx][ny] == 0 or board[nx][ny] == 3:
                        stack.append((nx, ny))

    if visited[13][13]:
        return 1

    return 0


def recurrent(x, y, visited):
    visited[x][y] = True
    if x == 13 and y == 13:
        return 1

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 16 and 0 <= ny < 16:
            if not visited[nx][ny]:
                if board[nx][ny] == 0 or board[nx][ny] == 3:
                    temp = recurrent(nx, ny, visited)
                    if temp == 1:
                        return 1

    return 0


for tc in range(1, 11):
    n = int(input())

    board = []
    for _ in range(16):
        board.append(list(int(s) for s in input()))

    # answer = dfs(board)
    answer= recurrent(1, 1, visited=[[False for _ in range(16)] for _ in range(16)])
    print(f"#{n} {answer}")
