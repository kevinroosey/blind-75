'''
347. Top K Frequent Elements

Level: Medium

Prompt:
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.
 

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.



'''
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        First, create a dictionary with key value of 
        value: num_occurences

        sort the dictionary from lowest occurences to highest

        iterate through the highest k elements, appending each element to the results list
        '''
        res = {} 
        final = [] #return val

        for n in range(len(nums)):
            res[nums[n]] = 1 + res[nums[n]] if nums[n] in res else 1
        res = dict(sorted(res.items(), key=lambda x:x[1]))
        
        for x in list(res)[(len(res) - k):(len(res))]:
            final.append(x)

        return final



        