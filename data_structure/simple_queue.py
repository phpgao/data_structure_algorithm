#! /usr/local/env python
# coding=utf-8

"""
队列 是一个先进先出(LIFO)的数据结构，元素依次加入队列，并依次出列
"""


# 声明一个node
# 包含一个值和指向下一个node的指针类
# 是不是有点像单链表
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class SimpleQueue:
    # 初始化操作
    def __init__(self, cap=None):
        self.header = None
        self.cap = cap

    # 重置
    def reset(self):
        self.header = None

    # 判断一个栈是否为空
    def is_empty(self):
        return not self.header

    # 入队
    def push(self, value):
        if self.cap is not None and self.cap <= self.size():
            raise Exception('Queue is full')
        node = self.header
        if node is None:
            self.header = Node(value)
        else:
            while node.next is not None:
                node = node.next
            node.next = Node(value)

    # 出队
    def pop(self):
        node = self.header
        if node is None:
            raise Exception('Queue is empty')
        else:
            self.header = node.next
            return node.value

    # 返回队首
    def head(self):
        node = self.header
        if node is None:
            raise Exception('Queue is empty')
        else:
            return node.value

    # 返回队尾
    def tail(self):
        node = self.header
        if node is None:
            raise Exception('Queue is empty')
        else:
            while node.next is not None:
                node = node.next
            return node.value

    # 计算队列长度
    def size(self):
        node = self.header
        if not node:
            return 0
        count = 0
        while node is not None:
            count += 1
            node = node.next
        return count

    # 预览队列
    def preview(self):
        node = self.header
        if node is None:
            raise Exception('Queue is empty')
        else:
            print '-' * 36
            while node is not None:
                print node.value
                node = node.next
            print 'tail'
            print '-' * 36


if __name__ == '__main__':
    q = SimpleQueue(4)

    q.push(1)
    q.push(2)
    print q.head()
    print q.size()
    print q.pop()
    print q.pop()
    print q.is_empty()

    q.push(1)
    q.reset()
    q.push(2)
    q.push(3)
    print q.tail()
    q.push(4)
    q.push(5)
    q.preview()
