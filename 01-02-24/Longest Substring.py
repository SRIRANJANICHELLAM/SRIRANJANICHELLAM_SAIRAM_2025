'''
Given a string s, find the length of the longest 
substring
 without repeating characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        m = 0
        dict = {}
        p,j = 0,0
        n = len(s)
        while(j < n):
            c = s[j]               
            dict[c] = 1 if not c in dict else dict[c] + 1                      
            if dict[c] > 1:
                while(dict[c] > 1):
                    dict[s[p]] -= 1
                    p += 1                    
            m = max(m, j - p + 1)
            j += 1
        return m
