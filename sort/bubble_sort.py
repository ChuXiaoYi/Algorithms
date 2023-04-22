# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 上午10:41
#       @Author  : cxy =.= 
#       @File    : bubble_sort.py
#       @Software: PyCharm
#       @Desc    : 冒泡排序，从小到大排序
# --------------------------------------
import copy
from util.tool import caculate_time


class BubbleSort(object):
    def __init__(self, li=None):
        self.list = li

    def swap(self, li, i, j):
        """
        交换元素，i，j表示下标
        :param i:
        :param j:
        :return:
        """
        li[i], li[j] = li[j], li[i]

    @caculate_time
    def bubble_sort_simple(self):
        """
        简单冒泡排序,时间复杂度O(n^2)
        :return:
        """
        li = copy.deepcopy(self.list)
        length = len(li)
        for i in range(length):
            for j in range(i + 1, length):
                if li[i] > li[j]:
                    self.swap(li, i, j)
        return li

    @caculate_time
    def bubble_sort(self):
        """
        冒牌排序，时间复杂度O(n^2)
        :return:
        """
        li = copy.deepcopy(self.list)
        length = len(li)
        for i in range(length):
            for j in range(length - 1 - i):
                if li[j] > li[j + 1]:
                    self.swap(li, j, j + 1)
        return li

    @caculate_time
    def bubble_sort_advance(self):
        """
        改进后的冒泡排序，时间复杂度O(n^2)
        设置一个flag，当某一轮没有发生变化时，证明排序已经有序了
        :return:
        """
        li = copy.deepcopy(self.list)
        length = len(li)
        for i in range(length):
            flag = True
            for j in range(length - 1 - i):
                if li[j] > li[j + 1]:
                    self.swap(li, j, j + 1)
                    flag = False
            if flag:
                break
        return li


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    bs = BubbleSort(li)
    bs.bubble_sort_simple()
    bs.bubble_sort()
    bs.bubble_sort_advance()
