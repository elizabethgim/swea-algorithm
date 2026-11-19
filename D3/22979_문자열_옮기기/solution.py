import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    S = input()
    K = int(input())
    X = list(map(int, input().split()))
    N = len(S)
    total = sum(X) % N

    if total > 0:
        first = S[:total]
        rest = S[total:]
        S = rest + first
    elif total < 0:
        end = S[total:]
        rest = S[:total]
        S = end + rest
    print(S)
