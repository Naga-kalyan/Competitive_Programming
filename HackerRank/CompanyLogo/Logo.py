if __name__ == '__main__':
    s = list(input())
    set1 = set(s)
    list1 = []
    for i in set1:
        list1.append([s.count(i), i])
    op1 = sorted(list1, key = lambda x:x[1])
    op2 = sorted(op1, key = lambda x:x[0], reverse = True)
    for op in op2[:3]:
        print(op[1]+' '+str(op[0]))
