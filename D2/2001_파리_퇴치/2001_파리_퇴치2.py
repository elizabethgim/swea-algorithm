import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    max_total = 0
    matrix = []

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    sum_matrix = list(list(0 for _ in range(N)) for _ in range(N))

    for i in range(N):
        for j in range(M):
            sum_matrix[i][0] = matrix[i][0] + sum_matrix[i-1][0]
            sum_matrix[0][i] = matrix[0][i] + sum_matrix[0][i-1]

    for i in range(1, N):
        for j in range(1, N):
            sum_matrix[i][j] = matrix[i][j] + sum_matrix[i-1][j] + sum_matrix[i][j-1] - sum_matrix[i-1][j-1]


    dp = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(M-1, N):
        for j in range(M-1, N):
            minus = 0
            if 0 <= i-M < N and 0 <= j-M < N:
                minus = sum_matrix[i - M][j] + sum_matrix[i][j-M] - sum_matrix[i - M][j - M]
            elif 0 <= i-M < N:
                minus = sum_matrix[i - M][j]
            elif 0 <= j-M < N:
                minus = sum_matrix[i][j-M]

            dp[i][j] = sum_matrix[i][j] - minus
            max_total = max(dp[i][j], max_total)

    print(f"#{test_case} {max_total}")
