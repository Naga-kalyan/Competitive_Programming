def retrieve_names(names, sentinel_character ,length):
    names=names.split(sentinel_character)
    for i in range(len(names)):
        x=names[i].split()
        if(len(x[0])>length):
            names[i]=x[0][0].capitalize()+' '+x[1].capitalize()
        else:
            names[i]=x[0].capitalize()+' '+x[1].capitalize()
    names_final=[]
    if(len(names)!=len(set(names))):
        names_dup=list(set(names))
        for i in range(len(names_dup)):
            z=names.count(names_dup[i])
            if(z!=1):
                for j in range(1,z+1):
                    names_final.append(names_dup[i]+str(j))
            else:
                names_final.append(names_dup[i])
    else:
        names_final=names
    return('-'.join(sorted(names_final)))
