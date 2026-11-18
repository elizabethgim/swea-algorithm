# import sys
# sys.stdin = open("input.txt", "r")

T = int(input())


def recurr(n, i, j):
    global N
    if i < 0 or i >= N:
        return
    if j < 0 or j >= N:
        return

    if visited[i][j]:
        return

    matrix[i][j] = n+1
    visited[i][j] = True

    # if j+1 < N and not visited[i][j+1]:
    #     recurr(n+1, i, j + 1)
    # if i+1 < N and not visited[i+1][j]:
    #     recurr(n+1, i + 1, j)
    # if j-1 >= 0 and not visited[i][j-1]:
    #     recurr(n+1, i, j - 1)
    # if i-1 >= 0 and not visited[i-1][j]:
    #     recurr(n+1, i - 1, j)

    if N - i - j - 1 <= 0:
        recurr(n+1, i, j + 1)
        recurr(n+1, i + 1, j)
        recurr(n+1, i, j - 1)
        recurr(n+1, i - 1, j)
    else:
        recurr(n + 1, i - 1, j)
        recurr(n + 1, i, j + 1)
        recurr(n + 1, i + 1, j)
        recurr(n + 1, i, j - 1)


for test_case in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    visited = [[False for _ in range(N)] for _ in range(N)]

    recurr(0, 0, 0)
    print(f"#{test_case}")

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()
