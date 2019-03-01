# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/2/28 下午5:04
#       @Author  : cxy =.= 
#       @File    : 26demo.py
#       @Software: PyCharm
#       @Desc    : 26. 删除排序数组中的重复项  https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/solution/
# ---------------------------------------------
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        index = 1
        while index < len(nums):
            if nums[index] == nums[index - 1]:
                nums.pop(index)
            else:
                index += 1
        return index

