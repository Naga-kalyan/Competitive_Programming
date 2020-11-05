T = int(input())
for _ in range(T):
    X, Y = map(int, input().split())
    diff = Y-X
    if(diff == 0):
        print(0)
    elif(X<Y):
        if(diff%2 != 0):
            print(1)
        else:
            diff = diff/2
            if(diff%2 == 0):
                print(3)
            else:
                print(2)
    else:
        if(diff%2 == 0):
            print(1)
        else:
            print(2)
