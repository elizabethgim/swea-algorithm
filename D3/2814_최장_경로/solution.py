import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def dfs(v, length):
    global answer
    answer = max(answer, length)

    for next in graph[v]:
        if not visited[next]:
            visited[next] = True
            dfs(next, length+1)
            visited[next] = False


for tc in range(1, T+1):
    graph = [[] for _ in range(11)]

    N, M = map(int, input().split())

    for _ in range(M):
        x, y = map(int, input().split())
        graph[x].append(y)
        graph[y].append(x)

    answer = 0
    for s in range(1, N+1):
        visited = [False] * (N+1)
        visited[s] = True
        dfs(s, 1)

    print(f"#{tc} {answer}")

