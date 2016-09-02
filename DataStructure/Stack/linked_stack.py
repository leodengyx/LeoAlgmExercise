class Node(object):
    '''
    Defines the Node for Stack
    '''
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __repr__(self):
        #return "{value: '%s', next: '%s'}" % (repr(self.value), repr(self.next))
        return str(self.value)

    def __str__(self):
        return str(self.value)

class Stack(object):
    '''
    Defines the Stack with Nodes
    '''
    def __init__(self):
        self.top = None

    def isEmpty(self):
        return self.top is None

    def push(self, value):
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self):
        node = self.top
        if node:
            self.top = node.next
            return node.value
        else:
            raise Exception("Stack is empty")

    def size(self):
        node = self.top
        num_nodes = 0
        while node:
            num_nodes += 1
            node = node.next
        return num_nodes

    def peak(self):
        if self.isEmpty():
            raise Exception("Stack is empty")
        return self.top.value

    def __repr__(self):
        items = list()
        if not self.isEmpty():
            node = self.top
            while node:
                items.append(node)
                node = node.next
            return "<top>" + repr(items)
        return repr(None)

    def __str__(self):
        items = list()
        if not self.isEmpty():
            node = self.top
            while node:
                items.append(node)
                node = node.next
            return "<top>" + str(items)
        return str(None)

def main():
    stack = Stack()
    stack.push(1)
    print(str(stack))
    stack.push(2)
    print(str(stack))
    stack.push(3)
    print(str(stack))
    print(stack.size())
    print(stack.peak())
    print(stack.pop())
    print(str(stack))
    print(stack.peak())

if __name__ == "__main__":
    main()
