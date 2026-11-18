import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    answer = 0
    dp = [1 for _ in range(N)]
    dp[N-1] = 1

    for i in range(N-2, -1, -1):
        for j in range(i+1, N):
            if numbers[j] > numbers[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(f"#{tc} {max(dp)}")
