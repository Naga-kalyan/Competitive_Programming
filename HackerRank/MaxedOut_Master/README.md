# Maxed-Out
# DESCRIPTION
You have been given a list of 10 numbers. The list goes as:

**[1, 7, 90, 33, 67, 56, 20, 39, 10, 30]**

The indexing of this list starts from 0 and goes up to 9. Given three indices, you have to write a function that calculates the maximum number which is present at these indices.

### Input
* The first line contains the number of test cases T.
* The next T lines contain 3 space-separated integers, which have a value between 0 to 9.

### Output
* For each test case T, print the maximum number from the above list, out of the three indices obtained from the input.

## Sample Test Cases

#### Sample Input
```
2
1 2 3
4 6 8
```
#### Sample Output
```
90
67
```
## Explanation
* For Test Case 1, the indices given are 1, 2 and 3, which means the selected numbers from the above list are: 7, 90 and 33 respectively. So, 90 is the greatest of these three numbers.
* For Test Case 2, the indices given are 4, 6 and 8, which means the selected numbers from the above list are: 67, 20 and 10 respectively. So, 67 is the greatest of these three numbers.
