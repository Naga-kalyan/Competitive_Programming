T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    l = list(map(int, input().split()))
    count = 1
    for i in range(1,a):
        if(l[i-1] != l[i]):
            count = count+1
    for j in range(b):
        c, d = map(int, input().split())
        if(c>1):
            if(l[c-2]!=l[c-1]):
                count = count-1 
        if(c<a):
            if(l[c]!=l[c-1]):
                count = count-1
        l[c-1] = d
        if(c>1):
            if(l[c-2]!=l[c-1]):
                count = count+1 
        if(c<a):
            if(l[c]!=l[c-1]):
                count = count+1
        print(count)
