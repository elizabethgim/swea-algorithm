'''
X = max(A, B) = A
Y = max(B, C) = B
Z = max(C, A) = C

A, B, C가 존재하는지

'''
import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for tc in range(1, T+1):
    X, Y, Z = map(int, input().split())

    A = min(X, Y)
    B = min(Y, Z)
    C = min(X, Z)

    flag = False
    if A > B:
        # X = max(A, B) = A
        if B > C:
            # Y = max(B, C) = B
            if C < A:
                # Z = max(C, A) = A
                # A, B, A
                # C < B
                # A < B
                # C < A < B
                flag = True
            else: # C >= A
                # Z = max(C, A) = C
                # A, B, C
                # A <= C < B, B < A, 상충
                flag = False
        else: # B <= C
            # if C < A:
                # B <= C < A, A > B 상충
            # else:
                # C >= A, A <= C,
                # B <= C, B < A
                # B < A <= C, B <= C 상충
            flag = False
    else: # A <= B
        if A == B == C:
            flag = True
        # X = max(A, B) = A
        # if B > C:
        #     # A <= B < C
        #     if C < A:
        #         # 상충
        #         flag = False
        #     else: # A <= C < B, A=B=C
        #         if A == B == C:
        #             flag = True
        #         else:
        #             flag = False
        # else: # B <= C
        #     if C < A:
        #         # B <= C < A, A<= B
        #         if A == B == C:
        #             flag = True
        #         else:
        #             flag = False
        #     else:
        #         # C >= A, A <= C,
        #         # B <= C, B < A
        #         # B < A <= C, B <= C 상충
        #         flag = False

    if flag:
        print(A, B, C)
    else:
        print(-1, -1, -1)