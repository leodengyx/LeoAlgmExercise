import math

class Heap(object):

    def __init__(self, nums=None):
        self.data = []
        if nums:
            self.build_heap(nums)

    def __str__(self):
        return str(self.data)

    def size(self):
        return len(self.data)

    def height(self):
        if self.size() == 0:
            return 0
        return math.floor(math.log(self.size(), 2)) + 1

    def get_parent(self, i):
        if i <= 0:
            return -1
        return int(math.ceil(i / 2.0) - 1)  # Be careful, here has to be 2.0, not 2

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
        else:
            return -1

    def heapify(self, i):
        smallest = i
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)
        if left_child != -1 and self.data[left_child] < self.data[smallest]:
            smallest = left_child
        if right_child != -1 and self.data[right_child] < self.data[smallest]:
            smallest = right_child
        if smallest is not i:
            self.data[i], self.data[smallest] = self.data[smallest], self.data[i]
            self.heapify(smallest)

    def push(self, elem):
        i = len(self.data)
        self.data.append(elem)
        parent = self.get_parent(i)
        while parent != -1 and self.data[parent] > self.data[i]:
            self.data[i], self.data[parent] = self.data[parent], self.data[i]
            i = parent
            parent = self.get_parent(i)

    def pop(self):
        if self.size() == 0:
            raise Exception("Heap is empty")
        self.data[0], self.data[-1] = self.data[-1], self.data[0]
        pop = self.data.pop(-1)
        self.heapify(0)
        return pop

    def build_heap(self, nums):
        self.data = nums[:]
        for i in range(self.get_parent(self.size() - 1), -1, -1):
            self.heapify(i)

if __name__ == "__main__":
    nums = [7, 5, 3, 1, 9, 4, 6, 8, 2]
    instance = Heap(nums)
    print(instance)

    instance.push(10)
    print(instance)

    instance.pop()
    print(instance)
