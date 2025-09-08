import sys
sys.setrecursionlimit(200000)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder_traversal(node):
    if node:
        inorder_traversal(node.left)
        print(node.val)
        inorder_traversal(node.right)

def main():
    values = list(map(int, input().split()))
    root = None

    for val in values:
        if val == 0:
            break
        root = insert(root, val)

    inorder_traversal(root)

if __name__ == "__main__":
    main()
