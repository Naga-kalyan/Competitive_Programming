n=int(input())
dict1={}
if(n>=2 and n<=10):
    for i in range(n):
        N=input().split()
        if(len(N)==4):
            dict1[N[0]]=(float(N[1])+float(N[2])+float(N[3]))/3
    name=input()
    print("{:.2f}".format(dict1[name])) 
