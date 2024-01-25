'''
Given a number N reverse the number and print it.

Example 1: Input: N = 123 Output: 321 Explanation: The reverse of 123 is 321

Example 2: Input: N = 234 Output: 432 Explanation: The reverse of 234 is 432

Input Format

123

Constraints

N <= 1000

Output Format

321

Sample Input 0
'''

Answer:


def reverse(np):
    return int(str(np)[::-1])
nN = int(input())
if nN <= 10000:
    r_nN = reverse(nN)
    print(r_nN)
else:
    print("Input value exceeds the constraint (nN <= 1000).")
