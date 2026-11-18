import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(s for s in input()))

    row_count = 0
    for i in range(H):
        flag = True
        for j in range(W):
            if board[i][j] == ".":
                flag = False
                break

        if flag:
            row_count += 1

    col_count = 0
    for j in range(W):
        flag = True
        for i in range(H):
            if board[i][j] == ".":
                flag = False
                break

        if flag:
            col_count += 1

    if row_count == H:
        print(min(row_count, col_count))
    else:
        print(row_count + col_count)