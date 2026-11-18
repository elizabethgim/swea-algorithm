'''
격자판의 행 하나 또는 열 하나를 고른다.
-> 경우의 수: H * W
고른 행 또는 열에 있는 모든 칸을 검은색으로 칠한다.
이미 검은색인 칸을 한 번 더 검은색으로 칠하면 여전히 검은색을 유지..

전체 행을 칠하는 경우
전체 열을 칠하는 경우

어떤 경우에 행을 고르는 게 유리한지 열을 고르는 게 유리한지
행과 열 모두를 고르는 경우도 있고


'''

import sys
sys.stdin = open("input.txt", "r")

from collections import deque

from collections import deque

T = int(input())

for tc in range(1, T+1):
    H, W = map(int, input().split())
    board = []
    for _ in range(H):
        board.append(list(s for s in input()))

    answer = 0

    que = deque()
    for i in range(H):
        if board[i][0] == "#":
            flag = True
            for j in range(W):
                if board[i][j] == ".":
                    flag = False
                    break

            if flag:
                que.append((i, 0))

    for j in range(W):
        flag = True
        for i in range(H):
            if board[i][j] == ".":
                flag = False
                break

        if flag:
            que.append((0, j))

    print(len(que))
