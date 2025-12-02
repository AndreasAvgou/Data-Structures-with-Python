# Filename: utils.py

def getHeight(root):
    if not root:
        return 0
    return root.height

def getBalance(root):
    if not root:
        return 0
    return getHeight(root.left) - getHeight(root.right)

def getMinValueNode(root):
    if root is None or root.left is None:
        return root
    return getMinValueNode(root.left)