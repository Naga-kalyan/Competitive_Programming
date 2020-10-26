T = int(input())
for _ in range(T):
    n, k = map(int, input().split())
    Q = list(map(int, input().split()))
    qk = 0
    for i in range(n):
        qk += Q[i]
        if(qk < k):
            print(i+1)
            break
        else:
            qk -=k
    else:
        print((sum(Q)//k)+1)
