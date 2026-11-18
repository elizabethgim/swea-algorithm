import sys
sys.stdin = open("sample_input.txt", "r")
T = int(input())


def bt(n, total, score):
    global max_score

    if total > L:
        return

    max_score = max(max_score, score)

    for i in range(n, N):
        bt(i+1, total+ingredients[i][1], score+ingredients[i][0])


for test_case in range(1, T+1):
    N, L = map(int, input().split())
    ingredients = []
    for _ in range(N):
        ingredients.append(list(map(int, input().split())))

    ingredients = sorted(ingredients, key=lambda x: x[0], reverse=True)

    max_score = 0
    bt(0, 0, 0)

    print(f"#{test_case} {max_score}")