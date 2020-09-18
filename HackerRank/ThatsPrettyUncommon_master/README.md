# That-s-Pretty-Uncommon!
# DESCRIPTION
Write a program that does the following:
* takes two lists as inputs
* creates two Pandas Series out of the lists
* prints all those elements which are not common to either of the lists.

#### Input Format
* The first line contains space-separated values, which represent the elements of the first list list1
* The second line contains space-separated values, which represent the elements of the second list list2

#### Output Format
* Print all those elements of both lists, which are not common between both; along with their dtype

### Sample Test Cases

#### Sample Input
```
1 2 3 4 5 6
4 5 6 7 8 9
```
#### Sample Output
```
0    1
1    2
2    3
6    7
7    8
8    9
dtype: object
```
#### Explanation

The numbers 4, 5 and 6 are common to both lists. Since, you have to print all elements which are not common to either of the lists. Hence, the output should be 1, 2, 3, 7, 8 and 9 along with their dtype.

