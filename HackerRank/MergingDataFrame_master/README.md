# MergingDataFrame
# DESCRIPTION
Write a program that does the following:
* **takes** three space-separated **integers** as input
* **generates** a series of evenly-spaced numbers as another **list** using the above values (using **NumPy arange**)
* **takes** another **list** as input
* **creates** two **Pandas Series** out of the lists
* **merges** both Series along the **index** axis, to form a **DataFrame**
* **takes column names** as inputs
* **prints** some (**n**) rows from the first OR last of the DataFrame along with the **column names**, depending on the input

**NOTE:** This DataFrame should contain the **column name**s as well as the data values, printed out to the console (STDOUT)

#### Input Format
* The first line contains three space-separated **integers**:
  * **stp** - the starting interval for the generated list
  * **enp** - the ending interval for the generated list
  * **step** - the step value (spacing between values) for the elements of the list
    * e.g. For the values 2, 12 and 3, the generated list **list1** will be: [2, 5, 8, 11]
* The second line contains the elements of the second list **list2**
* The third line contains two space-separated **strings** which should be the **column names** for the first and second lists respectively
* The last line contains two space-separated **integers**:
* **n** - This represents the number of rows that you have to print from the DataFrame.
* **pos** - This represents the position from where the rows have to be extracted. This can be only **1* (first) or **0** (last).

#### Output Format
* Depending on the values of **n** and **pos**, print the first/last **n** rows of the DataFrame on to the output console (STDOUT)

**NOTE:**
When printing the output, the elements of **list1** should always be present in the first column and elements of **list2** should always be present in the second column, else your test-cases will fail.

## Sample Test Cases

#### Sample Input
```
2 12 3
axe bar cat div eli fif gor had
NUM VAL
6 1
```
#### Sample Output
```
    NUM  VAL
0   2.0  axe
1   5.0  bar
2   8.0  cat
3  11.0  div
4   NaN  eli
5   NaN  fif
```
### Explanation
* There are only 4 elements in **list1** while there are 8 elements in **list2**
* With the values of **n** (6) and **pos** (1), the **1st 6** rows of the DataFrame are printed.
* Since, there are less number of corresponding elements in **list1**, hence the rest of the mapping under the column **NUM** shows up as **NaN**
* The column names, obtained from input, are **NUM** and **VAL**. They have been used as column names and can be seen at the head of the output.
