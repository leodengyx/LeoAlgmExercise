import math

class Heap(object):

    def __init__(self, nums= None):
        self.data = []
        if nums:
            build_heap(nums)

    def build_heap(self, nums):
        pass

    def size(self):
        return len(self.data)

    def height(self):
        if self.size() == 0:
            return 0
        return math.floor(math.log(self.size(), 2)) + 1

    def get_parent(self, i):
        if i <= 0:
            return -1
        return math.ceil(i / 2) - 1

    def get_left_child(self, i):
        if i < 0 or self.size() == 0:
            return -1
        if (i * 2 + 1) <= self.size() - 1:
            return i * 2 + 1
        else:
            return -1

    def get_right_child(self, i):
        if i < 0 or self.size() == 0:
            return -1
        if (i * 2 + 2) <= self.size() - 1:
            return i * 2 + 2

    def heapify(self, i):
        pass

    def push(self, elem):
        pass

    def pop(self):
        pass
