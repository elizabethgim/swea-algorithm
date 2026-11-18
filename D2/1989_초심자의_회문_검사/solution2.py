import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    answer = 1
    s = input()
    N = len(s)//2

    for i in range(N):
        if s[i] != s[len(s) - i-1]:
            answer = 0
            break

    print(f"#{tc} {answer}")