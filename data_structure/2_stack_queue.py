#! /usr/local/env python
# coding=utf-8

from simple_stack import *
from random import *
from collections import Counter

"""
本程序使用两个栈实现一个队列

队列讲究的是先进先出(FIFO)，所以我们使用一个栈来保存进入队列，当程序需要执行出队操作时，我们需要依次取出元素到另一个栈，然后把栈底元素弹出

优化技巧是判断状态，减少node的移动
"""


class TwoStackQueue:
    def __init__(self, cap=None):
        # 约定左边的栈用来存储数据
        # 约定右边的栈用来存储临时数据，即出队列时保存临时生成的栈
        self.left_stack = SimpleStack(cap)
        self.right_stack = SimpleStack(cap)
        self.cap = cap

    # 重置
    def reset(self):
        self.left_stack.top = None
        self.right_stack.top = None

    # 判断一个栈是否为空
    def is_empty(self):
        if self.left_stack.is_empty() and self.right_stack.is_empty():
            return True
        return False

    # 把一个栈的内容全部压入另一个栈，可选择是否保留一个(用于出队)
    def switch(self, in_stack, out_stack, remain=0):
        if self.is_empty():
            return

        while not in_stack.is_empty():
            if in_stack.size() > remain:
                out_stack.push(in_stack.pop())
            else:
                break

    # 入队
    def push(self, value):
        if self.cap is not None and self.cap <= self.size():
            raise Exception('Queue is full')
        # 如果右边为空
        if self.right_stack.is_empty():
            self.left_stack.push(value)
        else:
            self.switch(self.right_stack, self.left_stack)
            self.left_stack.push(value)

    # 出队
    def pop(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        if self.left_stack.is_empty():
            return self.right_stack.pop()
        else:
            self.switch(self.left_stack, self.right_stack, 1)
            return self.left_stack.pop()

    # 返回队首
    def head(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        if self.left_stack.is_empty():
            return self.right_stack.peak()
        else:
            self.switch(self.left_stack, self.right_stack, 1)
            return self.left_stack.peak()

    # 返回队尾
    def tail(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        if not self.right_stack.is_empty():
            self.switch(self.right_stack, self.left_stack, 1)
        return self.left_stack.peak()

    # 计算队列长度
    def size(self):
        return self.left_stack.size() + self.right_stack.size()

    # 预览队列
    def preview(self):
        if self.is_empty():
            raise Exception('Queue is empty')
        if not self.left_stack.is_empty():
            self.switch(self.left_stack, self.right_stack)

        self.right_stack.preview()

    def debug(self):
        if not self.left_stack.is_empty():
            self.left_stack.preview()
        else:
            print 'left is empty'

        if not self.right_stack.is_empty():
            self.right_stack.preview()
        else:
            print 'right is empty'


if __name__ == '__main__':
    q = TwoStackQueue()
    long_queue = [randint(0, 10) for i in range(0, 100)]
    # print long_queue
    result = Counter(long_queue)
    t = []
    for i in long_queue:
        if i == 0:
            t.append(q.pop())
        else:
            q.push(i)
    print t
    long_queue = [x for x in long_queue if x]
    print long_queue[:len(t)]
