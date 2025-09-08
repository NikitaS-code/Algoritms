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

def collect_leaves_inorder(node, leaves):
    if node is None:
        return
    collect_leaves_inorder(node.left, leaves)
    if node.left is None and node.right is None:
        leaves.append(node.val)
    collect_leaves_inorder(node.right, leaves)

def main():
    values = list(map(int, input().split()))
    root = None

    for val in values:
        if val == 0:
            break
        root = insert(root, val)

    leaves = []
    collect_leaves_inorder(root, leaves)

    for leaf in leaves:
        print(leaf)

if __name__ == "__main__":
    main()
