# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 下午5:11
#       @Author  : cxy =.= 
#       @File    : merge_sort.py
#       @Software: PyCharm
#       @Desc    : 归并排序，从小到大排序
# --------------------------------------


def merge_sort(li):
    """
    归并排序，使用递归
    :return:
    """
    length = len(li)
    if length <= 1:
        return li

    middle = length // 2
    left = merge_sort(li[:middle])
    right = merge_sort(li[middle:])
    return merge(left, right)


def merge(left_li, right_li):
    """
    合并左右两个列表
    :param left_li:
    :param right_li:
    :return:
    """
    result = []
    while left_li and right_li:
        if left_li[0] < right_li[0]:
            result.append(left_li.pop(0))
        else:
            result.append(right_li.pop(0))

    result.extend(left_li)
    result.extend(right_li)
    return result


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    print(merge_sort(li))
