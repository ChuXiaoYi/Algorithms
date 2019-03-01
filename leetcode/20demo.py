# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/2/28 下午2:38
#       @Author  : cxy =.= 
#       @File    : 20demo.py
#       @Software: PyCharm
#       @Desc    : 20. 有效的括号 https://leetcode-cn.com/problems/valid-parentheses/
# ---------------------------------------------

def is_valid(s: str) -> bool:
    stack = []
    mapping = {
        '}': '{',
        ')': '(',
        ']': '['
    }
    for char in s:
        if char in mapping:
            top = stack.pop() if stack else None
            if top != mapping[char]:
                return False
        else:
            stack.append(char)

    return not stack

if __name__ == '__main__':
    s = "{[]}"
    print(is_valid(s))

