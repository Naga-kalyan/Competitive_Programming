T = int(input())
for _ in range(T):
    N = int(input())
    a = list(map(int,input().split()))
    ans = 0
    Sum = 0
    for i in a:
        ans |= i
        Sum += i
        ans |= Sum
    print(ans)
