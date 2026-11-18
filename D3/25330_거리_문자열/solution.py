'''
숫자 d가 두 번 등장한다면, 두 숫자 사이에 있는 숫자의 개수는 d개이다.
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    S = input()

    count = [0 for _ in range(10)] # 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
    answer = "yes"

    flag = False
    for num in S:
        num = int(num)
        count[num] += 1
        if count[num] > 2:
            answer = "no"
            flag = True
            break

    # print(count)

    if not flag:
        for i in range(10):
            if count[i] == 0 or count[i] == 2:
                answer = "yes"
            else:
                answer = "no"
                flag = True
                break


    # for i in range(len(S)):
    #     num = int(S[i])
    #     print(num)
    #     if 0 <= i+num < len(S) and S[i] == S[i+num]:
    #         print(S[i], S[i+num])
    #         answer = "Yes"
    #     else:
    #         answer = "No"

    if not flag:
        checked = [False for _ in range(len(S))]
        N = len(S)

        for i in range(N):
            num = int(S[i])
            # print(checked)
            if checked[i]:
                continue
            checked[i] = True
            ni = i + num + 1
            # print(num, S[i], "=> ", ni)
            if 0<= ni < N:
                checked[ni] = True
                if int(S[ni]) == num:
                    answer = "yes"
                else:
                    answer = "no"
                    break
            else:
                answer = "no"
                break

        # print(answer)

    print(answer)