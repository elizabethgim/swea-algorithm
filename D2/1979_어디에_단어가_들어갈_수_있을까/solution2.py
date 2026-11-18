'''
흰 색 부분은 1
검은 색 부분은 0
'''

import sys
sys.stdin = open("sample.txt", "r")

T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    count = 0

    for i in range(N):
        total = 0
        for j in range(N):
            print(i, j, board[i][j])
            if board[i][j] == 1:
                total += 1
            else:
                if total == K:
                    count += 1
                total = 0
        print()

    for i in range(N):
        total = 0
        for j in range(N):
            print(j, i, board[j][i])
            if board[j][i] == 1:
                total += 1
            else:
                if total == K:
                    count += 1
                total = 0
        print("count: ", count)

    print(f"#{tc} {count}")
