'''
N: 10의 배수
N/10명까지 동일한 평점을 부여할 수 있는 학생 제한
총점이 동일한 경우는 없음

K번째 학생
총점 = 중간 35 기말 45 과제 20


'''
import sys
sys.stdin = open("input.txt", "r")
T = int(input())

for test_case in range(1, T+1):
    N, K = map(int, input().split())

    scores = []

    for i in range(N):
        m, l, a = map(int, input().split())

        total = 0.35 * m + 0.45 *l + 0.20*a
        scores.append((i, total))

    scores.sort(key = lambda x: x[1], reverse=True)

    grade = ["", "A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    g = 0
    students = ["" for _ in range(N)]
    start = scores[0][0]
    students[start] = "A+"

    # print(scores)

    for i in range(N):
        if i % (N//10) == 0:
            g = (g+1) % 10

        students[scores[i][0]] = grade[g]


        # print(scores[i][0], scores[i][1], grade[g])

    print(f"#{test_case} {students[K-1]}")