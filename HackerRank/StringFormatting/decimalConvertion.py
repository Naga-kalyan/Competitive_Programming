def print_formatted(number):
    n=len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(n,' '),oct(i)[2:].rjust(n,' '),hex(i)[2:].upper().rjust(n,' '),bin(i)[2:].rjust(n,' '))
