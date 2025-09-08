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

def find_second_max(root):
    parent = None
    node = root

    while node.right:
        parent = node
        node = node.right

    if node.left:
        node = node.left
        while node.right:
            node = node.right
        return node.val
    else:
        return parent.val

def main():
    values = list(map(int, input().split()))
    root = None

    for val in values:
        if val == 0:
            break
        root = insert(root, val)

    print(find_second_max(root))

if __name__ == "__main__":
    main()
