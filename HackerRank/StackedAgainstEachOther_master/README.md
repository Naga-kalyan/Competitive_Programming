# Stacked-against-Each-Other
# DESCRIPTION
Write a Python program that does the following:
* **takes** two **lists** as input - **list1** and **list2**
* **creates** two **Pandas Series** out of them
* **stacks** / **concatenates** both Series vertically and horizontally, along the **column** axis (**axis** = 1)

#### Input Format
* The first line contains space-separated values, which represent the elements of the first list **list1**
* The second line contains space-separated values, which represent the elements of the second list **list2**

### Constraints
* length of **list1** = **length of list2**

#### Output Format
* Print the dataframe containing the required output, with **list1** being the first column and **list2** being the second column 
* If the above constraint is NOT satisfied, print **NaN** for all missing values

## Sample Test Cases

#### Sample Input #1
```
0 1 2 3 4
a b c d e
```
#### Sample Output #1
```
   0  1
0  0  a
1  1  b
2  2  c
3  3  d
4  4  e
```
### Explanation #1
Both lists are converted into Series and then stacked against each other.
Then, the stacked/concatenated DataFrame is printed to STDOUT.

#### Sample Input #2
```
0 1 2 3
a b c d e
```
#### Sample Output #2
```
     0  1
0    0  a
1    1  b
2    2  c
3    3  d
4  NaN  e
```
### Explanation #2
Both lists are converted into Series and then stacked against each other.
Then, the stacked/concatenated DataFrame is printed to STDOUT.
The missing value of **list1** corresponding to that of **list2** has been printed as **NaN**.


