import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def dfs(R, C, board):
    visited = [[[[False for _ in range(16)] for _ in range(4)] for _ in range(C)] for _ in range(R)]
    stack = []
    # 위 왼쪽 오른쪽 아래
    dx = [-1, 0, 0, 1]
    dy = [0, -1, 1, 0]

    stack.append((0, 0, 2, 0)) # row, column, direction, memory

    while stack:
        r, c, d, m = stack.pop()

        if visited[r][c][d][m]:
            continue

        visited[r][c][d][m] = True

        code = board[r][c]

        if code == '@':
            return "YES"
        if code == "?":
            for i in range(4):
                nr = (r + dx[i]) % R
                nc = (c + dy[i]) % C

                stack.append((nr, nc, i, m))
            continue

        if code == '<':
            d = 1
        elif code == '>':
            d = 2
        elif code == 'v':
            d = 3
        elif code == '^':
            d = 0
        elif code == "_":
            if m == 0:
                d = 2
            else:
                d = 1
        elif code == "|":
            if m == 0:
                d = 3
            else:
                d = 0
        elif code == "+":
            m += 1
            if m == 16:
                m = 0
        elif code == "-":
            m -= 1
            if m == -1:
                m = 15
        elif code.isdigit():
            m = int(code)

        nr = (r + dx[d]) % R
        nc = (c + dy[d]) % C

        stack.append((nr, nc, d, m))

    return "NO"


for tc in range(1, T+1):
    R, C = map(int, input().split())
    board = []
    for i in range(R):
        board.append(list(s for s in input()))

    print(f"#{tc} {dfs(R, C, board)}")
