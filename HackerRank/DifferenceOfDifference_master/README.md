# DifferenceOfDifference
# DESCRIPTION
Write a Python program that does the following:
* **takes** an **integer list** as input
* **creates** a **Pandas Series** from the list
* **prints** the **difference of the difference** between consecutive elements of the list

#### Input Format
* The first line contains space-separated **integers**, which represent the elements of the input **list**

#### Output Format
* Print the **difference** of the consecutive elements of the list on the first line.
* Print the **difference of the difference** of the elements obtained from the above, on the second line
* For missing values, print **nan** (missing values will be present when you try to subtract the **0th** element from the **1st** element)

## Sample Test Cases

#### Sample Input
```
2 4 6 8 10 12 14 16
```
#### Sample Output
```
[nan, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]
[nan, nan, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
#### Explanation
* In the first line of output, the **difference** between consecutive elements of the **input list** is printed. Let's call this output list as **list_diff**
* In the second line of output, the **difference** between consecutive elements of **list_diff** is printed.
