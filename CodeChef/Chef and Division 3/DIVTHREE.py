for _ in range(int(input())):
    N, K, D = map(int,input().split())
    A = sum(list(map(int, input().split())))
    D3 = int(A/K)
    if(D3<D):
        print(D3)
    else:
        print(D)
