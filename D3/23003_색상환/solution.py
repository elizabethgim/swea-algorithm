'''
빨강색(red), 오렌지색(orange), 노란색(yellow), 초록색(green), 파랑색(blue), 보라색(purple)

서로 같은 색이라면 ‘E’
색상환에서 인접한 (한 변을 공유하고 있는) 색이라면 ‘A’
색상환에서 서로 반대에 있는 (마주보고 있는) 색이라면 ‘C’
셋 다 아니라면 ‘X’
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
order = ["red", "orange", "yellow", "green", "blue", "purple"]
advert = {"red": "green", "orange":"blue", "yellow": "purple", \
              "green": "red", "blue":"orange", "purple":"yellow"}

for tc in range(1, T+1):

    color1, color2 = input().split(' ')

    if color1 == color2:
        print('E')
    else:
        for i in range(6):
            if order[i] == color1:
                if order[(i+1) % 6] == color2 or order[i-1] == color2:
                    print('A')
                else:
                    if advert[color1] == color2:
                        print('C')
                    else:
                        print('X')