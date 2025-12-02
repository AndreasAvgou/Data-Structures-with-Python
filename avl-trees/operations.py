# Filename: operations.py
from node import TreeNode
from utils import getHeight, getBalance, getMinValueNode
from rotations import leftRotate, rightRotate

def insert(root, key):
    # Step 1 - Perform normal BST insertion
    if not root:
        return TreeNode(key)
    elif key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)

    # Step 2 - Update the height of the ancestor node
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # Step 3 - Get the balance factor
    balance = getBalance(root)

    # Step 4 - If the node is unbalanced, try out the 4 cases
    
    # Case 1 - Left Left
    if balance > 1 and key < root.left.val:
        return rightRotate(root)

    # Case 2 - Right Right
    if balance < -1 and key > root.right.val:
        return leftRotate(root)

    # Case 3 - Left Right
    if balance > 1 and key > root.left.val:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Case 4 - Right Left
    if balance < -1 and key < root.right.val:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root

def delete(root, key):
    # Step 1 - Perform standard BST delete
    if not root:
        return root

    elif key < root.val:
        root.left = delete(root.left, key)

    elif key > root.val:
        root.right = delete(root.right, key)

    else:
        if root.left is None:
            temp = root.right
            root = None
            return temp

        elif root.right is None:
            temp = root.left
            root = None
            return temp

        temp = getMinValueNode(root.right)
        root.val = temp.val
        root.right = delete(root.right, temp.val)

    # If the tree has only one node, simply return it
    if root is None:
        return root

    # Step 2 - Update the height of the ancestor node
    root.height = 1 + max(getHeight(root.left), getHeight(root.right))

    # Step 3 - Get the balance factor
    balance = getBalance(root)

    # Step 4 - If the node is unbalanced, try out the 4 cases
    
    # Case 1 - Left Left
    if balance > 1 and getBalance(root.left) >= 0:
        return rightRotate(root)

    # Case 2 - Right Right
    if balance < -1 and getBalance(root.right) <= 0:
        return leftRotate(root)

    # Case 3 - Left Right
    if balance > 1 and getBalance(root.left) < 0:
        root.left = leftRotate(root.left)
        return rightRotate(root)

    # Case 4 - Right Left
    if balance < -1 and getBalance(root.right) > 0:
        root.right = rightRotate(root.right)
        return leftRotate(root)

    return root