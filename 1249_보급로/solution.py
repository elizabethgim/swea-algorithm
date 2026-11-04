'''
dfs 재귀 문제 풀이
시간 초과
파이썬 재귀 제한으로 32크기의 배열부터 막힘 - Recurssion Error
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for test_case in range(1, T+1):
    n = int(input())
    board = []
    for _ in range(n):
        board.append(list(map(int, input())))

    visited = [[False for _ in range(n)] for _ in range(n)]
    visited[0][0] = True
    answer = 10 ** 100

    def dfs(x, y, d, visited, board, n):
        global answer
        if x == n - 1 and y == n - 1:
            answer = min(answer, d)
            return

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    dfs(nx, ny, d + board[nx][ny], visited, board, n)
                    visited[nx][ny] = False

    dfs(0, 0, board[0][0], visited, board, n)


    print(f"#{test_case} {answer}")
