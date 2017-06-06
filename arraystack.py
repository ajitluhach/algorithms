class Empty(Exception):
    """Inherits from the base class of exception, A new exception for the stack"""


class ArrayStack:
    """Last in first out implementation using a Python list as underlying storage"""

    def __init__(self):
        """Create an empty Stack"""
        self._data = []

    def __len__(self):
        """Returns length of the stack"""
        return len(self._data)

    def is_empty(self):
        """Check if the stack is empty"""
        return len(self._data) == 0

    def push(self, element):
        """Add an element to the top of the stack"""
        self._data.append(element)

    def top(self):
        """Returns the element on the top of the stack"""
        if self.is_empty():
            raise Empty('Stack is Empty')
        return self._data[-1]

    def pop(self):
        """Deletes the element from the top of the stack and returns it"""
        if self.is_empty():
            raise Empty("Stack is Empty")
        return self._data.pop()
