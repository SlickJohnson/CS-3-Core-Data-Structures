#!python
"""implementations of stack data structures."""
from linkedlist import LinkedList


class LinkedStack(object):
    """LinkedList stack implementation.

    Attributes:
        list: LinkedList -- stores the items

    """

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any.

        Args:
            iteratable: iterable -- Items to populate the stack with.
        """
        # Initialize a new linked list to store the items
        self.list = LinkedList()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.list.is_empty()

    def length(self):
        """Return the number of items in this stack."""
        return self.list.length()

    def push(self, item):
        """Insert the given item on the top of this stack.

        Args:
            item: anytype -- data that will be added to the stack.
        """
        self.list.prepend(item)  # O(1)

    def peek(self):
        """Return the item on the top of this stack."""
        peek = self.list.head  # O(1)
        if peek:  # O(1)
            return peek.data  # O(1)

        # Stack is empty, return None.
        return None  # O(1)

    def pop(self):
        """Remove and return the item on the top of this stack.

        Performance:
            Best/Worst: O(1), because pop only affects the head of the
                linkedlist.

        Returns: anytype -- returns the item that sits at the top of the stack.

        Raises:
            ValueError: if this stack is empty.

        """
        if self.is_empty():
            raise ValueError('Empty stack')

        pop = self.list.head.data  # O(1)
        self.list.delete(pop)  # O(1)

        return pop  # O(1)


class ArrayStack(object):
    """LinkedList stack implementation.

    Attributes:
        list: list -- stores the items

    """

    def __init__(self, iterable=None):
        """Initialize this stack and push the given items, if any.

        Args:
            iteratable: iterable -- Items to populate the stack with.
        """
        # Initialize a new list (dynamic array) to store the items
        self.list = list()
        if iterable is not None:
            for item in iterable:
                self.push(item)

    def __repr__(self):
        """Return a string representation of this stack."""
        return 'Stack({} items, top={})'.format(self.length(), self.peek())

    def is_empty(self):
        """Return True if this stack is empty, or False otherwise."""
        return self.length() == 0  # O(1)

    def length(self):
        """Return the number of items in this stack."""
        return len(self.list)

    def push(self, item):
        """Insert the given item on the top of this stack.

        Args:
            item: anytype -- data that will be added to the stack.

        Performance:
            Best/Worst: O(1), adding to the end of an list is O(1)
        """
        self.list.append(item)  # O(1)

    def peek(self):
        """Return the item on the top of this stack without removing it."""
        # Return None if stack is empty.
        if self.is_empty():
            return None

        return self.list[-1]  # O(1)

    def pop(self):
        """Remove and return the item on the top of this stack.

        Performance:
            Best/Worst: O(1), only concerned with the last entry in the list.

        Raises:
            ValueError: if stack is empty.

        """
        if self.is_empty():
            raise ValueError('Empty stack')

        return self.list.pop()  # O(1)


# Implement LinkedStack and ArrayStack above, then change the assignment below
# to use each of your Stack implementations to verify they each pass all tests
# Stack = LinkedStack
Stack = ArrayStack
