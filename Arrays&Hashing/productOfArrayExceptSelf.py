'''
238. Product of Array Except Self

Level: Medium

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.


'''

class Solution:
    '''
    1. Initialize a Solution Array of same size as input array with value.
    2. Store Prefix and Postfix Product so far in variables.
    3. Traverse the input array.
    4. Before updating the values for each i, multiply current solution array value at i with the value of prefix i.e.      multiply with prefix product of the previous i-1 elements.
    5. Similarly, calculate the postfix product value for n-i-1 where n is length of input array at each iteration.
    6. As in Step 4, before calculating the postfix for i'th value , multiply the solution_array[n-i-1] with the postfix product value i.e. products of input[i+1] to input[n-1].

    '''
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        res = [1] * length 
        prefix, postfix = 1, 1
        for n in range(length):
            res[n] *= prefix
            prefix *= nums[n]
            res[(length - n) - 1] *= postfix
            postfix *= nums[(length - n) - 1] 
        return res

        