class Stack:
    def __init__(self):
        self.elements = []
        
    def push(self, item):
        self.elements.append(item)
    
    def pop(self):
        if len(self.elements) == 0:
            return None
        return self.elements.pop()

class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.right = None
        self.left = None
        
def calc(node):
    if node.data == "+":
        return calc(node.left) + calc(node.right)
    elif node.data == "-":
        return calc(node.left) - calc(node.right)
    elif node.data == "*":
        return calc(node.left) * calc(node.right)
    elif node.data == "/":
        return calc(node.left) / calc(node.right)
    else:
        return int(node.data)

expr = "4 3 * 5 2 - +".split()

stack = Stack()

for term in expr:
    if term in "+-*/":
        node = TreeNode(term)
        node.right = stack.pop()
        node.left = stack.pop()
    else:
        node = TreeNode(int(term))
    
    stack.push(node)

root = stack.pop()
result = calc(root)

print("Result:", result)
