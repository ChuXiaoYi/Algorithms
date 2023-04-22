# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/21 上午11:56
#       @Author  : cxy =.= 
#       @File    : counting_sort.py
#       @Software: PyCharm
#       @Desc    : 计数排序
# --------------------------------------
from util.tool import caculate_time

@caculate_time
def countring_sort(arr):
    """
    通过计算arr每个元素的次数进行排序
    :param arr:
    :return:
    """
    index = 0
    max_value = max(arr)
    bucket_length = max_value + 1   # 桶的个数
    bucket = [0 for i in range(bucket_length)]

    # 桶的下标对应arr中的元素
    for i in arr:
        bucket[i] += 1

    for j in range(bucket_length):
        while bucket[j] > 0:
            arr[index] = j
            bucket[j] -= 1
            index += 1
    return arr


if __name__ == '__main__':
    arr = [6, 5, 3, 1, 8, 7, 2, 4]
    print(countring_sort(arr))
