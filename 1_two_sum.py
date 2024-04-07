'''
1. Two Sum

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

https://leetcode.com/problems/two-sum/description/
'''

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_nums = dict()
        for i, n in enumerate(nums):
            diff = target - n
            index_for_n = index_nums.get(diff, list())
            if len(index_for_n):
                return [index_for_n.pop(), i]
            else:
                if n in index_nums:
                    index_nums[n].append(i)
                else:
                    index_nums[n] = [i]
        
