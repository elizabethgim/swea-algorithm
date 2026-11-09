
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

def bfs(arr, N):
    que = deque()
    que.append((0, 0))

    visited = [set() for _ in range(N)]

    answer = set()
    answer.add(0)
    while que:
        index, total = que.popleft()

        if index == N:
            answer.add(total)
            continue

        if total in visited[index]:
            continue

        visited[index].add(total)

        que.append((index+1, total))
        que.append((index+1, total+arr[index]))

    return len(answer)


for test_case in range(1, T+1):
    N = int(input())
    num = list(map(int, input().split()))
    answer = bfs(num, N)
    print(f"#{test_case} {answer}")
