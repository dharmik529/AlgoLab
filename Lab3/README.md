# CMPSC 413 - Lab 3 
## Pattern Matching Algorithms

### Exercise 1: Naive Patter Matching 
**Naive pattern matching:**

Slide the pattern over text one index by one and check for a match. If a match is found, then slides by 1 again to check for subsequent matches.

**Given a text and a pattern, write a function search which takes a text and a pattern as inputs and prints all occurrences of the pattern in the text i.e., each of their start index. If there is no pattern, return -1. Assume that the length of the text is greater than the pattern**

**Write a pseudocode or an algorithm, explain your algorithm and perform the time complexity.** You can implement the algorithm in python or in Java. You cannot use a library to implement this algorithm.

Make the following function calls the following inputs:
```
Input-1: txt1[] = "This is a CMPSC 412 lab course. Students take this course along with CMPSC 462"
    Pat1[] = "CMPSC"
Output: Patterns found at index 10 and index _

Input-2: txt1[] = "This is a CMPSC 412 lab course. Students take this course alongcwith CMPSC 462"
    Pat2[] = "course"
Output: Patterns found at index __ and index __

Input-2: txt2[] = "AABAACAADAABAABAABBBBBAAABDCBA"
    Pat3[] = "BBBBBA"
Output: Patters found at index __
```

### Exercise 2: Knuth–Morris–Pratt (KMP) algorithm pattern matching algorithm
**KMP pattern matching**

The Naive pattern matching algorithm doesn’t work well in cases where there are many matching characters followed by a mismatching character. KMP uses an optimized approach and has a better time complexity. KMP uses Longest Proper Prefix which is Suffix (LPS).

Please find the details about the algorithm in [https://towardsdatascience.com/pattern-search-with-the- knuth-morris-pratt-kmp-algorithm-8562407dba5b](https://towardsdatascience.com/pattern-search-with-the- knuth-morris-pratt-kmp-algorithm-8562407dba5b)

**Given a text and a pattern, write a function search which takes a text and a pattern as inputs and prints all occurrences of the pattern in the text i.e., each of their start index.** If there is no pattern, return -1. Assume that the length of the text is greater than the pattern.

**Write a pseudocode or an algorithm, explain your algorithm and perform the time complexity.** You can implement the algorithm in python or in Java. You cannot use a library to implement this algorithm.

Make the following function calls the following inputs:
```
Input-1: txt1[] = "This is a CMPSC 412 lab course. Students take this course along with CMPSC 462"
    Pat1[] = "CMPSC"
Output: Patterns found at index 10 and index _

Input-2: txt1[] = "This is a CMPSC 412 lab course. Students take this course along with CMPSC 462"
    Pat2[] = "course"
Output: Patterns found at index __ and index __

Input-2: txt2[] = "AABAACAADAABAABAABBBBBAAABDCBA"
    Pat3[] = "BBBBBA"
Output: Patters found at index __
```

### Conclusion
Make sure to write a conclusion paragraph discussing your understanding about this exercise.

Deliverables:
- Report with appropriate screenshots of code snippets and results, comments/explanation and conclusion.
- 3-4 minutes Zoom video recording discussing your understanding about exercise-1 and 2. Run and show the demonstration of both exercise 1 and 2.

