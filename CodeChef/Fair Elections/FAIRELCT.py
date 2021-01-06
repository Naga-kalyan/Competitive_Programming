T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    A = sorted(list(map(int, input().split())))
    B = sorted(list(map(int, input().split())), reverse = True)
    count = 0
    sumA = sum(A)
    sumB = sum(B)
    k = min(N,M)
    for i in range(k):
        if(sumA>sumB):
            break
        else:
            sumA -= A[i]
            sumB -= B[i]
            sumA += B[i]
            sumB += A[i]
            count += 1
    if(sumA>sumB):
        print(count)
    else:
        print(-1)
