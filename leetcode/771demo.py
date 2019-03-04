# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/4 上午9:51
#       @Author  : cxy =.= 
#       @File    : 771demo.py
#       @Software: PyCharm
#       @Desc    : 771. 宝石与石头   https://leetcode-cn.com/problems/jewels-and-stones/
# ---------------------------------------------
# 方法一：
# class Solution:
#     def numJewelsInStones(self, J: str, S: str) -> int:
#         count = 0
#         for item in S:
#             if item in J:
#                 count += 1
#         return count

# 方法二：
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        return sum([S.count(i) for i in J])
