# SquaresPyramid
# DESCRIPTION
A Square's Pyramid is a pattern pyramid formed by squaring certain types of numbers. The rule to get squares of numbers containing 1's as their digits is as such:

	1**2= 1
	11**2 = 121
	111**2 = 12321
	1111**2 = 1234321

You have to write a code to print these numbers in a pyramid form, wherein you take as input the number of digits till which the pattern should go on.

#### Input
* The first line contains an integer which denotes the number of test cases **T**.
* The next **T** lines contain the value of **n** which denotes the maximum number of 1's digits that you want to use to make the pyramid.

### Constraints

* 1 <= T <= 15
* 1 <= n <= 8

#### Output
* For each test case **T**, the square of all numbers printed in a pyramid form, with a newline separator separating each pyramid pattern.

## Sample Test Cases

#### Sample Input
```
2
4
5
```
#### Sample Output
```
    1
   121
  12321
 1234321

    1
   121
  12321
 1234321
123454321
```
