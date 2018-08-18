#! /usr/local/env python
# coding=utf-8

from simple_stack import *

"""
本程序使用两个栈实现一个队列

队列讲究的是先进先出(FIFO)，所以我们使用一个栈来保存进入队列，当程序需要执行出队操作时，我们需要依次取出元素到另一个栈，然后把栈底元素弹出
"""

if __name__ == '__main__':
    # 在此我们规定遇到0->出队，其他数字入队
    q = [1, 2, 0, 44, 5, 0, 6, 0, 0, 0, 0, 4, 32, 0, 0, 0, 0, 423, 4, 234, 0, 1, 23, 0]
    stack_1 = SimpleStack()
    stack_2 = SimpleStack()
    for i in q:
        if i:
            stack_1.push(i)
        else:
            node = stack_1.top
            while node.next:
                pass
