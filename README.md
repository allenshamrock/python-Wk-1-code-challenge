
Challenges README


Challenge 1

Description

Given N boxes arranged in a row, each containing a certain number of bricks, the task is to determine the minimum number of moves needed to distribute the bricks such that each box contains exactly 10 bricks. In one move, you can take one brick from a box and move it to a neighboring box (either left or right).

Example

For example, if the initial arrangement of boxes is [9, 12, 8, 15, 10], the minimum number of moves needed would be 8.

Solution

The solution involves iteratively moving bricks from boxes with excess bricks to boxes with fewer bricks, ensuring that each box has exactly 10 bricks. The algorithm could be implemented efficiently using a greedy approach.

Challenge 2


Description

Write a function solution(A) that takes an array A of N integers as input and returns the maximum sum of two numbers whose digits add up to an equal sum. If no two numbers in the array have digits with an equal sum, the function should return -1.

Example

For instance, if the input array is [51, 71, 17, 42], the function should return 93, as 51 + 42 gives the maximum sum (93) among pairs of numbers with digits adding up to an equal sum.

Solution

The solution involves iterating through the array, calculating the sum of digits for each number, and storing them in appropriate data structures for comparison. An efficient approach could utilize hashing to track numbers with the same digit sums.

Challenge 3

Description

Write a function solution(N) that takes an integer N as input and returns a string of length N containing as many different lowercase letters ('a'-'z') as possible, with each letter occurring an equal number of times.

Example

For example, if N = 5, the function should return "abcde", where each letter occurs once.

Solution
The solution involves generating a string with a repeating pattern of lowercase letters such that the length of the string matches N. This can be achieved by cycling through the lowercase letters and concatenating them until the desired length is reached. If N is greater than 26, the pattern repeats.