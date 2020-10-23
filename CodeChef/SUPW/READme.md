# SUPW
In ICO School, all students have to participate regularly in SUPW. There is a different SUPW activity each day, and each activity has its own duration. The SUPW schedule for the next term has been announced, including information about the number of minutes taken by each activity.

Nikhil has been designated SUPW coordinator. His task is to assign SUPW duties to students, including himself. The school's rules say that no student can go three days in a row without any SUPW duty.

Nikhil wants to find an assignment of SUPW duty for himself that minimizes the number of minutes he spends overall on SUPW.

#### Input format
Line 1: A single integer N, the number of days in the future for which SUPW data is available.

Line 2: N non-negative integers, where the integer in position i represents the number of minutes required for SUPW work on day i.

#### Output format
The output consists of a single non-negative integer, the minimum number of minutes that Nikhil needs to spend on SUPW duties this term

### Sample Input 1
```
10
3 2 1 1 2 3 1 3 2 1
```

### Sample Output 1
```
4
```
(Explanation: 1+1+1+1)
### Sample Input 2
```
8
3 2 3 2 3 5 1 3
```
### Sample Output 2
```
5
```
(Explanation: 2+2+1)

## Test data
There is only one subtask worth 100 marks. In all inputs:
* 1 ≤ N ≤ 2×10^5
* The number of minutes of SUPW each day is between 0 and 10^4, inclusive.
