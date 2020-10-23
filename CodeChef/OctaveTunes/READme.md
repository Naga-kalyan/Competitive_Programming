Raj loves to listen to songs in his free time. It’s his birthday tomorrow and his friend Neelansh wants his gift to be the most unique. Being great at making music, he decides to produce a song for him. However, Raj likes songs according to their beauty. He determines the beauty of the song as the number of times all the octave musical tones are completed in ascending order.
<br>He begins with a jumbled tone of length N and numbers each octave tone as 1,2,3….8.
<br>Neelansh wants to maximize the beauty of the song but since he uses the trial version of the software,

* He cannot change the size of N.
* He cannot introduce any new tone, but can choose any two tones and swap their positions

However, Neelansh just received a mail that he needs to submit all his pending assignments by tomorrow. He has tons of assignments left to do, but he doesn’t want to spoil the idea of his gift. Can you help him?

#### INPUT
* The first line contains a single integer T- the number of test cases
* The first line of each test case contains a single integer N- the length of the song
* The second line contains N- space separated integers ai, ai+1,.....aN

#### OUTPUT
For each test case, print a single line containing one integer- the maximum possible beauty of the song

### CONSTRAINTS
1<=T<=102
<br>1<=N<=105
<br>1<=a<=8

### EXAMPLE INPUT
```
2
8
1 2 3 4 5 6 7 8
16
1 2 1 2 3 3 4 4 5 5 6 6 7 8 7 8
```
EXAMPLE OUTPUT
```
1
2
```
