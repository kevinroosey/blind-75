'''
128. Longest Consecutive Sequence

Level: Medium

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

 

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109

'''


class Solution(object):
    '''
    create 2 variables, longest and curr. By sorting the list, this allows us to iterate the nums list
    and check if there are any sequences. 
    '''
    def longestConsecutive(self, nums):
        if len(nums) == 0:
            return 0
        longest = 0
        curr = 0
        nums = sorted(nums)
        for n in range(len(nums) - 1):
            if nums[n + 1] == nums[n] + 1:
                curr += 1
                longest = max(longest, curr)
            elif nums[n + 1] == nums[n]:
                continue
            else:
                curr = 0
        return longest + 1


        
