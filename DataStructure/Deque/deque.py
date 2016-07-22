class Deque(object):
    '''
    Defines a class for double ended Queue
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, value):
        return self.items.insert(0, value)

    def addBack(self, value):
        return self.items.append(value)

    def removeFront(self):
        return self.items.pop(0)

    def removeBack(self):
        return self.items.pop(-1)

    def __repr__(self):
        return "<front>%s<back>" % repr(self.items)

    def __str__(self):
        return "<front>%s<back>" % str(self.items)


def main():
    deque = Deque()
    deque.addFront(1)
    print(str(deque))
    deque.addFront(2)
    print(str(deque))
    deque.addFront(3)
    print(str(deque))
    deque.addBack(10)
    print(str(deque))
    deque.addBack(20)
    print(str(deque))

if __name__ == '__main__':
    main()