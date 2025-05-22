import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    max_total = 0
    matrix = []

    for i in range(N):
        matrix.append(list(map(int, input().split())))

    for i in range(N):
        for j in range(N):
            total = 0
            for mi in range(M):
                for mj in range(M):
                    nx = i + mi
                    ny = j + mj

                    if nx < 0 or nx >= N or ny < 0 or ny >= N:
                        continue

                    total += matrix[nx][ny]

            max_total = max(total, max_total)

    print(f"#{test_case} {max_total}")

