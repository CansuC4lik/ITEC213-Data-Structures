class Node:
    def __init__(self, data):
        self.data = data
        self.left_child = None
        self.right_child = None

n1 = Node("root node")
n2 = Node("left child node")
n3 = Node("right child node")
n4 = Node("left grandchild node")

n1.left_child = n2
n1.right_child = n3
n2.left_child = n4


print("Traverse the left subtree of the binary tree:")
current = n1
while current:
    print(current.data)
    current = current.left_child

print("\n")


def inorder(root_node):
    if root_node is None:
        return
    inorder(root_node.left_child)
    print(root_node.data)
    inorder(root_node.right_child)


def preorder(root_node):
    if root_node is None:
        return
    print(root_node.data)
    preorder(root_node.left_child)
    preorder(root_node.right_child)


def postorder(root_node):
    if root_node is None:
        return
    postorder(root_node.left_child)
    postorder(root_node.right_child)
    print(root_node.data)


print("Inorder:")
inorder(n1)

print("\nPreorder:")
preorder(n1)

print("\nPostorder:")
postorder(n1)
