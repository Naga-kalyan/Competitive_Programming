T = int(input())
for _ in range(T):
    menus = 0
    p = int(input())
    price = [2048, 1024, 512, 256, 128, 64, 32, 16, 8, 4, 2, 1]
    for i in price:
        menus += p//i
        p = p%i
    print(menus)
