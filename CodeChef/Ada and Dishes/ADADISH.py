T = int(input())
for _ in range(T):
    N = int(input())
    C = list(map(int, input().split()))
    if(N == 1):
        print(C[0])
    elif(N == 2):
        print(max(C))
    else:
        C = sorted(C, reverse=True)
        a = C[0]
        b = C[1]
        for i in C[2:]:
            if(b<a):
                b += i
            else:
                a += i
        print(max(a, b))
        
