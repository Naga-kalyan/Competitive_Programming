# Not-Present
# DESCRIPTION
You have to write a program that does the following:
* **takes** two **lists** as inputs
* **creates** two **Pandas Series** from the above lists - **series1** and **series2**
* **removes** all items from **series1** which are present in **series2**

#### Input Format
*The first line contains elements of the first list - **list1**
* The second line contains elements of the second list - **list2**

#### Output Format
* Print all elements of the Series and its **dtype**, after performing the required operations as given in the Problem Statement.

## Sample Test Cases

#### Sample Input
```
4 5 2 3 4 1
4 5 6 7 8
```
#### Sample Output
```
2    2
3    3
5    1
dtype: object
```
### Explanation
* The numbers common between list1 and list2 are 4 and 5.
* Hence, after excluding 4 and 5 from list1, the elements which remain are 2, 3 and 1, which have been printed to STDOUT along with their index and dtype
