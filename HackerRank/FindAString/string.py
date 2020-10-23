def count_substring(string, sub_string):
    count=0
    i=0
    while(i!=len(string)-len(sub_string)+1):
        z=string[i:].find(sub_string)
        if(z!=-1):
            count+=1
            i=i+z+1
        else:
            break
    return count
