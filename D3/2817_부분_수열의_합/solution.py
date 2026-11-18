import sys
sys.stdin = open("input.txt", "r")
from collections import deque

T = int(input())


def dfs(N, K, num):
    que = deque()
    que.append((0, 0))
    count = 0

    while que:
        index, total = que.popleft()
        print(index, total)

        if index == N:
            if total == K:
                count += 1
            continue

        que.append((index+1, total))
        que.append((index+1, total+num[index]))

    return count


for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    print(N, K, num)

    answer = dfs(N, K, num)

    print(f"#{tc} {answer}")
