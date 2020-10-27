T = int(input())
for _ in range(T):
    N, K, X, Y = map(int, input().split())
    city_jumps = []
    for i in range(N+1):
        Z = (X+(K*i))%N
        if(Z == Y):
            print('YES')
            break
    else:
        print('NO')
