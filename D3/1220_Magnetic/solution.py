'''
S 극은 아래로 N극은 위로 올라감.

반대 방향으로 움직이는 자성체가 하나라도 있으면
교착 상태에 빠져 움직이지 않는다.

인접하다. 서로 다른 교착 상태?

한 열 내에서 두 개 이상 교착 상태가 있을 수 있음.

테이블 크기 100 * 100

'''

import sys
sys.stdin = open("input_2.txt", "r")


def simulate(table):
    n = len(table)

    while True:
        next_table = [row[:] for row in table]
        moved = False

        # 이동할 자성체 목록
        moves = []

        for i in range(n):
            for j in range(n):
                if table[i][j] == 1:
                    # 아래로 이동
                    if i == n-1:
                        moves.append((i, j, None))
                    elif table[i+1][j] == 0:
                        moves.append((i, j, (i+1, j)))
                elif table[i][j] == 2:
                    # 위로 이동
                    if i ==0:
                        moves.append((i, j, None))
                    elif table[i-1][j] == 0:
                        moves.append((i, j, (i-1, j)))

        targets = {}

        for i, j, dest in moves:
            if dest is not None:
                targets[dest] = targets.get(dest, 0) + 1

        for i, j, dest in moves:
            if dest is None:
                next_table[i][j] = 0
                moved = True

            elif targets[dest] == 1:
                ni, nj = dest
                next_table[i][j] = 0
                next_table[ni][nj] = table[i][j]
                moved = True
        table = next_table

        if not moved:
            break

    return table

T = 1
for test_case in range(1, T+1):
    n = int(input()) # 항상 100

    table = []
    for i in range(n):
        table.append(list(map(int, input().split(" "))))
        # print(table[i])

    result = simulate(table)

    # # 1은 S극, 2는 N극
    # for i in range(n):
    #     for j in range(n):
    #         print(table[i][j])
    #         if table[i][j] == 1:
    #             # move down
    #             print("move down")
    #             ni = i
    #             while ni < n-1:
    #                 print(ni, table[ni][j])
    #                 ni = ni + 1
    #                 # check
    #                 if table[ni][j] == 1 or table[ni][j] == 2:
    #                     break
    #
    #             if ni == n - 1:
    #                 table[ni-1][j] = table[i][j]
    #
    #             table[i][j] = 0
    #
    #         elif table[i][j] == 2:
    #             # move up
    #             print("move up")
    #             ni = i
    #             while ni > 0:
    #                 print(ni, table[ni][j])
    #                 ni = ni - 1
    #                 if table[ni][j] == 1 or table[ni][j] == 2:
    #                     break
    #
    #             if ni != 0:
    #                 table[ni][j] = table[i][j]
    #
    #             table[i][j] = 0
    #
    #         else:   # 0인 경우
    #             continue
    #
    # for i in range(n):
    #     print(table[i])
