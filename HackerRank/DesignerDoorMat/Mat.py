a=[int(i) for i in input().split()]
for i in range(1,a[0],2):
    print(('.|.'*i).center(a[1],'-'))
print('WELCOME'.center(a[1],'-'))
for i in reversed(range(1,a[0],2)):
    print(('.|.'*i).center(a[1],'-'))
