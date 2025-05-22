import sys
sys.stdin = open("input.txt", "r")

T = int(input())

for test_case in range(1, T+1):
    answer = str(test_case)
    count = 0
    if '3' in answer:
        count += answer.count('3')
    if '6' in answer:
        count += answer.count('6')
    if '9' in answer:
        count += answer.count('9')

    if count > 0:
        answer = count * "-"

    print(answer, end=" ")

