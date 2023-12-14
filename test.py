import lambdaFunctions
from lambdaFunctions import *


class node:
    def __init__(self, value=None):
        self.parent = None
        self.inner = None
        self.child = None
        self.value = value

    def __str__(self):
        return self.value

    def act(self):
        if callable(self.value):
            self.value()
        if self.child is not None:
            self.child.act()

    def act2(self):
        temp = 0
        if callable(self.value):
            pass
            # check if it has parameters



i = node(lambda: print("i"))
j = node(lambda: print("j"))
k = node(lambda x: print(x))

i.act()
j.act()

i.child = j

i.act()
