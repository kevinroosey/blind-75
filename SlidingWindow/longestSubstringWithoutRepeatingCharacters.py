'''
3. Longest Substring Without Repeating Characters

Level: Medium

Prompt:

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
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.

'''
class Solution:
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set() #using a set for substring bc sets do not allow repetition

        l = 0 #create left ptr for sliding window
        longest_substring = 0 # keep track of longest
        #iterate s
        for r in range(len(s)):
            #remove elements from substring until no repeats
            while s[r] in substring:
                substring.remove(s[l])
                l += 1
            substring.add(s[r])
            longest_substring = max(longest_substring, r - l + 1)
        
        return longest_substring
    
    