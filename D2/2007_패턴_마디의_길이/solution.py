import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    words = [s for s in input()]

    pattern = []
    start, end = 0, 1
    answer = 0
    while start <= end < len(words):
        if words[start] != words[end]:
            end += 1
            continue

        answer = max(answer, end-start)
        start += 1

    print(f"#{tc} {answer}")
