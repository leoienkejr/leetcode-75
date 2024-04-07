'''
238. Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

https://leetcode.com/problems/product-of-array-except-self/description/
'''

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l_ptr = 0
        r_ptr = len(nums) - 1
        forward_cumulative_product = []
        backward_cumulative_product = []

        while (l_ptr < len(nums)) and (r_ptr >= 0):
            if l_ptr == 0:
                forward_cumulative_product.append(nums[l_ptr])
            else:
                forward_cumulative_product.append(
                    nums[l_ptr] * forward_cumulative_product[l_ptr - 1]
                )

            if r_ptr == len(nums) - 1:
                backward_cumulative_product.insert(0, nums[r_ptr])
            else:
                backward_cumulative_product.insert(0, 
                    nums[r_ptr] * backward_cumulative_product[0]
                )
            
            l_ptr += 1
            r_ptr -= 1

        result = []
        for i in range(len(nums)):
            if (i > 0) and (i < len(nums) - 1):
                result.append(forward_cumulative_product[i-1] * backward_cumulative_product[i+1])
            elif i == 0:
                result.append(backward_cumulative_product[i+1])
            elif i == len(nums) - 1:
                result.append(forward_cumulative_product[i-1])

        return result
