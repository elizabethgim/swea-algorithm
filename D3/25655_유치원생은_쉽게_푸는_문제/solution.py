'''
X개가 될 때까지 계속 반복을 한다.
조합의 수가 많음, 조합을 일일이 구해야 할까?

닫힌 공간의 개수가 X인 가장 작은 음이 아닌 정수 N

10 = 1
11 = 0
12 = 0

40 = 1+1 = 2
41 = 0+1 = 1
42 = 0+1 = 1
43 = 0+1 = 1

X // 2 # 8이 최대 몇 개 들어갈 수 있느냐
X // 3 # 1인 값과 2인 값을 합해서 넣을 수 있는 최대 작은 수 08(X), 80

888
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

space = [1, 0, 0, 0, 1, 0, 1, 0, 2, 1]
for tc in range(1, T+1):
    X = int(input())

    number = ""
    if X == 1:
        print(0)
    else:
        if X % 2 == 0:
            for i in range(X // 2):
                number += "8"
        else:
            number += "4"
            for i in range((X-1)//2):
                number = number + "8"

        print(number)