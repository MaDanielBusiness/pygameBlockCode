from abc import ABC, abstractmethod


# Define the interface using an Abstract Base Class (ABC)
class CommandBlock(ABC):
    @abstractmethod
    def run(self):
        """ A command should perform some behavior when run """
        pass
