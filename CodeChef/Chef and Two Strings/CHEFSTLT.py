T = int(input())
for _ in range(T):
    S1 = input()
    S2 = input()
    qcount = 0
    discount = 0
    for i in range(len(S1)):
        if((S1[i] == '?') or (S2[i] == '?')):
            qcount += 1 
        elif(S1[i] != S2[i]):
            discount += 1
    print(discount, qcount+discount)
