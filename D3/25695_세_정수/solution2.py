import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    X, Y, Z = map(int, input().split())

    A = min(X, Z)
    B = min(X, Y)
    C = min(Y, Z)

    if max(A, B) == X and max(B, C) == Y and max(C, A) == Z:
        print(A, B, C)
    else:
        print(-1, -1, -1)