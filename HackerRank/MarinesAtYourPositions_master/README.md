# MarinesAtYourPositions
# DESCRIPTION
Write a Python program that does the following:
* **takes** a **list** as input - **list_input**
* **takes** another **list** as input - **list_pos**
* **creates** a **Pandas Series** from **list_input**
* **prints** all values of **list_input** which are present at the positions listed out by **list_pos**

#### Input Format
* The first line contains space-separated **values** (this value can be of any data type), which represent the elements of the list **list_input**
* The second line contains space-separated **integers**, which represent the elements of the list **list_pos**.
* These positions are on **0-based indexing**, i.e. indexing starts from 0.

#### Output Format
* For the positions listed out by **list_pos**, print all values from **list_input** which are present at those locations, along with its **dtype**

## Sample Test Cases

#### Sample Input
```
a b c d e f g h i j k l m n o p q r s t u v w x y z
0 4 8 14 20
```
#### Sample Output
```
0     a
4     e
8     i
14    o
20    u
dtype: object
```
### Explanation

Based on 0-based indexing, the values of **list_input** present at the positions: **0, 4, 8, 14** and **20** ARE **a, e, i, o** and **u** respectively.

