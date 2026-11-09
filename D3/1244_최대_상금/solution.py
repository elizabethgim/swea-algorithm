'''
교환을 이루고 나서 다시 해당 위치(교환된 배열에서)에서 다시 교환을 이루도록 만드는 로직이 헷갈렸음
'''
import sys
sys.stdin = open("input.txt", "r")

from collections import deque

T = int(input())

def length(n):
    numbers = deque()

    while n != 0:
        temp = n % 10
        numbers.appendleft(temp)
        n = n // 10


    return numbers

def toNumber(array):
    n = len(array)

    answer = 0
    one = 1

    for i in range(n-1, -1, -1):
        answer += array[i] * one
        one = one * 10

    return answer


for test_case in range(1, T+1):
    n, change = map(int, input().split())
    numbers = length(n)
    l = len(numbers)

    current = {tuple(numbers)}

    for k in range(change):
        next_set = set()

        for state in current:
            for i in range(l):
                for j in range(l):
                    changed = list(state)

                    if i == j:
                        continue

                    temp = changed[i]
                    changed[i] = changed[j]
                    changed[j] = temp

                    next_set.add(tuple(changed))

        current = next_set

    answer = max(toNumber(s) for s in current)

    print(f"#{test_case} {answer}")
