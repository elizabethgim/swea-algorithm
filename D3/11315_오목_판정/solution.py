import sys
sys.stdin = open("input.txt", "r")

T = int(input())

dx = [0, 0, -1, -1, -1, 1, 1, 1]
dy = [-1, 1, -1, 1, 0, -1, 0, 1]


for tc in range(1, T+1):
    N = int(input())
    answer = "NO"

    board = []
    for _ in range(N):
        board.append(list(s for s in input()))

    for i in range(N):
        for j in range(N):
            if board[i][j] == "o":
                okay = False
                for k in range(8):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    if 0 <= ni < N and 0 <= nj < N and board[ni][nj] == "o":
                        five = True
                        for m in range(5):
                            ni = i + dx[k] * m
                            nj = j + dy[k] * m

                            if 0 <= ni < N and 0 <= nj < N:
                                if board[ni][nj] == ".":
                                    five = False
                                    break
                            else:
                                five = False
                                break

                        if five:
                            okay = True
                            break

                if okay:
                    answer = "YES"

    print(f"#{tc} {answer}")