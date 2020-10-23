# Validating UID
ABCXYZ company has up to **100** employees.
<br>The company decides to create a unique identification number (UID) for each of its employees.
<br>The company has assigned you the task of validating all the randomly generated UIDs.
<br>A valid UID must follow the rules below:
* It must contain at least **2** uppercase English alphabet characters.
* It must contain at least **2** digits **(0 - 9)**.
* It should only contain alphanumeric characters **(a - z, A - Z & 0 - 9)**.
* No character should repeat.
* There must be exactly **10** characters in a valid UID.
#### Input Format

The first line contains an integer ***T***, the number of test cases.
<br>The next ***T*** lines contains an employee's UID.

#### Output Format

For each test case, print 'Valid' if the UID is valid. Otherwise, print 'Invalid', on separate lines. Do not print the quotation marks.

### Sample Input
```
2
B1CD102354
B1CDEF2354
```
### Sample Output
```
Invalid
Valid
```
## Explanation

**B1CD102354: 1** is repeating → Invalid
<br>**B1CDEF2354:** Valid
