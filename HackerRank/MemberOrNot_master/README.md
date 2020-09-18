# MemberOrNot
# DESCRIPTION
Write a program that takes a value **x** (i.e. a number, string, etc) and a list of values **A**, and returns **True** if **x** is a member of **A**, **False** otherwise.

**Note** that this is exactly what the **in** operator does, but for the sake of the exercise you should pretend Python did not have this operator.

#### Input Format:
* First line will contain a value, you have to test its membership in the list.
* The next line will contain an integer,**N**, indicating the number of elements in the list 
* The next N lines will contain the elements of the list.
#### Output Format:
* Print "**True**" (without quotes) if the value on the first line of input is in the list, else print "**False**" (without quotes).

## Sample test case:

#### input #1:
```
bug
3
bug
in
production
```
#### Output #1:
```
True
```
### Explanation
First line is the element whose membership you have to test, next line indicate the number of elements in the list, next lines are the elements of the list, in this case bug is the list ['bug', 'in', 'production'] Hence True
