import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    height = list(map(int, input().split()))
    answer = max(height) + 1

    total = sum(height) + answer
    N = len(height) + 1

    while True:
        if total % N == 0:
            break
        total += 1
        answer += 1

    print(answer)


