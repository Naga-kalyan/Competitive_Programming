# Chef Is Just Throwing Random Words
Chef once had a deep epiphany and ended up saying: Given a sequence of positive integers a1,a2,…,aN, if you take each of its 2N subsequences and write down the sum of elements of this subsequence, what will the bitwise OR of the written integers be?

Yes, you read it right, but can you solve it?

#### Input
* The first line of the input contains a single integer T denoting the number of test cases. The description of T test cases follows.
* The first line of each test case contains a single integer N.
* The second line contains N space-separated integers a1,a2,…,aN.

#### Output
* For each test case, print a single line containing one integer ― the bitwise OR of sums of all subsequences.

### Constraints
* 1 ≤ T ≤ 5
* 1 ≤ N ≤ 10^5
* 1 ≤ a_i < 2^30 for each valid i

### Example Input
```
2
2
1 1
3
1 9 8
```

### Example Output
```
3
27
```
