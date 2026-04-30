class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = Node(data)
        if self.top:
            node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.top = self.top.next
            self.size -= 1
            return data
        else:
            print("Stack is empty")

    def peek(self):
        if self.top:
            return self.top.data
        else:
            print("Stack is empty")


words = Stack()
words.push('ITEC212')
words.push('ITEC213')
words.push('ITEC255')

print("After adding the elements:")
current = words.top
while current:
    print(current.data)
    current = current.next

print("\nAfter deleting the top element:")
words.pop()

current = words.top
while current:
    print(current.data)
    current = current.next

print("\nPrint the top element:")
print(words.peek())
