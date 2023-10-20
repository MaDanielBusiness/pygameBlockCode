import lambdaFunctions
from lambdaFunctions import *

class node:
    def __init__(self, value = None):
        self.left = None
        self.right = None
        self.parent = None
        self.value = value

    def __str__(self):
        return self.value

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent


if __name__ == "test":
    boolb = node(True) # the value is the boolean
    hi = node(lambda : print("hi")) # the value is the function
    ifb = node((boolb, hi)) # the value is the parameters
    block = node(if_lambda(ifb.value)) # pass the function the parameters
    #block.value