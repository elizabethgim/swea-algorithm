import sys
sys.stdin = open("input.txt", "r")


T = 10
for test_case in range(1, T+1):
    n = int(input()) # 항상 100

    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
        # print(table[i])

    answer = 0 # 교착 상태 개수

    # 1은 S극, 2는 N극
    for j in range(n):
        prev = 0
        for i in range(n):
            if table[i][j] == 1:
                prev = 1

            elif table[i][j] == 2:
                if prev == 1:
                    answer += 1
                    prev = 0

    print(f"#{test_case} {answer}")
