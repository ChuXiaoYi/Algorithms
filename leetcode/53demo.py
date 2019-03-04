# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/4 上午11:27
#       @Author  : cxy =.= 
#       @File    : 53demo.py
#       @Software: PyCharm
#       @Desc    : 53. 最大子序和    https://leetcode-cn.com/problems/maximum-subarray/
# ---------------------------------------------
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_value = nums[0]
        sum_value = 0
        for i in range(len(nums)):
            sum_value = max(sum_value + nums[i], nums[i])
            max_value = max(sum_value, max_value)
        return max_value
