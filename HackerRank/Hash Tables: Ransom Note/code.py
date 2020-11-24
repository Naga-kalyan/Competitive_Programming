x, y = map(int, input().split())
S1 = sorted(input().split())
S2 = sorted(input().split())
k = 0
if (S1 != S2):
    for i in S2:
        if(i in S1):
            S1.remove(i)
        else:
            k = 1
            print('No')
            break
if(k==0):
    print('Yes')
