class Node:
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1

    def append_at_start(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.count += 1

    def append_at_a_location(self, target, data):
        current = self.head

        while current:
            if current.data == target:
                new_node = Node(data)
                new_node.prev = current
                new_node.next = current.next

                if current.next:
                    current.next.prev = new_node
                else:
                    self.tail = new_node

                current.next = new_node
                self.count += 1
                return

            current = current.next

    def iter(self):
        current = self.head
        while current:
            yield current.data
            current = current.next

    def contains(self, data):
        for node_data in self.iter():
            if data == node_data:
                print("Data item is present in the list.")
                return
        print("Data item is not present in the list.")


words = DoublyLinkedList()
words.append('ITEC212')
words.append('ITEC213')
words.append('ITEC215')
words.append('ITEC229')
words.append('ITEC255')

print("Items in doubly linked list before append")
current = words.head
while current:
    print(current.data)
    current = current.next

words.append_at_start('ITEC309')

print("\nAfter append at start")
current = words.head
while current:
    print(current.data)
    current = current.next

words.append('ITEC310')

print("\nAfter append at end")
current = words.head
while current:
    print(current.data)
    current = current.next

words.append_at_a_location('ITEC213', 'NEW_NODE')

print("\nAfter inserting after ITEC213")
current = words.head
while current:
    print(current.data)
    current = current.next


words.contains("ITEC213")
words.contains("ITEC214")
