T = int(input())
for _ in range(T):
    n, s1, s2, hp1, hp2 = map(int, input().split())
    a = list(map(int, input().split()))
    f1 = True
    f2 = True
    l1 = 0
    l2 = 0
    if(a[0] == 0):
        hp1 -= 5
        hp2 -= 5
        f1 = False
        f2 = False
    while(True):
        if f1 == True:
            l1 = min(l1+s1, n-1)
            if(a[l1] == 0):
                hp1 -= 5
                f1 = False
        else:
            f1 = True
        if(l1 >= n-1):
            print("A", abs(l1-l2))
            break
        if(hp1 <= 0):
            print("B", abs(l1-l2))
            break
        if f2 == True:
            l2 = min(l2+s2, n-1)
            if(a[l2] == 0):
                hp2 -= 5
                f2 = False
        else:
            f2 = True
        if(l2 >= n-1):
            print("B", abs(l1-l2))
            break
        if(hp2 <= 0):
            print("A", abs(l1-l2))
            break