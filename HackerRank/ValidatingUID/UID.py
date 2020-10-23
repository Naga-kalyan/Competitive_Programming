import re

def valid_UID(a):
    if len(a) != 10:
        return 'Invalid'
    if  not re.search(r'.*[A-Z].*[A-Z].*', a):
        return 'Invalid' 
    if not re.search(r'.*\d.*\d.*\d.*', a):
        return 'Invalid' 
    if not re.search(r'[a-zA-Z\d]{10}', a):
        return 'Invalid'
    if re.search(r'(.).*\1', a):
        return 'Invalid'
    return 'Valid'

for _ in range(int(input())):
    a = input()
    print(valid_UID(a))
