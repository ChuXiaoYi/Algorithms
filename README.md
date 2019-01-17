# Algorithms

参考文档：

- [十大经典排序算法（动图演示）](https://www.cnblogs.com/onepixel/p/7674659.html)
- [基于python的七种经典排序算法](https://my.oschina.net/u/3346994/blog/895131)
- [https://github.com/TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)
- [https://www.toptal.com/developers/sorting-algorithms](https://www.toptal.com/developers/sorting-algorithms)

### 算法概述
##### 算法分类
十种常见排序算法可以分为两大类：

> **非线性时间比较类排序**：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此称为非线性时间比较类排序。
>**线性时间非比较类排序**：不通过比较来决定元素间的相对次序，它可以突破基于比较排序的时间下界，以线性时间运行，因此称为线性时间非比较类排序。

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117132029221.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDE1NjQ4Nw==,size_16,color_FFFFFF,t_70)

##### 算法复杂度![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117132104136.png?x-oss-process=image/watermark,type_ZmFuZ3poZW5naGVpdGk,shadow_10,text_aHR0cHM6Ly9ibG9nLmNzZG4ubmV0L3dlaXhpbl80MDE1NjQ4Nw==,size_16,color_FFFFFF,t_70)

##### 相关概念
> **稳定**：如果a原本在b前面，而a=b，排序之后a仍然在b的前面。
> **不稳定**：如果a原本在b的前面，而a=b，排序之后 a 可能会出现在 b 的后面。
> **时间复杂度**：对排序数据的总的操作次数。反映当n变化时，操作次数呈现什么规律。
> **空间复杂度**：是指算法在计算机内执行时所需存储空间的度量，它也是数据规模n的函数。

### 冒泡排序（Bubble sort）
冒泡排序，有时也称为下沉排序，是一种简单的排序算法，它反复遍历要排序的列表，比较每对相邻的项目，如果它们的顺序不满足条件则交换它们。 重复遍历列表，直到不需要交换，这时列表就是已排序的。其核心思想是：两两比较相邻记录的关键字，如果反序则交换，直到没有反序记录为止。

##### 算法描述
1. 比较相邻的元素。如果第一个比第二个大，就交换它们两个；
2. 对每一对相邻元素作同样的工作，从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
3. 针对所有的元素重复以上的步骤，除了最后一个；
重复步骤1~3，直到排序完成。

##### 动态演示
![http://chuxiaoyi.cn/media/editor/1_20190117131748513004.gif](http://chuxiaoyi.cn/media/editor/1_20190117131748513004.gif)
##### 代码实现
```python
# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 上午10:41
#       @Author  : cxy =.=
#       @File    : bubble_sort.py
#       @Software: PyCharm
#       @Desc    : 冒泡排序，从小到大排序
# --------------------------------------
import copy
from tool import caculate_time


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
```
结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117132135480.png)
### 选择排序（Selection Sort）
选择排序(Selection-sort)是一种简单直观的排序算法。它的工作原理：首先在未排序序列中找到最小（大）元素，存放到排序序列的起始位置，然后，再从剩余未排序元素中继续寻找最小（大）元素，然后放到已排序序列的末尾。以此类推，直到所有元素均排序完毕。选择排序是表现最稳定的排序算法之一，因为无论什么数据进去都是O(n2)的时间复杂度，所以用到它的时候，数据规模越小越好。唯一的好处可能就是不占用额外的内存空间了吧。

##### 算法描述

n个记录的直接选择排序可经过n-1趟直接选择排序得到有序结果。具体算法描述如下：
- 初始状态：无序区为R[1..n]，有序区为空；
- 第i趟排序(i=1,2,3…n-1)开始时，当前有序区和无序区分别为R[1..i-1]和R(i..n）。该趟排序从当前无序区中-选出关键字最小的记录 R[k]，将它与无序区的第1个记录R交换，使R[1..i]和R[i+1..n)分别变为记录个数增加1个的新有序区和记录个数减少1个的新无序区；
- n-1趟结束，数组有序化了。

##### 动态演示
![http://chuxiaoyi.cn/media/editor/2_20190117140140131569.gif](http://chuxiaoyi.cn/media/editor/2_20190117140140131569.gif)

##### 代码实现
```python
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

```
结果：
![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117140406382.png)

