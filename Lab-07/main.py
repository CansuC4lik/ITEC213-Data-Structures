class ListQueue:
    def __init__(self):
        self.items = []
        self.front = 0
        self.rear = 0
        self.size = 3

    def enqueue(self, data):
        if self.size == self.rear:
            print("\nQueue is full")
        else:
            self.items.append(data)
            self.rear += 1

    def dequeue(self):
        if self.front == self.rear:
            print("Queue is empty")
        else:
            data = self.items.pop(0)
            self.rear -= 1
            return data


q = ListQueue()

q.enqueue("ITEC212")
q.enqueue("ITEC213")
q.enqueue("ITEC243")
q.enqueue("ITEC255")

print(q.items)

data = q.dequeue()
print(data)
print(q.items)

print(len(q.items))
