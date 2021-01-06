T = int(input())
for _ in range(T):
    N, K, x, y = map(int, input().split())
    if(x == y):
        print(N, N)
    else:
        if(x<y):
            final_cordinates = [[x+N-y, N], [N, N-y+x], [y-x, 0], [0, y-x]]
        else:
            final_cordinates = [[N, y+N-x], [y+N-x, N], [0, x-y], [x-y, 0]]
        result = final_cordinates[(K-1)%4]
        print(result[0], result[1])
