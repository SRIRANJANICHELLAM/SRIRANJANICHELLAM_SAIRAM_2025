You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, .

Constraints

The string consists of alphanumeric characters and spaces.
Note: in a word only the first character is capitalized. Example 12abc when capitalized remains 12abc.

Output Format

Print the capitalized string, .

Sample Input

chris alan
Sample Output

Chris Alan
Contest ends in 17 hours
Submissions: 82
Max Score: 10
Difficulty: Easy
Rate This Challenge:

1
2
​
3
import math
4
import os
5
import random
6
import re



SOLUTION:


def solve(ps):
    words = ps.split(' ')
    cp = (((i.capitalize() for i in words)))
    return ' '.join(cp)