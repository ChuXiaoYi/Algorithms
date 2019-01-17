# -*- coding: utf-8 -*-
# --------------------------------------
#       @Time    : 2019/1/17 上午10:58
#       @Author  : cxy =.= 
#       @File    : tool.py
#       @Software: PyCharm
#       @Desc    : 
# --------------------------------------
import datetime
from functools import wraps


def caculate_time(func):
    @wraps(func)
    def add_time(*args):
        start = datetime.datetime.now()
        result = func(*args)
        end = datetime.datetime.now()
        print("{}花费：{}ms".format(func.__name__, (end - start).microseconds))
        print("排序后结果：", end="")
        print(result)
        return result

    return add_time
