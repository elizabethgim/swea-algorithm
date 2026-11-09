'''
A[0] = 1
A[1] = 1

A[i], i >= 2
K <= i/2

A[i-2k]
A[i-k]
A[i]

i = 2, k <= 1 k=1
A[2-2] = A[0] = 1
A[2-1] = A[1] = 1
A[2] = x

x-1 = 1-1
x = 1+1-1 = 1
A[2] != 1
A[2] = 2

i = 3, k <= 1 k=1
A[3-2] = A[1] = 1
A[3-1] = A[2] = 2
A[3] = x

x-2 = 2-1
x = 2+2-1 = 3
A[3] != 3
A[3] = 1

i = 4, k <= 4/2 = 2, k=1,2
k=1
A[4-2] = A[2] = 2
A[4-1] = A[3] = 1
A[4] = x

x-1 = 1-2
x = 0
A[4] != 0


k = 2
A[4-4] = A[0] = 1
A[4-2] = A[2] = 1
A[4] = x

x-1 = 1-1
x!=1
A[4] = 3

'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())

N =  10001
A = [0 for _ in range(N + 1)]
A[0] = 1
A[1] = 1

for i in range(2, N):
    ban = set()

    for k in range(1, i // 2+1):
        ban.add(A[i - k] + A[i - k] - A[i - 2 * k])

    for kk in range(1, N):
        if kk not in ban:
            A[i] = kk
            break

for test_case in range(1, T+1):
    n = int(input())

    print(f"#{test_case} {A[n]}")