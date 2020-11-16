N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
start = 0
tasks = []
for i in range(N):
    if(a[i]>=start):
        tasks.append(i)
        start = b[i]
print(*tasks)
