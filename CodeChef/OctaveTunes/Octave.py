T = int(input())
for _ in range(T):
    N = int(input())
    a = sorted(list(map(int, input().split())))
    count = 0
    b = []
    for i in range(1, 9):
        b.append(a.count(i))
    print(min(b))
