import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    relation = ""
    nA, nB = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    same = 0
    for i in range(nA):
        for j in range(nB):
            if A[i] == B[j]:
                same += 1

    if same == nA == nB:
        relation = "="
    elif same == nA and nB > same:
        relation = "<"
    elif same == nB and nA > same:
        relation = ">"
    else:
        relation = "?"
    print(relation)
