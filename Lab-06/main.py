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

        new_node = Node(data, None, None)

        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        self.count += 1

    def delete(self, data):
        current = self.head
        node_deleted = False

        if current is None:
            print("List is empty")

        elif current.data == data:
            self.head = current.next
            if self.head:
                self.head.prev = None
            node_deleted = True

        elif self.tail.data == data:
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            node_deleted = True

        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    if current.next:
                        current.next.prev = current.prev
                    node_deleted = True
                    break
                current = current.next

            if not node_deleted:
                print("Item not found")

        if node_deleted:
            self.count -= 1

words = DoublyLinkedList()
words.append('ITEC212')
words.append('ITEC213')
words.append('ITEC215')

print("List is created")
current = words.head
while current:
    print(current.data)
    current = current.next

words.delete('ITEC213')
print("\nITEC213 is found and deleted.")
current = words.head
while current:
    print(current.data)
    current = current.next

words.delete('ITEC215')
print("\nITEC215 is found and deleted.")
current = words.head
while current:
    print(current.data)
    current = current.next
