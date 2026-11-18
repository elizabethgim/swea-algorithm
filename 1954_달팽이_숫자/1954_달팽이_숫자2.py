# 다른 풀이: https://velog.io/@seungjae/SWEA-1954.-%EB%8B%AC%ED%8C%BD%EC%9D%B4-%EC%88%AB%EC%9E%90
T = int(input())

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def snail(x, y, d, num):
    matrix[x][y] = num
    nx = x + dx[d]
    ny = y + dy[d]

    if num == N*N:
        return

    if nx < 0 or nx >= N or ny < 0 or ny >= N or matrix[nx][ny] > 0:
        d = (d+1) % 4
        snail(x, y, d, num)
    else:
        snail(nx, ny, d, num + 1)


for test_case in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    snail(0, 0, 0, 1)

    print(f"#{test_case}")

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()