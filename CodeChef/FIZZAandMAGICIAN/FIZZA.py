T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int, input().split()))
    max_count = 0
    for k in range(N-1):
        count = 0
        i = k
        while((((i+1)<N) and (a[i+1]==a[i]))or(((i+2)<N) and (a[i+2]==a[i]))):
            if(a[i+1]==a[i]):
                i += 1
            else:
                i += 2
            count += 1
        max_count = max(max_count, count)
    print(max_count)
