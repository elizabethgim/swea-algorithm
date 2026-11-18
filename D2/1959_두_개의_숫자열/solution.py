import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    na, nb = map(int, input().split())

    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    answer = 0
    if na <= nb:
        min_length = len(A)
        max_length = len(B)

        for i in range(max_length):
            total = 0
            # print(i)
            if i > max_length-min_length:
                continue

            for j in range(i, i+min_length):
                # print("result: ", A[j-i] * B[j])
                total += A[j-i] * B[j]
            # print(total)
            answer = max(total, answer)
    else:
        min_length = len(B)
        max_length = len(A)

        for i in range(max_length):
            total = 0

            if i > max_length-min_length:
                continue
            for j in range(i, i + min_length):
                total += B[j - i] * A[j]

            answer = max(total, answer)

    print(f"#{tc} {answer}")
