'''
1번은 무조건 넣어야함
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    checkpoints = list(map(int, input().split()))

    total = 0
    for i in range(1, N):
        total += abs(checkpoints[i] - checkpoints[i-1])

    max_save = 0
    for i in range(1, N-1):
        before = abs(checkpoints[i] - checkpoints[i-1]) + abs(checkpoints[i+1]-checkpoints[i])
        after = abs(checkpoints[i+1] - checkpoints[i-1])
        save = before - after
        if save > max_save:
            max_save = save

    print(total - max_save)
