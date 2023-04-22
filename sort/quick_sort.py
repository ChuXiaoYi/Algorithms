# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 下午6:55
#       @Author  : cxy =.= 
#       @File    : quick_sort.py
#       @Software: PyCharm
#       @Desc    : 快速排序
# --------------------------------------
from util.tool import caculate_time


class QuickSort(object):
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
    def quick_sort(self):
        """
        调用入口
        :return:
        """
        self.qsort(0, len(self.list) - 1)
        return self.list

    def qsort(self, low, high):
        """
        递归调用
        :return:
        """
        if low < high:
            pivot_index = self.partition(low, high)
            self.qsort(low, pivot_index - 1)
            self.qsort(pivot_index + 1, high)

    def partition(self, low, high):
        """
        在分区中选取一个基准元素（pivot），不断的移动游标，进行替换，使得左边为全部比他小的，右边为全部比他大的；
        并且，这个pivot也变化位置，但是值不变
        :param low:
        :param high:
        :return: pivot所在的下标
        """
        li = self.list
        pivot = self.list[low]
        while low < high:
            while low < high and li[high] > pivot:
                high -= 1
            self.swap(low, high)
            while low < high and li[low] < pivot:
                low += 1
            self.swap(low, high)
        return low


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    ss = QuickSort(li)
    ss.quick_sort()
