
class BinaryTreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.items:
            return self.items.pop()
        else:
            print("pop() error: Stack is empty.")
            return None

    def peek(self):
        if self.items:
            return self.items[-1]
        else:
            print("peek() error: Stack is empty.")
            return None

    def size(self):
        return len(self.items)

"""
1. Iterative preorder traversal of a binary tree
"""
def preorder(root):
    tree = []
    s = Stack()
    s.push(root)
    if root is None:
        return tree
    while not s.isEmpty():
        node = s.pop()
        tree.append(node.val)
        if node.right:
            s.push(node.right)
        if node.left:
            s.push(node.left)
    return tree 

"""
root = BinaryTreeNode(1)
root.left = BinaryTreeNode(2)
root.right = BinaryTreeNode(3)
root.right.left = BinaryTreeNode(4)
root.right.right = BinaryTreeNode(5)
"""

def search (plist, target_item):
    for i in range(len(plist)):             
        if plist[i] == target_item:
            return i


"""
2. Reconstruct Binary Tree
"""
# inorder traversal can be divided as [left-subtree-nodes, root, right-subtree-nodes]
# preorder traversal can be divided as [root, left-subtree-nodes, right-subtree-nodes]

def reconstructBT(preorder, inorder):
    for n in preorder:
        if n in inorder:
            root = BinaryTreeNode(n)
            break
    try:
        root_index = search(inorder, n)
    except:
        return 
    left_tree = inorder[:root_index]
    if len(left_tree) > 0:
        root.left = reconstructBT(preorder, left_tree)
    right_tree = inorder[root_index + 1:]
    if len(right_tree) > 0:
        root.right = reconstructBT(preorder, right_tree)
    return root



"""
3. Convert Binary Search Tree
"""
def convertBSTtoGST(root):
    total = 0
    if root is None:
        return
    buildGST(root, total)
    return root


def buildGST(root, total):
    if root.right is not None:
        total = buildGST(root.right, total)
    total = total + root.val
    root.val = total
    if root.left is not None:
        total = buildGST(root.left, total)
    return total
