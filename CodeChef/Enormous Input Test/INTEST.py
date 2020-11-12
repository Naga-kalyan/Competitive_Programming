(n, k) = map(int, input().split())
count = 0
for i in range(n):
	x = int(input())
	if x % k == 0:
		count += 1
print(count)	
