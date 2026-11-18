import sys
sys.stdin = open("input.txt", "r")

from collections import deque


def dfs(board):
    que = deque()

    for i in range(4):
        for j in range(4):
            que.append((i, j, str(board[i][j]))) # x, y, number

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    candidate = set()

    while que:
        x, y, num = que.popleft()

        if len(num) == 7:
            candidate.add(num)
            continue

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 4 and 0 <= ny < 4:
                que.append((nx, ny, num+str(board[nx][ny])))

    # print(candidate)
    return len(candidate)


T= int(input())
for tc in range(1, T+1):
    board = []
    for _ in range(4):
        board.append(list(map(int, input().split())))

    answer = dfs(board)
    print(f"#{tc} {answer}")
