'''
재귀는 시간초과

증간에 P층을 만나도
무조건 1층을 밟지 않으면 P-1이 돼서 해당 값을 피할 수 있다는 점
'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def recurr(index, curr):
    global answer
    # print(index, curr)
    if curr == P:
        return

    if index == N+1:
        answer = max(answer, curr)
        return

    recurr(index+1, curr)
    recurr(index+1, curr+index)


for tc in range(1, T+1):
    N, P = map(int, input().split())
    answer = 0

    # recurr(0, 0)
    same = False
    for i in range(N):
        answer += i
        if answer == P:
            same = True

    if same:
        print(answer-1)
    else:
        print(answer)

