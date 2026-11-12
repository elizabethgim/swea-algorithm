import sys
sys.stdin = open("input.txt", "r")

T = 10
n = 100
# T = 1
# n = 8

def check(s):
    start, end = 0, len(s)-1

    flag = True
    while start <= end:
        if s[start] != s[end]:
            flag = False
            break
        start += 1
        end -= 1

    return flag


for tc in range(1, T+1):
    t = int(input())
    board = []
    for _ in range(n):
        board.append(list(s for s in input().strip()))

    answer = 0

    for i in range(n):
        for j in range(n):
            col_part = []
            for k in range(n+1):
                row_part = board[i][j:j+k]
                if check(row_part):
                    answer = max(answer, len(row_part))

                if j+k >= 100:
                    continue

                col_part.append(board[j+k][i])
                # print(col_part)
                if check(col_part):
                    answer = max(answer, len(col_part))

    print(f"#{t} {answer}")
