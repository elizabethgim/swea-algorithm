'''
문제의 조건을 찾기 까다로운 문제

X를 R보다 같거나 작은 값으로 산정했을 때
X의 배수가 있음 -> 나머지는 0으로 X/2보다 작다.

X를 R보다 큰 값으로 산정했을 때
남는 개수가 N일 때
모든 N에 대해 X/2보다 크거나 작아야 함
-> L >= X/2 -> 2L >= X
'''

T = int(input())

for tc in range(1, T+1):
    L, R = map(int, input().split())

    if R < 2 * L:
        print("yes")
    else:
        print("no")
