'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
...
Answer:
class Solution:
    def climbStairs(self, n: int) -> int:
        yp=1
        p1=0
        for i in range(1,n+1):
            c=yp+p1 
            p1=yp
            yp=c
        return(yp)
        
