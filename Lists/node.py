# Filename: node.py

class Node:
    """ Represents a node in the Singly Linked List """

    def __init__(self):
        """ Creates a node object without data initially """
        self.data = None
        self.next = None

    def getData(self):
        return self.data

    def setData(self, value):
        self.data = value

    def getNext(self):
        return self.next

    def setNext(self, value):
        self.next = value