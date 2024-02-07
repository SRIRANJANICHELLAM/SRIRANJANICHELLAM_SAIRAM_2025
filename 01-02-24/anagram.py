'''
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true
'''
answer:
class Solution:
    def isAnagram(self, a: str, tp: str) -> bool:
        if len(a) != len(tp):
            return False
        count = collections.Counter(a)
        count.subtract(collections.Counter(tp))
        return all(freq == 0 for freq in count.values())
