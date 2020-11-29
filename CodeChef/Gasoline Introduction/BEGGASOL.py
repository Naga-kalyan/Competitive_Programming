T = int(input())
for _ in range(T):
    N = int(input())
    f = list(map(int, input().split()))
    dist = 0
    gas = f[0]
    if (f[0]!=0):
        for i in f[1:]:
            gas += i-1
            if(gas == 0):
                dist += 1
                break
            else:
                dist += 1
    print(dist+gas)
