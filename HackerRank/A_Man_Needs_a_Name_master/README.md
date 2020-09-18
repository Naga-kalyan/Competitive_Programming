# A Man Needs a Name
# DESCRIPTION
Write a program that does the following:
* **takes** a **list** as input
* **creates** a **Pandas Series** from the list above
* **takes** a **string** as input and **assigns** the string as a name to the Series
* **takes** the inputs for **n** & **pos** and prints some (**n**) rows from the first OR last of the Series, depending on the input

#### Input Format
* The first line contains the elements of the **list**
* The second line contains a **string** which is to be used as a name for the **Pandas Series** being generated.
* The last line contains two space-separated **integers**:
* **n** - This represents the number of rows that you have to print from the Series.
* **pos** - This represents the position from where the rows have to be extracted. This can be only 1 (first) or 0 (last).

#### Output Format
* Depending on the values of **n** and **pos**, print the first/last **n** rows of the Series on to the STDOUT
* Print the **Name** and **dtype** of the output Series with its name (from input) and data type.

## Sample Test Cases

#### Sample Input
```
a b c e d f g h i j k l m n o p q r s t u v w x y z
alphabets
3 1
```
#### Sample Output
```
0    a
1    b
2    c
Name: alphabets, dtype: object
```
### Explanation
* Based on the values of **n** (3) and **pos** (1), you have to print the **1st 3** rows of the Series.
* The **Name** of the Series is **alphabets**, as obtained from the input.
* The **dtype** of the Series is **object**.
