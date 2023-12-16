from abc import ABC, abstractmethod

class CompositeBlockInterface(ABC):
    @abstractmethod
    def operation(self):
        """
        leaf nodes have an operation
        inner nodes iterate through the children and call their operations
        """
        pass