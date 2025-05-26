import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))

    last = len(arr)-1
    arr = sorted(arr)

    while N > 0:
        arr[0] = arr[0] + 1
        arr[last] = arr[last] - 1
        N -= 1
        arr = sorted(arr)

    print(f"#{test_case} {arr[last]-arr[0]}")


