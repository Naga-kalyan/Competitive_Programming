# FIZZA and MAGICIAN
Fizza is a cute girl and she wants to be more beautiful. So she approached a magician to increase her beauty magically. But the magician's glasses accidently got locked inside the locker and he forgot the password. Without glasses he can't help her. The password is hidden in N integers i.e. **a[1],a[2],.....a[N]** written on his magical stick.The password is the maximum number of moves Fizza can perform, for any position i such that **1 < = i < = N** and integer **X** is present at i-th position. In one move she can perform one of the following operations ->

(1) If ( i + 1 < = N ) she can go to position (i + 1 ) if integer at ( i + 1 )-th position is equal to **X**.

(2) if ( i + 2 < = N ) she can go to position (i + 2 ) if integer at (i + 2)-th position is equal to **X**. Fizza is a bit worried about her beauty so she can't focus on the problem but she asked for your help to find the password.

#### Input:
* First line will contain T, number of testcases. Then the testcases follow.
* Each testcase consists of two lines of input.
* Input N.
* Input N integers .

#### Output:
For each testcase, output in a single line Maximum number of moves.

### Constraints
* 1 ≤ T ≤ 100
* 1 ≤ N ≤ 10^5
* 1 ≤ a[i] ≤ 2∗10^5

### Sample Input:
```
3
8
6 3 6 4 5 4 3 6
9
5 5 4 5 2 1 3 4 2
6
1 2 3 4 5 6
```

### Sample Output:
```
1
2
0
```

### EXPLANATION:
In the first case, integers at position 1 and 3 are the same and at alternate positions. In the second case, integers at position 1, 2, 4 follow the conditions.
