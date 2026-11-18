import sys
sys.stdin = open("input.txt", "r")

# T = int(input())
# for tc in range(1, T+1):
#     X, Y = map(int, input().split())
#
#     A = (X + Y) // 2
#     B = (X - Y) // 2
#
#     print(f"{A} {B}")

'''오답 풀이
반례
A = 4, B = 2일 때 합은 6 차는 2
'''
T = int(input())

for tc in range(1, T+1):
    X, Y = map(int, input().split())

    start = -100
    end = 100

    while start <= 100 and end >= -100:
        if start+end == X:
            if start - end == Y:
                break
            elif start - end < Y:
                end -= 1
            else:
                start += 1
        elif start+end > X:
            end -= 1
        else:
            start += 1

    # flag = False
    #
    # for start in range(-100, 101):
    #     for end in range(-100, 101):
    #         if start + end == X and start - end == Y:
    #             flag = True
    #             break
    #
    #     if flag:
    #         break

    print(f"{start} {end}")

