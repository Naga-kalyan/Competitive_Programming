# NumPy-Array
# DESCRIPTION
Write a simple program that takes three integers as input: **stp**, **enp** and **step** ; and uses these values to return evenly spaced values within the given interval.

#### Input Format
* The first line contains an **integer - stp** which represents the start of the interval.
* The second line contains an **integer - enp** which represents the end of the interval.
* The third line contains an **integer - step** which represents the spacing between consecutive values.

### Constraints
* 1 <= **stp** < **enp** <= 105
* 2 <= **step** < **enp** <= 105

#### Output Format
* If the above constraints are not satisfied, print "**Constraints are failing!**"
* If the above constraints are satisfied, print each element of the list in a new line, as is generated using the condition described in the Problem Statement.

## Sample Test Cases

#### Sample Input #1
```
2
11
3
```
#### Sample Output #1
```
2
5
8
11
```
### Explanation #1
* First element = **2**
* 2 + 3 = **5**
* 5 + 3 = **8**
* 8 + 3 = **11**
 
 Since, the above elements fall in the given range as specified by the input, hence they will be printed to STDOUT, with each element on a new line.

#### Sample Input #2
```
2
11
13
```
#### Sample Output #2
```
Constraints are failing!
```
### Explanation #2
* Since, the value of **step** is more than the value for **enp**, hence the message "**Constraints are failing!**" will be printed to STDOUT.
