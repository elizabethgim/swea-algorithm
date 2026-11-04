'''
https://swexpertacademy.com/main/code/problem/problemDetail.do
'''
T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    total = 0
    arr = list(map(int, input().split()))
    for a in arr:
        if a % 2 == 1:
            total += a
    print("#{} {}".format(test_case, total))
