# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/2/28 下午5:44
#       @Author  : cxy =.= 
#       @File    : 27demo.py
#       @Software: PyCharm
#       @Desc    : 27. 移除元素 https://leetcode-cn.com/problems/remove-element/submissions/
# ---------------------------------------------
from typing import List
from util.tool import caculate_time

class Solution:

    @caculate_time
    def removeElement(self, nums: List[int], val: int) -> int:
        index = len(nums) - 1
        while index >= 0:
            if nums[index] == val:
                nums.pop(index)
            index -= 1
        return len(nums)

if __name__ == '__main__':
    print(Solution().removeElement([3, 2, 2, 3], 3))

