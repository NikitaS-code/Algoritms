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

def is_avl_balanced(node):
    if node is None:
        return True, 0

    left_balanced, left_height = is_avl_balanced(node.left)
    right_balanced, right_height = is_avl_balanced(node.right)

    height = max(left_height, right_height) + 1
    balanced = (
        left_balanced and
        right_balanced and
        abs(left_height - right_height) <= 1
    )
    return balanced, height

def main():
    values = list(map(int, input().split()))
    root = None
    for val in values:
        if val == 0:
            break
        root = insert(root, val)

    balanced, _ = is_avl_balanced(root)
    print("YES" if balanced else "NO")

if __name__ == "__main__":
    main()
