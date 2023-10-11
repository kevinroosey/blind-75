'''
217. Contains Duplicate
Level: Easy

Prompt:
Given an integer array nums, return true if any value appears at least 
twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:
1 <= nums.length <= 105
-109 <= nums[i] <= 109
'''


class Solution(object):
    '''
    Make use of the fact that dictionaries cannot contain duplicate keys.
    Each value of nums gets assigned a key. If, at the end of the traversal, 
    the hashmap AND the nums list are the same length there are no duplicates, and vice versa.
    '''
    def containsDuplicate(self, nums):
        hashmap = {}
        for n in range(len(nums)):
            hashmap[nums[n]] = n
        return len(hashmap) != len(nums)