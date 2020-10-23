def minion_game(string):
    vowels='AEIOU'
    stuart=0
    kevin=0
    for i in range(len(string)):
        if(string[i] in vowels):
            kevin+=len(string)-i
        else:
            stuart+=len(string)-i
    if(stuart>kevin):
        print('Stuart',stuart)
    elif(stuart<kevin):
        print('Kevin',kevin)
    else:
        print('Draw')
