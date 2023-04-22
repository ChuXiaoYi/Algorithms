# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 下午3:25
#       @Author  : cxy =.= 
#       @File    : shell_sort.py
#       @Software: PyCharm
#       @Desc    : 希尔排序，从小到大排序
# --------------------------------------
from util.tool import caculate_time


class ShellSort(object):
    def __init__(self, li=None):
        self.list = li

    @caculate_time
    def shell_sort(self):
        """
        希尔排序,时间复杂度O(n^(3/2))
        :return:
        """
        length = len(self.list)
        gap = length
        while gap > 1:
            gap = int(gap/3)+1
            for i in range(gap, length):
                tmp = self.list[i]
                j = i-gap
                while j >= 0 and tmp < self.list[j]:
                    self.list[j+gap] = self.list[j]
                    j = j-gap
                self.list[j+gap] = tmp
        return self.list


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    ss = ShellSort(li)
    ss.shell_sort()
