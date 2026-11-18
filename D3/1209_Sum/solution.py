import sys
sys.stdin = open("input.txt", "r")

N = 100

for tc in range(1, 11):
    T = int(input())

    board = []
    for _ in range(N):
        board.append(list(map(int, input().split())))

    sum_total = set()

    total = 0
    total2 = 0

    for i in range(N):
        sum_total.add(sum(board[i]))

        col_total = 0
        for j in range(N):
            col_total += board[j][i]

            if i == j:
                total += board[i][j]

            if i+j == N-1:
                total2 += board[i][j]

        sum_total.add(col_total)

    sum_total.add(total)
    sum_total.add(total2)

    # print(sum_total)

    print(f"#{tc} {max(sum_total)}")
