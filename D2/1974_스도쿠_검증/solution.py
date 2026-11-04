'''
행 체크
열 체크
네모 체크

숫자 존재 여부 체크
boolean 배열에서 true/false
이미 true인데 다시 찾으면 break

네모 체크에서 특정 3x3 칸에서만 동작한다는 걸 놓침
'''

import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    puzzle = []
    for _ in range(9):
        puzzle.append(list(map(int, input().split())))

    dx = [0, 1, 2, 0, 1, 2, 0, 1, 2]
    dy = [0, 0, 0, 1, 1, 1, 2, 2, 2]

    flag = True

    for i in range(9):
        row_flag = True
        col_flag = True
        square_flag = True

        row_check = [False for _ in range(9)]
        col_check = [False for _ in range(9)]

        for j in range(9):
            # 행 체크
            if not row_check[puzzle[i][j]-1]:
                row_check[puzzle[i][j] - 1] = True
            else:
                row_flag = False
                break

            # 열 체크
            if not col_check[puzzle[j][i] - 1]:
                col_check[puzzle[j][i] - 1] = True
            else:
                col_flag = False
                break

            # 네모 체크
            # print(i, j, puzzle[i][j])
            if i % 3 == 0 and j % 3 == 0:
                square_check = [False for _ in range(9)]

                for k in range(9):
                    ni = i + dx[k]
                    nj = j + dy[k]

                    # print(ni, nj)
                    if 0 <= ni < 9 and 0 <= nj < 9:
                        # print(puzzle[ni][nj])
                        if not square_check[puzzle[ni][nj]-1]:
                            square_check[puzzle[ni][nj]-1] = True
                        else:
                            square_flag = False
                            break
                    else:
                        square_flag = True
                        break
            # print(square_flag)
            #
            # print(row_flag, col_flag, square_flag)
            # print()

        if not row_flag or not col_flag or not square_flag:
            flag = False
            break

    answer = 1

    if not flag:
        answer = 0

    print(f"#{test_case} {answer}")