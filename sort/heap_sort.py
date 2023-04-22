# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/18 下午2:48
#       @Author  : cxy =.= 
#       @File    : heap_sort.py
#       @Software: PyCharm
#       @Desc    : 堆排序
# --------------------------------------
from util.tool import caculate_time

@caculate_time
def heap_sort(arr):
    """
    构造大根堆，堆排序
    每次堆排序之后，都要进行最大根堆调整，使得堆顶为最大值
    :param arr:
    :return:
    """
    n = len(arr)
    first = n // 2 - 1  # 最后一个非叶子节点
    # 第一次构造大根堆
    for start in range(first, -1, -1):
        max_heapify(arr, start, n - 1)
    for end in range(n - 1, 0, -1):
        arr[end], arr[0] = arr[0], arr[end]
        max_heapify(arr, 0, end - 1)
    return arr


def max_heapify(arr, start, end):
    """
    最大根堆调整
    :param arr:
    :param start: 表示非叶子节点（也就是每个小分支的根节点）
    :param end: 边界下标
    :return:
    """
    root = start
    while True:
        child = root * 2 + 1
        if child > end:
            break
        elif child + 1 <= end and arr[child] < arr[child + 1]:
            child = child + 1  # 保证child为最大的子节点
        if arr[root] < arr[child]:
            arr[root], arr[child] = arr[child], arr[root]
        else:
            break


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    print(heap_sort(arr))
