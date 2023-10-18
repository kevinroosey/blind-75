'''
125. Valid Palindrome

Level: Easy

A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.

 

Example 1:

Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.
Example 2:

Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
Example 3:

Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''
class Solution:
    '''
    1. Set two variables as pointers. 
    2. loop through s while the left pointer is less than the right pointer
    3. check if both pointers are alphanumeric
    4. check if characters are the same, if not, return false
    '''
    def isPalindrome(self, s: str) -> bool:
        i = 0
        k = len(s) - 1

        while i < k:
            if s[i].isalnum() != True:
                i += 1
                continue
            elif s[k].isalnum() != True:
                k -= 1
                continue
            if s[i].lower() != s[k].lower():
                return False
            i += 1
            k -= 1
        
        return True

        
            
        