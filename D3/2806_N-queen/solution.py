'''
1. Possible
퀸을 둘 수 있는지 여부를 확인
- 퀸을 둘 수 없는 경우
    같은 행 또는 열에 있는 경우
    대각선으로 있는 경우: 대각선 위치의 열에서 현재 퀸의 열을 뺀 값과 대각선 위치의 행에서 현재 퀸의 행을 뺀 값의 절대값이 같다.

2. dfs
퀸을 계속 두기

N: 1
1
N: 2
0
N: 3
0

'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

# candidate 열만 저장, 각 원소의 인덱스가 행
def possible(curr_col, candidate):
    row = len(candidate)

    for i in range(row):
        if curr_col == candidate[i]:
            return False

        if abs(curr_col - candidate[i]) == abs(row-i):
            return False

    return True

def dfs(curr_row, candidate, n):
    if curr_row == n:
        return 1

    count = 0
    for i in range(n):
        if possible(i, candidate):
            candidate.append(i)
            count += dfs(curr_row+1, candidate, n)
            candidate.pop()

    return count

for test_case in range(1, T+1):
    n = int(input())
    answer = dfs(0, [], n)
    print(f"#{test_case} {answer}")
