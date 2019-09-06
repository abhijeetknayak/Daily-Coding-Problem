# Daily-Coding-Problem
Solutions to problems I could solve :P
1. Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
   For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
   Bonus: Can you do this in one pass?

2. Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in      the original array except the one at i.
   For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the          expected output would be [2, 3, 6].
   Follow-up: what if you can't use division?

4. Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest      positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
   For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
   You can modify the input array in-place.

61. Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
    Do this faster than the naive method of repeated multiplication.
    For example, pow(2, 10) should return 1024.
    
68. On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another           bishop located between them, i.e. bishops can attack through pieces. You are given N bishops, represented as (row, column) tuples on       a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair             doesn't matter: (1, 2) is considered the same as (2, 1).
    You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
   
69. Given a list of integers, return the largest product that can be made by multiplying any three integers.
    For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
    You can assume the list has at least three integers.
    
70. A number is considered perfect if its digits sum up to exactly 10. Given a positive integer n, return the n-th perfect number.
    For example, given 1, you should return 19. Given 2, you should return 28.
    
71. Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5() that       returns an integer from 1 to 5 (inclusive).
