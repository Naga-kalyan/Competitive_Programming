while(1):
    length=int(input())
    if(length==0):
        break
    List_1=list(map(int,input().split()))
    List_2 = [0]*length
    for i in range(0, len(List_1)):
        List_2[List_1[i]-1] = i+1
    if(List_1==List_2):
        print("ambiguous")
    else:
        print("not ambiguous")
