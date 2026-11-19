import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


def dfs(i, j):
    answer = 0
    que = deque()
    que.append((i, j, 1))

    while que:
        x, y, d = que.pop()
        answer = max(answer, d)

        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]

            if 0 <= nx < N and 0 <= ny < N:
                if (board[x][y] + 1) == board[nx][ny]:
                    que.append((nx, ny, d+1))

    return answer


for tc in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    answer = 0
    room = {}
    for i in range(N):
        for j in range(N):
            temp = dfs(i, j)

            if temp >= answer:
                if temp not in room.keys():
                    room[temp] = [board[i][j]]
                else:
                    room[temp].append(board[i][j])

                answer = temp

    print(f"#{tc} {min(room[answer])} {answer}")
