'''

(0, 0) (0, 1) (0, 2)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)

(2, 0) (1, 0) (0, 0)
(2, 1) (1, 1) (0, 1)
(2, 2) (1, 2) (0, 2)

(2, 2) (2, 0)

(0, 0) (0, 2)
3-0-1

x = 1
y = 0
nx = 0
ny = 1

x = 1
y = 1
nx = 1
ny = 1

x = 2
y = 2
nx = 2
ny = 0

nx = y
ny = N-x-1

(0, 0) (0, 1) (0, 2) (0, 3)
(1, 0) (1, 1) (1, 2)
(2, 0) (2, 1) (2, 2)
(3, 0)

(3, 0) (2, 0) (1, 0) (0, 0)
(2, 1) (1, 1) (0, 1)
(2, 2) (1, 2) (0, 2)


x = 3, y = 0
nx = 0 ny = 0
N-x-1

'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

def rotate(board, N):
    new_board = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        for j in range(N):
            new_board[j][N-i-1] = board[i][j]
            # 반시계 방향은 이렇게 하면 됨
            #        new_board[i][j] = board[j][N-i-1]

    return new_board

for tc in range(1, T+1):
    N = int(input())
    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    b90 = rotate(board, N)
    b180 = rotate(b90, N)
    b270 = rotate(b180, N)

    print(f"#{tc}")
    for i in range(N):
        for j in range(N):
            print(b90[i][j], end = "")
        print(" ", end="")
        for j in range(N):
            print(b180[i][j], end="")
        print(" ", end="")
        for j in range(N):
            print(b270[i][j], end="")
        print(" ", end="")

        print()
