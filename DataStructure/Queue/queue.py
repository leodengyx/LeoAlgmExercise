class Queue(object):
    '''
    Define a class for Queue
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(-1)

    def size(self):
        return len(self.items)

    def peak(self):
        if not self.isEmpty():
            return self.items[-1]
        else:
            raise Exception("Queue is empty")

    def __repr__(self):
        return "<back>" + repr(self.items) + "<front>"

    def __str__(self):
        return "<back>" + str(self.items) + "<front>"

def main():
    queue = Queue()
    queue.enqueue(1)
    print(str(queue))
    queue.enqueue(2)
    print(str(queue))
    queue.enqueue(3)
    print(str(queue))
    print(queue.size())
    print(queue.peak())
    print(queue.dequeue())
    print(str(queue))
    print(queue.peak())

if __name__ == "__main__":
    main()