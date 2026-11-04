'''

2011년 11월 11일 오전 11시 11분

14일 23시 59분
23-11=12
59-11=4

d*24*60+h*60+m

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

base_time = 11*24*60 + 11*60 + 11

for test_case in range(1, T+1):

    time_array = list(map(int, input().split()))

    total = time_array[0] * 24 * 60 + time_array[1] * 60 + time_array[2]

    answer = total - base_time
    if answer < 0:
        answer = -1

    print(f"#{test_case} {answer}")