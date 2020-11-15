for i in range(int(input())):
    salary=int(input())
    if(salary<1500):
        print("{:.2f}".format((salary+salary*0.1+salary*0.9)))
    elif(salary>=1500):
        print("{:.2f}".format((salary+500+salary*0.98)))
