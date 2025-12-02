# Filename: main.py
from operations import insert, delete
from traversal import preOrder

def main():
    root = None
    nums = [9, 5, 10, 0, 6, 11, -1, 1, 2]

    # Insertion Loop
    for num in nums:
        root = insert(root, num)

    # Preorder Traversal
    print("Preorder Traversal after insertion -")
    preOrder(root)
    print() # New line

    # Delete operation
    key_to_delete = 10
    root = delete(root, key_to_delete)

    # Preorder Traversal
    print(f"Preorder Traversal after deletion of {key_to_delete} -")
    preOrder(root)
    print() # New line

if __name__ == "__main__":
    main()