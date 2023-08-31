# CMPSC 413 - Lab1
## Algorithm Analysis

### Exercise 1
__Code and analyze (time complexity – algorithm analysis) to compute the greatest common divisor (GCD)
of two numbers.__

The time complexity of Euclid's GCD algorithm that I implemented is O(log(min(int1, int2))), where int1 and int2 are the two integers for which you are trying to find the greatest common divisor. This is because the algorithm repeatedly divides the larger number by the smaller number until the remainder is zero, and the number of times this division must be performed is logarithmic in the smaller of the two numbers.

```python
    gcd = lambda int1, int2: int1 if int2 == 0 else gcd(int2, int1 % int2)

    int1 : int
    int2 : int

    int1 = int(input('Enter first integer: '))
    int2 = int(input('Enter second integer: '))

    print(gcd(int1, int2))

```
__Output__
```
    Enter first integer: 48
    Enter second integer: 60
    12
```


### Exercise 2
Code and analyze (time complexity – algorithm analysis) to find maximum and minimum element from a
list (or an array). Test it with 1000 random elements and 10,000 random elements. Also, calculate the
actual CPU time it took find the minimum and maximum elements.

### Exercise 3
Write a program to find maximum and minimum element in a list (or an array) using Divide and Conquer
strategy and analyze the time complexity. Also, calculate the actual CPU time it took find the minimum
and maximum elements.

Steps to perform Divide and Conquer
1. To use divide and conquer as an algorithm design technique, you must divide the problem into two
smaller sub problems, solve each of them recursively, and then merge the two partial solutions into one
solution to the full problem.
2. Whenever the merging takes less time than solving the two sub problems, we get an efficient algorithm.
Divide-and conquer is a general algorithm design paradigm:
1. Divide: divide the input data S in two or more disjoint subsets S1, S2, ...
2. Recurrence: solve the sub problems recursively
3. Conquer: combine the solutions for S1, S2, ..., into a solution for S.
