class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = Node("Head")
        self.size = 0

    def peek(self):
        if self.size == 0:
            raise Exception("Empty stack")
        return self.head.next.value

    def push(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise Exception("Empty stack")
        currNode = self.head.next
        self.head.next = self.head.next.next
        self.size -= 1
        return currNode.value

    def __str__(self):
        currNode = self.head.next
        outStr = ""
        while currNode:
            outStr += str(currNode.value) + "->"
            currNode = currNode.next
        return outStr[:-2]

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(10)
    stack.push(1)
    print(str(stack))
    print(stack.pop())
    print(stack.peek())
