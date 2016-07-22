class Queue(object):
    '''
    Defines a class for Queue using 2 stacks
    '''
    def __init__(self):
        self.in_stack = []
        self.out_stack = []

    def isEmpty(self):
        return self.in_stack == [] and self.out_stack == []

    def enqueue(self, item):
        self.in_stack.append(item)

    def dequeue(self):
        if self.out_stack:
            return self.out_stack.pop(-1)
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop(-1))
            if not self.out_stack:
                raise Exception("Queue is empty")
            return self.out_stack.pop(-1)

    def size(self):
        return len(self.in_stack) + len(self.out_stack)

    def peak(self):
        if self.out_stack:
            return self.out_stack[-1]
        else:
            while self.in_stack:
                self.out_stack.append(self.in_stack.pop(-1))
            if not self.out_stack:
                raise Exception("Queue is empty")
            return self.out_stack[-1]

    def __repr__(self):
        return "IN_STACK: %s<back>, OUT_STACK: %s<front>" % (repr(self.in_stack), repr(self.out_stack))

    def __str__(self):
        return "IN_STACK: %s<back>, OUT_STACK: %s<front>" % (str(self.in_stack), str(self.out_stack))

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