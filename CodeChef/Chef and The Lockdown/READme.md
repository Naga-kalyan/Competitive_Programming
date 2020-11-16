# Chef and The Lockdown
The lockdown hasn’t been great for our chef as his restaurant business got sabotaged because of lockdown, nevertheless no worries our chef is a multi-talented guy. Chef has decided to be a freelancer and work remotely. According to chef’s maths, he should be able to work on maximum tasks assuming that he can only work on a single task at a time.

Assume that chef does N tasks. The start and finish time units of those tasks are given. Select the maximum number of tasks that can be performed by a chef, assuming that a he can only work on a single task at a time.

#### Input:
* The first input contains of size of array N representing the total number of tasks.
* The second and third lines contains N space-seperated integers representing the starting and finish time of the the tasks.

#### Output:
* A single line containing indices of tasks that chef will be able to do.

### Constraints
* 1 ≤ N ≤ 10^5
<br>**Note:** The lists have been sorted based on the ending times of the tasks.
### Sample Input 1:
```
3
10 12 20
20 25 30
```
### Sample Output 1:
```
0 2
```
### Sample Input 2:
```
6
1 2 0 6 3 7
2 4 5 7 9 10
```
### Sample Output 2:
```
0 1 3 5
```
