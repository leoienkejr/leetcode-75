

'''
217. Contains Duplicate

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

https://leetcode.com/problems/contains-duplicate/description/
'''

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        known_nums = set()
        for num in nums:
            if num in known_nums:
                return True
            known_nums.add(num)
        return False
