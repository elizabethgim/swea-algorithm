'''
N명의 사람
M초 K개의 붕어빵
1 <= N, M, K <= 100

해당 시점에 붕어빵이 몇 개 인지를 알아야함.
그걸 어떻게 알까?
'''

import sys
sys.stdin = open("input.txt", "r")

with open("output.txt", "r") as f:
    lines = f.read().splitlines()

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    people = list(map(int, input().split()))

    people.sort()

    max_time = people[-1]
    # print(max_time)

    cooked = [0 for _ in range(max_time+1)]
    flag = "Possible"

    if M == 0:
        cooked[0] = K

    if people[0] == 0:
        if cooked[0] == 0:
            flag = "Impossible"
    else:
        for i in range(1, max_time+1):
            if i % M == 0:
                cooked[i] = cooked[i-1] + K
            else:
                cooked[i] = cooked[i-1]
            # print(i, " Baking -> ", cooked)

            if i in people:
                if cooked[i] == 0:
                    flag = "Impossible"
                    break

                cooked[i] -= 1

    # print(cooked)

    # print(f"#{tc} {flag}")

    answer = "#"+str(tc)+" "+str(flag)

    if lines[tc-1].strip() != answer:
        print(tc, "No", lines[tc-1], "\nanswer:", answer)

