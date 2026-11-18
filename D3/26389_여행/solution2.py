import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    s = input()
    answer = "No"
    if (("N" in s) == ("S" in s)) and (("W" in s) == ("E" in s)):
        answer = "Yes"

    print(answer)
