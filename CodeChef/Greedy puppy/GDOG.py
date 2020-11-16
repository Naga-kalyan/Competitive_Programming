for _ in range(int(input())):
    x,y=map(int,input().split())
    m = 0
    for i in range(1, y+1):
        m = max(m, x%i)
    print(m)
