T = int(input())


def back(n, numbers, change, visited):
    global max_num

    key = (tuple(numbers), n)
    if key in visited:
        return

    visited.add(key)

    if n == change:
        max_num = max(max_num, int(''.join(map(str, numbers))))
        return

    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            numbers[i], numbers[j] = numbers[j], numbers[i]
            back(n + 1, numbers, change, visited)
            numbers[j], numbers[i] = numbers[i], numbers[j]


for test_case in range(1, T + 1):
    num, change = input().split()
    numbers = [int(n) for n in num]

    visited = set()
    max_num = 0

    change = int(change)

    back(0, numbers, change, visited)
    print(visited)
    print(f"#{test_case} {max_num}")
