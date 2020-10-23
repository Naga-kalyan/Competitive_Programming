# Monkey Power
There are n trees in a row and you have been given the height of these trees. On each tree there is one monkey and each monkey have particular power to climb the tree. Power of each monkey can be calculated as π(x). Where x is the total number of maximum consecutive trees (I.e. to the left of the current tree including itself also) which has height less than or equal to the height of the current tree. Print the maximum power that can be obtained among n monkeys. Here π(x) can be stated as: - π(x)=(x)∗(x−1)∗(x−2)∗….............1.

You have to answer t independent test cases.
<br>Output the answer modulo 10^9+7.
<br>The input/output is quite large, please use fast reading and writing methods.

#### Input
The first line of the input contains a single integer t test cases. Each description contains two lines: The first line contains a single integer n — the number of trees. The second line contains n integers height of trees.

#### Output
Print one line answer to modulo 10^9+7.

### Constraints: -
1<=T<=100
<br>1<=n<=10^5
<br>1<=height<=10^9

### Sample input: -
```
1
6
6 4 12 3 6 7
```

### Output: -
```
6
```

### EXPLANATION:-
For the first tree smaller or equal to itself to the left is only none. So, for the first monkey power will be π(1) =1. For the second tree smaller or equal to its left is none so π(1)=1.For the third tree the tree which is smaller or equal to its left is π(3)=6.And similarly for the rest of the trees.
