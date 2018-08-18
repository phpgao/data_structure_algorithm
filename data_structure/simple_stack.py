#! /usr/local/env python
# coding=utf-8

"""
栈 是一个后进先出(LIFO)的数据结构，元素越靠近栈底说明存在的更长，而越靠近栈顶则很有可能会被弹出。
"""


# 声明一个node
# 包含一个值和指向下一个node的指针类
# 是不是有点像单链表
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SimpleStack:
    # 初始化操作
    def __init__(self):
        self.top = None

    # 判断一个栈是否为空
    def is_empty(self):
        return not self.top

    # 入栈(压栈)
    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    # 出栈
    def pop(self):
        node = self.top
        if not node:
            raise Exception('Stack is empty')

        self.top = node.next
        return node.value

    # 返回栈顶元素
    def peek(self):
        node = self.top
        if not node:
            raise Exception('Stack is empty')
        return node.value

    def size(self):
        node = self.top
        if not node:
            raise Exception('Stack is empty')
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count


if __name__ == '__main__':
    s = SimpleStack()

    s.push(1)
    s.push(2)
    print s.pop()
    print s.pop()
    print s.is_empty()
    s.push(2)
    s.push(3)
    print s.size()
    print s.pop()
