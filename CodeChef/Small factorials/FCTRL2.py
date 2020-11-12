T = int(input())
for _ in range(T):
    N = int(input())
    fact = 1
    for i in range(1, N+1):
        fact = fact*i
    print(fact)
