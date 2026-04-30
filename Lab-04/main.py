class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):

        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node


words = SinglyLinkedList()

words.append('ITEC212')
words.append('ITEC213')
words.append('ITEC215')
words.append('ITEC229')
words.append('ITEC255')

current = words.head

while current:
    print(current.data)
    current = current.next
class Node:

    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def append(self, data):

        node = Node(data)
        
        if self.head is None:
            self.head = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node

words = SinglyLinkedList()
words.append('ITEC212')
words.append('ITEC213')
words.append('ITEC215')
words.append('ITEC229')
words.append('ITEC255')

current = words.head
while current:
    print(current.data)
    current = current.next
