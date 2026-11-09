N = 10**6
is_prime = [True for _ in range(N+1)]
is_prime[0] = False
is_prime[1] = False

for i in range(2, N+1):
    if is_prime[i]:
        for k in range(i*i, N+1, i):
            is_prime[k] = False

for i in range(N+1):
    if is_prime[i]:
        print(i, end=" ")
