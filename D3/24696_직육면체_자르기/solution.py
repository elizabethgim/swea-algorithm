'''
A, B, C 자연수

"여섯 면 중 한 면과 평행하게 자른다."
잘린 직육면체의 각 변의 길이 또한 자연수여야 함.
두 사람 게임에서 최선을 다한다.

나연이 먼저 -> 홀수면 나연이 우승
자를 수 있는 횟수가 짝수면 다현이가 우승,

직육면체 자를 수 있는지 없는지 어떻게 따질까??
자연수인 조건 활용
1*1*1이 최소 단위 개수

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    A, B, C = map(int,input().split())

    if (A * B * C) % 2 == 0:
        print(1)
    else:
        print(2)