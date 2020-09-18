# Frequency
# DESCRIPTION
Write a Python program that does the following:
* **takes** a **list** as input
* **creates** a **Pandas Series** from the list
* **prints** the **frequency count** of each unique value in the Series

#### Input Format
* The first line contains space-separated values, which represent the elements of a **list**

#### Output Format
* Print the **frequency count** of each unique value (in ascending order), with its **dtype**, to STDOUT

## Sample Test Cases

#### Sample Input #1
```
a a a b c c c d d d d e e e e e f f f f f f g g g g g g g h h h h h h h h
```
#### Sample Output #1
```
a    3
b    1
c    3
d    4
e    5
f    6
g    7
h    8
dtype: int64
```
### Explanation #1

The frequency of each unique letter has been printed out to the STDOUT, with the input values in ascending order.

### NOTE:
* This ascending order is NOT of the **frequency** of the letters (input values).
* This order is of the **letters** (input values) itself.

#### Sample Input #2
```
 2 2 2 2 2 2 2 2 2 1 1 1 1 3 3 3 3 3 3 3 4 4 4 4 4
```
#### Sample Output #2
```
1    4
2    9
3    7
4    5
dtype: int64
```
### Explanation #2

The frequency of each unique number has been printed out to the STDOUT, with the input values in ascending order.

### NOTE:
* This ascending order is NOT of the **frequency** of the numbers (input values).
* This order is of the **numbers** (input values) itself.
