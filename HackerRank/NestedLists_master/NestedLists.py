N=int(input())
python_students=[]
scores_list=[]
final_list=[]
if(N>=2 and N<=5):
    for i in range(N):
        names=input()
        scores=float(input())
        python_students.append([names,scores])
        scores_list.append(scores)
    scores_list=sorted(set(scores_list))
    for i in range(N):
        if(python_students[i][1]==scores_list[1]):
            final_list.append(python_students[i][0])
    for i in sorted(final_list):
        print(i)
