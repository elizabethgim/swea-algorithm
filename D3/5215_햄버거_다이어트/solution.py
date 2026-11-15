import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def dfs(cnt, total_like, total_calories, ingredients, visited):
    global answer, N, L

    if total_calories > L:
        return

    answer = max(answer, total_like)

    if cnt == N:
        return

    for i in range(cnt, N):     # 순열로 해보기
        if not visited[i]:
            visited[i] = True
            dfs(i, total_like+ingredients[i][0], total_calories+ingredients[i][1], ingredients, visited)
            visited[i] = False


def dfs2(cnt, total_like, total_calories, ingredients):
    global answer, N, L
    # print(cnt, total_like, total_calories)

    if total_calories > L:
        return

    if cnt == N:
        answer = max(answer, total_like)
        return

    dfs(cnt+1, total_like, total_calories, ingredients)
    dfs(cnt + 1, total_like + ingredients[cnt][0], total_calories + ingredients[cnt][1], ingredients)


def dfs3(cnt, total_like, total_calories):
    if total_calories > L:
        return 0

    if cnt == N:
        return total_like

    return max(
        dfs(cnt+1, total_like, total_calories),
        dfs(cnt+1, total_like + info[cnt][0], total_calories+info[cnt][1])
    )


for tc in range(1, T+1):
    N, L = map(int, input().split())

    info = []
    for _ in range(N):
        info.append(list(map(int, input().split())))

    answer = 0
    v = [False for _ in range(N)]

    # dfs(0, 0, 0, info, v)
    # dfs2(0, 0, 0, info)
    answer = dfs3(0, 0, 0)

    print(f"#{tc} {answer}")
