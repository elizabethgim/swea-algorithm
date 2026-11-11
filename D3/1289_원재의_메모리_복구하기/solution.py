import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for tc in range(1, T+1):
    numbers = [int(x) for x in input()]

    prev = 0
    count = 0
    for i in range(len(numbers)):
        if numbers[i] == 1:
            if prev == 0:
                prev = 1
                count += 1
        else:           # numbers[i] == 0
            if prev == 1:
                count += 1
                prev = 0

    print(f"#{tc} {count}")
