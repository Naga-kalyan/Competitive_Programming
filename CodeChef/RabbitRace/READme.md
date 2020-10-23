# Rabbit Race
2 rabbits A and B are having a hopping race along a straight path of n tiles, labelled with 0's and 1's.
<br>Each rabbit will hop a certain distance every jump. The stride values(ie hop length) for A and B are given as s1 and s2 respectively. (distance between consecutive 2 tiles = 1 hop length)
<br>Similarly, rabbit A and B will also have hp1 and hp2 as their health points.

The race will proceed with A and B hopping alternatively, starting from A. But there are certain rules to the race.
<br>Every time the rabbit lands on a tile labelled 0 he will lose 5hp, and will receive a penalty of being unable to hop for the following move.
<br>To win a rabbit must reach the end first, or the other rabbit must lose all hp
<br>The rabbit wins if he reaches the end of the race first, or if the other rabbit loses all hp before he does.

#### Note:
* The end of the race is reaching the last tile and not crossing it
* In a case where stride value > (distance of last tile from the start - distance of rabbit from the start) the stride value will equal distance of last tile from the start - distance of rabbit from the start
* In a situation where the leading rabbit hits the last tile and reaches 0hp simultaneously, he wins

### Input:
* The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.
* The first line of each test case contains five integers **n, s1, s2, hp1, hp2** respectively.
* The following line will have n space separated integers (0's and 1's) denoting the configuration of tiles from start to end.

### Output:
For each test case output a single line containing 1 character and a space separated integer, where character is the name of the winning rabbit (A/B) followed by an integer representing the absolute distance between the 2 players

### Constraints
1 <= T <= 1500
<br>1 <= n <= 103
<br>1 <= s1, s2 <= 10
<br>1 <= hp1, hp2 <= 1250

#### Example Input:
```
2
9 2 3 10 10
1 0 1 0 1 0 0 1 1
16 5 10 20 20
0 1 1 1 0 1 0 1 0 0 1 1 0 1 1 0
```

#### Example Output:
```
A 0
B 5
```

### Explanation:
Explanation will be a timeline represented from tile zero till the race stops (where the array positions are mentioned on the basis of 0 indexing)

## Case 1:
<br>A: 0 --> hp1: 10
<br>B: 0 --> hp2: 10
<br>A: 2 --> hp1: 10
<br>B: 3 --> hp2: 5
<br>A: 4 --> hp1: 10
<br>B: 3 --> hp2: 5
<br>A: 6 --> hp1: 5
<br>B: 6 --> hp2: 0
<br>**Answer:** A 0

## Case 2:
<br>A: 0 --> hp1: 15
<br>B: 0 --> hp2: 15
<br>A: 0 --> hp1: 15
<br>B: 0 --> hp2: 15
<br>A: 5 --> hp1: 15
<br>B: 10 --> hp2: 15
<br>A: 10 --> hp1: 15
<br>B: 15 --> END
<br>**Answer:** B 5
