# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 下午1:49
#       @Author  : cxy =.= 
#       @File    : select_sort.py
#       @Software: PyCharm
#       @Desc    : 选择排序，从小到大排序
# --------------------------------------
from util.tool import caculate_time


class SelectSort(object):
    def __init__(self, li=None):
        self.list = li

    def swap(self, i, j):
        """
        交换元素，i，j表示下标
        :param i:
        :param j:
        :return:
        """
        self.list[i], self.list[j] = self.list[j], self.list[i]

    @caculate_time
    def select_sort_simple(self):
        """
        选择排序,时间复杂度O(n^2)
        :return:
        """
        length = len(self.list)
        for i in range(length):
            min_index = i
            for j in range(i+1, length):
                if self.list[min_index] > self.list[j]:
                    min_index = j
            self.list[i], self.list[min_index] = self.list[min_index], self.list[i]
        return self.list


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    ss = SelectSort(li)
    ss.select_sort_simple()
