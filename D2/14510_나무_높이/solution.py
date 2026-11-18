import sys
sys.stdin = open("input.txt", "r")

T = int(input())


def can_finish(D, one, two):
    odd = (D+1) // 2
    even = D // 2
    two_used = min(two, even)
    one_needed = one + 2 * (two - two_used)
    return one_needed <= odd


for tc in range(1, T+1):
    N = int(input())
    trees = list(map(int, input().split()))
    max_tree_height = max(trees)

    one, two = 0, 0
    total = 0

    for h in trees:
        d = max_tree_height - h
        two += d // 2
        one += d % 2
        total += d

    low, high = 0, total * 2

    while low < high:
        mid = (low + high) // 2
        if can_finish(mid, one, two):
            high = mid
        else:
            low = mid + 1

    print(f"#{tc} {low}")
