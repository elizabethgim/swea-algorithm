'''
중복을 안 뺌
'''
import sys
sys.stdin = open("input.txt", "r")

T = 10


def check(l, arr):
    start, end = 0, l-1

    flag = True
    while start <= end:
        if arr[start] != arr[end]:
            flag = False
        start += 1
        end -= 1

    return flag


for tc in range(1, T+1):
    board = []
    length = int(input().strip())

    for _ in range(8):
        board.append(list(s for s in input()))

    count = 0

    # row
    for i in range(8):
        for j in range(8-length+1):
            temp = board[i][j:j+length]
            if check(length, temp):
                count += 1

    # column
    for i in range(8-length+1):
        for j in range(8):
            temp = []
            for k in range(length):
                endi = i + k
                temp.append(board[endi][j])

            if check(length, temp):
                count += 1

    print(f"#{tc} {count}")
