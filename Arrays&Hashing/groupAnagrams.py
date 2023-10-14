'''
49. Group Anagrams

Level: Medium


Prompt: Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]

'''
class Solution:
    '''
    First, create a map. It will store our data as such:
    {"sorted(key)": ["key1", "key2", .."keyN"]}
    To populate this anagrams map, iterate through the strs List.
    At each iteration, 1. sort the current strs value. 
    2. Append the str item to the sorted word index of anagram.

    Last, use builtin .values() fn to return a list of all the values.
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = defaultdict(list)

        for s in strs:
            word_sort = ''.join(sorted(s))
            anagram[word_sort].append(s)

        return list(anagram.values())




        