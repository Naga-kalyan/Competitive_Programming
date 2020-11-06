T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int, input().split()))
    Llist = [A[0]]
    Rlist = [A[N-1]]
    for i in range(1, N):
        Llist.append(min(Llist[-1]+1, A[i]))
        Rlist.append(min(Rlist[-1]+1, A[N-1-i]))
    print(*[min(Llist[i], Rlist[N-1-i]) for i in range(N)])
