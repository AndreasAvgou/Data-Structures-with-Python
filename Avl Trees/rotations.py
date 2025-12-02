# Filename: rotations.py
from utils import getHeight

def leftRotate(z):
    y = z.right
    T2 = y.left

    # Perform rotation
    y.left = z
    z.right = T2

    # Update heights
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    # Return the new root
    return y

def rightRotate(z):
    y = z.left
    T3 = y.right

    # Perform rotation
    y.right = z
    z.left = T3

    # Update heights
    z.height = 1 + max(getHeight(z.left), getHeight(z.right))
    y.height = 1 + max(getHeight(y.left), getHeight(y.right))

    # Return the new root
    return y