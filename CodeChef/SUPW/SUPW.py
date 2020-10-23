n = int(input())
a = list(map(int, input().split()))
for i in reversed(range(0,n-3)):
    a[i] += min(a[i+1],a[i+2],a[i+3])
print(min(a[:3]))
