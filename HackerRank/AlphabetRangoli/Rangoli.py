def print_rangoli(N):
    for i in range (-(N-1),N):
        for j in range (-2*(N-1),2*(N-1)+1):
            if j%2==0 and (abs(j//2)+abs(i))< N:
                print (chr(abs(j//2)+abs(i)+ord('a')),end='')
            else:
                print('-',end='')
        print()
