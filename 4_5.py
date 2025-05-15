class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert_and_get_depth(root, val, depth=1):
    if root is None:
        print(depth)
        return Node(val)

    if val < root.val:
        root.left = insert_and_get_depth(root.left, val, depth + 1)
    elif val > root.val:
        root.right = insert_and_get_depth(root.right, val, depth + 1)
    return root

def main():
    values = list(map(int, input().split()))
    root = None

    for val in values:
        if val == 0:
            break
        root = insert_and_get_depth(root, val)

if __name__ == "__main__":
    main()
