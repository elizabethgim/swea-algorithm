import sys
sys.stdin = open("input.txt", "r")

T = int(input())

money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for tc in range(1, T+1):
    N = int(input())

    i = 0
    cnt = [0 for _ in range(8)]

    for i in range(8):
        # print(N, N // money[i])
        cnt[i] += N // money[i]
        N = N - money[i] * (N // money[i])
        i += 1
        # print(cnt)

    print(f"#{tc}")
    for _ in range(8):
        print(cnt[_], end=" ")
    print()

