import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    word = input()

    start, end = 0, len(word)-1

    same = 1

    while start <= end:
        if word[start] != word[end]:
            same = 0
            break

        start += 1
        end -= 1

    print(f"#{tc} {same}")
