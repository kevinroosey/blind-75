'''
242. Valid Anagram
Level: Easy

Prompt:
Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

Constraints:

1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #base case
        if len(s) != len(t):
            return False
        '''
        create a dictionary for both s and t.
        iterate through both of the strings, adding 
        character:frequency as a keyvalue pair.

        At the end, both dictionaries should be the same if they are anagrams.
        '''
        sDict, tDict = {}, {}
        for c in range(len(s)):
            sDict[s[c]] = 1 + sDict.get(s[c], 0)
            tDict[t[c]] = 1 + tDict.get(t[c], 0)
        return sDict == tDict