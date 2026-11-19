'''
두 팀 중 한 명씩 선발
A, B
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    picked = [False for _ in range(N)]
    answer = ["" for _ in range(N)]

    for i in range(N):
        # A가 먼저 고름
        for j in range(N):
            a = A[j] - 1
            if not picked[a]:
                picked[a] = True
                answer[a] = "A"
                break
        # B가 고름
        for j in range(N):
            b = B[j] - 1
            if not picked[b]:
                picked[b] = True
                answer[b] = "B"
                break

    for a in answer:
        print(a, end="")
    print()
