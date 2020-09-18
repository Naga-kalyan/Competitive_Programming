# Numbered-Lists
# DESCRIPTION
As a beginner in Python programming, your first task is to create a list which prints 10 numbers between a given start point and end point.

Write a Python script to implement this.

#### Input
* The first line contains the number of test-cases **T**.
* The next **T** lines contain a start point integer and an end point integer.

### Constraints
* The start point should NOT be less than 1; else print **Out of Range**
* The end point should NOT exceed 100; else print **Out of Range**
* The difference between the start point and end point (inclusive of both) should always be equal to 10; else print **Difference Not in Range**
* The limits constraint should be checked before the **difference** constraint.

#### Output
Print the 10 numbers between the given range.

## Sample Test Cases

#### Sample Input
```
3
1 9
22 31
90 103
```
#### Sample Output
```
Difference Not in Range
[22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
Out of Range
```
