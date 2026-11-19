import sys
sys.stdin = open("input.txt", "r")

T = int(input())


for tc in range(1, T+1):
    S = input()

    # All "R"
    curr = 0
    max_distance = 0
    for s in S:
        if s == "?":
            curr += 1
        elif s == "R":
            curr += 1
        elif s == "L":
            curr -= 1
        max_distance = max(max_distance, abs(curr))

    curr = 0
    # All "L"
    for s in S:
        if s == "?":
            curr -= 1
        elif s == "R":
            curr += 1
        elif s == "L":
            curr -= 1

        max_distance = max(max_distance, abs(curr))

    print(max_distance)

    # combo = set()
    #
    # for i in range(len(S)):
    #     s = S[i]
    #     if s == "?":
    #         s[:i] + "L"
    #         s[:i] + "R"
    #
    # l, r, q = 0, 0, 0
    #
    # for s in S:
    #     if s == "L":
    #         l += 1
    #     elif s == "R":
    #         r += 1
    #     else:
    #         q += 1
    #
    # prev = ""
    # curr = 0
    # answer = 0
    # for s in S:
    #     if s == "L":
    #         curr -= 1
    #         prev = "L"
    #     elif s == "R":
    #         curr += 1
    #         prev = "R"
    #     else: # "?"
    #         if abs(answer+1) >= abs(answer-1) and prev == "R":
    #             curr = curr+1
    #             answer += 1
    #         elif abs(answer+1) < abs(answer-1) and prev == "L":
    #             curr = curr-1
    #             answer += 1
    #         else:
    #             if l > r:
    #                 curr = curr - 1
    #             elif l < r:
    #                 curr = curr + 1
    #             else:
    #                 if prev == "L":
    #                     curr = curr-1
    #                 elif prev == "R":
    #                     curr = curr+1
    #
    #     answer = max(answer, abs(curr))
    #
    # print(answer)

    # l, r = 0, 0
    # question = 0
    # robot = 0
    # dist = []
    # for s in S:
    #     if s == "L":
    #         robot -= 1
    #         dist.append(robot)
    #     elif s == "R":
    #         robot += 1
    #         dist.append(robot)
    #     else:
    #         question += 1
    #         dist.append(0)
    #
    # print(dist)
    #
    # if question == 0:
    #     print(robot)
    # else:
    #     if robot >= 0:
    #         robot += question
    #         print(robot)
    #     else:
    #         robot -= question
    #         print(abs(robot))
