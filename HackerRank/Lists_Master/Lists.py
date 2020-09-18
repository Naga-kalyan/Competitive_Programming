if __name__ == '__main__':
    N = int(input())
    l1=[]
    for _ in range(N):
        a=input().split()
        if(a[0]=='insert'):
            l1.insert(int(a[1]),int(a[2]))
        elif(a[0]=='append'):
            l1.append(int(a[1]))
        elif(a[0]=='reverse'):
            l1=l1[::-1]
        elif(a[0]=='pop'):
            l1.pop()
        elif(a[0]=='sort'):
            l1.sort()
        elif(a[0]=='remove'):
            l1.remove(int(a[1]))
        elif(a[0]=='print'):
            print(l1)
