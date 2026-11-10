import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    n = int(input())

    pascal = []

    for i in range(n+1):
        temp = [1 for _ in range(i)]

        for j in range(1, i-1):
            temp[j] = pascal[i-1][j-1] + pascal[i-1][j]

        pascal.append(temp)

    print(f"#{tc}")
    for i in range(1, n+1):
        for p in pascal[i]:
            print(p, end=" ")
        print()

