'''
1h 14m

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def move(x, y, nx, ny, d):
    print("move to", nx, ny)
    if 0 <= nx < H and 0 <= ny < W and board[nx][ny] == ".":
        board[x][y] = "."
        board[nx][ny] = d
        return True
    return False


def shoot(x, y, d):
    if d == "^":
        for k in range(x, -1, -1):
            if board[k][y] == "*":
                board[k][y] = "."
                break
            elif board[k][y] =="#":
                break

    elif d == "v":
        for k in range(x, H):
            if board[k][y] == "*":
                board[k][y] = "."
                break
            elif board[k][y] =="#":
                break
    elif d == "<":
        for k in range(y, -1, -1):
            if board[x][k] == "*":
                board[x][k] = "."
                break
            elif board[x][k] =="#":
                break
    elif d == ">":
        for k in range(y, W):
            if board[x][k] == "*":
                board[x][k] = "."
                break
            elif board[x][k] =="#":
                break


direction = {"U": "^", "L": "<", "R": ">", "D": "v"}

for tc in range(1, T+1):
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(s for s in input()))
        print(board[_])
    print()

    N = int(input())
    S = input()

    x, y = 0, 0
    d = ""
    for i in range(H):
        for j in range(W):
            if board[i][j] == "^" or board[i][j] == "v" or board[i][j] == "<" or board[i][j] == ">":
                x = i
                y = j
                d = board[i][j]
                break

    for s in S:
        print(s, "curr: ", x, y)
        if s == "U":
            nx = x - 1
            ny = y
        elif s == "D":
            nx = x + 1
            ny = y
        elif s == "L":
            nx = x
            ny = y - 1
        elif s == "R":
            nx = x
            ny = y + 1
        elif s == "S":
            nx = x
            ny = y
            shoot(x, y, d)

        if s != "S":
            d = direction[s]
            board[x][y] = d

            temp = move(x, y, nx, ny, d)
            print(temp)
            if temp:
                print("moved")
                x = nx
                y = ny

        # print board
        # for i in range(H):
        #     print(board[i])
        # print()

    print(f"#{tc} " , end="")
    # print board
    for i in range(H):
        for j in range(W):
            print(board[i][j], end="")
        print()
