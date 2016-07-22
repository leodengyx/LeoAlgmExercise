class Stack(object):
    '''
    Defines the Stack class using array
    '''
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.items.pop(-1)
        else:
            raise Exception("Stack is empty")

    def peak(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items) + "<top>"

def main():
    stack = Stack()
    stack.push(1)
    print(stack)
    stack.push(2)
    print(stack)
    stack.push(3)
    print(stack)
    print(stack.size())
    print(stack.peak())
    print(stack.pop())
    print(stack)
    print(stack.peak())

if __name__ == "__main__":
    main()
