import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for tc in range(1, T+1):
    N, K = map(int, input().split())
    num = list(map(int, input().split()))
    print(N, K, num)

    start, end = 0, 0
    total, count = 0, 0

    while start <= end and end < N:
        print(start, num[start])
        print(end, num[end])

        total += num[end]
        print(total)

        if total == K:
            total -= num[start]
            start += 1
            count += 1
        if total > K:
            total -= num[start]
            start += 1
        else:
            end += 1

        print("count: ", count)

    print(f"#{tc} {count}")
