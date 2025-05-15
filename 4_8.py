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

def collect_single_child_nodes(node, result):
    if node is None:
        return
    collect_single_child_nodes(node.left, result)
    if (node.left is None) != (node.right is None):
        result.append(node.val)
    collect_single_child_nodes(node.right, result)

def main():
    values = list(map(int, input().split()))
    root = None
    for val in values:
        if val == 0:
            break
        root = insert(root, val)

    result = []
    collect_single_child_nodes(root, result)

    for val in result:
        print(val)

if __name__ == "__main__":
    main()
