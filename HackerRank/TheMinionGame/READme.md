# The Minion Game
Kevin and Stuart want to play the '**The Minion Game**'.

### Game Rules
Both players are given the same string, **S**.
<br>Both players have to make substrings using the letters of the string **S**.
<br>Stuart has to make words starting with consonants.
<br>Kevin has to make words starting with vowels.
<br>The game ends when both players have made all possible substrings.
### Scoring
A player gets +1 point for each occurrence of the substring in the string **S**.

### For Example:
String **S** = BANANA
<br>Kevin's vowel beginning word = ANA
<br>Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.
<br>Your task is to determine the winner of the game and their score.

#### Input Format
A single line of input containing the string .
<br>**Note:** The string  will contain only uppercase letters: **[A-Z]**.

### Constraints
* **0 < len(S) <= 10^6**

#### Output Format
Print one line: the name of the winner and their score separated by a space.
<br>If the game is a draw, print Draw.

### Sample Input
```
BANANA
```
### Sample Output
```
Stuart 12
```

#### Note :
Vowels are only defined as ***AEIOU***. In this problem,  **Y**is not considered a vowel.
