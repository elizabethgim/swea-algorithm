import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N = input()
    cnt = 1

    numbers = set()

    total = 0
    while True:
        total += int(N)
        # print(total)
        S = str(total)
        for s in S:
            numbers.add(s)

        if len(numbers) == 10:
            break

    print(f"#{tc} {total}")

