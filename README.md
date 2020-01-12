# Daily-Coding-Problem
Solutions to problems I could solve :P

<1> Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
    For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
    Bonus: Can you do this in one pass?

<2> Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers     in the original array except the one at i.
    For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the       expected output would be [2, 3, 6].
    Follow-up: what if you can't use division?

<4> Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the         lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.
    For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
    You can modify the input array in-place.

<58> Implement a queue using two stacks. Recall that a queue is a FIFO (first-in, first-out) data structure with the following methods:      enqueue, which inserts an element into the queue, and dequeue, which removes it.

<60> Given a multiset of integers, return whether it can be partitioned into two subsets whose sums are the same.
     For example, given the multiset {15, 5, 20, 10, 35, 15, 10}, it would return true, since we can split it up into
     {15, 5, 10, 15, 10} and {20, 35}, which both add up to 55

<61> Implement integer exponentiation. That is, implement the pow(x, y) function, where x and y are integers and returns x^y.
     Do this faster than the naive method of repeated multiplication.
     For example, pow(2, 10) should return 1024.
    
<68> On our special chessboard, two bishops attack each other if they share the same diagonal. This includes bishops that have another        bishop located between them, i.e. bishops can attack through pieces. You are given N bishops, represented as (row, column) tuples        on a M by M chessboard. Write a function to count the number of pairs of bishops that attack each other. The ordering of the pair        doesn't matter: (1, 2) is considered the same as (2, 1).
     You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.
   
<69>. Given a list of integers, return the largest product that can be made by multiplying any three integers.
      For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
      You can assume the list has at least three integers.
    
<70>. A number is considered perfect if its digits sum up to exactly 10. Given a positive integer n, return the n-th perfect number.
      For example, given 1, you should return 19. Given 2, you should return 28.
    
<71>. Using a function rand7() that returns an integer from 1 to 7 (inclusive) with uniform probability, implement a function rand5()         that returns an integer from 1 to 5 (inclusive).

<73>. Given the head of a singly linked list, reverse it in-place.

<74>. Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is
      (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed). Given integers N and X, write a function that returns the number of           times X appears as a value in an N by N multiplication table.

<75>. Given an array of numbers, find the length of the longest increasing subsequence in the array. The subsequence does not                 necessarily have to be contiguous.
      For example, given the array [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15], the longest increasing subsequence has 
      length 6: it is 0, 2, 6, 9, 11, 15.

<76>. You are given an N by M 2D matrix of lowercase letters. Determine the minimum number of columns that can be removed to ensure that       each row is ordered from top to bottom lexicographically. That is, the letter at each column is lexicographically later as you go       down each row. It does not matter whether each row itself is ordered lexicographically.

<78>. Given k sorted singly linked lists, write a function to merge all the lists into one sorted singly linked list.

<81>. Given a mapping of digits to letters (as in a phone number), and a digit string, return all possible letters the number could represent. You can assume each valid number in the mapping is a single digit.
For example if {“2”: [“a”, “b”, “c”], 3: [“d”, “e”, “f”], …} then “23” should return [“ad”, “ae”, “af”, “bd”, “be”, “bf”, “cd”, “ce”, “cf"].

<88>. Implement division of two positive integers without using the division, multiplication, or modulus operators. Return the quotient as an integer, ignoring the remainder.

<90>. Given an integer n and a list of integers l, write a function that randomly generates a number from 0 to n-1 that isn't in l (uniform).

<92>. We're given a hashmap associating each courseId key with a list of courseIds values, which represents that the prerequisites of courseId are courseIds. Return a sorted ordering of courses such that we can finish all courses.
Return null if there is no such ordering.
For example, given {'CSC300': ['CSC100', 'CSC200'], 'CSC200': ['CSC100'], 'CSC100': []}, should return ['CSC100', 'CSC200', 'CSCS300'].

<155>. Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0))
You can assume that such element exists. For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

<157>. Given a string, determine whether any permutation of it is a palindrome. For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.

<158>. You are given an N by M matrix of 0s and 1s. Starting from the top left corner, how many ways are there to reach the bottom right corner?
You can only move right and down. 0 represents an empty space while 1 represents a wall you cannot walk through.
For example, given the following matrix:
[[0, 0, 1],
 [0, 0, 1],
 [1, 0, 0]]
Return two, as there are only two ways to get to the bottom right:
Right, down, down, right
Down, right, down, right
The top left corner and bottom right corner will always be 0.

<159>. Given a string, return the first recurring character in it, or null if there is no recurring character. For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

<194>. Suppose you are given two lists of n points, one list p1, p2, ..., pn on the line y = 0 and the other list q1, q2, ..., qn on the line y = 1. Imagine a set of n line segments connecting each point pi to qi. Write an algorithm to determine how many pairs of the line segments intersect.

<195>. Let A be an N by M matrix in which every row and every column is sorted. Given i1, j1, i2, and j2, compute the number of elements of M smaller than M[i1, j1] and larger than M[i2, j2]. For example, given the following matrix:
[[1, 3, 7, 10, 15, 20], [2, 6, 9, 14, 22, 25], [3, 8, 10, 15, 25, 30], [10, 11, 12, 23, 30, 35], [20, 25, 30, 35, 40, 45]]
And i1 = 1, j1 = 1, i2 = 3, j2 = 3, return 14 as there are 14 numbers in the matrix smaller than 6 or greater than 23.

<198>. Given a set of distinct positive integers, find the largest subset such that every pair of elements in the subset (i, j) satisfies either i % j = 0 or j % i = 0.
For example, given the set [3, 5, 10, 20, 21], you should return [5, 10, 20]. Given [1, 3, 6, 24], return [1, 3, 6, 24].



