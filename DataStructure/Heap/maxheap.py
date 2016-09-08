from heap import Heap

class Maxheap(Heap):

    def heapify(self, i):
        largest = i
        left_child = self.get_left_child(i)
        right_child = self.get_right_child(i)
        if left_child != -1 and self.data[largest] < self.data[left_child]:
            largest = left_child
        if right_child != -1 and self.data[largest] < self.data[right_child]:
            largest = right_child
        if largest != i:
            self.data[i], self.data[largest] = self.data[largest], self.data[i]
            self.heapify(largest)

    def push(self, elem):
        i = self.size()
        self.data.append(elem)
        parent = self.get_parent(i)
        while parent != -1 and self.data[parent] < self.data[i]:
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            i = parent
            parent = self.get_parent(i)

if __name__ == "__main__":
    nums = [7,5,3,1,9,4,6,8,2]
    instance = Maxheap(nums)
    print(instance)