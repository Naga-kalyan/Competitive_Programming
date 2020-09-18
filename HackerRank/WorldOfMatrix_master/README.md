# World-of-Matrix
# DESCRIPTION
Morpheus and his team of human rebels left in Zion have identified a new glitch in the Matrix World. Given an integer **N**, you have to identify which  type of world it refers to :
* If **N** is a multiple of 3 and an odd number, print **Matrix**
* If **N** is only an odd number, print **Glitch**
* If **N** is a multiple of 3 and an even number, print **Zion**
* If **N** is only an even number, print **Reality**

#### Input

* The first line contains the number of Test cases **T**.
* The next T lines contain a single integer value N, to be subsequently identified as a part of one of the four worlds, i.e. **Matrix, Glitch, Zion** or **Reality**.

### Constraints
* 1 <= N <= 200

#### Output

Print **Matrix, Glitch, Zion** or **Reality** based on the conditions as given above, in new lines.

## Sample Test Cases

#### Sample Input
```
6
2
3
4
5
6
7
```
#### Sample Output
```
Reality
Matrix
Reality
Glitch
Zion
Glitch
```
#### Explanation

For Test case 1:

**2**  is not a multiple of 3, but is only an even number; hence **Reality**.

For Test case 2:

**3** is a multiple of 3 and an odd number, hence **Matrix**.

For Test case 3:

**4** is not a multiple of 3, but is only even; hence **Reality**.

For Test case 4:

**5**  is not a multiple of 3, but is an odd number; hence **Glitch**.

For Test case 5:

**6** is a multiple of 3 and also an even number; hence **Zion**.

For Test case 6:

**7** is not a multiple of 3, but is an odd number; hence **Glitch**.
