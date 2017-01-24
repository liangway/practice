# -*- coding:utf-8 -*-

class Fruit:
    val = ''
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


if __name__ == '__main__':
    f1 = Fruit('apple')
    f2 = Fruit('apple')
    assert f1 == f2
