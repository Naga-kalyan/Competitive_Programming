T = int(input())
for _ in range(T):
    n = int(input())
    List = []
    for _ in range(n):
        List.append(list(map(int, input().split())))
    for i in reversed(range(0, n-1)):
        for j in range(0,i+1):
           List[i][j] += max(List[i+1][j], List[i+1][j+1])
    print(List[0][0])
