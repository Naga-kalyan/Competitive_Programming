from collections import OrderedDict
ordered_dictionary = OrderedDict()
for i in range(int(input())):
    a=input()
    if(a not in ordered_dictionary.keys()):
        ordered_dictionary[a]=1
    else:
        ordered_dictionary[a]=ordered_dictionary[a]+1
print(len(ordered_dictionary.keys()))
for i in ordered_dictionary.keys():
    print(ordered_dictionary[i],end=' ')
