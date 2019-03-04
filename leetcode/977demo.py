# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/4 下午12:27
#       @Author  : cxy =.= 
#       @File    : 977demo.py
#       @Software: PyCharm
#       @Desc    : 977. 有序数组的平方 https://leetcode-cn.com/problems/squares-of-a-sorted-array/submissions/
# ---------------------------------------------
from typing import List


class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        return sorted([item**2 for item in A])