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
    elif val > root.val:
        root.right = insert(root.right, val)
    return root

def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))

def main():
    values = list(map(int, input().split()))
    root = None

    for val in values:
        if val == 0:
            break
        root = insert(root, val)

    print(height(root))

if __name__ == "__main__":
    main()
