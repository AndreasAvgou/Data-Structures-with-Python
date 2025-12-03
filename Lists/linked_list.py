# Filename: linked_list.py
from node import Node
from utils import wait_for_input

class LinkedList:
    """ Represents the Singly Linked List """
    
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def size(self):
        curr_node = self.head
        count = 0
        while curr_node is not None:
            count += 1
            curr_node = curr_node.getNext()
        return count

    def search_position(self, value):
        """ 
        Helper function to find the correct position for insertion.
        Used to keep the list SORTED.
        Returns: (found_status, previous_node)
        """
        found = 0
        prev_node = None
        curr_node = self.head
        
        while (curr_node is not None) and (found == 0):
            # Because the list is sorted, we traverse while value is larger
            if value > curr_node.getData():
                prev_node = curr_node
                curr_node = curr_node.getNext()
            elif value == curr_node.getData():
                found = 1
            else:
                # If value is smaller than current, we stop (insertion point found)
                curr_node = None # Force exit loop
        return found, prev_node

    def insert_node(self, value):
        # Determine where to insert to maintain order
        found, prev_node = self.search_position(value)
        
        if found == 1:
            print("Value already exists!")
        else:
            new_node = Node()
            new_node.setData(value)
            
            if prev_node is None:
                # Case: Insert at the beginning (Head)
                curr_node = self.head
                if self.is_empty():
                    self.head = new_node
                else:
                    new_node.setNext(curr_node)
                    self.head = new_node
            else:
                # Case: Insert somewhere in the middle or end
                new_node.setNext(prev_node.getNext())
                prev_node.setNext(new_node)

    def find_node(self, value):
        """ Checks if a value exists in the list """
        found = 0
        curr_node = self.head
        while (curr_node is not None) and (found == 0):
            if curr_node.getData() == value:
                found = 1
            else:
                curr_node = curr_node.getNext()
        return found

    def remove_node(self, value):
        found = 0
        prev_node = None
        curr_node = self.head
        
        while (curr_node is not None) and (found == 0):
            if curr_node.getData() == value:
                found = 1
                if prev_node is not None:
                    # Bypass the current node
                    prev_node.setNext(curr_node.getNext())
                else:
                    # Removing the head
                    self.head = curr_node.getNext()
            else:
                prev_node = curr_node
                curr_node = curr_node.getNext()

    def print_list(self):
        print("\n\nList Size: %d\n\n" % (self.size()))
        curr_node = self.head
        s = ""
        while curr_node is not None:
            s = s + str(curr_node.getData())
            curr_node = curr_node.getNext()
            if curr_node is not None:
                s = s + " --> "
        print(s)
        wait_for_input()