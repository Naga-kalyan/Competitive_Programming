# Processing-of-names
# DESCRIPTION
You are given a string S which contains the names of people who registered online for an event. The names are of the following format - "firstname lastname" (quotes for clarity) and are separated by a non-alphabetic sentinel character x.

Your task is to write a function retrieve_names that retrieves the names, processes them and returns a string containing the processed names separated by ’-'. 

The processing of the retrieved names must satisfy the following conditions in the given order - 

1. If the length of the first name exceeds l, then use only the first letter of the first name as the value of firstname. 
2. If a name appears more than once, then, a number (starting from 1) should be appended to each occurrence of the name. 
3. For example, if the name ‘A Das’ occurs twice, then these names should be listed as ‘A Das1’ and ‘A Das2’ in the string.
4. Only the first letter of the firstname and the lastname should be in upper-case.
5. The names should be sorted alphabetically. 
6. For example, ‘Abc Def’ should come before ‘Abc Pqr’.
7. The sorted names in the string being returned should be separated by ‘-’. 

### Description of the function retrieve_names :
* function name : retrieve_names
* parameters : 
* s - the string of names
* x - the sentinel character
* l - the maximum allowable length of the firstname)
* returned value: a string of the processed names separated by ‘-’

### Constraints
* 1 <= length of firstname or lastname <= 30
* 1 <= number of names <= 100
* 1 <= l <= 10

## Sample Test Case
The following test case describes an input to the function retrieve_names and its corresponding output.

#### Input
```
(“Sachin Tendulkar:Amitabh Bachchan:Abhishek Bachchan:Sonu Nigam”,’:’,4)
```
#### Output
```
“A Bachchan1-A Bachchan2-S Tendulkar-Sonu Nigam”
```
### Note : The sample test cases are just for the understanding purpose.



