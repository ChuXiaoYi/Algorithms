# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 下午2:21
#       @Author  : cxy =.= 
#       @File    : insert_sort.py
#       @Software: PyCharm
#       @Desc    : 插入排序，从小到大排序
# --------------------------------------
from util.tool import caculate_time


class InsertSort(object):
    def __init__(self, li=None):
        self.list = li

    @caculate_time
    def insert_sort(self):
        """
        插入排序,时间复杂度O(n^2)
        :return:
        """
        length = len(self.list)
        for i in range(1, length):
            pre = i-1
            current = self.list[i]
            while pre >= 0 and current > self.list[pre]:
                self.list[pre+1] = self.list[pre]
                pre -= 1
            self.list[pre+1] = current

        return self.list


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    ss = InsertSort(li)
    ss.insert_sort()
