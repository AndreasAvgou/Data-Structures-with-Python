# Filename: traversal.py

def preOrder(root):
    if not root:
        return

    print("{0} ".format(root.val), end="")
    preOrder(root.left)
    preOrder(root.right)