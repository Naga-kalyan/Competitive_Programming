T = int(input())
mod = 10**9+7
for _ in range(T):
    n = int(input())
    height = list(map(int, input().split()))
    max_count = 0
    i = n-1
    while(i>=0):
        count = 0
        m = i
        while i>=0 and height[i]<=height[m]:
            i -= 1
            count += 1
        max_count = max(max_count,count)
    c=1
    for i in range(2, max_count+1):
        c = (c*i)%mod
    print(c)
