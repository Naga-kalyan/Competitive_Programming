# Conversion
# DESCRIPTION
You have to write a Python program which does the following:
* **takes** a **list** as input
* **converts** the list into a **Pandas Series**
* **reshapes** the Series into a **dataframe** of the order **m** x **n**, i.e. the dataframe has **m** rows and **n** columns

#### Input Format
* The first line contains two space-separated integers, representing the values of **m** and **n** respectively.
* The second line contains space-separated integers, which represent the elements of the **list**

#### Output Format
* If the product of m and n equals the length of the input **list**, print the converted **dataframe**
* If the product of m and n is **NOT EQUAL** to the length of the input **list**, print the message "**Weird Order!**"

### Constraints
* 2 <= **m**, **n** <= 10
* The product of **m** and **n** should be equal to the **length** of the input **list**

## Sample Test Cases

#### Sample Input #1
```
2 3
1 2 3 4 5 6 7 8
```
#### Sample Output #1
```
Weird Order!
```
### Explanation #1
Since the product of **m** and **n** is NOT EQUAL to the **length** of the input **list**, hence print "**Weird Order!**"


#### Sample Input #2
```
2 4
1 2 3 4 5 6 7 8
```
#### Sample Output #2
```
   0  1  2  3
0  1  2  3  4
1  5  6  7  8
```
### Explanation #2
Apart from the first column and first row [index] (containing the values **0** to **1** and **0** to **3** respectively), you can see that the rest of the elements have been reshaped to form a dataframe of **2 rows** and **4 columns**
