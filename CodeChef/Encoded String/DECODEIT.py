def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return(decimal)
T = int(input())
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
for _ in range(T):
    N = int(input())
    S = input()
    for i in range(0,N,4):
        deci = binaryToDecimal(int(S[i:i+4]))
        print(alphabets[deci], end = '')
    print()
