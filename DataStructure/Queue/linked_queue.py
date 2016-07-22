class Node(object):
    '''
    Defines a class for Queue Node
    '''
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        #return "{value: %s, next: '%s'}" % (self.value, self.next)
        return str(self.value)

    def __str__(self):
        return str(self.value)


class Queue(object):
    '''
    Defines a class for Queue which acts as a container for nodes that are
    inserted and removed according FIFO
    '''
    def __init__(self):
        self.front = None
        self.back = None

    def isEmpty(self):
        return (self.front is None) and (self.back is None)

    def enqueue(self, value):
        node = Node(value)
        if self.back:
            self.back.next = node
        self.back = node
        if self.front is None:
            self.front = node

    def dequeue(self):
        if self.front:
            value = self.front.value
            self.front = self.front.next
            if self.front is None:
                self.back = None
            return value
        else:
            raise Exception("Queue is empty")

    def size(self):
        node = self.front
        if node:
            num_nodes = 1
        else:
            return 0
        node = node.next
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def peak(self):
        if self.front:
            return self.front.value
        else:
            return None

    def __repr__(self):
        items = list()
        node = self.front
        while node:
            items.append(node)
            node = node.next
        return "<front>%s<back>" % repr(items)

    def __str__(self):
        items = list()
        node = self.front
        while node:
            items.append(node)
            node = node.next
        return "<front>%s<back>" % str(items)

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


def main():
    queue = Queue()
    queue.enqueue(1)

if __name__ == "__main__":
    main()
