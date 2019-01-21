
参考文档：

- [十大经典排序算法（动图演示）](https://www.cnblogs.com/onepixel/p/7674659.html)
- [基于python的七种经典排序算法](https://my.oschina.net/u/3346994/blog/895131)
- [https://github.com/TheAlgorithms/Python](https://github.com/TheAlgorithms/Python)
- [https://www.toptal.com/developers/sorting-algorithms](https://www.toptal.com/developers/sorting-algorithms)

### 算法概述
##### 算法分类
十种常见排序算法可以分为两大类：

>**非线性时间比较类排序**：通过比较来决定元素间的相对次序，由于其时间复杂度不能突破O(nlogn)，因此称为非线性时间比较类排序。

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

### 插入排序（Insertion Sort）
插入排序（Insertion-Sort）的算法描述是一种简单直观的排序算法。它的工作原理是通过构建有序序列，对于未排序数据，在已排序序列中从后向前扫描，找到相应位置并插入。插入排序在实现上，通常采用in-place排序（即只需用到O(1)的额外空间的排序），因而在从后向前扫描过程中，需要反复把已排序元素逐步向后挪位，为最新元素提供插入空间。

##### 算法描述
一般来说，插入排序都采用in-place在数组上实现。具体算法描述如下：
1. 从第一个元素开始，该元素可以认为已经被排序；
2. 取出下一个元素，在已经排序的元素序列中从后向前扫描；
3. 如果该元素（已排序）大于新元素，将该元素移到下一位置；
4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置；
5. 将新元素插入到该位置后；
重复步骤2~5。

##### 动态演示
![http://chuxiaoyi.cn/media/editor/4_20190117152003645485.gif](http://chuxiaoyi.cn/media/editor/4_20190117152003645485.gif)

##### 代码实现
```python
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
        选择排序,时间复杂度O(n^2)
        :return:
        """
        length = len(self.list)
        for i in range(1, length):
            pre = i-1
            current = self.list[i]
            while pre >= 0 and current < self.list[pre]:
                self.list[pre+1] = self.list[pre]
                pre -= 1
            self.list[pre+1] = current

        return self.list


if __name__ == '__main__':
    li = [4, 1, 7, 3, 8, 5, 9, 2, 6]
    ss = InsertSort(li)
    ss.insert_sort()
```

结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117152235170.png)

### 希尔排序（Shell Sort）
1959年Shell发明，第一个突破O(n2)的排序算法，是简单插入排序的改进版。它与插入排序的不同之处在于，它会优先比较距离较远的元素。希尔排序又叫**缩小增量排序**。

##### 算法描述
先将整个待排序的记录序列分割成为若干子序列分别进行直接插入排序，具体算法描述：
- 选择一个增量序列t1，t2，…，tk，其中ti>tj，tk=1；
- 按增量序列个数k，对序列进行k 趟排序；
- 每趟排序，根据对应的增量ti，将待排序列分割成若干长度为m 的子序列，分别对各子表进行直接插入排序。仅增量因子为1 时，整个序列作为一个表来处理，表长度即为整个序列的长度。

##### 动态演示
![http://chuxiaoyi.cn/media/editor/8_20190117180759376850.gif](http://chuxiaoyi.cn/media/editor/8_20190117180759376850.gif)

##### 代码实现
```python
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
```
结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117164732178.png)

### 归并排序（Merge Sort）
归并排序是建立在归并操作上的一种有效的排序算法。该算法是采用分治法（Divide and Conquer）的一个非常典型的应用。将已有序的子序列合并，得到完全有序的序列；即先使每个子序列有序，再使子序列段间有序。若将两个有序表合并成一个有序表，称为2-路归并。归并排序是一种稳定的排序方法。和选择排序一样，归并排序的性能不受输入数据的影响，但表现比选择排序好的多，因为始终都是O(nlogn）的时间复杂度。代价是需要额外的内存空间。
##### 算法描述
- 把长度为n的输入序列分成两个长度为n/2的子序列；
- 对这两个子序列分别采用归并排序；
- 将两个排序好的子序列合并成一个最终的排序序列。
##### 动态演示
![http://chuxiaoyi.cn/media/editor/7_20190117175952107766.gif](http://chuxiaoyi.cn/media/editor/7_20190117175952107766.gif)
##### 代码实现

```python
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
```

结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117180230724.png)

### 快速排序（Quick Sort）
快速排序（Quick Sort）由图灵奖获得者Tony Hoare发明，被列为20世纪十大算法之一。冒泡排序的升级版，交换排序的一种。快速排序的时间复杂度为O(nlog(n))。

快速排序算法的核心思想：通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，然后分别对这两部分继续进行排序，以达到整个记录集合的排序目的。
##### 算法描述
快速排序使用分治法来把一个串（list）分为两个子串（sub-lists）。具体算法描述如下：
- 从数列中挑出一个元素，称为 “基准”（pivot）；
- 重新排序数列，所有元素比基准值小的摆放在基准前面，所有元素比基准值大的摆在基准的后面（相同的数可以到任一边）。在这个分区退出之后，该基准就处于数列的中间位置。这个称为分区（partition）操作；
- 递归地（recursive）把小于基准值元素的子数列和大于基准值元素的子数列排序。
##### 动态演示
![http://chuxiaoyi.cn/media/editor/9_20190117192549821306.gif](http://chuxiaoyi.cn/media/editor/9_20190117192549821306.gif)
##### 代码实现

```python
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
```
结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190117192855484.png)

### 堆排序（Heap Sort）
堆排序在 top K 问题中使用比较频繁。堆排序是采用二叉堆的数据结构来实现的，虽然实质上还是一维数组。二叉堆是一个近似完全二叉树 。

**二叉堆具有以下性质**：

父节点的键值总是大于或等于（小于或等于）任何一个子节点的键值。
每个节点的左右子树都是一个二叉堆（都是最大堆或最小堆）。

##### 算法描述
- **构造最大堆（Build_Max_Heap）**：若数组下标范围为0~n，考虑到单独一个元素是大根堆，则从下标n/2开始的元素均为大根堆。于是只要从n/2-1开始，向前依次构造大根堆，这样就能保证，构造到某个节点时，它的左右子树都已经是大根堆。

- **堆排序（HeapSort）**：由于堆是用数组模拟的。得到一个大根堆后，数组内部并不是有序的。因此需要将堆化数组有序化。思想是移除根节点，并做最大堆调整的递归运算。第一次将heap[0]与heap[n-1]交换，再对heap[0...n-2]做最大堆调整。第二次将heap[0]与heap[n-2]交换，再对heap[0...n-3]做最大堆调整。重复该操作直至heap[0]和heap[1]交换。由于每次都是将最大的数并入到后面的有序区间，故操作完后整个数组就是有序的了。

- **最大堆调整（Max_Heapify）**：该方法是提供给上述两个过程调用的。目的是将堆的末端子节点作调整，使得子节点永远小于父节点 。

##### 动态演示
![http://www.chuxiaoyi.cn/media/editor/2_20190121113614440245.gif](http://www.chuxiaoyi.cn/media/editor/2_20190121113614440245.gif)

##### 代码实现
```python
# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/18 下午2:48
#       @Author  : cxy =.=
#       @File    : heap_sort.py
#       @Software: PyCharm
#       @Desc    : 堆排序
# --------------------------------------


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
```
结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190121113641271.png)

### 计数排序（Counting Sort）
计数排序不是基于比较的排序算法，其核心在于将输入的数据值转化为键存储在额外开辟的数组空间中。 作为一种线性时间复杂度的排序，计数排序要求输入的数据必须是有确定范围的整数。计数排序是一个稳定的排序算法。当输入的元素是 n 个 0到 k 之间的整数时，时间复杂度是O(n+k)，空间复杂度也是O(n+k)，其排序速度快于任何比较排序算法。当k不是很大并且序列比较集中时，计数排序是一个很有效的排序算法。

##### 算法描述
- 找出待排序的数组中最大元素；
- 统计数组中每个值为i的元素出现的次数，存入数组C的第i项；
- 反向填充目标数组：将每个元素i放在新数组的第C(i)项，每放一个元素就将C(i)减去1。

##### 动态演示
![http://www.chuxiaoyi.cn/media/editor/3_20190121131026884154.gif](http://www.chuxiaoyi.cn/media/editor/3_20190121131026884154.gif)

##### 代码实现
```python
# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/21 上午11:56
#       @Author  : cxy =.=
#       @File    : counting_sort.py
#       @Software: PyCharm
#       @Desc    : 计数排序
# --------------------------------------


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
```

结果：

![在这里插入图片描述](https://img-blog.csdnimg.cn/20190121131202835.png)