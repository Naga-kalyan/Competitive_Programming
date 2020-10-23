a = list(map(float, input().split()))
if((a[0]%5 == 0) and ((a[1]-a[0]-0.5)>=0)):
    print("{:.2f}".format(a[1]-a[0]-0.5))
else:
    print("{:.2f}".format(a[1]))
