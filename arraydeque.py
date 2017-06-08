class Empty(Exception):
    pass


class ArrayDeque:
    """Implement deque using Python List as the underlining data structure"""

    def __init__(self, capacity=16):
        """Initializes a new deque"""
        self._data = [None]*capacity
        self._size = 0
        self._front = 0
        self._last = 0

    def first(self):
        """Returns the first element in the queue, does not deletes them"""

        return self._data[self._front]

    def last(self):
        """Returns the last element in the queue, does not delete"""
        last = (self._front + self._size - 1) % len(self._data)
        return self.data[last]

    def __str__(self):
        """Display the whole deque as a list"""
        elements = []
        for f in range(self._size):
            element = (self._front + f) % len(self._data)
            elements.append(self._data[element])
        return elements

    def is_empty(self):
        return self._size == 0

    def __len__(self):
        return self._size

    def resize(self, cap):
        """Doubles the size of the self._data"""
        old = self._data
        self._data = [None]*cap
        walk = self._front  # Copy all the elements of the previous list
        # copy them to start of the new list, notice
        # the next loop
        for k in range(self._size):
            self._data[k] = old[walk]
            walk = (walk + 1) % len(old)
        self._front = 0

    def add_first(self, e):
        """Add an element to the front of the deque, wrap around needed"""
        if self._size == len(self._data):
            popped_from_back = self.delete_last
        self._front = (self._front - 1) % len(self._data)
        self._data[self._front] = e

    def delete_last(self, e):
        """Deletes an element from the last. Wrap around and resizing could\
                be needed"""
        if self.is_empty():
            raise Empty('Queue is empty')
        to_delete = (self._front + self._size - 1) % len(self._data)
        answer = self._data[to_delete]
        self._data[to_delete] = None
        self._size -= 1

        if 0 < self._size < len(self._data)//4:
            self.resize(len(self._data)//2)
        return answer

    def delete_first(self):
        """Delete the element from the front of the queue."""
        if self.is_empty():
            raise Empty('Queue is Empty')
        to_delete = self._data[self._front]
        self._data[self.front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data)//4:
            self.resize(len(self._data)//2)
        return to_delete

    def add_last(self, e):
        """This function is same as adding the element at the back.\
                Same as enque"""
        if self._size == len(self._data):
            self.resize(len(self._data)*2)
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
