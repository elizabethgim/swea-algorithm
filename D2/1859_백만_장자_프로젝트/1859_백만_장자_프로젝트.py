import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    answer = 0
    max_num = 0

    for i in range(N-1, -1, -1):
        if max_num < arr[i]:
            max_num = arr[i]

        answer += max_num - arr[i]
    print('#{} {}'.format(test_case, answer))

