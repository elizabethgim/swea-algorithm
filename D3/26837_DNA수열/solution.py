import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for tc in range(1, T+1):
    N, S = input().split()

    a, c = 0, 0
    height = {(0, 0): 1}
    count = 0

    for ch in S:
        if ch == "A":
            a += 1
        elif ch == "T":
            a -= 1
        elif ch == "C":
            c += 1
        else: # "G"
            c -= 1

        key = (a, c)
        print(key, height)
        if key in height:
            count += height[key]
            height[key] += 1
        else:
            height[key] = 1
        # height[(a, c)] = height.get((a, c), 0) + 1

    # count = 0
    # for k in height.values():
    #     count += k * (k-1) // 2

    print(count)
