# Empire Business
*“Jesse, you asked me if I was in the meth business, or the money business… Neither. I’m in the empire business.”*

Walter’s sold his stack in Gray Matter Technologies, a company which he deserved half a credit, for peanuts. Now this company is worth a billion dollar company. Walter wants to get it's shares to have his Empire Business back and he founds an opportunity.

There are N persons having shares A1,A2,A3,…AN in this company. Walter can buy these shares with their minimum Sold Values.

Sold Values of a person's share i (1 ≤ i ≤ N) with another person's share j (1 ≤ j ≤ N) is equal to A_j+|i−j|. So, a person's share can have N possible sold values and Walter has to find minimum sold value among them for each person.

Since Walter has to run his meth business also he asks you to find minimum sold value for each person.

#### Input:
* First line will contain T, number of test cases. Then the testcases follow.
* The First line of each test case contains a integer N.
* The Second line of each test case contains N space integers namely A1,A2,…AN.

#### Output:
For each test case, output in single line N space integers denoting minimum sold value for each person.

### Constraints
* 1 ≤ T ≤ 10^5
* 1 ≤ N ≤ 2∗10^6
* 1 ≤ A_i ≤ 10^9
<br>Sum of N over all test cases will not exceed 2∗10^6.

### Sample Input:
```
2
5
6 5 5 5 2
5
1 2 3 4 5
```

### Sample Output:
```
6 5 4 3 2
1 2 3 4 5
```
## Explanation
**For first case:**

Sold value for index 1: 6, 6, 7, 8, 6
<br>Sold value for index 2: 7, 5, 6, 7, 5
<br>Sold value for index 3: 8, 6, 5, 6, 4
<br>Sold value for index 4: 9, 7, 6, 5, 3
<br>Sold value for index 5: 10, 8, 7, 6, 2
<br>Minimum sold value for each index will be 6, 5, 4, 3, 2.
